# 🖼️ Image Encryption Tool – Task 02

## 📌 Overview
This project is part of my **Cyber Security Internship at SkillCraft Technology**.  
The task is to develop a **simple image encryption tool** using **pixel manipulation**.

Two reversible methods are implemented:
1. **XOR**: Applies an XOR operation with a user-provided key to each pixel channel (0–255).  
2. **Shuffle**: Deterministically shuffles pixels using a user-provided random **seed** (and unshuffles for decryption).

> ⚠️ Educational tool for learning basic image security concepts. Not intended for production-grade confidentiality.

---

## 🧱 Project Structure
```
SCT_CS_2/
├─ image_encryption.py
├─ README.md
└─ examples/
   └─ (add your screenshots or sample images here)
```

---

## 🛠️ Installation

### Option A: Quick Run (System Python)
1) Ensure Python 3.8+ is installed  
   ```bash
   python --version
   # or
   python3 --version
   ```
2) Install dependencies
   ```bash
   pip install pillow numpy
   # or
   pip3 install pillow numpy
   ```

### Option B: Virtual Environment (Recommended)
```bash
python -m venv .venv
# Activate:
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Linux/macOS
# source .venv/bin/activate

pip install --upgrade pip
pip install pillow numpy
```

---

## 🚀 Usage

### 1) XOR Method (symmetric, same key to decrypt)
**Encrypt**
```bash
python image_encryption.py -i input.jpg -o enc_xor.png -m xor --mode encrypt --key 153
```
**Decrypt**
```bash
python image_encryption.py -i enc_xor.png -o dec_xor.png -m xor --mode decrypt --key 153
```

### 2) Shuffle Method (seeded permutation)
**Encrypt**
```bash
python image_encryption.py -i input.jpg -o enc_shuffle.png -m shuffle --mode encrypt --seed 98765
```
**Decrypt**
```bash
python image_encryption.py -i enc_shuffle.png -o dec_shuffle.png -m shuffle --mode decrypt --seed 98765
```

> Tip: PNG is recommended for encrypted outputs to avoid JPEG compression artifacts.

---

## ✅ Notes
- All processing is done in **RGB**; alpha channel (if any) is dropped for simplicity.
- XOR with any integer is supported (internally reduced to 0–255).
- Shuffle uses a deterministic permutation derived from the given seed; using the **same seed** reverses it.

---

## 🏆 Internship Info
- **Internship Track:** Cyber Security  
- **Track Code:** CS  
- **Task 02:** Image Encryption Tool  
- **Organization:** SkillCraft Technology