import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password contains at least one of each character type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices from all characters
    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number.")
