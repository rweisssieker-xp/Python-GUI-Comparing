import customtkinter as ctk
import datetime

class IntSpinbox(ctk.CTkFrame):
    def __init__(self, *args, width: int = 100, height: int = 32, step_size: int = 1, command=None, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, padx=3, pady=3, sticky="ew")

        self.add_button = ctk.CTkButton(self, text="+", width=height-6, height=height-6,
                                                   command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> int:
        try:
            return int(self.entry.get())
        except ValueError:
            return 0

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter Ultimate CRM Demo")
        self.geometry("1100x800")

        # Set appearance
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_label = ctk.CTkLabel(self.sidebar_frame, text="Ultimate CRM", font=ctk.CTkFont(size=20, weight="bold"))
        self.sidebar_label.pack(pady=20)

        self.tab_view = ctk.CTkTabview(self, width=850)
        self.tab_view.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.tab_dashboard = self.tab_view.add("Dashboard")
        self.tab_customers = self.tab_view.add("Customer List")
        self.tab_admin = self.tab_view.add("Add Customer")
        self.tab_settings = self.tab_view.add("Settings")

        self.setup_dashboard()
        self.setup_customers()
        self.setup_admin()
        self.setup_settings()

    def setup_dashboard(self):
        self.tab_dashboard.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Metric Cards
        for i, (title, val, color) in enumerate([("Total Customers", "1,284", None), 
                                                 ("Active Leads", "342", "green"), 
                                                 ("Sales Volume", "$452k", "blue")]):
            card = ctk.CTkFrame(self.tab_dashboard)
            card.grid(row=0, column=i, padx=10, pady=20, sticky="nsew")
            ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=14)).pack(pady=10)
            ctk.CTkLabel(card, text=val, font=ctk.CTkFont(size=24, weight="bold"), text_color=color).pack(pady=5)

    def setup_customers(self):
        search_frame = ctk.CTkFrame(self.tab_customers, fg_color="transparent")
        search_frame.pack(fill="x", pady=10)
        ctk.CTkEntry(search_frame, placeholder_text="Search database...", width=400).pack(side="left", padx=10)
        ctk.CTkButton(search_frame, text="Search Now", width=120).pack(side="left")

        self.table_frame = ctk.CTkScrollableFrame(self.tab_customers, label_text="Customer Database (15 Records)")
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        headers = ["ID", "Organization", "Status", "Value", "Date"]
        for i, h in enumerate(headers):
            ctk.CTkLabel(self.table_frame, text=h, font=ctk.CTkFont(weight="bold")).grid(row=0, column=i, padx=15, pady=5, sticky="w")

        data = [
            ("101", "Tesla Inc.", "Active", "$25k", "2024-05-12"),
            ("102", "SpaceX", "Lead", "$120k", "2024-05-18"),
            ("103", "Apple", "Active", "$88k", "2024-04-30"),
            ("104", "Acme Corp", "Inactive", "$5k", "2023-11-20"),
            ("105", "Globex", "Active", "$15k", "2024-05-22"),
            ("106", "Hooli", "Lead", "$200k", "2024-05-25"),
            ("107", "Stark Ind.", "Active", "$45k", "2024-05-10"),
            ("108", "Wayne Ent.", "Active", "$60k", "2024-05-14"),
            ("109", "Umbrella", "Lead", "$12k", "2024-05-01"),
            ("110", "Initech", "Active", "$3k", "2024-05-20"),
            ("111", "Cyberdyne", "Active", "$90k", "2024-05-15"),
            ("112", "Soylent", "Lead", "$8k", "2024-05-18"),
            ("113", "Massive Dy.", "Active", "$75k", "2024-05-02"),
            ("114", "Tyrell Corp", "Active", "$110k", "2024-05-19"),
            ("115", "Weyland-Y.", "Lead", "$140k", "2024-05-26"),
        ]
        
        for r, row in enumerate(data, start=1):
            for i, val in enumerate(row):
                ctk.CTkLabel(self.table_frame, text=val).grid(row=r, column=i, padx=15, pady=2, sticky="w")

    def setup_admin(self):
        container = ctk.CTkScrollableFrame(self.tab_admin)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # 1. Text Entry
        ctk.CTkLabel(container, text="Name:").pack(anchor="w", pady=(10,0))
        self.name_entry = ctk.CTkEntry(container, placeholder_text="Enter Name", width=400)
        self.name_entry.pack(pady=5, anchor="w")

        # 2. Text Area (Textbox in CTK)
        ctk.CTkLabel(container, text="Notes:").pack(anchor="w", pady=(10,0))
        self.notes_text = ctk.CTkTextbox(container, height=100, width=400)
        self.notes_text.pack(pady=5, anchor="w")

        # 3. Dropdown
        ctk.CTkLabel(container, text="Industry:").pack(anchor="w", pady=(10,0))
        self.ind_option = ctk.CTkOptionMenu(container, values=["Tech", "Bio", "Finance", "Energy"], width=400)
        self.ind_option.pack(pady=5, anchor="w")

        # 4. Radio Buttons (via Segmented Button)
        ctk.CTkLabel(container, text="Account Type:").pack(anchor="w", pady=(10,0))
        self.type_seg = ctk.CTkSegmentedButton(container, values=["B2B", "B2C", "NGO"], width=400)
        self.type_seg.pack(pady=5, anchor="w")
        self.type_seg.set("B2B")

        # 5. CheckBox
        self.news_check = ctk.CTkCheckBox(container, text="Subscribe to Newsletter")
        self.news_check.pack(pady=10, anchor="w")

        # 6. Switch
        self.active_switch = ctk.CTkSwitch(container, text="Account Active")
        self.active_switch.pack(pady=5, anchor="w")
        self.active_switch.select()

        # 7. Slider
        ctk.CTkLabel(container, text="Priority Weight:").pack(anchor="w", pady=(10,0))
        self.priority_slider = ctk.CTkSlider(container, from_=0, to=100, width=400)
        self.priority_slider.pack(pady=5, anchor="w")

        # 8. SpinBox (Custom)
        ctk.CTkLabel(container, text="Employee Count:").pack(anchor="w", pady=(10,0))
        self.spinbox = IntSpinbox(container, width=150, step_size=5)
        self.spinbox.pack(pady=5, anchor="w")
        self.spinbox.set(50)

        # 9. Date Picker (Mockup Entry)
        ctk.CTkLabel(container, text="Entry Date:").pack(anchor="w", pady=(10,0))
        self.date_entry = ctk.CTkEntry(container, placeholder_text="YYYY-MM-DD", width=400)
        self.date_entry.insert(0, str(datetime.date.today()))
        self.date_entry.pack(pady=5, anchor="w")

        # 10. Progress Bar
        ctk.CTkLabel(container, text="Sync Progress:").pack(anchor="w", pady=(10,0))
        self.progress = ctk.CTkProgressBar(container, width=400)
        self.progress.pack(pady=5, anchor="w")
        self.progress.set(0.65)

        # 11. Buttons
        btn_frame = ctk.CTkFrame(container, fg_color="transparent")
        btn_frame.pack(pady=20, anchor="w")
        ctk.CTkButton(btn_frame, text="Submit Data").pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Reset Form", fg_color="gray").pack(side="left", padx=5)

    def setup_settings(self):
        ctk.CTkLabel(self.tab_settings, text="Application Settings", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=20)
        self.mode_switch = ctk.CTkSwitch(self.tab_settings, text="Enable Dark Mode", command=self.change_appearance_mode_event)
        self.mode_switch.pack()
        self.mode_switch.select()

    def change_appearance_mode_event(self):
        if self.mode_switch.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

if __name__ == "__main__":
    app = App()
    app.mainloop()
