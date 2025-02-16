import hashlib
import base64
from PIL import Image

def decrypt_text(encrypted_text, password):
    """Decrypt the text using the same password."""
    key = hashlib.sha256(password.encode()).hexdigest()[:16]
    decoded_text = base64.b64decode(encrypted_text).decode()
    if decoded_text.startswith(key):
        return decoded_text[len(key):]
    else:
        return "Incorrect password! Decryption failed."

def extract_text_from_image(image_path, password):
    """Extract and decrypt the hidden message from the image metadata."""
    img = Image.open(image_path)
    metadata = img.info

    if "hidden_message" in metadata:
        encrypted_text = metadata["hidden_message"]
        decrypted_text = decrypt_text(encrypted_text, password)
        print("Decrypted Message:", decrypted_text)
    else:
        print("No hidden message found in the image.")

# Get inputs
image_path = r'encryptedimg.png'
password = input("Enter decryption password: ")

# Extract and decrypt text
extract_text_from_image(image_path, password)
