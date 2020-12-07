class PermissionCollection:
    def __init__(self, *permissions, method='or'):
        self.permissions = permissions
        self.method = method

    def can(self):
        if not self.permissions:
            return False
        for perm in self.permissions:
            if perm.can():
                if self.method == 'or':
                    return True
            else:
                if self.method == 'and':
                    return False

        return self.method == 'and'
