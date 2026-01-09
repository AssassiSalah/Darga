import tkinter as tk
from tkinter import messagebox
from transform import transform_word

# -------------------------------------------------
# 3. FUNCTION CALLED WHEN USER PRESSES THE BUTTON
# -------------------------------------------------
def process_word():
    word = entry.get().strip()
    if not word:
        messagebox.showerror("Error", "Please enter a word!")
        return

    transformed = transform_word(word)
    output_label.config(text=f"Output: {transformed}")

    # Save original + transformed to file
    with open("file.txt", "a", encoding="utf-8") as f:
        f.write(f"{word} -> {transformed}\n")

    messagebox.showinfo("Saved", "Word saved to file.txt!")

# -----------------------------------------
# 4. GUI CREATION USING TKINTER
# -----------------------------------------
root = tk.Tk()
root.title("Letter Replacement Encoder")
root.geometry("400x250")

title_label = tk.Label(root, text="Letter Encoder", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter your word:")
entry_label.pack()

entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=5)

btn = tk.Button(root, text="Transform", font=("Arial", 12), command=process_word)
btn.pack(pady=10)

output_label = tk.Label(root, text="Output: ", font=("Arial", 14))
output_label.pack(pady=10)

root.mainloop()
