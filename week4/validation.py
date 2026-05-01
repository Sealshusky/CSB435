import re

class ValidationError(Exception):
    pass

def valid_username(s):
    s = s.strip().lower()
    if not re.fullmatch(r"[a-z0-9-]{3,20}", s):
        raise ValidationError("Invalid username")
    return s

def valid_email(s):
    s = s.strip()
    if s.count("@") > 1:
        parts = [p for p in s.split("@") if p]
        if len(parts) == 2:
            s = parts[0] + "@" + parts[1]
        else:
            raise ValidationError("Invalid email")
    if not re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", s):
        raise ValidationError("Invalid email")
    local, domain = s.split("@", 1)
    return local + "@" + domain.lower()

def valid_filename(s):
    s = s.strip()
    while s.endswith("."):
        s = s[:-1]
    if "/" in s or "\\" in s or ".." in s:
        raise ValidationError("Invalid filename")
    if not re.fullmatch(r"[A-Za-z0-9._-]+", s):
        raise ValidationError("Invalid filename")
    return 
