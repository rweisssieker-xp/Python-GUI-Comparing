import PySimpleGUI as sg
import datetime

def main():
    sg.theme("DarkBlue3")

    # --- TAB 1: OVERVIEW ---
    tab1_layout = [
        [sg.Text("Corporate Sales Dashboard", font=("Any", 20, "bold"))],
        [sg.Frame("Key Metrics", [
            [sg.Column([
                [sg.Text("Total Revenue", font=("Any", 12))], [sg.Text("$2.1M", font=("Any", 18, "bold"), text_color="cyan")]
            ]), sg.VerticalSeparator(),
            sg.Column([
                [sg.Text("New Leads", font=("Any", 12))], [sg.Text("480", font=("Any", 18, "bold"), text_color="lightgreen")]
            ]), sg.VerticalSeparator(),
            sg.Column([
                [sg.Text("Risk Portfolio", font=("Any", 12))], [sg.Text("Low", font=("Any", 18, "bold"), text_color="yellow")]
            ])]
        ], padding=20)]
    ]

    # --- TAB 2: DATABASE ---
    data = [[100+i, f"Organization {i} Inc.", f"admin_{i}@corp.net", "Partner" if i%3==0 else "Prospect"] for i in range(1, 16)]
    tab2_layout = [
        [sg.Text("Filtered Client List (15 Records)", font=("Any", 16))],
        [sg.Input(key="-SEARCH-", size=(40,1)), sg.Button("Search")],
        [sg.Table(values=data, headings=["ID", "Entity", "Primary Email", "Category"], 
                  num_rows=10, auto_size_columns=True, expand_x=True, expand_y=True, key="-TABLE-")]
    ]

    # --- TAB 3: MAINTENANCE ---
    tab3_layout = [
        [sg.Text("Detailed Lead Profile Registration", font=("Any", 16, "bold"))],
        # 1. Input
        [sg.Text("Lead Name:", size=(20,1)), sg.Input(key="-NAME-", expand_x=True)],
        # 2. Multiline
        [sg.Text("Relationship Bio:", size=(20,1)), sg.Multiline(key="-BIO-", size=(40, 5), expand_x=True)],
        # 3. Combo
        [sg.Text("Industry Sector:", size=(20,1)), sg.Combo(["Finance", "Logistics", "BioTech", "Retail"], key="-IND-", expand_x=True)],
        # 4. Radios
        [sg.Text("Account Type:", size=(20,1)), sg.Radio("Enterprise", "R1", default=True), sg.Radio("Education", "R1"), sg.Radio("NGO", "R1")],
        # 5. Checkbox
        [sg.Checkbox("Marketing Automation Enabled", default=True, key="-MARKETING-")],
        # 6. Switch (Mocked with sg.Checkbox)
        [sg.Checkbox("ACCOUNT ACTIVE & VISIBLE", key="-ACTIVE-")],
        # 7. Slider
        [sg.Text("Conversion Probability:", size=(20,1)), sg.Slider(range=(0,100), default_value=45, orientation='h', expand_x=True)],
        # 8. Spin
        [sg.Text("Licensed User Count:", size=(20,1)), sg.Spin([i for i in range(1, 1000)], initial_value=25, key="-SEATS-")],
        # 9. Calendar / Date mockup
        [sg.Text("Target Close Date:", size=(20,1)), sg.Input(key="-DATE-", size=(20,1)), sg.CalendarButton("Pick Date", target="-DATE-")],
        # 10. ProgressBar
        [sg.Text("Sync Status:"), sg.ProgressBar(100, orientation='h', size=(20, 20), key="-PROG-")],
        # Buttons
        [sg.Button("Register Opportunity", button_color=("white", "green")), sg.Button("Clear Form")]
    ]

    layout = [
        [sg.TabGroup([[sg.Tab("Dashboard", tab1_layout), 
                       sg.Tab("Records", tab2_layout), 
                       sg.Tab("Maintenance", tab3_layout)]], expand_x=True, expand_y=True)],
        [sg.Button("Exit Application")]
    ]

    window = sg.Window("PySimpleGUI Ultimate CRM", layout, size=(1000, 750), resizable=True, finalize=True)
    window["-PROG-"].update(68)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit Application"):
            break
        if event == "Register Opportunity":
            sg.popup(f"Account for {values['-NAME-']} successfully staged!")

    window.close()

if __name__ == "__main__":
    main()
