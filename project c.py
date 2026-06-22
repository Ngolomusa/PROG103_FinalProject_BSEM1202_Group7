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