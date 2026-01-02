"""
Remi CRM Demo - Pure Python web GUI
Remi creates web interfaces using only Python
"""

import remi.gui as gui
from remi import start, App

class CRMApp(App):
    def __init__(self, *args):
        super(CRMApp, self).__init__(*args)
    
    def main(self):
        container = gui.VBox(width='100%', height='100%', margin='0px auto', style={'padding': '20px'})
        
        # Header
        title = gui.Label("Enterprise CRM System", width='100%', style={'font-size': '24px', 'font-weight': 'bold', 'text-align': 'center', 'margin': '10px'})
        subtitle = gui.Label("Built with Remi - Pure Python Web GUI", width='100%', style={'text-align': 'center', 'margin': '10px'})
        container.append(title)
        container.append(subtitle)
        
        # Tabs
        self.tabs = gui.TabBox(width='100%', height='600px')
        
        # Tab 1: Dashboard
        dashboard_tab = gui.VBox(width='100%', height='100%', style={'padding': '20px'})
        dashboard_title = gui.Label("Enterprise Data Overview", style={'font-size': '20px', 'font-weight': 'bold', 'margin': '10px'})
        dashboard_tab.append(dashboard_title)
        
        # Metrics
        metrics_container = gui.HBox(width='100%', style={'margin': '20px 0'})
        
        sales_box = gui.VBox(width='30%', style={'background-color': '#e3f2fd', 'padding': '20px', 'margin': '10px', 'border-radius': '8px', 'text-align': 'center'})
        sales_box.append(gui.Label("Global Sales", style={'font-weight': 'bold'}))
        sales_box.append(gui.Label("$1.28M", style={'font-size': '24px', 'color': 'blue', 'font-weight': 'bold'}))
        metrics_container.append(sales_box)
        
        conversion_box = gui.VBox(width='30%', style={'background-color': '#e8f5e9', 'padding': '20px', 'margin': '10px', 'border-radius': '8px', 'text-align': 'center'})
        conversion_box.append(gui.Label("Conversion", style={'font-weight': 'bold'}))
        conversion_box.append(gui.Label("18.4%", style={'font-size': '24px', 'color': 'green', 'font-weight': 'bold'}))
        metrics_container.append(conversion_box)
        
        tasks_box = gui.VBox(width='30%', style={'background-color': '#ffebee', 'padding': '20px', 'margin': '10px', 'border-radius': '8px', 'text-align': 'center'})
        tasks_box.append(gui.Label("Pending Tasks", style={'font-weight': 'bold'}))
        tasks_box.append(gui.Label("14", style={'font-size': '24px', 'color': 'red', 'font-weight': 'bold'}))
        metrics_container.append(tasks_box)
        
        dashboard_tab.append(metrics_container)
        
        # Progress bar
        progress_label = gui.Label("System Synchronization State", style={'font-weight': 'bold', 'margin': '20px 10px 10px'})
        dashboard_tab.append(progress_label)
        progress_bar = gui.Progress(width='100%', max_value=100, value=72, style={'height': '30px', 'margin': '10px'})
        dashboard_tab.append(progress_bar)
        progress_text = gui.Label("72% Complete", style={'margin': '10px'})
        dashboard_tab.append(progress_text)
        
        self.tabs.append_tab(dashboard_tab, "Performance Dashboard")
        
        # Tab 2: Customers
        customers_tab = gui.VBox(width='100%', height='100%', style={'padding': '20px'})
        customers_title = gui.Label("Customer Registry", style={'font-size': '20px', 'font-weight': 'bold', 'margin': '10px'})
        customers_tab.append(customers_title)
        
        # Search
        search_input = gui.Input(width='100%', placeholder='Search customers...', style={'padding': '10px', 'margin': '10px'})
        customers_tab.append(search_input)
        
        # Customer table (simplified as list)
        customer_list = gui.VBox(width='100%', style={'margin': '10px'})
        for i in range(1, 16):
            customer_item = gui.Label(
                f"ID: {100+i} | Client {i} Corp | Tech | ${i*10}k | {70+i}%",
                width='100%',
                style={'padding': '5px', 'border-bottom': '1px solid #ccc'}
            )
            customer_list.append(customer_item)
        customers_tab.append(customer_list)
        
        self.tabs.append_tab(customers_tab, "Customer Registry")
        
        # Tab 3: Admin
        admin_tab = gui.VBox(width='100%', height='100%', style={'padding': '20px'})
        admin_title = gui.Label("System Administration", style={'font-size': '20px', 'font-weight': 'bold', 'margin': '10px'})
        admin_tab.append(admin_title)
        admin_subtitle = gui.Label("Global Client Registry Entry", style={'font-weight': 'bold', 'margin': '10px'})
        admin_tab.append(admin_subtitle)
        
        # Form fields
        form_container = gui.VBox(width='100%', style={'margin': '10px'})
        
        org_name = gui.Input(width='100%', placeholder='Organization Lead Name', style={'padding': '10px', 'margin': '5px'})
        form_container.append(org_name)
        
        notes = gui.TextInput(width='100%', placeholder='Relationship History / Notes', style={'padding': '10px', 'margin': '5px', 'height': '100px'})
        form_container.append(notes)
        
        industry = gui.DropDown.new_from_list(['Finance', 'Healthcare', 'Tech', 'Education'], width='100%', style={'padding': '10px', 'margin': '5px'})
        industry.set_value('Tech')
        form_container.append(gui.Label("Industry Vertical:", style={'margin': '5px'}))
        form_container.append(industry)
        
        strategy = gui.DropDown.new_from_list(['B2B (Enterprise)', 'B2C (Retail)'], width='100%', style={'padding': '10px', 'margin': '5px'})
        strategy.set_value('B2B (Enterprise)')
        form_container.append(gui.Label("Market Strategy:", style={'margin': '5px'}))
        form_container.append(strategy)
        
        billing_check = gui.CheckBoxLabel("Enable Advanced Billing Tier", width='100%', style={'margin': '5px'})
        form_container.append(billing_check)
        
        web_check = gui.CheckBoxLabel("ACCOUNT VISIBLE ON WEB PORTAL", width='100%', style={'margin': '5px'})
        form_container.append(web_check)
        
        priority_label = gui.Label("Engagement Priority (0-100):", style={'margin': '5px'})
        form_container.append(priority_label)
        priority_slider = gui.Slider(0, 100, 50, width='100%', style={'margin': '5px'})
        form_container.append(priority_slider)
        
        seats = gui.Input(width='100%', placeholder='Dedicated Seat Count', value='10', style={'padding': '10px', 'margin': '5px'})
        form_container.append(seats)
        
        contract_date = gui.Input(width='100%', placeholder='Contract Start Date (YYYY-MM-DD)', style={'padding': '10px', 'margin': '5px'})
        form_container.append(contract_date)
        
        meeting_time = gui.Input(width='100%', placeholder='Preferred Meeting Time (HH:MM)', style={'padding': '10px', 'margin': '5px'})
        form_container.append(meeting_time)
        
        submit_btn = gui.Button("Submit Entry", width='100%', style={'padding': '10px', 'margin': '10px', 'background-color': '#4CAF50', 'color': 'white'})
        form_container.append(submit_btn)
        
        result_label = gui.Label("", width='100%', style={'margin': '10px', 'color': 'green'})
        form_container.append(result_label)
        
        def on_submit(widget):
            result_label.set_text(f"Entry submitted for: {org_name.get_value()}")
        
        submit_btn.onclick.connect(on_submit)
        
        admin_tab.append(form_container)
        self.tabs.append_tab(admin_tab, "System Administration")
        
        container.append(self.tabs)
        
        return container

if __name__ == "__main__":
    start(CRMApp, address='127.0.0.1', port=8080, start_browser=True)
