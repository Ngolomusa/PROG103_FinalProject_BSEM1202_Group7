import tkinter as tk
from tkinter import messagebox



# ==========================================
# MODERN COLOR PALETTE & STYLES
# ==========================================
BG_APP = "#000000"          # Soft light grayish-blue background
BG_CARD = "#FFFFFF"         # Crisp white for input areas
TEXT_DARK = "#FF0000"       # High-contrast dark slate for text
TEXT_LIGHT = "#7F8C8D"      # Muted gray for secondary text
THEME_BLUE = "#2980B9"      # Corporate Header Blue
TERM_BG = "#1E272E"         # Dark Terminal Background
TERM_FG = "#00D2D3"         # Bright Cyan Terminal Text


# Button Colors (Normal / Hover)
BTN_CALC = ("#27AE60", "#2ECC71")   # Emerald Green
BTN_CLEAR = ("#F39C12", "#F1C40F")  # Amber Orange
BTN_VIEW = ("#2980B9", "#3498DB")   # Modern Blue
BTN_EXIT = ("#C0392B", "#E74C3C")   # Crimson Red

# ==========================================
# SYSTEM LOGIC & FUNCTIONS
# ==========================================
sales_records = []

def calculate_report():
    try:
        product_name = entry_name.get().strip()
        if not product_name:
            messagebox.showerror("Input Error", "Product name cannot be empty.")
            return
            
        quantity = int(entry_qty.get())
        cost_price = float(entry_cost.get())
        selling_price = float(entry_sell.get())
        discount = float(entry_discount.get())
        expenses = float(entry_expenses.get())
        
        if quantity < 0 or cost_price < 0 or selling_price < 0 or discount < 0 or expenses < 0:
            messagebox.showerror("Input Error", "Numeric values must be positive.")
            return

        # Processing Logic
        total_cost = quantity * cost_price
        total_revenue = quantity * selling_price
        net_revenue = total_revenue - discount
        final_profit = net_revenue - (total_cost + expenses)

        # Store record in history
        sales_records.append(f"[{product_name.upper()}] - Net Profit: Le {final_profit:,.2f}")

        # Formatting Output Display
        output_text.delete("1.0", tk.END)
        report = (
            f"==================================================\n"
            f"     SMALL BUSINESS SALES REPORT (SDG 8)      \n"
            f"==================================================\n"
            f" Product Name       : {product_name.upper()}\n"
            f" Quantity Sold      : {quantity} Units\n"
            f"--------------------------------------------------\n"
            f" Total Cost Outlay  : Le {total_cost:,.2f}\n"
            f" Gross Revenue      : Le {total_revenue:,.2f}\n"
            f" Discount Applied   : Le {discount:,.2f}\n"
            f" Operating Expenses : Le {expenses:,.2f}\n"
            f"==================================================\n"
            f" TOTAL NET PROFIT   : Le {final_profit:,.2f}\n"
            f"=================================================="
        )
        output_text.insert(tk.END, report)

    except ValueError:
        messagebox.showerror("Format Error", "Please ensure Quantity is a whole number and prices are numeric.")

def clear_fields():
    """Resets all input fields to their default state."""
    entry_name.delete(0, tk.END)
    
    entry_qty.delete(0, tk.END)
    entry_cost.delete(0, tk.END)
    entry_sell.delete(0, tk.END)
    
    entry_discount.delete(0, tk.END)
    entry_discount.insert(0, "0")
    
    entry_expenses.delete(0, tk.END)
    entry_expenses.insert(0, "0")
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, ">>> System cleared. Ready for new entry...")

def view_records():
    """Displays the saved history of transactions."""
    output_text.delete("1.0", tk.END)
    if not sales_records:
        output_text.insert(tk.END, ">>> No previous records found in the current session.")
    else:
        output_text.insert(tk.END, "============= PREVIOUS SALES RECORDS =============\n\n")
        for idx, record in enumerate(sales_records, 1):
            output_text.insert(tk.END, f" {idx}. {record}\n")

def create_hover_button(parent, text, cmd, colors):
    """Creates a modern flat button with mouse hover color animations."""
    base_color, hover_color = colors
    btn = tk.Button(parent, text=text, command=cmd, bg=base_color, fg="white", 
                    font=("Tahoma", 10, "bold"), relief="flat", cursor="hand2", pady=8)
    
    # Hover events
    btn.bind("<Enter>", lambda e: btn.configure(bg=hover_color))
    btn.bind("<Leave>", lambda e: btn.configure(bg=base_color))
    return btn

