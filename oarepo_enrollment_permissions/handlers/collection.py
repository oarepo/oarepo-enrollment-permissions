from elasticsearch_dsl import Q
from flask import current_app
from invenio_accounts.models import User
from oarepo_enrollments import EnrollmentHandler
from sqlalchemy.util import classproperty


class CollectionHandler(EnrollmentHandler):
    cached_collection_filter = None

    def enroll(self, user: User, **kwargs) -> None:
        # this enrollment is enforced dynamically, does not influence data, so just pass
        pass

    def revoke(self, user: User, **kwargs) -> None:
        # this enrollment is enforced dynamically, does not influence data, so just pass
        pass

    @classproperty
    def collection_filter(cls):
        if cls.cached_collection_filter:
            return cls.cached_collection_filter
        cls.cached_collection_filter = \
            current_app.config['OAREPO_ENROLLMENT_PERMISSIONS_COLLECTION_FILTER']
        return cls.cached_collection_filter

    @classmethod
    def get_elasticsearch_filter(cls, search=None, queryset=None, **kwargs):
        collections = []
        for enrollment in queryset:
            collection = enrollment.external_key
            operations = enrollment.extra_data.get('operations')
            if not collection or not operations:
                continue
            if 'read' not in operations:
                continue
            collections.append(collection)

        if collections:
            es_filter = getattr(search.Meta, 'permissions_collection_filter', None) or cls.collection_filter
            if callable(es_filter):
                return es_filter(search=search, collections=collections, **kwargs)
            return Q('terms', **{es_filter: collections})
        return None

    def post_filter_elasticsearch_result(self, search=None, result=None, **kwargs):
        # can be used to hide metadata from results
        pass
