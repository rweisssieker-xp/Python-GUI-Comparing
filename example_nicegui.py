from nicegui import ui
from datetime import datetime

def main():
    ui.query('body').style('background-color: #f0f2f5')
    
    with ui.tabs().classes('w-full bg-white shadow-md') as tabs:
        t1 = ui.tab('Intelligence', icon='analytics')
        t2 = ui.tab('Accounts', icon='groups')
        t3 = ui.tab('Operations', icon='manage_accounts')

    with ui.tab_panels(tabs, value=t1).classes('w-full bg-transparent p-6'):
        # --- TAB 1: DASHBOARD ---
        with ui.tab_panel(t1):
            with ui.row().classes('w-full justify-center gap-6'):
                for title, val, color in [('Global MRR', '$142k', 'blue'), 
                                         ('Active Leads', '342', 'green'), 
                                         ('Support P1', '3', 'red')]:
                    with ui.card().classes('w-72 h-40 items-center justify-center p-4 shadow-lg'):
                        ui.label(title).classes('text-gray-400 uppercase text-xs font-bold')
                        ui.label(val).classes(f'text-4xl font-black text-{color}-600')

        # --- TAB 2: ACCOUNTS (15 ROWS) ---
        with ui.tab_panel(t2):
            columns = [
                {'name': 'id', 'label': 'ID', 'field': 'id', 'sortable': True},
                {'name': 'name', 'label': 'Organization', 'field': 'name', 'align': 'left'},
                {'name': 'email', 'label': 'Email', 'field': 'email'},
                {'name': 'status', 'label': 'Status', 'field': 'status'},
            ]
            rows = [
                {'id': 100+i, 'name': f'Enterprise Corp {i}', 'email': f'admin{i}@corp.io', 'status': 'Active' if i%2 else 'Lead'}
                for i in range(1, 16)
            ]
            ui.table(columns=columns, rows=rows, row_key='id').classes('w-full shadow-sm bg-white')

        # --- TAB 3: OPERATION FORM (10+ CONTROLS) ---
        with ui.tab_panel(t3):
            with ui.card().classes('max-w-3xl mx-auto p-8 shadow-xl bg-white'):
                ui.label('Lead Intake & System Registry').classes('text-2xl font-black mb-4')
                
                # 1. Text Input
                ui.input(label='Primary Contact Name').classes('w-full mb-2')
                
                # 2. Text Area
                ui.textarea(label='Background Narrative / Discovery Notes').classes('w-full mb-2')
                
                with ui.row().classes('w-full gap-4'):
                    # 3. Dropdown (Select)
                    ui.select(['SaaS', 'FinTech', 'Health', 'Retail'], label='Vertical').classes('flex-1')
                    # 4. Number Input
                    ui.number(label='Seat Count', value=10, min=1).classes('w-32')
                
                # 5. Radio
                ui.label('Onboarding Strategy:').classes('text-sm text-gray-500 mt-2')
                ui.radio(['Self-Serve', 'Guided', 'Concierge'], value='Guided').props('inline')
                
                # 6. Checkbox & Switch
                with ui.row().classes('w-full items-center gap-8 mt-4'):
                    ui.checkbox('Marketing Automation Opt-in', value=True)
                    ui.switch('Premium Instance Enabled')
                
                # 7. Slider
                ui.label('Success Probability Weighting:').classes('text-sm text-gray-500 mt-2')
                ui.slider(min=0, max=10, value=7).classes('w-full mb-4')
                
                # 8. Date Component
                with ui.input('Target Expansion Date') as date:
                    with ui.menu().props('no-parent-event') as menu:
                        with ui.date().bind_value(date):
                            with ui.row().classes('justify-end'):
                                ui.button('Close', on_click=menu.close).props('flat')
                    with date.add_slot('append'):
                        ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

                # 9. Progress
                ui.label('Sync Progress:').classes('text-xs text-gray-400 mt-4')
                ui.linear_progress(value=0.42).classes('w-full mb-6')
                
                # 10. Buttons
                with ui.row().classes('w-full gap-4'):
                    ui.button('Commit Entry', on_click=lambda: ui.notify('Data Persistent in Cloud')).classes('flex-1 py-4')
                    ui.button('Clear', color='grey-4').classes('w-32')

    ui.run(title='NiceGUI Ultimate CRM', reload=False, port=8081)

if __name__ in {"__main__", "__mp_main__"}:
    main()
