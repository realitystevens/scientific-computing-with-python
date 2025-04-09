"""
Password Generator. Generates a random password based on user-defined constraints.
The password will include a mix of uppercase letters, lowercase letters, digits, and special characters.
"""

import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    while True:
        password = ''
        
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password


new_password = generate_password()
print('Generated password:', new_password)





if __name__=='__main__':
    generate_password()