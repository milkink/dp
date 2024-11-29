from itertools import product

def brute_force_attack(password):
    words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    max_len = len(password)
    count = 0

    for r in range(1, max_len + 1):
        for combo in product(words, repeat=r):
            count += 1
            if ''.join(combo) == password:
                print(''.join(combo), "is found after", count, "combinations")
                return

password = input("Enter the password: ")
brute_force_attack(password)
