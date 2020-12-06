from elasticsearch_dsl import Q

from oarepo_enrollment_permissions import RecordsSearch


class CustomAnonymousRecordsSearch(RecordsSearch):
    class Meta:
        default_anonymous_filter = Q('term', collection='A')


class CustomAnonymousRecordsCallableSearch(RecordsSearch):
    class Meta:
        @classmethod
        def default_anonymous_filter(cls, search=None, **kwargs):
            assert search
            return Q('term', collection='A')


class RecordsSecuritySearch(RecordsSearch):
    pass
