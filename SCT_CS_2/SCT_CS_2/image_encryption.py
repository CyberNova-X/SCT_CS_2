"""
Image Encryption Tool (Pixel Manipulation)
Author: Gaurang Bhatt
Internship: SkillCraft Technology (Cyber Security Track)
Task 02: Simple image encryption using pixel manipulation
Methods: XOR-per-pixel, Pixel Shuffle (seeded)
"""

import argparse
from PIL import Image
import numpy as np
import os
import sys
from typing import Tuple

def ensure_rgb(img: Image.Image) -> Image.Image:
    if img.mode != "RGB":
        return img.convert("RGB")
    return img

def xor_bytes(arr: np.ndarray, key: int) -> np.ndarray:
    key = key % 256
    return np.bitwise_xor(arr, key)

def seeded_permutation(n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    perm = np.arange(n)
    rng.shuffle(perm)
    return perm

def inverse_permutation(perm: np.ndarray) -> np.ndarray:
    inv = np.empty_like(perm)
    inv[perm] = np.arange(len(perm))
    return inv

def shuffle_pixels(arr: np.ndarray, seed: int, encrypt: bool = True) -> np.ndarray:
    h, w, c = arr.shape
    flat = arr.reshape(-1, c)
    perm = seeded_permutation(flat.shape[0], seed)
    if encrypt:
        shuffled = flat[perm]
    else:
        inv = inverse_permutation(perm)
        shuffled = flat[inv]
    return shuffled.reshape(h, w, c)

def process_image(input_path: str, output_path: str, method: str, mode: str, key: int, seed: int) -> None:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input image not found: {input_path}")
    img = Image.open(input_path)
    img = ensure_rgb(img)
    arr = np.array(img, dtype=np.uint8)

    if method == "xor":
        if mode == "encrypt":
            out = xor_bytes(arr, key)
        elif mode == "decrypt":
            out = xor_bytes(arr, key)
        else:
            raise ValueError("mode must be 'encrypt' or 'decrypt'")

    elif method == "shuffle":
        if mode == "encrypt":
            out = shuffle_pixels(arr, seed, encrypt=True)
        elif mode == "decrypt":
            out = shuffle_pixels(arr, seed, encrypt=False)
        else:
            raise ValueError("mode must be 'encrypt' or 'decrypt'")
    else:
        raise ValueError("Unknown method. Use 'xor' or 'shuffle'.")

    out_img = Image.fromarray(out)
    out_img.save(output_path)
    print(f"[OK] Saved: {output_path}")

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Simple Image Encryption Tool (XOR / Shuffle)")
    p.add_argument("--input", "-i", required=True, help="Path to input image (any format supported by Pillow)")
    p.add_argument("--output", "-o", required=True, help="Path to output image")
    p.add_argument("--method", "-m", choices=["xor", "shuffle"], required=True, help="Encryption method")
    p.add_argument("--mode", choices=["encrypt", "decrypt"], required=True, help="Operation mode")
    p.add_argument("--key", type=int, default=123, help="XOR key (0-255) - used when method=xor")
    p.add_argument("--seed", type=int, default=12345, help="Shuffle seed (integer) - used when method=shuffle")
    return p.parse_args()

if __name__ == "__main__":
    try:
        args = parse_args()
        process_image(args.input, args.output, args.method, args.mode, args.key, args.seed)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)