# json pointer identifying collection
OAREPO_ENROLLMENT_PERMISSIONS_COLLECTION_JSONPOINTER = None

# A filter that denotes a collection. Can be either a path interpreted by Q
# or a callable taking search and a list of allowed collection identifiers
# returning Q/ES bool
# (search: RecordsSearch = None, collections=["A", "B"], **kwargs) => Q|Bool
OAREPO_ENROLLMENT_PERMISSIONS_COLLECTION_FILTER = 'collection'

# A filter for filtering records. Can be either a path interpreted by Q
# or a callable taking search and a list of allowed record uuids
# returning Q/ES bool
# (search: RecordsSearch = None, record_uuids=["A", "B"], **kwargs) => Q|Bool
#
# normally there is no need to override this
OAREPO_ENROLLMENT_PERMISSIONS_RECORD_FILTER = '_id'
