# SCT_CS_2
Image Encryption Tool (Task 02 – Cyber Security Internship at SkillCraft Technology)  


📖 Overview

This project is part of my Cyber Security Internship at SkillCraft Technology.
The Image Encryption Tool allows you to securely encrypt and decrypt images using:

🔒 XOR Cipher (key-based)

🔀 Pixel Shuffle (seed-based randomization)

#⚙️ Installation

You can run this project on Linux (Kali) or Windows.
A Python virtual environment is recommended.

#           🐧 On Kali Linux

# Update packages
sudo apt update

# Install Python & venv
sudo apt install python3 python3-venv -y

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
sudo apt install python3-pil python3-numpy -y

#           🪟 On Windows


# Check Python
python --version

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install pillow numpy


#        ▶️ Usage   #

#   🔹 XOR Method

  Encrypt

python image_encryption.py -i input.jpg -o enc_xor.png -m xor --mode encrypt --key 153


  Decrypt

python image_encryption.py -i enc_xor.png -o dec_xor.png -m xor --mode decrypt --key 153



#     🔹 Shuffle Method

  Encrypt

python image_encryption.py -i input.jpg -o enc_shuffle.png -m shuffle --mode encrypt --seed 98765

  Decrypt

python image_encryption.py -i enc_shuffle.png -o dec_shuffle.png -m shuffle --mode decrypt --seed 98765



*****************************************************************************
SCT_CS_2/
├── image_encryption.py     # Main script
├── README.md               # Documentation
├── requirements.txt        # Dependencies
└── examples/               # Example runs & screenshots

#   📸 Example Run

Encryption & Decryption Example:

python image_encryption.py -i input.jpg -o enc_xor.png -m xor --mode encrypt --key 153
python image_encryption.py -i enc_xor.png -o dec_xor.png -m xor --mode decrypt --key 153


#  ✅ Notes

Works with .jpg, .png, .bmp.

Key/Seed must be same for encryption & decryption.

Always run inside venv to avoid conflicts.

