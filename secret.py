# importing the function from utils
from django.core.management.utils import get_random_secret_key


def main():
    print("Generating and printing a new SECRET_KEY:\n")
    print(f"SECRET_KEY={get_random_secret_key()}")


if __name__ == "__main__":
    main()
