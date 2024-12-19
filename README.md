# 🚀 **Browser Password Extractor**

An advanced Python script designed to **extract saved passwords** from popular web browsers such as Chrome, Firefox, Edge, Brave, and more. The script decrypts stored credentials to demonstrate how browser passwords are managed and secured. This tool is **intended for educational purposes only** and highlights the importance of securing your credentials against unauthorized access.

---

> ⚠️ **Important Disclaimer**: This tool is **not to be used for malicious purposes**. Ensure you have explicit permission before using it to access any device or account. Unauthorized access to data is illegal and a violation of privacy laws.

---

## 📋 **Table of Contents**

- [✨ Features](#✨-features)
- [🌐 Supported Browsers](#🌐-supported-browsers)
- [🛠️ Installation](#🛠️-installation)
- [🏃‍♂️ Usage](#🏃‍♂️-usage)
- [⚖️ Legal Disclaimer](#⚖️-legal-disclaimer)
- [📜 License](#📜-license)

---

## ✨ **Features**

- 🔐 **Extract passwords** from multiple browsers.
- 🛡️ **Decrypt** encrypted passwords using each browser’s unique encryption method.
- 💾 **Save extracted passwords** to a readable text file.
- 🌐 **Upload the file** to a file-sharing service (optional).
- 🔗 **Shorten the file URL** for easy sharing.
- 🖥️ **Send the file URL to a Discord channel**: Pick the webhook URL via the GUI and send the link directly to your Discord channel.

---

## 🌐 **Supported Browsers**

This script supports the following browsers:

- **Google Chrome**
- **Microsoft Edge**
- **Mozilla Firefox**
- **Brave**
- **Opera**
- **Vivaldi**
- **Yandex**
- **Chromium**

---

## 🛠️ **Installation**

To get started, you'll need **Python 3.x** and some essential libraries. These can be easily installed using `pip`. The script will automatically download and install the required dependencies for you.

### 1. Install Dependencies

Open a terminal or command prompt and run:

```bash
pip install pycryptodome requests pywin32
