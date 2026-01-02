"""
Gradio CRM Demo - ML/AI focused web framework
Gradio creates web interfaces for Python functions
"""

import gradio as gr
import pandas as pd

# Sample data for customer registry
def get_customer_data():
    data = []
    for i in range(1, 16):
        data.append({
            "ID": 100 + i,
            "Organization": f"Client {i} Corp",
            "Sector": "Tech",
            "Revenue": f"${i*10}k",
            "Score": f"{70+i}%"
        })
    return pd.DataFrame(data)

# Dashboard metrics
def show_dashboard():
    metrics_html = """
    <div style="display: flex; gap: 20px; margin: 20px 0;">
        <div style="flex: 1; padding: 20px; background: #e3f2fd; border-radius: 8px;">
            <h3>Global Sales</h3>
            <h2 style="color: blue;">$1.28M</h2>
        </div>
        <div style="flex: 1; padding: 20px; background: #e8f5e9; border-radius: 8px;">
            <h3>Conversion</h3>
            <h2 style="color: green;">18.4%</h2>
        </div>
        <div style="flex: 1; padding: 20px; background: #ffebee; border-radius: 8px;">
            <h3>Pending Tasks</h3>
            <h2 style="color: red;">14</h2>
        </div>
    </div>
    <div style="margin: 20px 0;">
        <h3>System Synchronization State</h3>
        <progress value="72" max="100" style="width: 100%; height: 30px;"></progress>
        <p>72% Complete</p>
    </div>
    """
    return metrics_html

# Admin form processing
def process_admin_form(org_name, notes, industry, strategy, billing, web_visible, priority, seats, contract_date, meeting_time, brand_color):
    result = f"""
    <h3>Entry Submitted Successfully!</h3>
    <p><strong>Organization:</strong> {org_name}</p>
    <p><strong>Industry:</strong> {industry}</p>
    <p><strong>Strategy:</strong> {strategy}</p>
    <p><strong>Advanced Billing:</strong> {'Yes' if billing else 'No'}</p>
    <p><strong>Web Visible:</strong> {'Yes' if web_visible else 'No'}</p>
    <p><strong>Priority:</strong> {priority}</p>
    <p><strong>Seats:</strong> {seats}</p>
    <p><strong>Contract Date:</strong> {contract_date}</p>
    <p><strong>Meeting Time:</strong> {meeting_time}</p>
    <p><strong>Brand Color:</strong> <span style="color: {brand_color};">{brand_color}</span></p>
    """
    return result

# Create interface with tabs
with gr.Blocks(title="Gradio Ultimate CRM Demo", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Enterprise CRM System")
    gr.Markdown("Built with Gradio - ML/AI focused web framework")
    
    with gr.Tabs():
        # Tab 1: Dashboard
        with gr.Tab("Performance Dashboard"):
            dashboard_html = gr.HTML(show_dashboard())
            refresh_btn = gr.Button("Refresh Metrics")
            refresh_btn.click(fn=show_dashboard, outputs=dashboard_html)
        
        # Tab 2: Customer Registry
        with gr.Tab("Customer Registry"):
            customer_df = gr.Dataframe(
                get_customer_data(),
                headers=["ID", "Organization", "Sector", "Revenue", "Score"],
                interactive=False,
                wrap=True
            )
            search_input = gr.Textbox(label="Search customers", placeholder="Enter search term...")
            search_btn = gr.Button("Search")
            
            def search_customers(query):
                df = get_customer_data()
                if query:
                    filtered = df[df['Organization'].str.contains(query, case=False)]
                    return filtered
                return df
            
            search_btn.click(fn=search_customers, inputs=search_input, outputs=customer_df)
        
        # Tab 3: Administration
        with gr.Tab("System Administration"):
            gr.Markdown("### Global Client Registry Entry")
            
            with gr.Row():
                with gr.Column():
                    org_name = gr.Textbox(label="Organization Lead Name", placeholder="Enter organization name")
                    notes = gr.Textbox(label="Relationship History / Notes", lines=5, placeholder="Enter notes...")
                    industry = gr.Dropdown(label="Industry Vertical", choices=["Finance", "Healthcare", "Tech", "Education"])
                    strategy = gr.Radio(label="Market Strategy", choices=["B2B (Enterprise)", "B2C (Retail)"])
                    billing = gr.Checkbox(label="Enable Advanced Billing Tier")
                    web_visible = gr.Checkbox(label="ACCOUNT VISIBLE ON WEB PORTAL")
                
                with gr.Column():
                    priority = gr.Slider(label="Engagement Priority", minimum=0, maximum=100, value=50)
                    seats = gr.Number(label="Dedicated Seat Count", value=10, minimum=1, maximum=1000)
                    contract_date = gr.Textbox(label="Contract Start Date", placeholder="YYYY-MM-DD")
                    meeting_time = gr.Textbox(label="Preferred Meeting Time", placeholder="HH:MM")
                    brand_color = gr.ColorPicker(label="Brand Color", value="#000000")
            
            submit_btn = gr.Button("Submit Entry", variant="primary")
            result_output = gr.HTML()
            
            submit_btn.click(
                fn=process_admin_form,
                inputs=[org_name, notes, industry, strategy, billing, web_visible, priority, seats, contract_date, meeting_time, brand_color],
                outputs=result_output
            )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)
