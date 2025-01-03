from fastapi import Depends
from dependencies.auth_utils import get_user_logged_in, validate_user_role



def role_required(allowed_roles: list):
    def dependency(user=Depends	(get_user_logged_in)):
        validate_user_role(user, allowed_roles)
        return user
    return dependency

