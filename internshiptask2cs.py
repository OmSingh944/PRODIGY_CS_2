from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img, dtype=np.uint8)

    # Add key to every pixel (mod 256)
    encrypted = (arr.astype(np.uint16) + key) % 256
    encrypted = encrypted.astype(np.uint8)

    Image.fromarray(encrypted).save(output_path)
    print(f"Encrypted image saved as: {output_path}")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img, dtype=np.uint8)

    # Subtract key from every pixel (mod 256)
    decrypted = (arr.astype(np.int16) - key) % 256
    decrypted = decrypted.astype(np.uint8)

    Image.fromarray(decrypted).save(output_path)
    print(f"Decrypted image saved as: {output_path}")

def main():
    print("===== Image Encryption Tool =====")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Enter your choice (1/2): ")

    input_path = input("Enter image file name (e.g., photo.jpg): ")
    output_path = input("Enter output file name (e.g., output.png): ")
    key = int(input("Enter secret key (0-255): ")) % 256

    if choice == "1":
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()