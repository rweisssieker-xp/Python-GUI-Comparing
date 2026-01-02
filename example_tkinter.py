import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class TkinterCRMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Standard Tkinter Ultimate CRM Demo")
        self.root.geometry("1100x800")

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        self.setup_overview_tab()
        self.setup_database_tab()
        self.setup_admin_tab()

    def setup_overview_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Performance Dashboard")
        
        ttk.Label(tab, text="Enterprise Data Overview", font=("Helvetica", 20, "bold")).pack(pady=20)
        
        cards_frame = ttk.Frame(tab)
        cards_frame.pack(pady=10)
        
        for name, val, color in [("Global Sales", "$1.28M", "blue"), 
                                 ("Conversion", "18.4%", "green"), 
                                 ("Pending Task", "14", "red")]:
            f = ttk.LabelFrame(cards_frame, text=name, padding=20)
            f.pack(side="left", padx=15)
            ttk.Label(f, text=val, font=("Arial", 22, "bold"), foreground=color).pack()

    def setup_database_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Customer Registry")

        tree = ttk.Treeview(tab, columns=("ID", "Entity", "Industry", "Value", "Health"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Entity", text="Organization")
        tree.heading("Value", text="Revenue")
        tree.heading("Industry", text="Sector")
        tree.heading("Health", text="Score")
        
        for i in range(1, 16):
            tree.insert("", "end", values=(100+i, f"Client {i} Corp", "Tech", f"${i*10}k", f"{70+i}%"))
        
        tree.pack(expand=True, fill='both', padx=10, pady=10)

    def setup_admin_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="System Administration")

        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # 1. Name Entry
        ttk.Label(scrollable_frame, text="Organization Lead Name:").pack(anchor="w", pady=(10,0))
        ttk.Entry(scrollable_frame, width=50).pack(pady=5, anchor="w")

        # 2. Multi-line Notes
        ttk.Label(scrollable_frame, text="Relationship History / Notes:").pack(anchor="w", pady=(10,0))
        txt = scrolledtext.ScrolledText(scrollable_frame, height=5, width=40)
        txt.pack(pady=5, anchor="w")

        # 3. Dropdown
        ttk.Label(scrollable_frame, text="Industry Vertical:").pack(anchor="w", pady=(10,0))
        ttk.Combobox(scrollable_frame, values=["Finance", "Healthcare", "Tech", "Edu"], width=47).pack(pady=5, anchor="w")

        # 4. Radio
        ttk.Label(scrollable_frame, text="Market Strategy:").pack(anchor="w", pady=(10,0))
        r_f = ttk.Frame(scrollable_frame)
        r_f.pack(anchor="w")
        v = tk.StringVar(value="b2b")
        ttk.Radiobutton(r_f, text="B2B (Enterprise)", variable=v, value="b2b").pack(side="left")
        ttk.Radiobutton(r_f, text="B2C (Retail)", variable=v, value="b2c").pack(side="left")

        # 5. Checkbox
        ttk.Checkbutton(scrollable_frame, text="Enable Advanced Billing Tier").pack(pady=10, anchor="w")

        # 6. Switch (Mocked with specialized Checkbutton)
        ttk.Checkbutton(scrollable_frame, text="ACCOUNT VISIBLE ON WEB PORTAL").pack(pady=5, anchor="w")

        # 7. Slider
        ttk.Label(scrollable_frame, text="Engagement Priority (0-100):").pack(anchor="w", pady=(10,0))
        ttk.Scale(scrollable_frame, from_=0, to=100, length=300).pack(pady=5, anchor="w")

        # 8. Spinbox
        ttk.Label(scrollable_frame, text="Dedicated Seat Count:").pack(anchor="w", pady=(10,0))
        tk.Spinbox(scrollable_frame, from_=0, to=1000, width=48).pack(pady=5, anchor="w")

        # 9. Date Picker (Text Input as Date Picker not available in standard Tkinter)
        ttk.Label(scrollable_frame, text="Target Renewal Date (YYYY-MM-DD):").pack(anchor="w", pady=(10,0))
        ttk.Entry(scrollable_frame, width=50).pack(pady=5, anchor="w")

        # 10. Progress Bar
        ttk.Label(scrollable_frame, text="Data Migration Success Rate:").pack(anchor="w", pady=(10,0))
        pb = ttk.Progressbar(scrollable_frame, length=300, value=65)
        pb.pack(pady=5, anchor="w")

        # 11. Buttons
        b_f = ttk.Frame(scrollable_frame)
        b_f.pack(pady=20, anchor="w")
        ttk.Button(b_f, text="Register Record", command=lambda: messagebox.showinfo("Success", "Record Persisted")).pack(side="left", padx=5)
        ttk.Button(b_f, text="Clear Form").pack(side="left", padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterCRMApp(root)
    root.mainloop()
