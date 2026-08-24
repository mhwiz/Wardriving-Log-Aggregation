import tkinter as tk
from tkinter import filedialog
import os
import subprocess

clsc = 'cls' if os.name == "nt" else "clear"
subprocess.run(clsc, shell=True, check=True)

root = tk.Tk()
root.withdraw()

print("Base file")
base = filedialog.askopenfilename(
    title="Select Base File",
    filetypes=[("Log Files", "*.log")]
)

if not base:
    print("No base file selected.")
    exit()

print("Select file/s to add")
aggregate = filedialog.askopenfilenames(
    title="Select file/s to add",
    filetypes=[("Log Files", ".log")]
)

if not aggregate:
    print("No files selected.")
    exit()

with open(base, "r", encoding="utf-8") as file:
    base_lines = file.readlines()

combined_lines = []

for line in base_lines:
    clean = line.strip()
    if clean == "":
        continue
    combined_lines.append(clean + "\n")

for filename in aggregate:

    if filename == base:
        continue

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines[2:]:

            clean = line.strip()

            if clean == "":
                continue

            combined_lines.append(clean + "\n")

output_file = filedialog.asksaveasfilename(
    title="Aggregated",
    defaultextension=".log",
    filetypes=[("Log Files", ".log")]
)

if output_file:
    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(combined_lines)

    print(f"Combined file:{output_file}")
else:
    print("Job cancelled.")
