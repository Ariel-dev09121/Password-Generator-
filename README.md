# 🔐 Secure Password Generator

A modern, dark-themed password generator built with **Python** and **Tkinter**.
Generate strong, cryptographically secure passwords with a clean and intuitive interface.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📸 Preview

> *(Add a screenshot or GIF here — e.g. `![preview](screenshot.png)`)*

---

## ✨ Features

- 🔒 **Cryptographically secure** — uses Python's `secrets` module instead of `random`
- 🎨 **Modern dark UI** with a custom color palette
- 🎛️ **Customizable character sets** — toggle uppercase, lowercase, digits, and symbols
- 📏 **Flexible length** — from 4 to 128 characters
- ✅ **Robust input validation** — rejects letters, empty input, `0`, and out-of-range values
- 💪 **Strength indicator** — visual feedback based on length and character variety
- 📋 **Copy to clipboard** with a single click
- © **Dynamic author footer** — auto-updates the year using `datetime`

---

## 🚀 Getting Started

### Requirements

- Python **3.8+**
- `tkinter` (usually bundled with Python — on Linux you may need `sudo apt install python3-tk`)

No external dependencies are required. 🎉

### Run the app

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python password_generator.py# Password-Generator-
