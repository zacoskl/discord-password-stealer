# 🚀 Browser Password Extractor

A Python script to **extract saved passwords** from multiple web browsers like Chrome, Firefox, Edge, Brave, and more. The script demonstrates how encrypted passwords are stored in browser profiles and can be decrypted to gain access. This tool is for **educational purposes only** and showcases the importance of securing stored credentials.

## 📋 Table of Contents

- [Features](#features)
- [Supported Browsers](#supported-browsers)
- [Installation](#installation)
- [Usage](#usage)
- [Legal Disclaimer](#legal-disclaimer)

## 💡 Features

- **Extract passwords** from supported browsers.
- **Decrypt stored passwords** using browser-specific encryption methods.
- **Save passwords** to a file in a human-readable format.
- **Upload the file** to a file-sharing service (optional).
- **Shorten the file URL** for easier sharing.

## 🌐 Supported Browsers

This script currently supports the following browsers:

- **Google Chrome**
- **Microsoft Edge**
- **Mozilla Firefox**
- **Brave**
- **Opera**
- **Vivaldi**
- **Yandex**
- **Chromium**

The script can be easily customized to support additional browsers or exclude specific ones.

## 🛠️ Installation

To use this script, you'll need Python 3.x and a few Python libraries. You can install the required dependencies via `pip`:

```bash
pip install pycryptodome requests pywin32
