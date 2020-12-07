from flask_login import current_user

from oarepo_enrollment_permissions.proxies import current_enrollment_permissions


def read_permission_factory(*args, **kwargs):
    return current_enrollment_permissions.get_action_permission(current_user, 'read', **kwargs)


def update_permission_factory(*args, **kwargs):
    return current_enrollment_permissions.get_action_permission(current_user, 'update', **kwargs)


def delete_permission_factory(*args, **kwargs):
    return current_enrollment_permissions.get_action_permission(current_user, 'delete', **kwargs)


def create_permission_factory(*args, **kwargs):
    return current_enrollment_permissions.get_action_permission(current_user, 'create', **kwargs)
