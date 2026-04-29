# file: password_cli.py

from password_backend import generate_password

def main():
    print("=== PASSWORD GENERATOR (CLI) ===")

    try:
        length = int(input("Enter password length: "))
        upper = input("Include uppercase? (y/n): ").lower() == 'y'
        lower = input("Include lowercase? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, upper, lower, digits, symbols)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input!")

if __name__ == "__main__":
    main()