# ==========================================
# MAIN GUI WINDOW SETUP
# ==========================================
root = tk.Tk()
root.title("Sierra Leone SALES Tracker")
root.geometry("650x700")
root.configure(bg=BG_APP)
root.resizable(True, True)

# --- HEADER BANNER ---
header_frame = tk.Frame(root, bg=THEME_BLUE, height=70)
header_frame.pack(fill=tk.X, side=tk.TOP)
header_frame.pack_propagate(False)

title_lbl = tk.Label(header_frame, text="SME Sales & Expense Calculator", 
                     font=("Segoe UI", 16, "bold"), bg=THEME_BLUE, fg="white")
title_lbl.pack(pady=10)

sub_lbl = tk.Label(header_frame, text="Limkokwing University - PROG103", 
                   font=("Segoe UI", 9, "italic"), bg=THEME_BLUE, fg="#D6EAF8")
sub_lbl.pack(pady=0)

# --- INPUT CARD (WHITE CONTAINER) ---
card_frame = tk.Frame(root, bg=BG_CARD, highlightbackground="#D5D8DC", highlightthickness=1)
card_frame.pack(pady=20, padx=30, fill=tk.X)

input_frame = tk.Frame(card_frame, bg=BG_CARD)
input_frame.pack(pady=15, padx=20)

labels_text = [
    "Product Description Name:", "Quantity Dispatched Sold:", 
    "Unit Cost Price (Le):", "Unit Selling Price (Le):", 
    "Discount Given (Le):", "Total Operating Expenses (Le):"
]

entries = []
for i, text in enumerate(labels_text):
    # Modern styled label
    lbl = tk.Label(input_frame, text=text, font=("Tahoma", 9, "bold"), bg=BG_CARD, fg=TEXT_DARK)
    lbl.grid(row=i, column=0, sticky="w", pady=8, padx=10)
    
    # Modern styled entry field (flat with solid subtle border)
    entry = tk.Entry(input_frame, font=("Tahoma", 10), width=28, relief="solid", bd=1, bg="#F8F9F9")
    entry.grid(row=i, column=1, pady=8, padx=10, ipady=4)
    entries.append(entry)

# Map entries to variables
entry_name, entry_qty, entry_cost, entry_sell, entry_discount, entry_expenses = entries

# Set Defaults
entry_discount.insert(0, "0")
entry_expenses.insert(0, "0")

# --- BUTTONS ROW ---
btn_frame = tk.Frame(root, bg=BG_APP)
btn_frame.pack(pady=5, fill=tk.X, padx=30)

# Configure columns to space buttons equally
for i in range(4):
    btn_frame.columnconfigure(i, weight=1)

btn_calc = create_hover_button(btn_frame, "EXECUTE REPORT", calculate_report, BTN_CALC)
btn_calc.grid(row=0, column=0, padx=5, sticky="ew")

btn_clear = create_hover_button(btn_frame, "CLEAR FIELDS", clear_fields, BTN_CLEAR)
btn_clear.grid(row=0, column=1, padx=5, sticky="ew")

btn_view = create_hover_button(btn_frame, "VIEW RECORDS", view_records, BTN_VIEW)
btn_view.grid(row=0, column=2, padx=5, sticky="ew")

btn_exit = create_hover_button(btn_frame, "SHUTDOWN", root.quit, BTN_EXIT)
btn_exit.grid(row=0, column=3, padx=5, sticky="ew")

# --- TERMINAL OUTPUT DISPLAY ---
output_frame = tk.Frame(root, bg=BG_APP)
output_frame.pack(pady=15, padx=30, fill=tk.BOTH, expand=True)

output_text = tk.Text(output_frame, font=("Courier New", 10, "bold"), bg=TERM_BG, fg=TERM_FG, 
                      relief="flat", padx=15, pady=15, insertbackground="white")
output_text.pack(fill=tk.BOTH, expand=True)

# Initial Welcome Message
output_text.insert(tk.END, ">>> SYSTEM INITIALIZED...\n>>> READY FOR FINANCIAL DATA INPUT.")

# Run Application
root.mainloop()