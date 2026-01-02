from appJar import gui

def main():
    app = gui("appJar Ultimate CRM Demo", "1100x800")
    app.setBg("whitesmoke")
    app.setFont(14)

    app.startTabbedFrame("CRMHub")
    
    # --- TAB 1: OVERVIEW ---
    app.startTab("Summary")
    app.addLabel("t1", "Enterprise Analytics Dashboard", row=0, colspan=3)
    app.setLabelFont("t1", 22, "bold")
    
    app.startLabelFrame("Key Metrics", row=1, colspan=3)
    metrics_frame = app.startFrame("metrics", row=1, colspan=3)
    app.addLabel("m1", "Pipeline: $4.2M", row=1, column=0)
    app.setLabelFg("m1", "blue")
    app.addLabel("m2", "Conversion: 18.2%", row=1, column=1)
    app.setLabelFg("m2", "green")
    app.addLabel("m3", "Leads: 342", row=1, column=2)
    app.setLabelFg("m3", "red")
    app.stopFrame()
    app.stopLabelFrame()
    
    app.addLabel("l_progress", "System Synchronization State:")
    app.addMeter("sync_meter")
    app.setMeter("sync_meter", 72)
    app.stopTab()

    # --- TAB 2: DATABASE ---
    app.startTab("Accounts")
    data = [["ID", "Organization", "HQ", "Rep", "Value"]]
    for i in range(1, 16):
        data.append([str(100+i), f"Entity {i} Corp", "Berlin", "Rep A", f"${i*10}k"])
    
    app.addTable("t_db", data)
    app.stopTab()

    # --- TAB 3: ADMIN (10+ CONTROLS) ---
    app.startTab("Maintenance")
    app.addLabel("l_admin", "Global Client Registry Entry", row=0, colspan=2)
    app.setLabelBg("l_admin", "navy")
    app.setLabelFg("l_admin", "white")
    
    # 1. Input
    app.addLabelEntry("Full Legal Name")
    # 2. TextArea
    app.addLabelTextArea("Historical Notes")
    # 3. OptionBox
    app.addLabelOptionBox("Sector Vertical", ["Finance", "Energy", "Tech", "Gov"])
    # 4. Radios
    app.addRadioButton("category", "B2B Enterprise")
    app.addRadioButton("category", "B2C Consumer")
    # 5. Checkbox
    app.addCheckBox("Enable Marketing Automation")
    # 6. Switch (Mocked with checkbox styled or simple)
    app.addCheckBox("VISIBLE ON DIRECTOR")
    # 7. Scale (Slider)
    app.addLabelScale("Priority Weighting")
    # 8. SpinBox
    app.addLabelSpinBox("Seat Allocation", [i for i in range(0, 1001, 10)])
    # 9. Date Picker
    app.addDatePicker("Renewal Date")
    
    def on_click(btn):
        name = app.getEntry("Full Legal Name")
        app.infoBox("System Notification", f"Record for {name} successfully committed.")

    app.addButton("Commit to Database", on_click)
    app.stopTab()

    app.stopTabbedFrame()
    app.go()

if __name__ == "__main__":
    main()
