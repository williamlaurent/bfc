import itertools
import string

def brute_force_crack(password_length, charset):
    for attempt in itertools.product(charset, repeat=password_length):
        password = "".join(attempt)
        print(f"Trying password: {password}")

if __name__ == "__main__":
    password_length = int(input("Enter the password length: "))
    charset = string.ascii_letters + string.digits + string.punctuation
    brute_force_crack(password_length, charset)
