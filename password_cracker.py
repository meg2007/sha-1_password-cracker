import hashlib

def crack_sha1_hash(hash, use_salts = False):
    # Read the passwords file
    with open("top-10000-passwords.txt", "r") as file:
        passwords = file.read().splitlines()

    # If salts are not used, perform basic cracking
    if not use_salts:
        for password in passwords:
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            if hashed_password == hash:
                return password
        return "PASSWORD NOT IN DATABASE"

    # Read the known salts file
    with open("known-salts.txt", "r") as file:
        salts = file.read().splitlines()

    # Iterate through each password and each salt
    for password in passwords:
        for salt in salts:
            # Test password with salt prepended
            hashed_prepend = hashlib.sha1((salt + password).encode()).hexdigest()
            if hashed_prepend == hash:
                return password

            # Test password with salt appended
            hashed_append = hashlib.sha1((password + salt).encode()).hexdigest()
            if hashed_append == hash:
                return password

    return "PASSWORD NOT IN DATABASE"