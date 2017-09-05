import base64
import hmac
import uuid

from hashlib import sha1
from datetime import datetime


def create_token(system_id, secret_id, string=None):
    # Сгенерировать рандомную строку
    rnd_str = str(uuid.uuid4()).encode('ascii') if not string else string.encode('ascii')
    # Получить хэш от этой строки
    nonce_hash = sha1(rnd_str)
    nonce = nonce_hash.hexdigest().upper()
    # Получить дату в формате Unix timestamp
    timestamp = str(datetime.now().timestamp()).replace('.', ',')
    # Сформировать зашифрованную подпись
    sing_str = "{0}&{1}&{2}&{3}".format(secret_id, system_id, nonce, timestamp)
    hashed = hmac.new(secret_id.encode('ascii'), sing_str.encode('ascii'), sha1)
    # Сгенерировать уникальный ключ безопасности запроса
    secret_token = base64.urlsafe_b64encode(hashed.digest())
    res = dict(nonce=nonce, timestamp=timestamp, token=secret_token, system_id=system_id)
    return res

if __name__ == '__main__':
    SYSTEM_ID = 'testsystem'
    SECRET_ID = '5F27CEF4779428FDAFE2370E3CF6E8FAC6356AA3'
    RND_STR = '2cbbf1dd-6bbc-447b-8889-977082c965cb'
    token = create_token(SYSTEM_ID, SECRET_ID)
    [print(key, ' - ', value) for key, value in token.items()]


# Online C# compiler - http://rextester.com/
"""
using System;
using System.Security.Cryptography;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Your code goes here
            Test.DoStuff();
        }
    }

    public class Test {

        const string systemID = "testsystem";
        const string secretID = "5F27CEF4779428FDAFE2370E3CF6E8FAC6356AA3";

        public static void DoStuff() {

            // случайная последовательность символов
            Random rnd = new Random();
            string nonce = SHA1(rnd.Next().ToString());
            //string nonce = SHA1("2cbbf1dd-6bbc-447b-8889-977082c965cb");
            // 64 битное число секунд в формате Unix timestamp.
            string timestamp = (DateTime.UtcNow - new DateTime(1970, 1, 1)).TotalSeconds.ToString();
            // зашифрованная подпись
            //string timestamp = "1504597541";
            string sing_str = string.Format("{0}&{1}&{2}&{3}", secretID, systemID, nonce, timestamp);
            string token = Hash(sing_str, secretID);
            Console.WriteLine(nonce);
            Console.WriteLine(timestamp);
            Console.WriteLine(token);
        }

         private static string Hash(string message, string secretKey) {
            byte[] msgBytes = System.Text.Encoding.ASCII.GetBytes(message);
            byte[] keyBytes = System.Text.Encoding.ASCII.GetBytes(secretKey);
            byte[] hashBytes;
            using (HMACSHA1 hmac = new HMACSHA1(keyBytes)){
                hashBytes = hmac.ComputeHash(msgBytes);
            }
            return System.Convert.ToBase64String(hashBytes);
         }

         private static string SHA1(string stringToHash) {
             // SHA1 is 160bit
            SHA1 sha = new SHA1Managed();
            byte[] hash = sha.ComputeHash(Encoding.ASCII.GetBytes(stringToHash));
            StringBuilder stringBuilder = new StringBuilder();
            foreach (byte b in hash) {
                stringBuilder.AppendFormat("{0:x2}", b);
            }
            return stringBuilder.ToString().ToUpper();
         }
    }
}
"""