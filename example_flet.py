import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Flet Ultimate CRM Demo"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1100
    page.window_height = 800
    page.padding = 20

    def on_tab_change(e):
        index = e.control.selected_index
        dashboard_view.visible = (index == 0)
        customer_view.visible = (index == 1)
        form_view.visible = (index == 2)
        page.update()

    # --- VIEWS ---
    
    # 1. Dashboard View
    dashboard_view = ft.Column([
        ft.Text("Business Intelligence Dashboard", size=32, weight="bold"),
        ft.Row([
            ft.Container(ft.Column([ft.Text("Annual Revenue"), ft.Text("$1.42M", size=24, weight="bold")]), padding=25, border_radius=15, border=ft.border.all(1, ft.colors.BLUE_400), width=300),
            ft.Container(ft.Column([ft.Text("Qualified Leads"), ft.Text("128", size=24, weight="bold", color="green")]), padding=25, border_radius=15, border=ft.border.all(1, ft.colors.GREEN_400), width=300),
            ft.Container(ft.Column([ft.Text("Customer Churn"), ft.Text("2.4%", size=24, weight="bold", color="red")]), padding=25, border_radius=15, border=ft.border.all(1, ft.colors.RED_400), width=300),
        ], alignment="center", spacing=20)
    ], visible=True, expand=True)

    # 2. Customer Table View (15 Rows)
    data_rows = [
        ft.DataRow(cells=[ft.DataCell(ft.Text(str(100+i))), ft.DataCell(ft.Text(f"Enterprise {i}")), ft.DataCell(ft.Text(f"contact{i}@corp.com")), ft.DataCell(ft.Text("Active" if i%2 else "Lead"))])
        for i in range(1, 16)
    ]
    
    customer_view = ft.Column([
        ft.Text("Client Directory", size=28, weight="bold"),
        ft.Row([
            ft.TextField(label="Search by name...", prefix_icon=ft.icons.SEARCH, expand=True),
            ft.IconButton(icon=ft.icons.FILTER_ALT)
        ]),
        ft.ListView(expand=1, spacing=10, padding=10, controls=[
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID")),
                    ft.DataColumn(ft.Text("Company")),
                    ft.DataColumn(ft.Text("Email")),
                    ft.DataColumn(ft.Text("Status")),
                ],
                rows=data_rows
            )
        ])
    ], visible=False, expand=True)

    # 3. Registration Form View (10+ Controls)
    form_view = ft.Column([
        ft.Text("New Account Registration", size=28, weight="bold"),
        ft.TextField(label="Full Legal Name", width=600, helper_text="Enter the official company name"),
        ft.TextField(label="Historical Notes", width=600, multiline=True, min_lines=3, max_lines=5),
        ft.Dropdown(
            label="Industry Sector",
            options=[ft.dropdown.Option("Technology"), ft.dropdown.Option("Healthcare"), ft.dropdown.Option("Finance"), ft.dropdown.Option("Retail")],
            width=600
        ),
        ft.Row([
            ft.Text("Account Category:"),
            ft.RadioGroup(content=ft.Row([
                ft.Radio(value="b2b", label="B2B (Corperate)"),
                ft.Radio(value="b2c", label="B2C (Consumer)"),
                ft.Radio(value="ngo", label="Non-Profit"),
            ]))
        ]),
        ft.Row([
            ft.Checkbox(label="Marketing Consent", value=True),
            ft.Switch(label="Premium Support Tier", value=False),
        ]),
        ft.Slider(min=0, max=100, divisions=10, label="Service Level Priority: {value}"),
        ft.Row([
            ft.Text("Employee Scale:"),
            ft.NumberControl(value=50, step=10, width=150),
        ]),
        ft.Row([
            ft.Text("Registration Date:"),
            ft.ElevatedButton("Pick Date", icon=ft.icons.CALENDAR_MONTH, on_click=lambda _: date_picker.pick_date()),
            ft.Text(datetime.date.today().strftime("%Y-%m-%d")),
        ]),
        ft.Text("Processing Synchronization:"),
        ft.ProgressBar(width=600, value=0.4, color="blue"),
        ft.Row([
            ft.ElevatedButton("Submit Entry", color="white", bgcolor=ft.colors.BLUE_700, width=200),
            ft.OutlinedButton("Reset Form", width=200),
        ])
    ], visible=False, expand=True, scroll=ft.ScrollMode.AUTO)

    date_picker = ft.DatePicker(
        on_change=lambda e: print(f"Selected: {e.data}"),
        first_date=datetime.datetime(2023, 1, 1),
        last_date=datetime.datetime(2026, 12, 31),
    )
    page.overlay.append(date_picker)

    # Main Layout
    tabs = ft.Tabs(
        selected_index=0,
        on_change=on_tab_change,
        tabs=[
            ft.Tab(text="Overview", icon=ft.icons.DASHBOARD_ROUNDED),
            ft.Tab(text="Database", icon=ft.icons.FORMAT_LIST_BULLETED),
            ft.Tab(text="Operations", icon=ft.icons.ADMIN_PANEL_SETTINGS),
        ]
    )

    page.add(tabs, ft.Divider(), dashboard_view, customer_view, form_view)

if __name__ == "__main__":
    ft.app(target=main)
