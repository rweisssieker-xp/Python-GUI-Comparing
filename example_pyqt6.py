import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, 
                             QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, 
                             QTableWidgetItem, QLineEdit, QComboBox, QRadioButton, 
                             QCheckBox, QPushButton, QSlider, QProgressBar, QFormLayout, 
                             QFrame, QTextEdit, QSpinBox, QDateEdit, QScrollArea)
from PyQt6.QtCore import Qt, QDate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Ultimate CRM Demo")
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
        header = QLabel("Enterprise CRM Analytics")
        header.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        layout.addWidget(header)

        metrics = QHBoxLayout()
        stats = [("Global Deals", "1,840", "#2980b9"), 
                 ("Success Rate", "94.5%", "#27ae60"), 
                 ("Average Deal", "$22.4k", "#8e44ad")]
                 
        for m_name, m_val, m_color in stats:
            card = QFrame()
            card.setStyleSheet(f"border: 1px solid #ddd; border-radius: 10px; background: white; padding: 20px;")
            v = QVBoxLayout(card)
            v.addWidget(QLabel(m_name, styleSheet="color: #7f8c8d; font-size: 13px;"))
            v.addWidget(QLabel(m_val, styleSheet=f"font-size: 24px; font-weight: bold; color: {m_color};"))
            metrics.addWidget(card)
        
        layout.addLayout(metrics)
        layout.addStretch()
        self.tabs.addTab(tab, "Overview")

    def setup_customer_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        self.table = QTableWidget(15, 4)
        self.table.setHorizontalHeaderLabels(["Account Name", "Relationship Manager", "Annual Value", "Risk Level"])
        
        managers = ["Alice", "Bob", "Charlie", "Diana"]
        for i in range(1, 16):
            self.table.setItem(i-1, 0, QTableWidgetItem(f"Account {100+i}"))
            self.table.setItem(i-1, 1, QTableWidgetItem(managers[(i-1) % 4]))
            self.table.setItem(i-1, 2, QTableWidgetItem(f"${i*5}k"))
            self.table.setItem(i-1, 3, QTableWidgetItem("Low" if (i-1)%3 == 0 else "Medium"))
        
        layout.addWidget(self.table)
        self.tabs.addTab(tab, "Portfolio")

    def setup_admin_tab(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        tab = QWidget()
        layout = QVBoxLayout(tab)
        form = QFormLayout()

        form.addRow("Lead Full Name:", QLineEdit())
        form.addRow("Discovery Notes:", QTextEdit())
        
        cb = QComboBox()
        cb.addItems(["Finance", "Logistics", "Energy", "Tech"])
        form.addRow("Target Sector:", cb)

        radios = QWidget()
        r_layout = QHBoxLayout(radios)
        r_layout.addWidget(QRadioButton("Tier 1"))
        r_layout.addWidget(QRadioButton("Tier 2"))
        r_layout.addWidget(QRadioButton("Tier 3"))
        form.addRow("Priority Tier:", radios)

        form.addRow(QCheckBox("Agreed to Master Agreement"))
        form.addRow(QCheckBox("Account Active Status"))
        
        form.addRow("Relationship Weight:", QSlider(Qt.Orientation.Horizontal))
        form.addRow("Projected Seat Count:", QSpinBox())
        
        de = QDateEdit(calendarPopup=True)
        de.setDate(QDate.currentDate())
        form.addRow("Go-Live Target:", de)
        
        pg = QProgressBar()
        pg.setValue(45)
        form.addRow("Qualification Depth:", pg)
        
        layout.addLayout(form)
        
        btns = QHBoxLayout()
        btns.addWidget(QPushButton("Register Entry", styleSheet="background: #27ae60; color: white; padding: 10px;"))
        btns.addWidget(QPushButton("Discard", styleSheet="background: #e74c3c; color: white; padding: 10px;"))
        layout.addLayout(btns)
        
        layout.addStretch()
        scroll.setWidget(tab)
        self.tabs.addTab(scroll, "Maintenance")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
