# Python GUI Framework Comparison Dashboard

A comprehensive comparison project for 25+ Python GUI frameworks with complete CRM demo implementations.

## 📋 Project Description

This project provides an interactive comparison platform for the most important Python GUI frameworks. Each framework is presented with a complete CRM demo application that demonstrates 15+ records, 10+ UI components, and complex layouts.

### Features

- **25+ GUI Frameworks** - From standard Tkinter to modern web-based and terminal UI solutions
- **Complete CRM Demos** - Each framework shows an enterprise CRM application with:
  - Performance dashboard with metrics
  - Customer database with 15+ entries
  - Administration form with 10+ UI components
- **Interactive Dashboard** - Central launcher to start all framework demos
- **Comparison Matrix** - Clear table with technology, license, and use cases

## 🎯 Supported Frameworks

### Standard & Modern
- **Standard Tkinter** - Tcl/Tk, PSF/BSD License
- **CustomTkinter** - Modern UI with Tkinter simplicity
- **PySide6** - Official Qt binding (LGPL)
- **PyQt6** - Qt Framework (GPL/Commercial)
- **wxPython** - Native Look & Feel (LGPL)
- **Kivy** - Touch/Mobile-optimized (MIT)
- **PySimpleGUI** - Rapid Prototyping (LGPL/Commercial)
- **Dear PyGui** - GPU-accelerated, ImGui-based (MIT)

### Web-Based
- **Flet** - Flutter-based, Cross-platform (Apache 2)
- **NiceGUI** - FastAPI/Vue.js Stack (MIT)
- **PyWebView** - Embedded Browser (BSD)
- **Eel** - Chrome/WebSocket Integration (MIT)
- **Flexx** - Python to JavaScript Compiler (BSD)
- **Streamlit** - Data Science Dashboards (Apache 2)
- **Gradio** - ML/AI Interfaces (Apache 2)
- **Dash** - Plotly Analytical Dashboards (MIT)
- **Remi** - Pure Python Web GUI (Apache 2)

### Terminal UI
- **Textual** - Modern Terminal UI Framework (MIT)
- **Rich** - Terminal Formatting Library (MIT)

### Specialized
- **Gooey** - CLI to GUI Converter (MIT)
- **Toga** - BeeWare Native Framework (BSD)
- **appJar** - Educational Framework (Apache 2)

### Legacy / Mockups
- **PyGUI** - Native Wrapper (difficult on Windows)
- **PyForms** - .NET-Style (complex dependencies)
- **Libavg** - Multimedia Engine (C++ build required)

## 📦 Installation

### Prerequisites

- **Python 3.8+** (recommended: Python 3.10 or higher)
- **Windows 10/11** (the application uses Windows-specific features like `CREATE_NEW_CONSOLE`)
- **pip** (usually installed with Python)

### Step-by-Step Guide

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd python_gui_Vergleiche
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   
   **Windows (PowerShell):**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
   
   **Windows (CMD):**
   ```cmd
   .venv\Scripts\activate.bat
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   **Note:** Some frameworks require additional system dependencies:
   - **Kivy**: May require additional system libraries
   - **PyQt6/PySide6**: Qt framework is automatically installed
   - **wxPython**: Native widgets, works out-of-the-box

5. **Start the application**
   ```bash
   python main_dashboard.py
   ```

## 🚀 Usage

### Main Dashboard

After starting, the main dashboard opens with:

- **Left Sidebar**: List of all available framework demos
- **Right Area**: Comparison matrix with framework information
- **Info Box**: Status and error messages

### Starting a Framework Demo

1. Click on a framework button in the sidebar
2. The demo starts in a separate window/console
3. The dashboard remains open for further launches

### Framework Categories

- **Standard & Modern**: Traditional desktop frameworks
- **Web-Based**: Browser-based or web technology frameworks
- **Specialized**: Specialized frameworks for specific use cases
- **Legacy/Mockups**: Frameworks with installation issues (show info dialog)

## 🏗️ Project Structure

```
python_gui_Vergleiche/
├── main_dashboard.py          # Main dashboard with launcher
├── requirements.txt            # Python dependencies
├── mock_template.py            # Template for mock implementations
├── example_tkinter.py          # Standard Tkinter demo
├── example_customtkinter.py    # CustomTkinter demo
├── example_pyside6.py          # PySide6 demo
├── example_pyqt6.py            # PyQt6 demo
├── example_wxpython.py         # wxPython demo
├── example_kivy.py             # Kivy demo
├── example_pysimplegui.py      # PySimpleGUI demo
├── example_dearpygui.py        # Dear PyGui demo
├── example_flet.py             # Flet demo
├── example_nicegui.py          # NiceGUI demo
├── example_pywebview.py        # PyWebView demo
├── example_eel.py              # Eel demo
├── example_flexx.py            # Flexx demo
├── example_gooey.py            # Gooey demo
├── example_toga.py             # Toga demo
├── example_appjar.py          # appJar demo
├── example_pygui.py            # PyGUI mock
├── example_pyforms.py          # PyForms mock
└── example_libavg.py           # Libavg mock
```

## 🔧 Technical Details

### Virtual Environment

The application supports both virtual environments (`.venv`) and system Python:

- **With .venv**: Automatic detection and usage
- **Without .venv**: Uses `sys.executable` (system Python)

### Windows-Specific Features

- `subprocess.CREATE_NEW_CONSOLE`: Each demo starts in a separate console
- Error output is visible in a separate terminal
- PID display for process management

### Temporary Files

Some frameworks create temporary files:

- **Eel**: Creates `eel_web/` folder with HTML files
- These are automatically generated and can be ignored

## 🐛 Troubleshooting

### Problem: Framework demo does not start

**Solution:**
- Check the console for error messages
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Some frameworks require additional system libraries

### Problem: Import errors

**Solution:**
- Activate the virtual environment
- Install missing packages: `pip install <package-name>`
- Check Python version: `python --version` (should be 3.8+)

### Problem: Web frameworks do not start browser

**Solution:**
- **NiceGUI**: Automatically starts local server, browser opens
- **Eel**: Requires Chrome/Chromium installed
- **PyWebView**: Uses system browser engine
- **Flexx**: Starts local server, browser opens automatically

### Problem: Mock frameworks only show info dialog

**Expected behavior:**
- PyGUI, Libavg, and PyForms show info dialogs
- These frameworks are difficult to install on Windows
- The mock implementations explain the reasons

## 📊 Comparison Matrix

The comparison matrix in the dashboard shows:

- **Framework**: Name of the framework
- **Tech / Engine**: Underlying technology
- **License**: License model
- **Best Use Case**: Recommended use cases

## 🤝 Contributing

Improvements and extensions are welcome! Possible areas:

- Additional framework implementations
- Improved error handling
- Cross-platform support (Linux, macOS)
- Extended documentation

## 📝 License

This project serves comparison and learning purposes. The individual frameworks have their own licenses (see comparison matrix).

## 🙏 Acknowledgments

Thanks to all developers of Python GUI frameworks who made this comparison project possible.

---

**Note**: This project is designed for comparison and learning purposes. For production applications, you should consult the specific documentation of the individual frameworks.
