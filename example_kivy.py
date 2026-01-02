from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.checkbox import Checkbox
from kivy.uix.switch import Switch
from kivy.uix.spinner import Spinner
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class CRMTab1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=40, spacing=20, **kwargs)
        with self.canvas.before:
            Color(0.1, 0.1, 0.12, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        self.add_widget(Label(text="Executive Dashboard", font_size='32sp', bold=True, color=(0, 0.8, 1, 1)))
        
        metrics = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=0.4)
        for t, v, c in [("MRR", "$2.4M", (0, 0.5, 0.8, 1)), ("LEADS", "842", (0, 0.7, 0.3, 1)), ("CHURN", "0.2%", (0.8, 0.2, 0.2, 1))]:
            btn = Button(text=f"{t}\n{v}", font_size='20sp', background_color=c, halign='center')
            metrics.add_widget(btn)
        self.add_widget(metrics)
        
        self.add_widget(Label(text="Database Sync Priority", size_hint_y=None, height=40))
        self.add_widget(ProgressBar(max=100, value=78, size_hint_y=None, height=50))

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class KivyUltimateCRM(App):
    def build(self):
        self.title = "Kivy Ultimate CRM Pro"
        Window.size = (1100, 800)
        
        tp = TabbedPanel(do_default_tab=False)

        # TAB 1: DASHBOARD
        tab1 = TabbedPanelItem(text="Summary")
        tab1.add_widget(CRMTab1())
        tp.add_widget(tab1)

        # TAB 2: REGISTRY (15 rows of data)
        tab2 = TabbedPanelItem(text="Database")
        sc = ScrollView(size_hint=(1, 1), bar_width=10)
        grid = GridLayout(cols=4, spacing=2, size_hint_y=None, padding=2)
        grid.bind(minimum_height=grid.setter('height'))
        
        # Header Row
        cols = ["REF ID", "ORGANIZATION", "STATUS", "CONTRACT VAL"]
        for c in cols:
            lbl = Label(text=c, bold=True, height=50, size_hint_y=None, color=(1,1,1,1))
            with lbl.canvas.before:
                Color(0.2, 0.2, 0.25, 1)
                Rectangle(size=lbl.size, pos=lbl.pos)
            lbl.bind(size=lambda i,v: i.canvas.before.clear() or (i.canvas.before.add(Color(0.2,0.2,0.25,1)) or i.canvas.before.add(Rectangle(size=i.size, pos=i.pos))))
            grid.add_widget(lbl)
            
        # 15 Data Rows (IDs 101-115)
        for i in range(1, 16):
            row_data = [str(100+i), f"Global Tech Group {i}", "VIP" if i%5==0 else "Active", f"${i*1200}"]
            for d in row_data:
                item = Label(text=d, height=45, size_hint_y=None, font_size='14sp')
                # Alternate row colors for visibility
                bg_c = (0.15, 0.15, 0.17, 1) if i%2==0 else (0.1, 0.1, 0.11, 1)
                with item.canvas.before:
                    Color(*bg_c)
                    rect = Rectangle(size=item.size, pos=item.pos)
                item.bind(size=lambda i_inst,v: i_inst.canvas.before.clear() or (i_inst.canvas.before.add(Color(*( (0.15, 0.15, 0.17, 1) if (grid.children.index(i_inst)//4)%2==1 else (0.1, 0.1, 0.11, 1) ))) or i_inst.canvas.before.add(Rectangle(size=i_inst.size, pos=i_inst.pos))))
                grid.add_widget(item)
                
        sc.add_widget(grid)
        tab2.add_widget(sc)
        tp.add_widget(tab2)

        # TAB 3: ADMIN
        tab3 = TabbedPanelItem(text="Operations")
        adm_scroll = ScrollView()
        adm_box = BoxLayout(orientation='vertical', padding=40, spacing=15, size_hint_y=None)
        adm_box.bind(minimum_height=adm_box.setter('height'))
        
        adm_box.add_widget(Label(text="NEW ACCOUNT REGISTRY", font_size='22sp', bold=True, size_hint_y=None, height=60))
        
        # 1. Text
        adm_box.add_widget(Label(text="Primary Contact Full Name:", size_hint_y=None, height=30, halign='left'))
        adm_box.add_widget(TextInput(multiline=False, size_hint_y=None, height=40))
        
        # 2. TextArea
        adm_box.add_widget(Label(text="Lead Background & Notes:", size_hint_y=None, height=30))
        adm_box.add_widget(TextInput(multiline=True, size_hint_y=None, height=120))
        
        # 3. Dropdown
        adm_box.add_widget(Label(text="Vertical Market Segment:", size_hint_y=None, height=30))
        adm_box.add_widget(Spinner(text='Select Industry', values=('Aerospace', 'FinTech', 'Logistics', 'Retail'), size_hint_y=None, height=45))
        
        # 4. Radios
        adm_box.add_widget(Label(text="Commercial Model (B2B / B2C):", size_hint_y=None, height=30))
        r_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        r_box.add_widget(Label(text="B2B"))
        r_box.add_widget(Checkbox(group='m', active=True))
        r_box.add_widget(Label(text="B2C"))
        r_box.add_widget(Checkbox(group='m'))
        adm_box.add_widget(r_box)
        
        # 5/6. Checkbox & Switch
        row_feat = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        row_feat.add_widget(Label(text="Marketing Opt-in:"))
        row_feat.add_widget(Checkbox(active=True))
        row_feat.add_widget(Label(text="Public Visibility:"))
        row_feat.add_widget(Switch(active=True))
        adm_box.add_widget(row_feat)
        
        # 7. Slider
        adm_box.add_widget(Label(text="Estimated Priority Weighting:", size_hint_y=None, height=30))
        adm_box.add_widget(Slider(min=0, max=100, value=35, size_hint_y=None, height=40))
        
        # 8. SpinBox
        adm_box.add_widget(Label(text="Projected Seat Allocation:", size_hint_y=None, height=30))
        s_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=45)
        s_box.add_widget(Button(text="-", size_hint_x=0.2))
        s_box.add_widget(TextInput(text="150", readonly=True, halign='center'))
        s_box.add_widget(Button(text="+", size_hint_x=0.2))
        adm_box.add_widget(s_box)
        
        # 9. Date
        adm_box.add_widget(Label(text="Review Date (YYYY-MM-DD):", size_hint_y=None, height=30))
        adm_box.add_widget(TextInput(text="2024-12-31", size_hint_y=None, height=40))
        
        # Final Action
        adm_box.add_widget(Button(text="COMMIT TO ENTERPRISE CLOUD", size_hint_y=None, height=60, background_color=(0, 0.5, 1, 1), bold=True))
        
        adm_scroll.add_widget(adm_box)
        tab3.add_widget(adm_scroll)
        tp.add_widget(tab3)

        return tp

if __name__ == "__main__":
    KivyUltimateCRM().run()
