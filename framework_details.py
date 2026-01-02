"""
Detailed information for each framework including pros/cons, code examples, and limitations.
"""

FRAMEWORK_DETAILS = {
    "Standard Tkinter": {
        "pros": [
            "Built-in with Python - no installation needed",
            "Simple and easy to learn",
            "Cross-platform (Windows, Linux, macOS)",
            "Large community and extensive documentation",
            "Lightweight and fast startup"
        ],
        "cons": [
            "Outdated appearance",
            "Limited modern UI components",
            "No native date picker or switch",
            "Limited styling options",
            "Not suitable for complex applications"
        ],
        "code_example": """
# Simple Tkinter example
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My App")
ttk.Label(root, text="Hello World").pack()
ttk.Button(root, text="Click Me").pack()
root.mainloop()
        """,
        "installation": "No installation needed - comes with Python",
        "limitations": [
            "No native date picker (must use third-party)",
            "No native switch/toggle widget",
            "Limited theme support",
            "Basic styling capabilities"
        ],
        "documentation_url": "https://docs.python.org/3/library/tkinter.html"
    },
    "CustomTkinter": {
        "pros": [
            "Modern, beautiful UI",
            "Easy migration from Tkinter",
            "Dark mode support",
            "Customizable themes",
            "Active development"
        ],
        "cons": [
            "Requires separate installation",
            "Smaller community than Tkinter",
            "Some advanced features missing",
            "Still based on Tkinter limitations"
        ],
        "code_example": """
# CustomTkinter example
import customtkinter as ctk

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("My App")
ctk.CTkLabel(app, text="Hello World").pack()
ctk.CTkButton(app, text="Click Me").pack()
app.mainloop()
        """,
        "installation": "pip install customtkinter",
        "limitations": [
            "No native date picker",
            "Limited to Tkinter's underlying capabilities",
            "Some widgets still look basic"
        ],
        "documentation_url": "https://customtkinter.tomschimansky.com/"
    },
    "PySide6": {
        "pros": [
            "Official Qt binding (LGPL license)",
            "Professional, native-looking UI",
            "Excellent documentation",
            "Cross-platform including mobile",
            "Rich widget set",
            "Great performance"
        ],
        "cons": [
            "Steeper learning curve",
            "Larger installation size",
            "More complex than Tkinter",
            "Requires understanding of Qt concepts"
        ],
        "code_example": """
# PySide6 example
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])
window = QMainWindow()
button = QPushButton("Click Me")
window.setCentralWidget(button)
window.show()
app.exec()
        """,
        "installation": "pip install PySide6",
        "limitations": [
            "Large download size",
            "Complex for simple applications",
            "Requires Qt runtime"
        ],
        "documentation_url": "https://doc.qt.io/qtforpython/"
    },
    "PyQt6": {
        "pros": [
            "Mature and stable",
            "Professional UI capabilities",
            "Excellent performance",
            "Rich widget library",
            "Cross-platform including mobile"
        ],
        "cons": [
            "GPL license (commercial license required for closed-source)",
            "Large installation size",
            "Steeper learning curve",
            "More complex API"
        ],
        "code_example": """
# PyQt6 example
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])
window = QMainWindow()
button = QPushButton("Click Me")
window.setCentralWidget(button)
window.show()
app.exec()
        """,
        "installation": "pip install PyQt6",
        "limitations": [
            "License restrictions for commercial use",
            "Large download size",
            "Complex for beginners"
        ],
        "documentation_url": "https://www.riverbankcomputing.com/static/Docs/PyQt6/"
    },
    "wxPython": {
        "pros": [
            "Native look and feel",
            "Mature and stable",
            "Good cross-platform support",
            "Rich widget set",
            "No licensing issues"
        ],
        "cons": [
            "Slower development pace",
            "Larger installation size",
            "More complex than Tkinter",
            "Smaller community than Qt"
        ],
        "code_example": """
# wxPython example
import wx

app = wx.App()
frame = wx.Frame(None, title="My App")
panel = wx.Panel(frame)
button = wx.Button(panel, label="Click Me")
frame.Show()
app.MainLoop()
        """,
        "installation": "pip install wxPython",
        "limitations": [
            "No mobile support",
            "Slower than Qt alternatives",
            "Less modern appearance"
        ],
        "documentation_url": "https://docs.wxpython.org/"
    },
    "Kivy": {
        "pros": [
            "Touch-friendly interface",
            "Mobile support (Android, iOS)",
            "Modern, customizable UI",
            "Good for games and multimedia",
            "Cross-platform"
        ],
        "cons": [
            "Different programming paradigm",
            "Larger installation size",
            "Steeper learning curve",
            "Not ideal for traditional desktop apps"
        ],
        "code_example": """
# Kivy example
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="Click Me")

MyApp().run()
        """,
        "installation": "pip install kivy",
        "limitations": [
            "No native date picker",
            "Different from traditional GUI frameworks",
            "Requires understanding of Kivy language"
        ],
        "documentation_url": "https://kivy.org/doc/stable/"
    },
    "PySimpleGUI": {
        "pros": [
            "Very easy to learn",
            "Rapid prototyping",
            "Excellent documentation",
            "Active community",
            "Multiple backends (Tkinter, Qt, etc.)"
        ],
        "cons": [
            "Less flexible than native frameworks",
            "Performance limitations",
            "Limited customization",
            "Wrapper around other frameworks"
        ],
        "code_example": """
# PySimpleGUI example
import PySimpleGUI as sg

layout = [[sg.Text("Hello World")], [sg.Button("Click Me")]]
window = sg.Window("My App", layout)
window.read()
window.close()
        """,
        "installation": "pip install PySimpleGUI",
        "limitations": [
            "No native switch widget",
            "Limited styling options",
            "Performance overhead"
        ],
        "documentation_url": "https://www.pysimplegui.org/"
    },
    "Dear PyGui": {
        "pros": [
            "GPU-accelerated",
            "High performance",
            "Modern, immediate-mode GUI",
            "Great for tools and dashboards",
            "Lightweight"
        ],
        "cons": [
            "No native switch widget",
            "Different programming model",
            "Smaller community",
            "Less suitable for traditional apps"
        ],
        "code_example": """
# Dear PyGui example
import dearpygui.dearpygui as dpg

dpg.create_context()
with dpg.window(label="My App"):
    dpg.add_text("Hello World")
    dpg.add_button(label="Click Me")
dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
        """,
        "installation": "pip install dearpygui",
        "limitations": [
            "No native switch (uses checkbox)",
            "Immediate-mode paradigm",
            "Less traditional widget set"
        ],
        "documentation_url": "https://dearpygui.readthedocs.io/"
    },
    "Flet": {
        "pros": [
            "Flutter-based, modern UI",
            "Cross-platform including mobile",
            "Easy to learn",
            "Beautiful default styling",
            "Active development"
        ],
        "cons": [
            "Requires Flutter runtime",
            "Larger installation size",
            "Newer framework (less mature)",
            "Smaller community"
        ],
        "code_example": """
# Flet example
import flet as ft

def main(page: ft.Page):
    page.add(ft.Text("Hello World"))
    page.add(ft.ElevatedButton("Click Me"))

ft.app(target=main)
        """,
        "installation": "pip install flet",
        "limitations": [
            "Requires Flutter SDK for some features",
            "Larger app size",
            "Less mature ecosystem"
        ],
        "documentation_url": "https://flet.dev/docs/"
    },
    "NiceGUI": {
        "pros": [
            "Web-based, accessible anywhere",
            "Modern UI components",
            "Easy to learn",
            "Great for dashboards",
            "Automatic browser integration"
        ],
        "cons": [
            "Requires browser",
            "Web-based (not native desktop)",
            "Network dependency",
            "Less suitable for offline apps"
        ],
        "code_example": """
# NiceGUI example
from nicegui import ui

ui.label("Hello World")
ui.button("Click Me", on_click=lambda: ui.notify("Clicked!"))
ui.run()
        """,
        "installation": "pip install nicegui",
        "limitations": [
            "Web-based only",
            "Requires browser",
            "Not true native desktop app"
        ],
        "documentation_url": "https://nicegui.io/documentation"
    },
    "PyWebView": {
        "pros": [
            "Embed HTML/CSS/JS",
            "Lightweight",
            "Easy integration",
            "Use existing web technologies"
        ],
        "cons": [
            "Requires browser engine",
            "Not true native UI",
            "Limited native features",
            "Security considerations"
        ],
        "code_example": """
# PyWebView example
import webview

html = "<html><body><h1>Hello World</h1></body></html>"
webview.create_window("My App", html=html)
webview.start()
        """,
        "installation": "pip install pywebview",
        "limitations": [
            "Web-based only",
            "Requires browser engine",
            "Not native widgets"
        ],
        "documentation_url": "https://pywebview.flowrl.com/"
    },
    "Eel": {
        "pros": [
            "Easy Python-JavaScript bridge",
            "Use web technologies",
            "Simple API",
            "Good for web developers"
        ],
        "cons": [
            "Requires Chrome",
            "Web-based only",
            "Not native UI",
            "Limited offline capabilities"
        ],
        "code_example": """
# Eel example
import eel

eel.init('web')
@eel.expose
def my_python_function():
    return "Hello from Python"

eel.start('index.html')
        """,
        "installation": "pip install eel",
        "limitations": [
            "Requires Chrome browser",
            "Web-based only",
            "Not native desktop app"
        ],
        "documentation_url": "https://github.com/ChrisKnott/Eel"
    },
    "Flexx": {
        "pros": [
            "Python to JavaScript compiler",
            "Use web technologies",
            "Cross-platform",
            "Modern UI capabilities"
        ],
        "cons": [
            "Smaller community",
            "Less active development",
            "Steeper learning curve",
            "Requires browser"
        ],
        "code_example": """
# Flexx example
from flexx import flx

class MyApp(flx.Widget):
    def init(self):
        flx.Label(text="Hello World")
        flx.Button(text="Click Me")

app = flx.App(MyApp)
app.launch('browser')
flx.run()
        """,
        "installation": "pip install flexx",
        "limitations": [
            "No native date picker",
            "No native switch",
            "Web-based only",
            "Smaller community"
        ],
        "documentation_url": "https://flexx.readthedocs.io/"
    },
    "Gooey": {
        "pros": [
            "Convert CLI to GUI automatically",
            "Very easy to use",
            "No GUI code needed",
            "Great for simple tools"
        ],
        "cons": [
            "Limited customization",
            "No native switch",
            "No table/grid support",
            "Only for CLI tools"
        ],
        "code_example": """
# Gooey example
from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser()
    parser.add_argument('name', help='Your name')
    args = parser.parse_args()
    print(f"Hello {args.name}")

main()
        """,
        "installation": "pip install Gooey",
        "limitations": [
            "Only for CLI tools",
            "No native switch",
            "No table support",
            "Limited customization"
        ],
        "documentation_url": "https://github.com/chriskiehl/Gooey"
    },
    "Toga": {
        "pros": [
            "Native widgets on each platform",
            "Mobile support",
            "Cross-platform",
            "Part of BeeWare suite"
        ],
        "cons": [
            "Complex installation",
            "Smaller community",
            "Less mature",
            "Steeper learning curve"
        ],
        "code_example": """
# Toga example
import toga

def button_handler(widget):
    print("Clicked!")

def build(app):
    box = toga.Box()
    button = toga.Button("Click Me", on_press=button_handler)
    box.add(button)
    return box

app = toga.App("My App", "org.example.myapp", startup=build)
app.main_loop()
        """,
        "installation": "pip install toga",
        "limitations": [
            "No native date picker",
            "Complex installation",
            "Less mature ecosystem"
        ],
        "documentation_url": "https://toga.readthedocs.io/"
    },
    "appJar": {
        "pros": [
            "Very simple API",
            "Great for education",
            "Easy to learn",
            "Good documentation"
        ],
        "cons": [
            "Limited features",
            "Smaller community",
            "Based on Tkinter",
            "No native switch"
        ],
        "code_example": """
# appJar example
from appJar import gui

app = gui()
app.addLabel("title", "Hello World")
app.addButton("Click Me", lambda: app.infoBox("Info", "Clicked!"))
app.go()
        """,
        "installation": "pip install appJar",
        "limitations": [
            "No native switch",
            "Limited to Tkinter capabilities",
            "Smaller community"
        ],
        "documentation_url": "https://appjar.info/"
    }
}

# Add default entries for frameworks without detailed info
for framework_name in ["PyGUI", "PyForms", "Libavg"]:
    if framework_name not in FRAMEWORK_DETAILS:
        FRAMEWORK_DETAILS[framework_name] = {
            "pros": ["Specialized use case"],
            "cons": ["Difficult installation", "Limited documentation", "Small community"],
            "code_example": "# See mock_template.py for installation issues",
            "installation": "See mock_template.py - installation issues on Windows",
            "limitations": ["Installation difficulties", "Limited Windows support"],
            "documentation_url": "See framework documentation"
        }
