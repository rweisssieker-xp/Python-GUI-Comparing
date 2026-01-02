"""
Structured comparison data for all GUI frameworks.
Contains metrics, features, and detailed information for comparison.
"""

# Extended comparison matrix data
FRAMEWORK_DATA = {
    "Standard Tkinter": {
        "tech": "Tcl/Tk",
        "license": "PSF/BSD",
        "use_case": "Simple tools, Prototyping",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Einfach",
        "python_version": "3.8+",
        "install_difficulty": "Einfach",
        "community": "Hoch",
        "performance": "Mittel",
        "documentation": "Gut",
        "category": "Standard & Modern"
    },
    "CustomTkinter": {
        "tech": "Tkinter++",
        "license": "MIT",
        "use_case": "Modern UI with Tkinter ease",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Einfach",
        "python_version": "3.8+",
        "install_difficulty": "Einfach",
        "community": "Mittel",
        "performance": "Mittel",
        "documentation": "Gut",
        "category": "Standard & Modern"
    },
    "PySide6": {
        "tech": "Qt (Official)",
        "license": "LGPL",
        "use_case": "Commercial Qt apps",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": True},
        "learning_curve": "Mittel",
        "python_version": "3.6+",
        "install_difficulty": "Mittel",
        "community": "Hoch",
        "performance": "Hoch",
        "documentation": "Exzellent",
        "category": "Standard & Modern"
    },
    "PyQt6": {
        "tech": "Qt",
        "license": "GPL/Comm",
        "use_case": "Professional Desktop",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": True},
        "learning_curve": "Mittel",
        "python_version": "3.6+",
        "install_difficulty": "Mittel",
        "community": "Hoch",
        "performance": "Hoch",
        "documentation": "Exzellent",
        "category": "Standard & Modern"
    },
    "wxPython": {
        "tech": "wxWidgets",
        "license": "LGPL",
        "use_case": "Native look & feel",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Mittel",
        "python_version": "3.6+",
        "install_difficulty": "Mittel",
        "community": "Mittel",
        "performance": "Hoch",
        "documentation": "Gut",
        "category": "Standard & Modern"
    },
    "Kivy": {
        "tech": "OpenGL",
        "license": "MIT",
        "use_case": "Touch, Multi-platform",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": True},
        "learning_curve": "Mittel",
        "python_version": "3.7+",
        "install_difficulty": "Mittel",
        "community": "Hoch",
        "performance": "Hoch",
        "documentation": "Gut",
        "category": "Standard & Modern"
    },
    "PySimpleGUI": {
        "tech": "Wrapper",
        "license": "LGPL/Comm",
        "use_case": "Rapid Prototypes",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Einfach",
        "python_version": "3.4+",
        "install_difficulty": "Einfach",
        "community": "Hoch",
        "performance": "Mittel",
        "documentation": "Exzellent",
        "category": "Standard & Modern"
    },
    "Dear PyGui": {
        "tech": "ImGui/GPU",
        "license": "MIT",
        "use_case": "Performance, Vision",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Mittel",
        "python_version": "3.7+",
        "install_difficulty": "Mittel",
        "community": "Mittel",
        "performance": "Hoch",
        "documentation": "Gut",
        "category": "Standard & Modern"
    },
    "Flet": {
        "tech": "Flutter",
        "license": "Apache 2",
        "use_case": "Cross-platform consistency",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": True},
        "learning_curve": "Einfach",
        "python_version": "3.7+",
        "install_difficulty": "Einfach",
        "community": "Mittel",
        "performance": "Hoch",
        "documentation": "Gut",
        "category": "Web-Based"
    },
    "NiceGUI": {
        "tech": "FastAPI/Vue",
        "license": "MIT",
        "use_case": "Modern Dashboards",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": True},
        "learning_curve": "Einfach",
        "python_version": "3.8+",
        "install_difficulty": "Einfach",
        "community": "Mittel",
        "performance": "Mittel",
        "documentation": "Gut",
        "category": "Web-Based"
    },
    "PyWebView": {
        "tech": "Browser",
        "license": "BSD",
        "use_case": "Embedded HTML wrappers",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Einfach",
        "python_version": "3.6+",
        "install_difficulty": "Einfach",
        "community": "Mittel",
        "performance": "Mittel",
        "documentation": "Basis",
        "category": "Web-Based"
    },
    "Eel": {
        "tech": "Chrome/WS",
        "license": "MIT",
        "use_case": "Web-frontends for Python",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Einfach",
        "python_version": "3.5+",
        "install_difficulty": "Einfach",
        "community": "Mittel",
        "performance": "Mittel",
        "documentation": "Basis",
        "category": "Web-Based"
    },
    "Flexx": {
        "tech": "Web Stack",
        "license": "BSD",
        "use_case": "Hybrid Web/Desktop",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Mittel",
        "python_version": "3.6+",
        "install_difficulty": "Mittel",
        "community": "Niedrig",
        "performance": "Mittel",
        "documentation": "Basis",
        "category": "Web-Based"
    },
    "Gooey": {
        "tech": "Tkinter",
        "license": "MIT",
        "use_case": "CLI to GUI conversion",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Einfach",
        "python_version": "3.6+",
        "install_difficulty": "Einfach",
        "community": "Mittel",
        "performance": "Mittel",
        "documentation": "Gut",
        "category": "Specialized"
    },
    "Toga": {
        "tech": "Native",
        "license": "BSD",
        "use_case": "Native Mobile/Desktop",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": True},
        "learning_curve": "Mittel",
        "python_version": "3.7+",
        "install_difficulty": "Komplex",
        "community": "Mittel",
        "performance": "Hoch",
        "documentation": "Gut",
        "category": "Specialized"
    },
    "appJar": {
        "tech": "Tkinter",
        "license": "Apache 2",
        "use_case": "Educational purposes",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Einfach",
        "python_version": "3.6+",
        "install_difficulty": "Einfach",
        "community": "Niedrig",
        "performance": "Mittel",
        "documentation": "Gut",
        "category": "Specialized"
    },
    "PyGUI": {
        "tech": "Native",
        "license": "MIT",
        "use_case": "Lightweight Wrapper",
        "platforms": {"windows": False, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Mittel",
        "python_version": "3.5+",
        "install_difficulty": "Komplex",
        "community": "Niedrig",
        "performance": "Mittel",
        "documentation": "Basis",
        "category": "Legacy / Specialized Mockups"
    },
    "PyForms": {
        "tech": ".NET/Qt",
        "license": "MIT",
        "use_case": "Windows-specific tools",
        "platforms": {"windows": True, "linux": False, "macos": False, "mobile": False},
        "learning_curve": "Mittel",
        "python_version": "3.6+",
        "install_difficulty": "Komplex",
        "community": "Niedrig",
        "performance": "Mittel",
        "documentation": "Basis",
        "category": "Legacy / Specialized Mockups"
    },
    "Libavg": {
        "tech": "Multimedia",
        "license": "LGPL",
        "use_case": "Multimedia, Graphics",
        "platforms": {"windows": True, "linux": True, "macos": True, "mobile": False},
        "learning_curve": "Schwer",
        "python_version": "3.6+",
        "install_difficulty": "Komplex",
        "community": "Niedrig",
        "performance": "Hoch",
        "documentation": "Basis",
        "category": "Legacy / Specialized Mockups"
    }
}

# Feature support matrix
FEATURE_MATRIX = {
    "Standard Tkinter": {
        "native_date_picker": False,
        "native_switch": False,
        "native_table": True,
        "themes_styling": False,
        "custom_widgets": True,
        "drag_drop": False,
        "multithreading": True,
        "web_integration": False
    },
    "CustomTkinter": {
        "native_date_picker": False,
        "native_switch": True,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": False,
        "multithreading": True,
        "web_integration": False
    },
    "PySide6": {
        "native_date_picker": True,
        "native_switch": True,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": True,
        "multithreading": True,
        "web_integration": True
    },
    "PyQt6": {
        "native_date_picker": True,
        "native_switch": True,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": True,
        "multithreading": True,
        "web_integration": True
    },
    "wxPython": {
        "native_date_picker": True,
        "native_switch": True,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": True,
        "multithreading": True,
        "web_integration": False
    },
    "Kivy": {
        "native_date_picker": False,
        "native_switch": True,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": True,
        "multithreading": True,
        "web_integration": False
    },
    "PySimpleGUI": {
        "native_date_picker": True,
        "native_switch": False,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": False,
        "multithreading": True,
        "web_integration": False
    },
    "Dear PyGui": {
        "native_date_picker": True,
        "native_switch": False,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": False,
        "multithreading": True,
        "web_integration": False
    },
    "Flet": {
        "native_date_picker": True,
        "native_switch": True,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": True,
        "multithreading": True,
        "web_integration": True
    },
    "NiceGUI": {
        "native_date_picker": True,
        "native_switch": True,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": True,
        "multithreading": True,
        "web_integration": True
    },
    "PyWebView": {
        "native_date_picker": True,
        "native_switch": True,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": True,
        "multithreading": True,
        "web_integration": True
    },
    "Eel": {
        "native_date_picker": True,
        "native_switch": True,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": True,
        "multithreading": True,
        "web_integration": True
    },
    "Flexx": {
        "native_date_picker": False,
        "native_switch": False,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": False,
        "multithreading": True,
        "web_integration": True
    },
    "Gooey": {
        "native_date_picker": True,
        "native_switch": False,
        "native_table": False,
        "themes_styling": False,
        "custom_widgets": False,
        "drag_drop": False,
        "multithreading": False,
        "web_integration": False
    },
    "Toga": {
        "native_date_picker": False,
        "native_switch": True,
        "native_table": True,
        "themes_styling": False,
        "custom_widgets": True,
        "drag_drop": False,
        "multithreading": True,
        "web_integration": False
    },
    "appJar": {
        "native_date_picker": True,
        "native_switch": False,
        "native_table": True,
        "themes_styling": False,
        "custom_widgets": True,
        "drag_drop": False,
        "multithreading": True,
        "web_integration": False
    },
    "PyGUI": {
        "native_date_picker": False,
        "native_switch": False,
        "native_table": False,
        "themes_styling": False,
        "custom_widgets": False,
        "drag_drop": False,
        "multithreading": True,
        "web_integration": False
    },
    "PyForms": {
        "native_date_picker": True,
        "native_switch": True,
        "native_table": True,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": True,
        "multithreading": True,
        "web_integration": False
    },
    "Libavg": {
        "native_date_picker": False,
        "native_switch": False,
        "native_table": False,
        "themes_styling": True,
        "custom_widgets": True,
        "drag_drop": False,
        "multithreading": True,
        "web_integration": False
    }
}

# Feature labels for display
FEATURE_LABELS = {
    "native_date_picker": "Native Date Picker",
    "native_switch": "Native Switch/Toggle",
    "native_table": "Native Table/Grid",
    "themes_styling": "Themes/Styling",
    "custom_widgets": "Custom Widgets",
    "drag_drop": "Drag & Drop",
    "multithreading": "Multithreading",
    "web_integration": "Web Integration"
}
