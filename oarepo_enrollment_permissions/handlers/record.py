from elasticsearch_dsl import Q
from flask import current_app
from invenio_accounts.models import User
from oarepo_enrollments import EnrollmentHandler, Enrollment
from sqlalchemy.util import classproperty


class RecordHandler(EnrollmentHandler):
    cached_record_filter = None
    cached_index_pid_types = None

    def enroll(self, user: User, **kwargs) -> None:
        # this enrollment is enforced dynamically, does not influence data, so just pass
        pass

    def revoke(self, user: User, **kwargs) -> None:
        # this enrollment is enforced dynamically, does not influence data, so just pass
        pass

    @classproperty
    def record_filter(cls):
        if cls.cached_record_filter:
            return cls.cached_record_filter
        cls.cached_record_filter = \
            current_app.config['OAREPO_ENROLLMENT_PERMISSIONS_RECORD_FILTER']
        return cls.cached_record_filter

    @classmethod
    def cache_pid_types(cls):
        if cls.cached_index_pid_types is None:
            cls.cached_index_pid_types = {}
            rest_config = current_app.config['RECORDS_REST_ENDPOINTS']
            for config in rest_config.values():
                if config.get('search_index') and config.get('pid_type'):
                    cls.cached_index_pid_types[config.get('search_index')] = config.get('pid_type')

    @classmethod
    def get_pid_type(cls, search, indices):
        pid_type = getattr(search.Meta, 'pid_type', None)
        if pid_type:
            return pid_type
        if indices:
            cls.cache_pid_types()
            for index in indices:
                if index in cls.cached_index_pid_types:
                    return cls.cached_index_pid_types[index]

        raise AttributeError(f'Could not get pid type for indices {indices}. '
                             f'Please add property `pid_type` on your search class\' Meta. '
                             f'See the documentation for details.')

    @classmethod
    def get_elasticsearch_filter(cls, search=None, queryset=None, indices=None, **kwargs):
        records = []
        pid_type = cls.get_pid_type(search, indices)
        for enrollment in queryset.filter(Enrollment.external_key.startswith(f'{pid_type}:')):
            record = enrollment.external_key.split(':', maxsplit=1)[1]
            operations = enrollment.extra_data.get('operations')
            if not record or not operations:
                continue
            if 'read' not in operations:
                continue
            records.append(record)

        if records:
            es_filter = getattr(search.Meta, 'permissions_record_filter', None) or cls.record_filter
            if callable(es_filter):
                return es_filter(search=search, records=records, **kwargs)
            return Q('terms', **{es_filter: records})
        return None

    def post_filter_elasticsearch_result(self, search=None, result=None, **kwargs):
        # can be used to hide metadata from results
        pass
