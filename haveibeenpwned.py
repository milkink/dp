import requests
import hashlib

# Read the file containing usernames and passwords
with open('pw.txt', 'r') as f:
    for line in f:
        # Split the line into username and password
        username, password = line.strip().split(',')

        # Hash the password using SHA-1 algorithm
        password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

        # Make a request to "Have I Been Pwned" API to check if the password has been leaked
        response = requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")

        # If the response status code is 200, it means the password has been leaked
        if response.status_code == 200:
            # Get the list of hashes of leaked passwords that start with the same prefix
            hashes = [line.split(':') for line in response.text.splitlines()]
            
            # Check if the hash of the input password matches any of the leaked passwords
            for h, count in hashes:
                if password_hash[5:] == h:
                    print(f"Password for user {username} has been leaked {count} times.")
                    break
        else:
            print(f"Could not check password for user {username}.")






