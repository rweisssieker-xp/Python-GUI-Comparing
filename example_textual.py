"""
Textual CRM Demo - Modern terminal UI framework
Textual creates rich terminal applications
"""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, DataTable, Input, Button, Select, Checkbox, Label, ProgressBar, Static
from textual.binding import Binding
from datetime import datetime

class CRMApp(App):
    """A Textual CRM application."""
    
    CSS = """
    Screen {
        background: $surface;
    }
    
    .metrics {
        height: 5;
        margin: 1;
    }
    
    .metric-box {
        width: 1fr;
        padding: 1;
        border: solid $primary;
        margin: 1;
    }
    
    .title {
        text-style: bold;
        color: $accent;
    }
    """
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("d", "switch_tab('dashboard')", "Dashboard"),
        Binding("c", "switch_tab('customers')", "Customers"),
        Binding("a", "switch_tab('admin')", "Admin"),
    ]
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        
        with Container(id="app"):
            with Horizontal(id="tabs"):
                yield Button("Dashboard", id="tab-dashboard", variant="primary")
                yield Button("Customers", id="tab-customers")
                yield Button("Admin", id="tab-admin")
            
            # Dashboard Tab
            with Container(id="dashboard", classes="tab-content"):
                yield Label("Enterprise Data Overview", classes="title")
                with Horizontal(classes="metrics"):
                    with Container(classes="metric-box"):
                        yield Label("Global Sales", classes="title")
                        yield Label("$1.28M", id="sales")
                    with Container(classes="metric-box"):
                        yield Label("Conversion", classes="title")
                        yield Label("18.4%", id="conversion")
                    with Container(classes="metric-box"):
                        yield Label("Pending Tasks", classes="title")
                        yield Label("14", id="tasks")
                
                yield Label("System Synchronization State", classes="title")
                yield ProgressBar(total=100, progress=72, id="sync-progress")
                yield Label("72% Complete", id="sync-label")
            
            # Customers Tab
            with Container(id="customers", classes="tab-content", display=False):
                yield Label("Customer Registry", classes="title")
                yield Input(placeholder="Search customers...", id="search-input")
                table = DataTable(id="customer-table")
                table.add_columns("ID", "Organization", "Sector", "Revenue", "Score")
                for i in range(1, 16):
                    table.add_row(
                        str(100+i),
                        f"Client {i} Corp",
                        "Tech",
                        f"${i*10}k",
                        f"{70+i}%"
                    )
                yield table
            
            # Admin Tab
            with Container(id="admin", classes="tab-content", display=False):
                yield Label("System Administration", classes="title")
                yield Label("Global Client Registry Entry")
                
                yield Input(placeholder="Organization Lead Name", id="org-name")
                yield Input(placeholder="Relationship History / Notes", id="notes")
                
                yield Select(
                    [("Finance", "finance"), ("Healthcare", "healthcare"), ("Tech", "tech"), ("Education", "education")],
                    prompt="Industry Vertical",
                    id="industry"
                )
                
                yield Select(
                    [("B2B (Enterprise)", "b2b"), ("B2C (Retail)", "b2c")],
                    prompt="Market Strategy",
                    id="strategy"
                )
                
                yield Checkbox("Enable Advanced Billing Tier", id="billing")
                yield Checkbox("ACCOUNT VISIBLE ON WEB PORTAL", id="web-visible")
                
                yield Label("Engagement Priority (0-100):")
                yield ProgressBar(total=100, progress=50, id="priority-bar")
                
                yield Input(placeholder="Dedicated Seat Count", id="seats")
                yield Input(placeholder="Contract Start Date (YYYY-MM-DD)", id="contract-date")
                yield Input(placeholder="Preferred Meeting Time (HH:MM)", id="meeting-time")
                
                yield Button("Submit Entry", id="submit-btn", variant="primary")
                yield Static("", id="submit-result")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "tab-dashboard":
            self.switch_tab("dashboard")
        elif event.button.id == "tab-customers":
            self.switch_tab("customers")
        elif event.button.id == "tab-admin":
            self.switch_tab("admin")
        elif event.button.id == "submit-btn":
            self.submit_form()
    
    def switch_tab(self, tab_name: str) -> None:
        """Switch between tabs."""
        # Hide all tabs
        self.query_one("#dashboard", Container).display = False
        self.query_one("#customers", Container).display = False
        self.query_one("#admin", Container).display = False
        
        # Reset button styles
        self.query_one("#tab-dashboard", Button).variant = "default"
        self.query_one("#tab-customers", Button).variant = "default"
        self.query_one("#tab-admin", Button).variant = "default"
        
        # Show selected tab
        if tab_name == "dashboard":
            self.query_one("#dashboard", Container).display = True
            self.query_one("#tab-dashboard", Button).variant = "primary"
        elif tab_name == "customers":
            self.query_one("#customers", Container).display = True
            self.query_one("#tab-customers", Button).variant = "primary"
        elif tab_name == "admin":
            self.query_one("#admin", Container).display = True
            self.query_one("#tab-admin", Button).variant = "primary"
    
    def submit_form(self) -> None:
        """Process form submission."""
        org_name = self.query_one("#org-name", Input).value
        result = f"Entry submitted for: {org_name}"
        self.query_one("#submit-result", Static).update(result)
    
    def action_switch_tab(self, tab: str) -> None:
        """Action to switch tabs."""
        self.switch_tab(tab)

if __name__ == "__main__":
    app = CRMApp()
    app.run()
