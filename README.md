💰 Capital Growth Calculator
A modern Python GUI app to calculate capital growth over time with:

✅ Compound interest

✅ Inflation adjustment

✅ Annually increasing cash injections

All with exportable CSV reports!

Built using ttkbootstrap for a clean, modern interface.

✨ Features
📈 Compound capital growth:

Annual interest rate

Annual inflation

Yearly contributions (inflation-adjusted)

🪄 Modern UI with input validation

📊 Real vs Nominal capital tracking

📂 CSV export with timestamped reports

🛡️ Robust error handling with info popups

✅ Executable build (.exe) for easy sharing

🖼️ Screenshot


Clean and intuitive interface for visualizing capital growth over time.

🚀 Getting Started
✅ Prerequisites
Install dependencies and run the app:

bash
Copy
Edit
pip install ttkbootstrap
python main.py
🏗️ Build .EXE for Windows
Use PyInstaller to build a standalone executable:

bash
Copy
Edit
pip install pyinstaller
pyinstaller --onefile --windowed main.py
Output will be located in the dist/ directory:

css
Copy
Edit
dist/
└── main.exe ✅
📤 Export Example
When you click “Export CSV”, a file like this will be generated:

capital_report_2025-07-11-15-30-10.csv

Year	Interest	Nominal Cash Added	Total Capital (Nominal)	Total Capital (Real)
1	500.00	500.00	2000.00	2000.00
2	1000.00	625.00	3625.00	2900.00
...	...	...	...	...

🛠️ Technologies Used
🐍 Python 3

🎨 ttkbootstrap (modern Tkinter theming)

📦 csv, datetime, tkinter.filedialog

📄 License
MIT License — feel free to use, modify, and share this project.

🙌 Author
Michael Zaref
💼 Software Engineer
📧 mzaref360@gmail.com
🔗 linkedin.com/in/michael-zaref-82ba1b1a4
🐙 github.com/michaelzaref

⭐️ Show Your Support
If you like this project, please star ⭐ the repo and share it with others!

