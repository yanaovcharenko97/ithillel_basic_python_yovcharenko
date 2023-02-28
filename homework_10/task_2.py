from random import choice
from string import ascii_letters, digits


def generate_password(length):
    allowed_chars = ascii_letters + digits + "_"
    length = max(length, 8)

    while True:
        password = "".join(choice(allowed_chars) for _ in range(length))

        if (any(i.islower() for i in password) and
                any(i.isupper() for i in password) and
                any(i.isdigit() for i in password) and
                all(password[idx] != password[idx + 1] for idx in range(len(password) - 1))):
            return password


def main():
    password = generate_password(20)
    print(password)


if __name__ == "__main__":
    main()
