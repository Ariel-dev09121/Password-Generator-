import tkinter as tk
from tkinter import ttk
import string
import secrets
from datetime import datetime          # 1) import datetime

# ============================================================
#  AUTHOR
# ============================================================
AUTHOR = "Ariel"   # 👈 change this to your real name if you want

# ============================================================
#  COLOR PALETTE
# ============================================================
COLOR_BG       = "#0f172a"
COLOR_PANEL    = "#1e293b"
COLOR_ACCENT   = "#38bdf8"
COLOR_ACCENT2  = "#a855f7"
COLOR_TEXT     = "#f1f5f9"
COLOR_GRAY     = "#64748b"
COLOR_ERROR    = "#ef4444"
COLOR_OK       = "#22c55e"

# ============================================================
#  FOOTER FUNCTION (adapted to the dark theme)
# ============================================================
def add_footer(window):
    """Adds a separator line and the footer with the current year."""
    year = datetime.now().year         # 2) dynamic current year
    text = f"© {year} {AUTHOR} - All rights reserved"

    # Separator adapted to the dark theme
    separator = tk.Frame(window, height=1, bg=COLOR_PANEL)
    separator.pack(side="bottom", fill="x")

    # Footer label
    footer = tk.Label(window, text=text,
                      font=("Arial", 8),
                      bg=COLOR_BG, fg=COLOR_GRAY)
    footer.pack(side="bottom", pady=4)
    return footer

# ============================================================
#  WINDOW
# ============================================================
window = tk.Tk()
window.title("🔐 Secure Password Generator")
window.geometry("520x700")        # a bit taller for the footer
window.configure(bg=COLOR_BG)
window.resizable(False, False)

# 👇 IMPORTANT: the footer is created BEFORE the large widgets
add_footer(window)

# ============================================================
#  FUNCTIONS
# ============================================================
def get_alphabet():
    alphabet = ""
    if var_upper.get():    alphabet += string.ascii_uppercase
    if var_lower.get():    alphabet += string.ascii_lowercase
    if var_digits.get():   alphabet += string.digits
    if var_symbols.get():  alphabet += string.punctuation
    return alphabet


def calculate_strength(length, type_count):
    if type_count == 0:
        return "No options", COLOR_ERROR
    points = 0
    if length >= 12:   points += 2
    elif length >= 8:  points += 1
    points += type_count

    if points >= 6:   return "💪 Very strong", COLOR_OK
    elif points >= 4: return "✅ Strong", "#84cc16"
    elif points >= 2: return "⚠️ Weak", "#f59e0b"
    else:             return "❌ Very weak", COLOR_ERROR


def generate():
    text = entry_length.get().strip()

    if text == "":
        status_label.config(text="⚠️ Enter a length", fg=COLOR_ERROR)
        return

    if not text.isdigit():
        status_label.config(
            text="❌ Numbers only (no letters or symbols)",
            fg=COLOR_ERROR
        )
        return

    length = int(text)

    if length == 0:
        status_label.config(text="❌ Length cannot be 0", fg=COLOR_ERROR)
        return

    if length < 4:
        status_label.config(
            text="❌ Minimum 4 characters for safety", fg=COLOR_ERROR
        )
        return

    if length > 128:
        status_label.config(text="❌ Maximum 128 characters", fg=COLOR_ERROR)
        return

    alphabet = get_alphabet()
    if alphabet == "":
        status_label.config(
            text="❌ Select at least one character option", fg=COLOR_ERROR
        )
        return

    password = "".join(secrets.choice(alphabet) for _ in range(length))
    password_label.config(text=password, fg=COLOR_ACCENT)

    type_count = sum([var_upper.get(), var_lower.get(),
                      var_digits.get(), var_symbols.get()])
    strength_text, strength_color = calculate_strength(length, type_count)
    strength_label.config(text=f"Strength: {strength_text}", fg=strength_color)

    status_label.config(text="✅ Password generated with secrets", fg=COLOR_OK)
    copy_button.config(state="normal")


def copy():
    password = password_label.cget("text")
    if password and password != "—":
        window.clipboard_clear()
        window.clipboard_append(password)
        status_label.config(text="📋 Copied to clipboard", fg=COLOR_ACCENT2)

