import hashlib
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

passencrypted = encrypt_string("6")
print(passencrypted)