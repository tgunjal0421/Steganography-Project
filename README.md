# **🔒 Image-Based Steganography using Python**  

## **📌 Overview**  
This project implements **image-based steganography**, allowing users to **hide and retrieve secret messages within images** using **password-based encryption**. The hidden text is securely stored in the image metadata, ensuring **confidentiality without altering the image quality**.  

---

## **⚡ Features**  
✅ **Secure Text Hiding** – Encrypts text inside image metadata using a password.  
✅ **Lossless Steganography** – Image quality remains unchanged after encryption.  
✅ **Password Protection** – Only the correct password can decrypt the hidden message.  
✅ **Lightweight & Efficient** – No significant increase in file size.  
✅ **Simple Command-Line Interface** – Easy to use with minimal dependencies.  

---

## **🛠️ Technologies Used**  
- **Python** – Core programming language  
- **Pillow (PIL)** – Image processing  
- **Hashlib** – Password hashing  
- **Base64** – Encoding & decoding  
- **Git & GitHub** – Version control  
- **VS Code** – Development environment  

---

## **📜 How It Works?**  
### **🔐 Encryption Process:**  
1️⃣ User selects an **image** and **enters a text message**.  
2️⃣ A **password** is used to encrypt the message securely.  
3️⃣ The encrypted text is **embedded in the image metadata**.  
4️⃣ The modified image is saved as `encryptedimg.png`.  

### **🔓 Decryption Process:**  
1️⃣ User selects the **encrypted image** and enters the **password**.  
2️⃣ The hidden text is **retrieved and decrypted**.  
3️⃣ If the password is incorrect, the message **remains unreadable**.  

---

## **📸 Screenshots**  
![image](https://github.com/user-attachments/assets/63ef3cc3-350e-4f88-a0ea-eaebb459965e)

---

## **🎯 Future Enhancements**  
🚀 **Automated Batch Processing** – Encrypt multiple images at once.  
🔐 **Stronger Encryption** – Implement AES or hybrid encryption.  
📱 **Mobile & Web Integration** – Develop a cross-platform application.  
🤖 **AI-Based Detection** – Identify steganography-based security threats.  

---

## **📌 Contributing**  
Feel free to **fork this repository**, create a **new branch**, and submit a **pull request** with improvements!  

---

## **📄 License**  
This project is **open-source** under the **MIT License**.  

---

