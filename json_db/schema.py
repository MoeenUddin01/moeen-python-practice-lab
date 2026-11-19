def validate_user_record(record):
    if not isinstance(record, dict):
        raise ValueError("Record must be a dictionary")

    required_keys = ["id", "username", "role"]

    for keys in required_keys:
        if keys not in record:
            raise ValueError(f"{keys} is missing")

    if not isinstance(record["id"], (int, str)):
        raise ValueError("Id must be int")

    if not isinstance(record["username"], (str)):
        raise ValueError("Username must be String")

    if not isinstance(record["role"], (str)):
        raise ValueError("Invalid data")

    if not record["username"].strip():
        raise ValueError("user name cannot be empty")

    if not record["role"].strip():
        raise ValueError("Role must not be empty")

    return True


if __name__ == "__main__":
    print("testing the file")
    d1 = validate_user_record({"id": 1223, "username": "Moeen", "role": "Ai engineer"})
    print(d1)
