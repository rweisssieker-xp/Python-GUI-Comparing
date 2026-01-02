import dearpygui.dearpygui as dpg

def save_callback(sender, data):
    print("Record Persisted to GPU memory space!")

def main():
    dpg.create_context()
    dpg.create_viewport(title='Dear PyGui Ultimate CRM Demo', width=1100, height=800)

    with dpg.window(label="Enterprise Management System", width=1080, height=760, no_close=True, no_move=True):
        with dpg.tab_bar():
            
            # --- TAB 1: DASHBOARD ---
            with dpg.tab(label="Performance Analytics"):
                dpg.add_text("Global Business Intelligence Overview", color=[0, 255, 0])
                with dpg.group(horizontal=True):
                    with dpg.child_window(width=300, height=100, border=True):
                        dpg.add_text("Quarterly MRR")
                        dpg.add_text("$1,420,500", color=[0, 200, 255])
                    with dpg.child_window(width=300, height=100, border=True):
                        dpg.add_text("Lead Conversion Rate")
                        dpg.add_text("24.8%", color=[255, 200, 0])
                    with dpg.child_window(width=300, height=100, border=True):
                        dpg.add_text("Urgent Issues")
                        dpg.add_text("3", color=[255, 50, 50])

            # --- TAB 2: REGISTER ---
            with dpg.tab(label="Consumer Registry"):
                with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                               borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):
                    dpg.add_table_column(label="Ref#")
                    dpg.add_table_column(label="Entity Name")
                    dpg.add_table_column(label="Primary Contact")
                    dpg.add_table_column(label="Current Status")

                    for i in range(1, 16):
                        with dpg.table_row():
                            dpg.add_text(f"{100+i}")
                            dpg.add_text(f"Corporation {i} Allied")
                            dpg.add_text(f"manager_{i}@client.com")
                            dpg.add_text("ACTIVE" if i%2 else "STAGING")

            # --- TAB 3: ADMIN ---
            with dpg.tab(label="Lifecycle Operations"):
                dpg.add_text("Account Provisioning Form", color=[0, 255, 255])
                
                # 1. Input Text
                dpg.add_input_text(label="Legal Entity Name", width=400)
                
                # 2. Multiline Notes
                dpg.add_input_text(label="Relationship Notes", multiline=True, height=100, width=400)
                
                # 3. Combo
                dpg.add_combo(["Retail", "Gov", "Defense", "SaaS"], label="Vertical Sector", width=400)
                
                # 4. Radio
                dpg.add_radio_button(["B2B", "B2C", "NGO"], label="Commercial Logic", horizontal=True)
                
                # 5. Checkbox
                dpg.add_checkbox(label="Automated Audit Trail Enabled", default_value=True)
                
                # 6. Switch (Mocked with checkbox)
                dpg.add_checkbox(label="SYSTEM ACTIVE")
                
                # 7. Slider
                dpg.add_slider_int(label="Internal Priority Score", default_value=50, width=400)
                
                # 8. Spin / Input Int
                dpg.add_input_int(label="Base License Seats", default_value=10, width=400)
                
                # 9. Date Picker
                with dpg.group(horizontal=True):
                    dpg.add_text("Renewal Date:")
                    dpg.add_date_picker(label="Date", default_value={'month_day': 15, 'year': 2024, 'month': 12})
                
                # 10. Progress Bar
                dpg.add_text("Database Synchronization Depth:")
                dpg.add_progress_bar(label="Sync", default_value=0.72, width=400)
                
                # 11. Buttons
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Commit to CRM", callback=save_callback, width=150)
                    dpg.add_button(label="Reset Fields", width=150)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()
