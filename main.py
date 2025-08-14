from PIL import Image

def encrypt_image(input_path, output_path, key):
    """Encrypt the image by adding 'key' to each pixel's RGB values."""
    img = Image.open(input_path)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print(f"[+] Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    """Decrypt the image by subtracting 'key' from each pixel's RGB values."""
    img = Image.open(input_path)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print(f"[+] Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    key = 50  # Secret key (integer between 1-255)

    # Encrypt the original image
    encrypt_image("original.jpg", "encrypted.png", key)

    # Decrypt the image back to original
    decrypt_image("encrypted.png", "decrypted.png", key)
