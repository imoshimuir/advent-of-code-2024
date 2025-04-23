import keyring

# Retrieve the password
password = keyring.get_password("poetry-repository-pydu", "Imogen Muir")

print(password)  # Output: super_secret_password
