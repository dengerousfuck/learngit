import hashlib
import binascii,base64
def _md5(str):
    str = str.encode('utf-8')
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
def _baseword(userpwd):
    userpwd = binascii.a2b_hex(userpwd)
    userpwd = base64.b64encode(userpwd)
    userpwd = userpwd.decode()
    return userpwd