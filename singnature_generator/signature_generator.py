import base64
import calendar
import hmac
import uuid

from datetime import datetime
from hashlib import sha1


def create_token(system_id, secret_id):
    # Сгенерировать рандомную строку
    rnd_str = str(uuid.uuid4()).encode('ascii')
    # Получить хэш от этой строки
    nonce_hash = sha1(rnd_str)
    nonce = nonce_hash.hexdigest()
    # Получить дату в формате Unix timestamp
    d = datetime.utcnow()
    timestamp = calendar.timegm(d.utctimetuple())
    # Сформировать зашифрованную подпись
    sing_str = "{0}&{1}&{2}&{3}".format(system_id, secret_id, nonce, timestamp)
    hashed = hmac.new(secret_id.encode('ascii'), sing_str.encode('ascii'), sha1)
    # Сгенерировать уникальный ключ безопасности запроса
    secret_token = base64.urlsafe_b64encode(hashed.digest())
    return secret_token

if __name__ == '__main__':
    SYSTEM_ID = 'testsystem_1'
    SECRET_ID = '5F27CEF4779428FDAFE2370E3CF6E8FAC6356AA3'
    token = create_token(SYSTEM_ID, SECRET_ID)
    print(token)
