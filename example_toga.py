import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class TogaCRMApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title="Toga Ultimate CRM Demo", size=(1100, 800))

        # --- TAB 1: DASHBOARD ---
        dash_box = toga.Box(style=Pack(direction=COLUMN, padding=20))
        dash_box.add(toga.Label("Global Business Analytics", style=Pack(font_size=20, font_weight="bold", padding_bottom=10)))
        
        stat_row = toga.Box(style=Pack(direction=ROW, padding=10))
        for m_name, m_val in [("Global MRR", "$1.2M"), ("Open Leads", "450"), ("Support Load", "12")]:
            card = toga.Box(style=Pack(direction=COLUMN, padding=15))
            card.add(toga.Label(m_name, style=Pack(font_size=10)))
            card.add(toga.Label(m_val, style=Pack(font_size=16, font_weight="bold")))
            stat_row.add(card)
        dash_box.add(stat_row)

        # --- TAB 2: REGISTRY (15 ROWS) ---
        reg_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        data = [(str(100+i), f"Corp {i} Systems", "Active" if i%2 else "Staging", f"${i*5}k") for i in range(1, 16)]
        table = toga.Table(
            headings=["ID", "Entity", "Status", "Value"],
            data=data,
            style=Pack(flex=1)
        )
        reg_box.add(table)

        # --- TAB 3: ADMIN (10+ CONTROLS) ---
        admin_content = toga.Box(style=Pack(direction=COLUMN, padding=20))
        
        admin_content.add(toga.Label("System Record Entry", style=Pack(font_size=16, font_weight="bold", padding_bottom=10)))
        
        # 1. Text Input
        admin_content.add(toga.Label("Primary Account Name:"))
        self.name_input = toga.TextInput(style=Pack(padding_bottom=10))
        admin_content.add(self.name_input)
        
        # 2. Multiline
        admin_content.add(toga.Label("Internal Background Notes:"))
        self.notes_input = toga.MultilineTextInput(style=Pack(height=100, padding_bottom=10))
        admin_content.add(self.notes_input)
        
        # 3. Selection
        admin_content.add(toga.Label("Industry Sector:"))
        self.sector_selection = toga.Selection(items=["Tech", "Manufacturing", "Finance", "Energy"], style=Pack(padding_bottom=10))
        admin_content.add(self.sector_selection)
        
        # 4. Radio (Toga uses RadioButton with shared group)
        admin_content.add(toga.Label("Account Category:"))
        group = toga.Group("Type")
        self.r_b2b = toga.RadioButton("B2B Enterprise", group=group)
        self.r_b2c = toga.RadioButton("B2C Individual", group=group)
        admin_content.add(self.r_b2b)
        admin_content.add(self.r_b2c)
        
        # 5. Switch
        self.active_switch = toga.Switch("Account Active Status", value=True, style=Pack(padding_top=10))
        admin_content.add(self.active_switch)
        
        # 7. Slider
        admin_content.add(toga.Label("Priority Weighting:", style=Pack(padding_top=10)))
        self.priority_slider = toga.Slider(range=(0, 100), value=45, style=Pack(padding_bottom=10))
        admin_content.add(self.priority_slider)
        
        # 8. Number Input
        admin_content.add(toga.Label("Member Seat Count:"))
        self.seats_input = toga.NumberInput(step=5, min_value=0, style=Pack(padding_bottom=10))
        admin_content.add(self.seats_input)
        
        # 10. Progress
        admin_content.add(toga.Label("Cloud Synchronization State:"))
        self.progress = toga.ProgressBar(max=100, value=65, style=Pack(padding_bottom=10))
        admin_content.add(self.progress)
        
        # Buttons
        btn_box = toga.Box(style=Pack(direction=ROW, padding_top=20))
        btn_box.add(toga.Button("Register Organization", on_press=self.save_record, style=Pack(padding_right=10)))
        btn_box.add(toga.Button("Reset Form"))
        admin_content.add(btn_box)

        admin_scroll = toga.ScrollContainer(content=admin_content, style=Pack(flex=1))

        # Tabs
        self.container = toga.OptionContainer(
            content=[
                ("Analytics", dash_box),
                ("Registry", reg_box),
                ("Maintenance", admin_scroll),
            ]
        )

        self.main_window.content = self.container
        self.main_window.show()

    def save_record(self, widget):
        self.main_window.info_dialog("Info", f"Organization {self.name_input.value} saved!")

if __name__ == "__main__":
    app = TogaCRMApp("Ultimate CRM", "org.beeware.crm")
    app.main_loop()