# ============================================================
#  HEADER
# ============================================================
tk.Label(window, text="🔐 Password Generator",
         font=("Arial", 20, "bold"),
         bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=(25, 5))

tk.Label(window, text="Secure, random and unpredictable",
         font=("Arial", 10),
         bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=(0, 20))

# ============================================================
#  LENGTH PANEL
# ============================================================
length_panel = tk.Frame(window, bg=COLOR_PANEL, padx=20, pady=15)
length_panel.pack(fill="x", padx=40, pady=5)

tk.Label(length_panel, text="Password length:",
         font=("Arial", 11, "bold"),
         bg=COLOR_PANEL, fg=COLOR_TEXT).pack(anchor="w")

entry_length = tk.Entry(length_panel, font=("Courier", 14),
                        bg="#0b1220", fg=COLOR_ACCENT,
                        insertbackground=COLOR_ACCENT,
                        relief="flat", justify="center",
                        width=10)
entry_length.pack(pady=8)
entry_length.insert(0, "16")

tk.Label(length_panel, text="Numbers only • min 4 • max 128",
         font=("Arial", 9),
         bg=COLOR_PANEL, fg=COLOR_GRAY).pack()

# ============================================================
#  OPTIONS PANEL
# ============================================================
options_panel = tk.LabelFrame(window, text=" What to include? ",
                              font=("Arial", 10, "bold"),
                              bg=COLOR_BG, fg=COLOR_ACCENT,
                              labelanchor="nw",
                              bd=1, relief="solid")
options_panel.pack(fill="x", padx=40, pady=15)

var_upper   = tk.BooleanVar(value=True)
var_lower   = tk.BooleanVar(value=True)
var_digits  = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

def create_check(text, var):
    return tk.Checkbutton(options_panel, text=text, variable=var,
                          bg=COLOR_BG, fg=COLOR_TEXT,
                          selectcolor=COLOR_PANEL,
                          activebackground=COLOR_BG,
                          activeforeground=COLOR_ACCENT,
                          font=("Arial", 10),
                          anchor="w")

create_check("Uppercase   (A-Z)", var_upper).pack(fill="x", padx=15, pady=3)
create_check("Lowercase   (a-z)", var_lower).pack(fill="x", padx=15, pady=3)
create_check("Digits      (0-9)", var_digits).pack(fill="x", padx=15, pady=3)
create_check("Symbols     (!@#$...)", var_symbols).pack(fill="x", padx=15, pady=3)

# ============================================================
#  GENERATE BUTTON
# ============================================================
generate_button = tk.Button(window, text="⚡ GENERATE PASSWORD",
                            command=generate,
                            font=("Arial", 13, "bold"),
                            bg=COLOR_ACCENT, fg=COLOR_BG,
                            relief="flat", pady=12,
                            cursor="hand2")
generate_button.pack(fill="x", padx=40, pady=10)

# ============================================================
#  RESULT
# ============================================================
tk.Label(window, text="Your password:",
         font=("Arial", 10),
         bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=(10, 0))

password_label = tk.Label(window, text="—",
                          font=("Courier", 14, "bold"),
                          bg=COLOR_BG, fg=COLOR_ACCENT,
                          wraplength=460, justify="center")
password_label.pack(pady=8, padx=20)

copy_button = tk.Button(window, text="📋 Copy to clipboard",
                        command=copy,
                        font=("Arial", 10),
                        bg=COLOR_PANEL, fg=COLOR_TEXT,
                        relief="flat", pady=8,
                        cursor="hand2",
                        state="disabled")
copy_button.pack(pady=5)

strength_label = tk.Label(window, text="",
                          font=("Arial", 10, "bold"),
                          bg=COLOR_BG, fg=COLOR_GRAY)
strength_label.pack(pady=(10, 0))

status_label = tk.Label(window, text="",
                        font=("Arial", 10),
                        bg=COLOR_BG, fg=COLOR_GRAY,
                        wraplength=460)
status_label.pack(pady=10)

# ============================================================
#  START
# ============================================================
window.mainloop()