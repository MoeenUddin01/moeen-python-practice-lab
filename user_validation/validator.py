from config import MIN_PASSWORD_LENGTH, FORBIDDEN_USERNAMES, ALLOWED_DOMAINS


class ProfileValidation:
    def __init__(self, username, email, passward):
        self.username = username
        self.email = email
        self.passward = passward

    def email_validate(self, email):
        if isinstance(email, str):
            return False

        if "@" not in email:
            return False

        for i in ALLOWED_DOMAINS:
            if email.endwith(i):
                return True
        return False
