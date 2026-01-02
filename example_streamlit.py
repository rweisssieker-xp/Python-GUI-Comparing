"""
Streamlit CRM Demo - Web-based data science framework
Streamlit creates web apps automatically from Python scripts
"""

import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="Streamlit Ultimate CRM Demo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Performance Dashboard", "Customer Registry", "System Administration"])

if page == "Performance Dashboard":
    st.title("Enterprise Data Overview")
    st.markdown("---")
    
    # Metrics cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Global Sales", "$1.28M", "12%")
    with col2:
        st.metric("Conversion Rate", "18.4%", "2.3%")
    with col3:
        st.metric("Pending Tasks", "14", "-3")
    
    st.markdown("---")
    
    # Chart
    chart_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Sales': [120000, 135000, 128000, 142000, 128000]
    })
    st.line_chart(chart_data.set_index('Month'))
    
    # Progress bar
    st.subheader("System Synchronization State")
    st.progress(0.72)
    st.caption("72% Complete")

elif page == "Customer Registry":
    st.title("Customer Registry")
    
    # Create sample data
    data = []
    for i in range(1, 16):
        data.append({
            "ID": 100 + i,
            "Organization": f"Client {i} Corp",
            "Sector": "Tech",
            "Revenue": f"${i*10}k",
            "Score": f"{70+i}%"
        })
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Search functionality
    search_term = st.text_input("Search customers")
    if search_term:
        filtered_df = df[df['Organization'].str.contains(search_term, case=False)]
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

elif page == "System Administration":
    st.title("System Administration")
    st.markdown("Global Client Registry Entry")
    
    # Form with 10+ components
    with st.form("admin_form"):
        # 1. Text Input
        org_name = st.text_input("Organization Lead Name", placeholder="Enter organization name")
        
        # 2. Text Area
        notes = st.text_area("Relationship History / Notes", height=100, placeholder="Enter notes...")
        
        # 3. Selectbox
        industry = st.selectbox("Industry Vertical", ["Finance", "Healthcare", "Tech", "Education"])
        
        # 4. Radio buttons
        market_strategy = st.radio("Market Strategy", ["B2B (Enterprise)", "B2C (Retail)"])
        
        # 5. Checkbox
        advanced_billing = st.checkbox("Enable Advanced Billing Tier")
        
        # 6. Toggle (Switch)
        web_visible = st.toggle("ACCOUNT VISIBLE ON WEB PORTAL")
        
        # 7. Slider
        priority = st.slider("Engagement Priority", 0, 100, 50)
        
        # 8. Number input
        seat_count = st.number_input("Dedicated Seat Count", min_value=1, max_value=1000, value=10)
        
        # 9. Date input
        contract_date = st.date_input("Contract Start Date")
        
        # 10. Time input
        meeting_time = st.time_input("Preferred Meeting Time")
        
        # 11. Color picker
        brand_color = st.color_picker("Brand Color", "#000000")
        
        # Submit button
        submitted = st.form_submit_button("Submit Entry")
        
        if submitted:
            st.success("Entry submitted successfully!")
            st.json({
                "Organization": org_name,
                "Industry": industry,
                "Strategy": market_strategy,
                "Priority": priority,
                "Seats": seat_count
            })

# Footer
st.markdown("---")
st.caption("Streamlit CRM Demo - Built with Streamlit framework")
