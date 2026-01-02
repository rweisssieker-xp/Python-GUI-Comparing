import customtkinter as ctk
import subprocess
import os
import sys
from comparison_data import FRAMEWORK_DATA, FEATURE_MATRIX, FEATURE_LABELS
from framework_details import FRAMEWORK_DETAILS
from tkinter import messagebox

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Python GUI Framework Comparison Dashboard (19+ Frameworks)")
        self.geometry("1400x900")

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar with buttons (Scrollable)
        self.sidebar = ctk.CTkScrollableFrame(self, width=280, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.sidebar_label = ctk.CTkLabel(self.sidebar, text="Framework Launcher", font=ctk.CTkFont(size=20, weight="bold"))
        self.sidebar_label.pack(pady=20)

        self.frameworks = [
            # Standard & Modern
            ("Standard Tkinter", "example_tkinter.py"),
            ("CustomTkinter", "example_customtkinter.py"),
            ("PySide6 (Official Qt)", "example_pyside6.py"),
            ("PyQt6 (Qt)", "example_pyqt6.py"),
            ("wxPython (Native)", "example_wxpython.py"),
            ("Kivy (Touch/Mobile)", "example_kivy.py"),
            ("PySimpleGUI", "example_pysimplegui.py"),
            ("Dear PyGui (GPU)", "example_dearpygui.py"),
            # Web-Based
            ("Flet (Flutter-based)", "example_flet.py"),
            ("NiceGUI (Web-Stack)", "example_nicegui.py"),
            ("PyWebView (Embedded)", "example_pywebview.py"),
            ("Eel (Chrome/Web)", "example_eel.py"),
            ("Flexx (Python->JS)", "example_flexx.py"),
            # Specialized
            ("Gooey (CLI to GUI)", "example_gooey.py"),
            ("Toga (BeeWare/Native)", "example_toga.py"),
            ("appJar", "example_appjar.py"),
            # Legacy / Specialized Mockups
            ("PyGUI (Native Wrapper)", "example_pygui.py"),
            ("PyForms (.NET style)", "example_pyforms.py"),
            ("Libavg (Multimedia)", "example_libavg.py"),
        ]

        for name, script in self.frameworks:
            btn = ctk.CTkButton(self.sidebar, text=name, command=lambda s=script: self.launch(s))
            btn.pack(padx=20, pady=5, fill="x")

        # Main Area with Tabs
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Tab 1: Comparison Matrix
        self.matrix_tab = self.tab_view.add("Comparison Matrix")
        self.setup_matrix_tab()
        
        # Tab 2: Feature Matrix
        self.feature_tab = self.tab_view.add("Feature Comparison")
        self.setup_feature_tab()
        
        # Tab 3: Framework Details
        self.details_tab = self.tab_view.add("Framework Details")
        self.setup_details_tab()

    def setup_matrix_tab(self):
        # Filter and Search Section
        filter_frame = ctk.CTkFrame(self.matrix_tab)
        filter_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(filter_frame, text="Filters & Search", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)
        
        filter_row1 = ctk.CTkFrame(filter_frame, fg_color="transparent")
        filter_row1.pack(fill="x", padx=10, pady=5)
        
        # Search
        ctk.CTkLabel(filter_row1, text="Search:").pack(side="left", padx=5)
        self.search_entry = ctk.CTkEntry(filter_row1, placeholder_text="Framework name...", width=200)
        self.search_entry.pack(side="left", padx=5)
        self.search_entry.bind("<KeyRelease>", lambda e: self.apply_filters())
        
        # Category Filter
        ctk.CTkLabel(filter_row1, text="Category:").pack(side="left", padx=5)
        self.category_filter = ctk.CTkOptionMenu(filter_row1, values=["All", "Standard & Modern", "Web-Based", "Specialized", "Legacy / Specialized Mockups"], command=lambda x: self.apply_filters())
        self.category_filter.pack(side="left", padx=5)
        
        # Platform Filter
        ctk.CTkLabel(filter_row1, text="Platform:").pack(side="left", padx=5)
        self.platform_filter = ctk.CTkOptionMenu(filter_row1, values=["All", "Windows", "Linux", "macOS", "Mobile"], command=lambda x: self.apply_filters())
        self.platform_filter.pack(side="left", padx=5)
        
        # Sort
        filter_row2 = ctk.CTkFrame(filter_frame, fg_color="transparent")
        filter_row2.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(filter_row2, text="Sort by:").pack(side="left", padx=5)
        self.sort_option = ctk.CTkOptionMenu(filter_row2, values=["Name", "Learning Curve", "Performance", "Community"], command=lambda x: self.apply_filters())
        self.sort_option.pack(side="left", padx=5)
        
        # Export Button
        export_btn = ctk.CTkButton(filter_row2, text="Export CSV", command=self.export_csv, width=120)
        export_btn.pack(side="right", padx=5)
        
        export_json_btn = ctk.CTkButton(filter_row2, text="Export JSON", command=self.export_json, width=120)
        export_json_btn.pack(side="right", padx=5)

        # Scrollable Matrix Area
        self.matrix_scroll = ctk.CTkScrollableFrame(self.matrix_tab)
        self.matrix_scroll.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.render_matrix()

    def setup_feature_tab(self):
        # Feature Matrix Header
        header_frame = ctk.CTkFrame(self.feature_tab)
        header_frame.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(header_frame, text="Feature Support Matrix", font=ctk.CTkFont(size=18, weight="bold")).pack()
        
        # Scrollable Feature Matrix
        self.feature_scroll = ctk.CTkScrollableFrame(self.feature_tab)
        self.feature_scroll.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.render_feature_matrix()

    def setup_details_tab(self):
        # Framework Selection
        select_frame = ctk.CTkFrame(self.details_tab)
        select_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(select_frame, text="Select Framework:", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=10)
        self.details_framework = ctk.CTkOptionMenu(select_frame, values=list(FRAMEWORK_DATA.keys()), command=self.show_framework_details)
        self.details_framework.pack(side="left", padx=10)
        
        # Details Display Area
        self.details_scroll = ctk.CTkScrollableFrame(self.details_tab)
        self.details_scroll.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Show first framework by default
        if FRAMEWORK_DATA:
            self.show_framework_details(list(FRAMEWORK_DATA.keys())[0])

    def get_filtered_frameworks(self):
        """Get frameworks based on current filters and search"""
        search_text = self.search_entry.get().lower()
        category = self.category_filter.get()
        platform = self.platform_filter.get()
        
        filtered = []
        for name, script in self.frameworks:
            # Extract base name (remove parenthetical info)
            base_name = name.split(" (")[0]
            
            if base_name not in FRAMEWORK_DATA:
                continue
                
            data = FRAMEWORK_DATA[base_name]
            
            # Search filter
            if search_text and search_text not in name.lower() and search_text not in data["use_case"].lower():
                continue
            
            # Category filter
            if category != "All" and data["category"] != category:
                continue
            
            # Platform filter
            if platform != "All":
                platform_key = platform.lower()
                if platform_key == "mobile":
                    if not data["platforms"]["mobile"]:
                        continue
                elif not data["platforms"].get(platform_key, False):
                    continue
            
            filtered.append((name, script, base_name))
        
        # Sort
        sort_by = self.sort_option.get()
        if sort_by == "Name":
            filtered.sort(key=lambda x: x[0])
        elif sort_by == "Learning Curve":
            order = {"Einfach": 0, "Mittel": 1, "Schwer": 2}
            filtered.sort(key=lambda x: order.get(FRAMEWORK_DATA[x[2]].get("learning_curve", "Mittel"), 1))
        elif sort_by == "Performance":
            order = {"Hoch": 0, "Mittel": 1, "Niedrig": 2}
            filtered.sort(key=lambda x: order.get(FRAMEWORK_DATA[x[2]].get("performance", "Mittel"), 1))
        elif sort_by == "Community":
            order = {"Hoch": 0, "Mittel": 1, "Niedrig": 2}
            filtered.sort(key=lambda x: order.get(FRAMEWORK_DATA[x[2]].get("community", "Mittel"), 1))
        
        return filtered

    def apply_filters(self):
        """Re-render matrix with current filters"""
        # Clear existing rows
        for widget in self.matrix_scroll.winfo_children():
            widget.destroy()
        self.render_matrix()

    def render_matrix(self):
        """Render the comparison matrix"""
        # Header
        headers = ["Framework", "Tech", "License", "Platforms", "Learning", "Python", "Performance", "Community"]
        self.render_matrix_row(headers, is_header=True)
        
        # Data rows
        filtered = self.get_filtered_frameworks()
        for name, script, base_name in filtered:
            data = FRAMEWORK_DATA[base_name]
            platforms = []
            if data["platforms"]["windows"]: platforms.append("Win")
            if data["platforms"]["linux"]: platforms.append("Lin")
            if data["platforms"]["macos"]: platforms.append("Mac")
            if data["platforms"]["mobile"]: platforms.append("Mob")
            platform_str = ", ".join(platforms) if platforms else "None"
            
            row_data = [
                name,
                data["tech"],
                data["license"],
                platform_str,
                data["learning_curve"],
                data["python_version"],
                data["performance"],
                data["community"]
            ]
            self.render_matrix_row(row_data, is_header=False)

    def render_matrix_row(self, data, is_header=False):
        """Render a single matrix row"""
        row_frame = ctk.CTkFrame(self.matrix_scroll, fg_color="transparent" if not is_header else None)
        row_frame.pack(fill="x", padx=5, pady=2)
        
        widths = [180, 120, 100, 100, 80, 80, 90, 90]
        for i, val in enumerate(data):
            lbl = ctk.CTkLabel(row_frame, text=str(val), width=widths[i], anchor="w", justify="left")
            if is_header:
                lbl.configure(font=ctk.CTkFont(weight="bold", size=12))
            lbl.pack(side="left", padx=5, pady=3)

    def render_feature_matrix(self):
        """Render the feature comparison matrix"""
        # Header row
        header_frame = ctk.CTkFrame(self.feature_scroll)
        header_frame.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkLabel(header_frame, text="Framework", width=180, font=ctk.CTkFont(weight="bold")).pack(side="left", padx=5)
        for feature_key, feature_label in FEATURE_LABELS.items():
            ctk.CTkLabel(header_frame, text=feature_label, width=120, font=ctk.CTkFont(weight="bold")).pack(side="left", padx=5)
        
        # Data rows
        for name, script in self.frameworks:
            base_name = name.split(" (")[0]
            if base_name not in FEATURE_MATRIX:
                continue
            
            row_frame = ctk.CTkFrame(self.feature_scroll)
            row_frame.pack(fill="x", padx=5, pady=2)
            
            ctk.CTkLabel(row_frame, text=name, width=180, anchor="w").pack(side="left", padx=5)
            
            features = FEATURE_MATRIX[base_name]
            for feature_key in FEATURE_LABELS.keys():
                supported = features.get(feature_key, False)
                symbol = "✓" if supported else "✗"
                color = "green" if supported else "gray"
                ctk.CTkLabel(row_frame, text=symbol, width=120, text_color=color, font=ctk.CTkFont(size=14)).pack(side="left", padx=5)

    def show_framework_details(self, framework_name):
        """Show detailed information for a framework"""
        # Clear existing content
        for widget in self.details_scroll.winfo_children():
            widget.destroy()
        
        if framework_name not in FRAMEWORK_DATA:
            return
        
        data = FRAMEWORK_DATA[framework_name]
        features = FEATURE_MATRIX.get(framework_name, {})
        details = FRAMEWORK_DETAILS.get(framework_name, {})
        
        # Title
        title = ctk.CTkLabel(self.details_scroll, text=framework_name, font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=10)
        
        # Basic Info
        info_frame = ctk.CTkFrame(self.details_scroll)
        info_frame.pack(fill="x", padx=10, pady=5)
        
        info_text = f"Technology: {data['tech']}\n"
        info_text += f"License: {data['license']}\n"
        info_text += f"Category: {data['category']}\n"
        info_text += f"Best Use Case: {data['use_case']}\n"
        info_text += f"Python Version: {data['python_version']}\n"
        info_text += f"Learning Curve: {data['learning_curve']}\n"
        info_text += f"Installation Difficulty: {data['install_difficulty']}\n"
        info_text += f"Performance: {data['performance']}\n"
        info_text += f"Community Activity: {data['community']}\n"
        info_text += f"Documentation: {data['documentation']}\n\n"
        
        info_text += "Platform Support:\n"
        platforms = data['platforms']
        if platforms['windows']: info_text += "  ✓ Windows\n"
        if platforms['linux']: info_text += "  ✓ Linux\n"
        if platforms['macos']: info_text += "  ✓ macOS\n"
        if platforms['mobile']: info_text += "  ✓ Mobile\n"
        
        ctk.CTkLabel(info_frame, text=info_text, anchor="w", justify="left", font=ctk.CTkFont(size=12)).pack(padx=10, pady=10, anchor="w")
        
        # Pros and Cons
        if details:
            pros_cons_frame = ctk.CTkFrame(self.details_scroll)
            pros_cons_frame.pack(fill="x", padx=10, pady=5)
            
            pros_text = "Pros:\n"
            for pro in details.get("pros", []):
                pros_text += f"  • {pro}\n"
            
            cons_text = "\nCons:\n"
            for con in details.get("cons", []):
                cons_text += f"  • {con}\n"
            
            ctk.CTkLabel(pros_cons_frame, text=pros_text + cons_text, anchor="w", justify="left", font=ctk.CTkFont(size=12)).pack(padx=10, pady=10, anchor="w")
            
            # Installation
            if details.get("installation"):
                install_frame = ctk.CTkFrame(self.details_scroll)
                install_frame.pack(fill="x", padx=10, pady=5)
                ctk.CTkLabel(install_frame, text=f"Installation: {details['installation']}", anchor="w", justify="left", font=ctk.CTkFont(size=12)).pack(padx=10, pady=5, anchor="w")
            
            # Limitations
            if details.get("limitations"):
                limits_frame = ctk.CTkFrame(self.details_scroll)
                limits_frame.pack(fill="x", padx=10, pady=5)
                limits_text = "Limitations:\n"
                for limit in details["limitations"]:
                    limits_text += f"  • {limit}\n"
                ctk.CTkLabel(limits_frame, text=limits_text, anchor="w", justify="left", font=ctk.CTkFont(size=12)).pack(padx=10, pady=5, anchor="w")
            
            # Documentation Link
            if details.get("documentation_url"):
                doc_frame = ctk.CTkFrame(self.details_scroll)
                doc_frame.pack(fill="x", padx=10, pady=5)
                doc_text = f"Documentation: {details['documentation_url']}"
                ctk.CTkLabel(doc_frame, text=doc_text, anchor="w", justify="left", font=ctk.CTkFont(size=12)).pack(padx=10, pady=5, anchor="w")
        
        # Features
        features_frame = ctk.CTkFrame(self.details_scroll)
        features_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(features_frame, text="Supported Features:", font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=10, pady=5)
        
        features_text = ""
        for feature_key, feature_label in FEATURE_LABELS.items():
            supported = features.get(feature_key, False)
            symbol = "✓" if supported else "✗"
            features_text += f"{symbol} {feature_label}\n"
        
        ctk.CTkLabel(features_frame, text=features_text, anchor="w", justify="left", font=ctk.CTkFont(size=12)).pack(padx=10, pady=5, anchor="w")

    def export_csv(self):
        """Export comparison matrix to CSV"""
        try:
            from tkinter import filedialog
            from export_utils import export_to_csv
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
            )
            
            if filename:
                filtered = self.get_filtered_frameworks()
                frameworks_list = [(name, script) for name, script, _ in filtered]
                export_to_csv(filename, frameworks_list)
                messagebox.showinfo("Export successful", f"Data exported to {filename}")
        except Exception as e:
            messagebox.showerror("Export failed", str(e))

    def export_json(self):
        """Export comparison data to JSON"""
        try:
            from tkinter import filedialog
            from export_utils import export_to_json
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            
            if filename:
                filtered = self.get_filtered_frameworks()
                frameworks_list = [(name, script) for name, script, _ in filtered]
                export_to_json(filename, frameworks_list)
                messagebox.showinfo("Export successful", f"Data exported to {filename}")
        except Exception as e:
            messagebox.showerror("Export failed", str(e))

    def launch(self, script_name):
        """Launch a framework demo"""
        path = os.path.join(os.path.dirname(__file__), script_name)
        
        if not os.path.exists(path):
            messagebox.showerror("Error", f"The demo file '{script_name}' was not found.")
            return
        
        # Non-blocking launch using the virtual environment if available
        venv_python = os.path.join(os.path.dirname(__file__), ".venv", "Scripts", "python.exe")
        python_exec = venv_python if os.path.exists(venv_python) else sys.executable
        
        try:
            process = subprocess.Popen([python_exec, path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        except Exception as e:
            messagebox.showerror("Error", f"ERROR STARTING DEMO: {str(e)}")
            import traceback
            print(traceback.format_exc())

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
