#!/usr/bin/env python3
import crypt
import requests
import urllib.parse
import string

BASE_URL = "http://10.10.239.40/"
USERNAME = "guest:"
SEPARATOR = ":"
CHARSET = string.printable

def get_secure_cookie(user_agent: str) -> str:
    session = requests.Session()
    response = session.get(BASE_URL, headers={"User-Agent": user_agent})
    cookie = session.cookies.get("secure_cookie")
    return urllib.parse.unquote(cookie)

def main():
    discovered = ""

    while True:
        ua_padding_length = (7 - len(USERNAME + SEPARATOR + discovered)) % 8
        user_agent = "A" * ua_padding_length
        prefix = USERNAME + user_agent + SEPARATOR + discovered

        block_index = len(prefix) // 8

        secure_cookie = get_secure_cookie(user_agent)
        target_block = secure_cookie[block_index * 13:(block_index + 1) * 13]
        salt = target_block[:2]

        found_char = False
        for char in CHARSET:
            candidate = (prefix + char)[-8:]
            candidate_hash = crypt.crypt(candidate, salt)
            if candidate_hash == target_block:
                discovered += char
                print(char, end="", flush=True)
                found_char = True
                break

        if not found_char:
            break

    print()

if __name__ == "__main__":
    main()
