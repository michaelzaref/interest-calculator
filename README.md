# 💰 Capital Growth Calculator

A modern Python GUI app to calculate capital growth over time with compound interest, inflation, and annually increasing cash injections — all with exportable CSV reports!

Built with [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) for a clean, stylish interface.

---

## ✨ Features

- 📈 Calculates compound capital growth with:
  - Annual interest rate
  - Annual inflation
  - Increasing yearly contributions (adjusted for inflation)
- 🪄 Modern GUI design with input validation
- 📊 Real vs Nominal capital tracking
- 📂 Export results to a timestamped `.csv` report
- 🛡️ Error handling and info popups
- ✅ Built as `.exe` for easy distribution (see below)

---

## 🖼️ Screenshot

![screenshot](assets/screenshot.png)

> *Example of the capital growth report in a modern interface.*

---

## 🚀 Getting Started

### ✅ Prerequisites

Install the required package:

```bash
pip install ttkbootstrap
python main.py

🏗️ Build .EXE (Windows)
Use PyInstaller to convert to an executable:

pip install pyinstaller

pyinstaller --onefile --windowed main.py
Output will be in the dist/ folder:
dist/
└── main.exe ✅

📤 Export Example
When you click "Export CSV", it will generate a file like:

capital_report_2025-07-11-15-30-10.csv
| Year | Interest | Nominal Cash Added | Total Capital (Nominal) | Total Capital (Real) |
| ---- | -------- | ------------------ | ----------------------- | -------------------- |
| 1    | 500.00   | 500.00             | 2000.00                 | 2000.00              |
| 2    | 1000.00  | 625.00             | 3625.00                 | 2900.00              |
| ...  | ...      | ...                | ...                     | ...                  |


🛠️ Technologies Used
🐍 Python 3

🎨 ttkbootstrap (modern Tkinter theming)

📦 csv, datetime, tkinter.filedialog

📄 License
MIT License — feel free to use, modify, and distribute.

🙌 Author
Michael Zaref
💼 Software Engineer
📧 mzaref360@gmail.com
🔗 linkedin.com/in/michael-zaref-82ba1b1a4
🐙 github.com/michaelzaref

⭐️ Show your support
If you like this project, please ⭐️ the repo and share it!
