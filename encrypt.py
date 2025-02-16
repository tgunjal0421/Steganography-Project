import hashlib
import os
import base64
from PIL import Image, PngImagePlugin

def encrypt_text(text, password):
    """Generate a hashed key and encrypt text using base64 encoding."""
    key = hashlib.sha256(password.encode()).hexdigest()[:16]
    encoded_text = base64.b64encode((key + text).encode()).decode()
    return encoded_text

def embed_text_in_image(image_path, text, password):
    """Embed encrypted text inside the image metadata."""
    img = Image.open(image_path)
    encrypted_text = encrypt_text(text, password)

    # Create PNG
    png_info = PngImagePlugin.PngInfo()
    png_info.add_text("hidden_message", encrypted_text)

    # Save the image
    img.save("encryptedimg.png", "PNG", pnginfo=png_info)

    print("Encryption complete. Use the same password for decryption.")
    
    os.system(f'start {image_path}')

# Get inputs
image_path = r'mypic.jpg'
text = input("Enter text to hide: ")
password = input("Enter encryption password: ")

# Encrypt and embed text
embed_text_in_image(image_path, text, password)

