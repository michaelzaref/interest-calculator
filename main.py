import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import filedialog
from ttkbootstrap.dialogs import Messagebox
import csv
from datetime import datetime

# Global results holder
results_data = []

def calculate():
    global results_data
    try:
        initial_capital = float(entry_initial.get())
        interest_rate = float(entry_interest.get()) / 100
        inflation_rate = float(entry_inflation.get()) / 100
        base_cash = float(entry_cash.get())
        years = int(entry_years.get())

        capital = initial_capital
        tree.delete(*tree.get_children())
        results_data = []

        for year in range(1, years + 1):
            nominal_cash = base_cash * ((1 + inflation_rate) ** (year - 1))
            interest = capital * interest_rate
            capital += interest + nominal_cash
            real_capital = capital / ((1 + inflation_rate) ** (year - 1))

            row = {
                "Year": year,
                "Interest": round(interest, 2),
                "Nominal Cash Added": round(nominal_cash, 2),
                "Total Capital (Nominal)": round(capital, 2),
                "Total Capital (Real)": round(real_capital, 2)
            }
            results_data.append(row)
            tree.insert("", "end", values=tuple(row.values()))

    except Exception as e:
        Messagebox.show_error(f"An error occurred:\n{e}")

def export_csv():
    if not results_data:
        Messagebox.show_info("There is no data to export.\nPlease click 'Calculate' first.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    default_filename = f"capital_report_{timestamp}.csv"

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save as",
        initialfile=default_filename
    )

    if file_path:
        try:
            with open(file_path, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=results_data[0].keys())
                writer.writeheader()
                writer.writerows(results_data)
            Messagebox.show_info(f"CSV exported successfully to:\n{file_path}")
        except Exception as e:
            Messagebox.show_error(f"Failed to save CSV:\n{e}")

# App setup
app = tb.Window(themename="cosmo")
app.title("Capital Growth Calculator")
app.geometry("850x550")

# Input frame
frame_inputs = tb.Frame(app, padding=10)
frame_inputs.pack(fill=X, padx=10, pady=10)

# Input fields
fields = [
    ("Initial Capital", "1000"),
    ("Interest Rate (%)", "50"),
    ("Inflation Rate (%)", "25"),
    ("Base Cash (Year 1)", "500"),
    ("Years", "5")
]

entries = []
for i, (label, default) in enumerate(fields):
    lbl = tb.Label(frame_inputs, text=label)
    lbl.grid(row=i, column=0, sticky=W, pady=5)
    entry = tb.Entry(frame_inputs)
    entry.insert(0, default)
    entry.grid(row=i, column=1, pady=5, padx=10, sticky=EW)
    entries.append(entry)

entry_initial, entry_interest, entry_inflation, entry_cash, entry_years = entries

# Buttons
btn_calc = tb.Button(frame_inputs, text="Calculate", bootstyle=PRIMARY, command=calculate)
btn_calc.grid(row=len(fields), column=0, pady=10)

btn_export = tb.Button(frame_inputs, text="Export CSV", bootstyle=SUCCESS, command=export_csv)
btn_export.grid(row=len(fields), column=1, pady=10)

# Treeview
cols = ["Year", "Interest", "Nominal Cash Added", "Total Capital (Nominal)", "Total Capital (Real)"]
tree = tb.Treeview(app, columns=cols, show="headings", bootstyle=INFO)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=160)
tree.pack(fill=BOTH, expand=YES, padx=10, pady=10)

app.mainloop()
