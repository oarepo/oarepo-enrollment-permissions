# json pointer identifying collection
OAREPO_ENROLLMENT_PERMISSIONS_COLLECTION_JSONPOINTER = None

# A filter that denotes a collection. Can be either a path interpreted by Q
# or a callable taking search and a list of allowed collection identifiers
# returning Q/ES bool
# (search: RecordsSearch = None, collections=["A", "B"], **kwargs) => Q|Bool
OAREPO_ENROLLMENT_PERMISSIONS_COLLECTION_FILTER = 'collection'

# A filter that denotes a collection. Can be either a path interpreted by Q
# or a callable taking search and a list of allowed collection identifiers
# returning Q/ES bool
# (search: RecordsSearch = None, collections=["A", "B"], **kwargs) => Q|Bool
OAREPO_ENROLLMENT_PERMISSIONS_RECORD_FILTER = 'control_number'
