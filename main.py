import hashlib
import os

def find_password(hash_type, hash_value):
    hash_functions = {
        'md5': hashlib.md5,
        'sha512': hashlib.sha512,
        'sha256': hashlib.sha256,
    }

    hash_function = hash_functions.get(hash_type)
    if not hash_function:
        print("Unsupported hash type.")
        return

    current_folder = os.path.dirname(os.path.abspath(__file__))
    wordlist_path = os.path.join(current_folder, 'wordlist.txt')

    with open(wordlist_path, 'r', encoding='utf-8') as file:
        for line in file:
            hashed_word = hash_function(line.strip().encode()).hexdigest()
            if hashed_word == hash_value:
                print('[***] Found Password in list:', line.strip())
                return

    print("error")

if __name__ == "__main__":
    hash_type = input("hash type: ").lower()
    hash_value = input("hash value: ")

    find_password(hash_type, hash_value)
