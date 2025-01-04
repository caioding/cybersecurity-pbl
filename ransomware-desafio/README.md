# Ransomware Desafio

This project demonstrates a simple ransomware-like encryption and decryption process using Python. It includes scripts to encrypt and decrypt files using the `cryptography` library. This is a project that uses project-based learning to learn and teach encryption and decryption concepts.

## Files

- **[encrypter.py](encrypter.py)**: Script to encrypt a file.
- **[decrypter.py](decrypter.py)**: Script to decrypt a file.
- **[test.txt](test.txt)**: Sample text file to demonstrate encryption and decryption.
- **[requirements.txt](requirements.txt)**: List of Python dependencies.
- **[.gitignore](.gitignore)**: Git ignore file to exclude unnecessary files from version control.

## ⚙️ Setup

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

### 🔒 Encryption

1. Run the `encrypter.py` script to encrypt `test.txt`:
    ```bash
    python encrypter.py
    ```
2. The content of `test.txt` will be encrypted, and a `key.key` file will be generated.

### 🔓 Decryption

1. Ensure that the `key.key` file generated during encryption is in the same directory as `decrypter.py`.
2. Run the `decrypter.py` script to decrypt `test.txt`:
    ```bash
    python decrypter.py
    ```
3. The content of `test.txt` will be decrypted back to its original form.

## 📝 Note

- Ensure that the `key.key` file generated during encryption is kept safe, as it is required for decryption.
- This project is for educational purposes only. Use it responsibly.

## 📜 License

This project is licensed under the MIT License.