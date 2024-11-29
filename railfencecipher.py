def rail_fence_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    direction_down = False
    row, col = 0, 0
    
    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        rail[row][col] = char
        col += 1
        row += 1 if direction_down else -1
    
    encrypted_text = ''.join([''.join(row) for row in rail if row != '\n'])
    return encrypted_text.replace('\n', '')

def rail_fence_decrypt(cipher_text, key):
    rail = [['\n' for _ in range(len(cipher_text))] for _ in range(key)]
    direction_down = None
    row, col = 0, 0
    
    for _ in cipher_text:
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher_text)):
            if rail[i][j] == '*' and index < len(cipher_text):
                rail[i][j] = cipher_text[index]
                index += 1
    
    result = []
    row, col = 0, 0
    for _ in range(len(cipher_text)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        row += 1 if direction_down else -1
    return ''.join(result)

def main():
    while True:
        print("\nRail Fence Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            key = int(input("Enter key (number of rails): "))
            encrypted_text = rail_fence_encrypt(text, key)
            print(f"Encrypted text: {encrypted_text}")
        elif choice == '2':
            cipher_text = input("Enter text to decrypt: ")
            key = int(input("Enter key (number of rails): "))
            decrypted_text = rail_fence_decrypt(cipher_text, key)
            print(f"Decrypted text: {decrypted_text}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
