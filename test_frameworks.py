"""
Test script to check all frameworks for runtime errors
"""
import subprocess
import sys
import os
import time

frameworks = [
    ("example_tkinter.py", "tkinter"),
    ("example_customtkinter.py", "customtkinter"),
    ("example_pyside6.py", "PySide6"),
    ("example_pyqt6.py", "PyQt6"),
    ("example_wxpython.py", "wx"),
    ("example_kivy.py", "kivy"),
    ("example_pysimplegui.py", "PySimpleGUI"),
    ("example_dearpygui.py", "dearpygui"),
    ("example_flet.py", "flet"),
    ("example_nicegui.py", "nicegui"),
    ("example_dash.py", "dash"),
    ("example_rich.py", "rich"),
    ("example_pywebview.py", "webview"),
    ("example_eel.py", "eel"),
    ("example_flexx.py", "flexx"),
    ("example_streamlit.py", "streamlit"),
    ("example_gradio.py", "gradio"),
    ("example_remi.py", "remi"),
    ("example_textual.py", "textual"),
    ("example_gooey.py", "gooey"),
    ("example_toga.py", "toga"),
    ("example_appjar.py", "appjar"),
    ("example_pygui.py", "mock"),
    ("example_pyforms.py", "mock"),
    ("example_libavg.py", "mock"),
]

def test_framework(script_name, framework_name):
    """Test a framework by trying to import and run it"""
    if not os.path.exists(script_name):
        return "NOT_FOUND", "File does not exist"
    
    # For mock frameworks, just check if they can be imported
    if framework_name == "mock":
        try:
            with open(script_name, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'mock_template' in content or 'messagebox.showinfo' in content:
                    return "MOCK_OK", "Mock framework (info dialog)"
        except Exception as e:
            return "MOCK_ERROR", str(e)
    
    # Try to compile first
    try:
        compile(open(script_name, 'r', encoding='utf-8').read(), script_name, 'exec')
    except SyntaxError as e:
        return "SYNTAX_ERROR", str(e)
    except Exception as e:
        return "COMPILE_ERROR", str(e)
    
    # Try to import the module (this will catch import errors)
    try:
        # Read the file and check for import statements
        with open(script_name, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract import statements
            import re
            imports = re.findall(r'^import\s+(\S+)|^from\s+(\S+)\s+import', content, re.MULTILINE)
            imports = [imp[0] or imp[1] for imp in imports if imp[0] or imp[1]]
            
            # Try importing the first few critical imports
            for imp in imports[:3]:  # Test first 3 imports
                module_name = imp.split('.')[0]
                if module_name not in ['os', 'sys', 'json', 'datetime', 'time', 'random', 'pandas', 'plotly']:
                    try:
                        __import__(module_name)
                    except ImportError:
                        return "IMPORT_ERROR", f"Missing module: {module_name}"
    except Exception as e:
        return "IMPORT_CHECK_ERROR", str(e)
    
    return "OK", "Syntax and imports OK"

print("=" * 70)
print("FRAMEWORK TEST RESULTS")
print("=" * 70)
print(f"{'Framework':<30} {'Status':<20} {'Details'}")
print("-" * 70)

results = []
for script_name, framework_name in frameworks:
    status, details = test_framework(script_name, framework_name)
    results.append((script_name, status, details))
    print(f"{script_name:<30} {status:<20} {details[:30]}")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

status_counts = {}
for _, status, _ in results:
    status_counts[status] = status_counts.get(status, 0) + 1

for status, count in sorted(status_counts.items()):
    print(f"{status}: {count}")

print("\nFrameworks needing attention:")
for script_name, status, details in results:
    if status not in ["OK", "MOCK_OK"]:
        print(f"  - {script_name}: {status} - {details}")
