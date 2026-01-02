import wx
import wx.grid
import wx.adv

class CRMFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='wxPython Ultimate CRM Demo', size=(1100, 800))
        
        self.nb = wx.Notebook(self)
        
        self.setup_dashboard_tab()
        self.setup_customer_tab()
        self.setup_admin_tab()
        
        self.Show()

    def setup_dashboard_tab(self):
        p = wx.Panel(self.nb)
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        lbl = wx.StaticText(p, label="Corporate Intelligence Hub")
        lbl.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer.Add(lbl, 0, wx.ALL, 25)
        
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        metrics = [("Pipeline Growth", "+12.4%", "Green"), 
                   ("Market Share", "8.2%", "Blue"), 
                   ("Open Issues", "42", "Red")]
                   
        for text, val, color in metrics:
            card = wx.StaticBox(p, label=text)
            csizer = wx.StaticBoxSizer(card, wx.VERTICAL)
            v_lbl = wx.StaticText(p, label=val)
            v_lbl.SetFont(wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
            v_lbl.SetForegroundColour(color)
            csizer.Add(v_lbl, 0, wx.ALL, 20)
            hsizer.Add(csizer, 1, wx.EXPAND | wx.ALL, 10)
        
        sizer.Add(hsizer, 0, wx.EXPAND)
        p.SetSizer(sizer)
        self.nb.AddPage(p, "Overview")

    def setup_customer_tab(self):
        p = wx.Panel(self.nb)
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        grid = wx.grid.Grid(p)
        grid.CreateGrid(15, 4)
        grid.SetColLabelValue(0, "Enterprise Name")
        grid.SetColLabelValue(1, "HQ Location")
        grid.SetColLabelValue(2, "Annual Spend")
        grid.SetColLabelValue(3, "Health Score")
        
        for i in range(1, 16):
            grid.SetCellValue(i-1, 0, f"Organization {100+i}")
            grid.SetCellValue(i-1, 1, ["Berlin", "London", "NY", "Tokyo"][i%4])
            grid.SetCellValue(i-1, 2, f"${i*1200}")
            grid.SetCellValue(i-1, 3, f"{80+i-1}%")
        
        sizer.Add(grid, 1, wx.EXPAND | wx.ALL, 10)
        p.SetSizer(sizer)
        self.nb.AddPage(p, "Registry")

    def setup_admin_tab(self):
        scroll_win = wx.ScrolledWindow(self.nb)
        scroll_win.SetScrollRate(20, 20)
        p = scroll_win
        
        main_v_sizer = wx.BoxSizer(wx.VERTICAL)
        f_sizer = wx.FlexGridSizer(rows=12, cols=2, vgap=12, hgap=15)
        
        # 1. Text Entry
        f_sizer.Add(wx.StaticText(p, label="Authorized Lead Name:"))
        f_sizer.Add(wx.TextCtrl(p, value="Pending..."), 1, wx.EXPAND)
        
        # 2. Multi-line Text
        f_sizer.Add(wx.StaticText(p, label="Discovery Internal Notes:"))
        f_sizer.Add(wx.TextCtrl(p, style=wx.TE_MULTILINE, size=(300, 80)), 1, wx.EXPAND)
        
        # 3. Choice
        f_sizer.Add(wx.StaticText(p, label="Industry Vertical:"))
        f_sizer.Add(wx.Choice(p, choices=["FinTech", "Health", "Edu", "Gov"]))
        
        # 4. Radios
        f_sizer.Add(wx.StaticText(p, label="Deployment Group:"))
        r_box = wx.BoxSizer(wx.HORIZONTAL)
        r_box.Add(wx.RadioButton(p, label="Cloud-Native", style=wx.RB_GROUP))
        r_box.Add(wx.RadioButton(p, label="On-Premise"))
        f_sizer.Add(r_box)
        
        # 5. Checkbox
        f_sizer.Add(wx.StaticText(p, label="Permissions:"))
        f_sizer.Add(wx.CheckBox(p, label="Admin Access Requested"))
        
        # 6. Switch (Mock with CheckBox for wx compatibility)
        f_sizer.Add(wx.StaticText(p, label="System Visibility:"))
        f_sizer.Add(wx.CheckBox(p, label="VISIBLE ON GLOBAL DIRECTORY"))
        
        # 7. Slider
        f_sizer.Add(wx.StaticText(p, label="Engagement Priority:"))
        f_sizer.Add(wx.Slider(p, value=50, minValue=0, maxValue=100), 1, wx.EXPAND)
        
        # 8. SpinBox
        f_sizer.Add(wx.StaticText(p, label="Seat Allocation:"))
        f_sizer.Add(wx.SpinCtrl(p, value="10"))
        
        # 9. Date Picker
        f_sizer.Add(wx.StaticText(p, label="Next Review Date:"))
        f_sizer.Add(wx.adv.DatePickerCtrl(p, style=wx.adv.DP_DROPDOWN))
        
        # 10. Gauge (Progress)
        f_sizer.Add(wx.StaticText(p, label="Sync Completion:"))
        gauge = wx.Gauge(p, range=100)
        gauge.SetValue(45)
        f_sizer.Add(gauge, 1, wx.EXPAND)
        
        main_v_sizer.Add(f_sizer, 0, wx.ALL | wx.EXPAND, 25)
        
        # 12. Buttons
        btn_box = wx.BoxSizer(wx.HORIZONTAL)
        btn_box.Add(wx.Button(p, label="Persist Changes"), 0, wx.ALL, 5)
        btn_box.Add(wx.Button(p, label="Reset Form"), 0, wx.ALL, 5)
        main_v_sizer.Add(btn_box, 0, wx.ALIGN_CENTER | wx.BOTTOM, 30)
        
        p.SetSizer(main_v_sizer)
        self.nb.AddPage(p, "Administration")

if __name__ == '__main__':
    app = wx.App()
    frame = CRMFrame()
    app.MainLoop()
