import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length
        self.alphabets = string.ascii_letters
        self.digits = string.digits
        self.special_characters = string.punctuation
        self.password_characters = list(self.alphabets + self.digits + self.special_characters)

    def generate_random_password(self):
        """Generate a password with random characters."""
        return "".join(random.sample(self.password_characters, self.length))

    def generate_password_with_conditions(self, alpha_count, digit_count, special_count):
        """Generate a password based on specified counts."""
        total_count = alpha_count + digit_count + special_count
        if total_count > self.length:
            raise ValueError("Total character count exceeds password length.")
        password = []
        password.extend(random.choices(self.alphabets, k=alpha_count))
        password.extend(random.choices(self.digits, k=digit_count))
        password.extend(random.choices(self.special_characters, k=special_count))
        if total_count < self.length:
            password.extend(random.choices(self.password_characters, k=self.length - total_count))
        random.shuffle(password)
        return "".join(password)

# Example Usage
try:
    print("1: Generate password with conditions")
    print("2: Generate random password")
    option = input("Choose an option: ")
    length = int(input("Enter password length: "))

    generator = PasswordGenerator(length)

    if option == "1":
        alpha = int(input("Enter the number of alphabets: "))
        digits = int(input("Enter the number of digits: "))
        special = int(input("Enter the number of special characters: "))
        print("Generated Password:", generator.generate_password_with_conditions(alpha, digits, special))
    elif option == "2":
        print("Generated Password:", generator.generate_random_password())
    else:
        print("Invalid option selected.")
except ValueError as e:
    print("Error:", e)

