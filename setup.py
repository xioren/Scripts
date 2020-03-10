from secrets import token_bytes
import hashlib


'''
--digest lengths--
md5: 32
sha1: 40
sha256: 64
sha512: 128
blake2b: variable
shake_256: variable
'''


def hashes(set):
    if set == 1:
        return hashlib.algorithms_guaranteed
    else:
        return hashlib.algorithms_available


def hash_this(algorithm, string, salt=None, shake_size=None, blake2b_size=None):
    hash = hashlib.new(algorithm, string.encode(), digest_size=blake2b_size)
    if salt:
        if type(salt) is int:
            hash.update(token_bytes(salt))
        else:
            hash.update(salt.encode())
    if shake_size:
        return hash.hexdigest(shake_size)
    else:
        return hash.hexdigest()


password = r"xiorenfromshenzhen"


print(hash_this('md5', password))
# print(hashes(2))
