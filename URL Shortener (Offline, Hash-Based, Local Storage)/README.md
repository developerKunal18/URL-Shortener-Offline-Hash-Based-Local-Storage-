# 🌐 Offline URL Shortener 

## 💡 Overview
The **Offline URL Shortener** is a Python-based tool that converts long URLs into short, easy-to-share codes — without using any API, internet connection, or web server.

It demonstrates how real-world URL shortening services work by combining **hashing**, **base62 encoding**, and **local persistence** using a JSON database.

---

## 🚀 Features

### ✔ URL Shortening
Converts long URLs into short 6-character codes.

### ✔ URL Expansion
Expands a short code back to the original URL.

### ✔ Offline & Local
Works completely offline using a local JSON file.

### ✔ Collision-Resistant
Uses SHA-256 hashing to reduce collisions.

### ✔ Lightweight
No external libraries required.

### ✔ Persistent Storage
All shortened URLs are saved in `urls.json`.

---

## 🧠 Concepts & Technologies Used
- Python
- SHA-256 hashing
- Base62 encoding
- JSON-based data storage
- String encoding & decoding
- CLI menu-driven interface

---

## 📦 Installation

No dependencies required.

### Run the program:
```bash
python url_shortener.py
