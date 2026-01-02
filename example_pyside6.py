import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, 
                             QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, 
                             QTableWidgetItem, QLineEdit, QComboBox, QRadioButton, 
                             QCheckBox, QPushButton, QSlider, QProgressBar, QFormLayout, 
                             QFrame, QTextEdit, QSpinBox, QDateEdit, QScrollArea)
from PySide6.QtCore import Qt, QDate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Ultimate CRM Demo")
        self.resize(1100, 800)

        # Tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.setup_dashboard_tab()
        self.setup_customer_tab()
        self.setup_admin_tab()

    def setup_dashboard_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        header = QLabel("Performance intelligence Dashboard")
        header.setStyleSheet("font-size: 26px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(header)

        cards_layout = QHBoxLayout()
        metrics = [("Total Revenue", "$1.45M", "#1f77b4"), 
                   ("Active Pipelines", "128", "green"), 
                   ("High Priority Leads", "14", "red")]
                   
        for label, val, color in metrics:
            card = QFrame()
            card.setFrameShape(QFrame.StyledPanel)
            card.setStyleSheet(f"border: 2px solid #ccc; border-radius: 12px; padding: 25px; background: white;")
            v_layout = QVBoxLayout(card)
            v_layout.addWidget(QLabel(label, styleSheet="color: #666; font-size: 14px;"))
            val_lbl = QLabel(val)
            val_lbl.setStyleSheet(f"font-size: 28px; font-weight: bold; color: {color};")
            v_layout.addWidget(val_lbl)
            cards_layout.addWidget(card)
        
        layout.addLayout(cards_layout)
        layout.addStretch()
        self.tabs.addTab(tab, "Overview")

    def setup_customer_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        search_layout = QHBoxLayout()
        search_layout.addWidget(QLineEdit(placeholderText="Search organizations..."))
        search_layout.addWidget(QPushButton("Apply Filters"))
        layout.addLayout(search_layout)

        self.table = QTableWidget(15, 5)
        self.table.setHorizontalHeaderLabels(["ID", "Organization", "Industry", "Value", "Renewal"])
        
        data = [
            ("101", "Tesla Inc.", "Auto", "$2M", "2024-12-01"),
            ("102", "SpaceX", "Aero", "$5M", "2025-01-15"),
            ("103", "Apple", "Tech", "$1.5M", "2024-11-20"),
            ("104", "Microsoft", "Tech", "$4M", "2025-03-10"),
            ("105", "Amazon", "Retail", "$3M", "2024-10-05"),
            ("106", "Meta", "Social", "$800k", "2025-02-14"),
            ("107", "Google", "Search", "$6M", "2024-09-30"),
            ("108", "Netflix", "Media", "$400k", "2025-05-22"),
            ("109", "Adobe", "SaaS", "$1.2M", "2024-12-25"),
            ("110", "Salesforce", "CRM", "$900k", "2025-01-01"),
            ("111", "Slack", "Comm", "$300k", "2024-08-15"),
            ("112", "Zoom", "Video", "$500k", "2024-07-20"),
            ("113", "Spotify", "Music", "$200k", "2025-04-10"),
            ("114", "Twitter", "Social", "$100k", "2024-06-30"),
            ("115", "Uber", "Trans", "$600k", "2025-02-28"),
        ]
        
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(val))
        
        layout.addWidget(self.table)
        self.tabs.addTab(tab, "Database")

    def setup_admin_tab(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        tab = QWidget()
        layout = QVBoxLayout(tab)
        form = QFormLayout()

        # 1. Text Entry
        form.addRow("Organization Name:", QLineEdit())
        
        # 2. Text Area
        form.addRow("Detailed Biography:", QTextEdit())
        
        # 3. Dropdown
        cb = QComboBox()
        cb.addItems(["Enterprise", "Startup", "Non-Profit", "Government"])
        form.addRow("Sector Type:", cb)

        # 4. Radio
        radios = QWidget()
        r_layout = QHBoxLayout(radios)
        r_layout.addWidget(QRadioButton("B2B Sales"))
        r_layout.addWidget(QRadioButton("B2C Consumer"))
        r_layout.addWidget(QRadioButton("Gov / Other"))
        form.addRow("Market Strategy:", radios)

        # 5. Checkbox
        form.addRow(QCheckBox("Enroll in VIP Program"))

        # 6. Switch (Mocked with styled CheckBox)
        sw = QCheckBox("Account Status: ENABLED")
        sw.setChecked(True)
        form.addRow(sw)

        # 7. Slider
        form.addRow("Priority Score:", QSlider(Qt.Horizontal))

        # 8. SpinBox
        form.addRow("Total Employees:", QSpinBox())

        # 9. Date Edit
        de = QDateEdit(calendarPopup=True)
        de.setDate(QDate.currentDate())
        form.addRow("Registration Date:", de)

        # 10. Progress Bar
        pg = QProgressBar()
        pg.setValue(68)
        form.addRow("Onboarding Progress:", pg)

        layout.addLayout(form)
        
        # 11. Buttons
        btn_layout = QHBoxLayout()
        submit_btn = QPushButton("Commit Record")
        submit_btn.setStyleSheet("background-color: #2c3e50; color: white; padding: 12px; font-weight: bold;")
        reset_btn = QPushButton("Reset Form")
        btn_layout.addWidget(submit_btn)
        btn_layout.addWidget(reset_btn)
        layout.addLayout(btn_layout)
        
        layout.addStretch()
        scroll.setWidget(tab)
        self.tabs.addTab(scroll, "Administration")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
