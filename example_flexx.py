from flexx import flx

class CRMApp(flx.Widget):
    def init(self):
        with flx.VBox(style="background: #fdfdfd; padding: 20px;"):
            flx.Label(text='Flexx Enterprise Hub', style='font-size: 26px; font-weight: bold; margin-bottom: 20px;')
            
            with flx.TabView(flex=1):
                # --- TAB 1: OVERVIEW ---
                with flx.VBox(title='Analytics', style="padding: 20px;"):
                    with flx.HBox():
                        with flx.VBox(style="border: 1px solid gray; padding: 15px; margin: 10px;"):
                            flx.Label(text="Revenue Q1")
                            flx.Label(text="$1.1M", style="font-size: 20px; color: blue;")
                        with flx.VBox(style="border: 1px solid gray; padding: 15px; margin: 10px;"):
                            flx.Label(text="New Accounts")
                            flx.Label(text="38", style="font-size: 20px; color: green;")
                
                # --- TAB 2: REGISTRY ---
                with flx.VBox(title='Accounts', style="padding: 10px; overflow-y: auto;"):
                    flx.Label(text="ID | Entity Name | Assigned Rep | Value", style="font-weight: bold;")
                    for i in range(1, 16):
                        flx.Label(text=f"{100+i} | Global Corp {i} | Admin Alpha | ${i*12}k")
                
                # --- TAB 3: ADMIN ---
                with flx.VBox(title='Inventory', style="padding: 20px;"):
                    flx.Label(text="Add Asset to Pipeline:", style="font-weight: bold; font-size: 16px;")
                    
                    # 1. Text Input
                    flx.Label(text="Asset Name:")
                    self.inp = flx.LineEdit(placeholder_text="Enter asset name", style="width: 300px;")
                    
                    # 2. Text Area (Multiline)
                    flx.Label(text="Detailed Description:")
                    self.text_area = flx.MultiLineEdit(placeholder_text="Enter detailed notes...", style="width: 300px; height: 100px;")
                    
                    # 3. Dropdown
                    flx.Label(text="System Classification:")
                    flx.ComboBox(options=["High Priority", "Normal", "Low"], style="width: 300px;")
                    
                    # 4. Radio Buttons
                    flx.Label(text="Deployment Type:")
                    with flx.HBox():
                        flx.RadioButton(text="Internal", checked=True)
                        flx.RadioButton(text="External")
                    
                    # 5. Checkbox
                    flx.CheckBox(text="Enable Proxy Access")
                    
                    # 6. Switch (Flexx doesn't have native switch, using checkbox with different label)
                    flx.CheckBox(text="SYSTEM ACTIVE STATUS", checked=True)
                    
                    # 7. Slider
                    flx.Label(text="Probability Score:")
                    flx.Slider(title="Score", min=0, max=100, value=45, style="width: 300px;")
                    
                    # 8. SpinBox (Number Input)
                    flx.Label(text="Seat Count:")
                    self.spin_input = flx.LineEdit(text="10", style="width: 100px;")
                    
                    # 9. Date Picker (Flexx doesn't have native date picker, using text input)
                    flx.Label(text="Review Date (YYYY-MM-DD):")
                    self.date_input = flx.LineEdit(text="2024-12-31", style="width: 200px;")
                    
                    # 10. Progress Bar
                    flx.Label(text="Sync Progress:")
                    self.prog = flx.ProgressBar(value=0.68, style="width: 300px;")
                    
                    # 11. Buttons
                    with flx.HBox():
                        self.btn = flx.Button(text="Submit Record", style="background: #27ae60; color: white;")
                        self.reset_btn = flx.Button(text="Reset Form", style="background: #95a5a6; color: white;")
                    
                    self.status = flx.Label(text="Status: Ready")

    @flx.reaction('btn.pointer_click')
    def _on_save(self, *events):
        self.status.set_text(f"Status: Record {self.inp.text} Staged!")
    
    @flx.reaction('reset_btn.pointer_click')
    def _on_reset(self, *events):
        self.inp.set_text("")
        self.text_area.set_text("")
        self.spin_input.set_text("10")
        self.date_input.set_text("2024-12-31")
        self.status.set_text("Status: Form Reset")

if __name__ == '__main__':
    print("Flexx: Starting server and launching browser...")
    app = flx.App(CRMApp)
    app.launch('browser')
    flx.run()
