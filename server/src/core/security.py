from passlib.context import CryptContext

# NOTE: These utility methods are stored here instead of `auth module
# because they are also used by `user` module. Due to the loosely coupled
# structure of the API, the modules cannot directly share utility methods.

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(password: str, hash_pw: str) -> bool:
    """
    Verifies password against a hash.

    Args:
        password: To be verified.
        hash_pw: Hashed string.

    Returns:
        bool: True if password is valid.
    """
    return pwd_context.verify(password, hash_pw)


def hash_password(password: str) -> str:
    """
    Hashes a password.

    Args:
        password: To be hashed.

    Returns:
        str: Hashed password.
    """
    return pwd_context.hash(password)
