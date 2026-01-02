# Python GUI Framework Comparison Dashboard

Ein umfassendes Vergleichsprojekt für 19+ Python GUI-Frameworks mit vollständigen CRM-Demo-Implementierungen.

## 📋 Projektbeschreibung

Dieses Projekt bietet eine interaktive Vergleichsplattform für die wichtigsten Python GUI-Frameworks. Jedes Framework wird mit einer vollständigen CRM-Demo-Anwendung präsentiert, die 15+ Datensätze, 10+ UI-Komponenten und komplexe Layouts demonstriert.

### Features

- **19+ GUI-Frameworks** - Von Standard-Tkinter bis zu modernen Web-basierten Lösungen
- **Vollständige CRM-Demos** - Jedes Framework zeigt eine Enterprise-CRM-Anwendung mit:
  - Performance-Dashboard mit Metriken
  - Kunden-Datenbank mit 15+ Einträgen
  - Administrationsformular mit 10+ UI-Komponenten
- **Interaktives Dashboard** - Zentraler Launcher zum Starten aller Framework-Demos
- **Vergleichsmatrix** - Übersichtliche Tabelle mit Technologie, Lizenz und Anwendungsfällen

## 🎯 Unterstützte Frameworks

### Standard & Modern
- **Standard Tkinter** - Tcl/Tk, PSF/BSD Lizenz
- **CustomTkinter** - Modernes UI mit Tkinter-Einfachheit
- **PySide6** - Offizielle Qt-Bindung (LGPL)
- **PyQt6** - Qt-Framework (GPL/Commercial)
- **wxPython** - Native Look & Feel (LGPL)
- **Kivy** - Touch/Mobile-optimiert (MIT)
- **PySimpleGUI** - Rapid Prototyping (LGPL/Commercial)
- **Dear PyGui** - GPU-beschleunigt, ImGui-basiert (MIT)

### Web-Based
- **Flet** - Flutter-basiert, Cross-platform (Apache 2)
- **NiceGUI** - FastAPI/Vue.js Stack (MIT)
- **PyWebView** - Eingebetteter Browser (BSD)
- **Eel** - Chrome/WebSocket Integration (MIT)
- **Flexx** - Python zu JavaScript Compiler (BSD)

### Specialized
- **Gooey** - CLI zu GUI Konverter (MIT)
- **Toga** - BeeWare Native Framework (BSD)
- **appJar** - Educational Framework (Apache 2)

### Legacy / Mockups
- **PyGUI** - Native Wrapper (schwierig auf Windows)
- **PyForms** - .NET-Style (komplexe Dependencies)
- **Libavg** - Multimedia Engine (C++ Build erforderlich)

## 📦 Installation

### Voraussetzungen

- **Python 3.8+** (empfohlen: Python 3.10 oder höher)
- **Windows 10/11** (die Anwendung nutzt Windows-spezifische Features wie `CREATE_NEW_CONSOLE`)
- **pip** (normalerweise mit Python installiert)

### Schritt-für-Schritt Anleitung

1. **Repository klonen oder herunterladen**
   ```bash
   git clone <repository-url>
   cd python_gui_Vergleiche
   ```

2. **Virtuelle Umgebung erstellen** (empfohlen)
   ```bash
   python -m venv .venv
   ```

3. **Virtuelle Umgebung aktivieren**
   
   **Windows (PowerShell):**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
   
   **Windows (CMD):**
   ```cmd
   .venv\Scripts\activate.bat
   ```

4. **Dependencies installieren**
   ```bash
   pip install -r requirements.txt
   ```

   **Hinweis:** Einige Frameworks benötigen zusätzliche System-Dependencies:
   - **Kivy**: Möglicherweise zusätzliche System-Bibliotheken
   - **PyQt6/PySide6**: Qt-Framework wird automatisch installiert
   - **wxPython**: Native Widgets, funktioniert out-of-the-box

5. **Anwendung starten**
   ```bash
   python main_dashboard.py
   ```

## 🚀 Nutzung

### Haupt-Dashboard

Nach dem Start öffnet sich das Haupt-Dashboard mit:

- **Linke Sidebar**: Liste aller verfügbaren Framework-Demos
- **Rechter Bereich**: Vergleichsmatrix mit Framework-Informationen
- **Info-Box**: Status- und Fehlermeldungen

### Framework-Demo starten

1. Klicken Sie auf einen Framework-Button in der Sidebar
2. Die Demo startet in einem separaten Fenster/Konsole
3. Das Dashboard bleibt geöffnet für weitere Starts

### Framework-Kategorien

- **Standard & Modern**: Traditionelle Desktop-Frameworks
- **Web-Based**: Browser-basierte oder Web-Technologie nutzende Frameworks
- **Specialized**: Spezialisierte Frameworks für bestimmte Anwendungsfälle
- **Legacy/Mockups**: Frameworks mit Installationsproblemen (zeigen Info-Dialog)

## 🏗️ Projektstruktur

```
python_gui_Vergleiche/
├── main_dashboard.py          # Haupt-Dashboard mit Launcher
├── requirements.txt            # Python Dependencies
├── mock_template.py            # Template für Mock-Implementierungen
├── example_tkinter.py          # Standard Tkinter Demo
├── example_customtkinter.py    # CustomTkinter Demo
├── example_pyside6.py          # PySide6 Demo
├── example_pyqt6.py            # PyQt6 Demo
├── example_wxpython.py         # wxPython Demo
├── example_kivy.py             # Kivy Demo
├── example_pysimplegui.py      # PySimpleGUI Demo
├── example_dearpygui.py        # Dear PyGui Demo
├── example_flet.py             # Flet Demo
├── example_nicegui.py          # NiceGUI Demo
├── example_pywebview.py        # PyWebView Demo
├── example_eel.py              # Eel Demo
├── example_flexx.py            # Flexx Demo
├── example_gooey.py            # Gooey Demo
├── example_toga.py             # Toga Demo
├── example_appjar.py           # appJar Demo
├── example_pygui.py            # PyGUI Mock
├── example_pyforms.py          # PyForms Mock
└── example_libavg.py           # Libavg Mock
```

## 🔧 Technische Details

### Virtuelle Umgebung

Die Anwendung unterstützt sowohl virtuelle Umgebungen (`.venv`) als auch System-Python:

- **Mit .venv**: Automatische Erkennung und Nutzung
- **Ohne .venv**: Verwendet `sys.executable` (System-Python)

### Windows-spezifische Features

- `subprocess.CREATE_NEW_CONSOLE`: Jede Demo startet in separater Konsole
- Fehlerausgabe ist in separatem Terminal sichtbar
- PID-Anzeige für Prozess-Management

### Temporäre Dateien

Einige Frameworks erstellen temporäre Dateien:

- **Eel**: Erstellt `eel_web/` Ordner mit HTML-Dateien
- Diese werden automatisch generiert und können ignoriert werden

## 🐛 Troubleshooting

### Problem: Framework-Demo startet nicht

**Lösung:**
- Prüfen Sie die Konsole auf Fehlermeldungen
- Stellen Sie sicher, dass alle Dependencies installiert sind: `pip install -r requirements.txt`
- Einige Frameworks benötigen zusätzliche System-Bibliotheken

### Problem: Import-Fehler

**Lösung:**
- Aktivieren Sie die virtuelle Umgebung
- Installieren Sie fehlende Packages: `pip install <package-name>`
- Prüfen Sie die Python-Version: `python --version` (sollte 3.8+ sein)

### Problem: Web-Frameworks starten Browser nicht

**Lösung:**
- **NiceGUI**: Startet automatisch lokalen Server, Browser öffnet sich
- **Eel**: Benötigt Chrome/Chromium installiert
- **PyWebView**: Nutzt System-Browser-Engine
- **Flexx**: Startet lokalen Server, Browser öffnet sich automatisch

### Problem: Mock-Frameworks zeigen nur Info-Dialog

**Erwartetes Verhalten:**
- PyGUI, Libavg und PyForms zeigen Info-Dialoge
- Diese Frameworks sind schwer auf Windows zu installieren
- Die Mock-Implementierungen erklären die Gründe

## 📊 Vergleichsmatrix

Die Vergleichsmatrix im Dashboard zeigt:

- **Framework**: Name des Frameworks
- **Tech / Engine**: Unterliegende Technologie
- **License**: Lizenzmodell
- **Best Use Case**: Empfohlene Anwendungsfälle

## 🤝 Beitragen

Verbesserungen und Erweiterungen sind willkommen! Mögliche Bereiche:

- Zusätzliche Framework-Implementierungen
- Verbesserte Fehlerbehandlung
- Cross-Platform Support (Linux, macOS)
- Erweiterte Dokumentation

## 📝 Lizenz

Dieses Projekt dient zu Vergleichs- und Lernzwecken. Die einzelnen Frameworks haben ihre eigenen Lizenzen (siehe Vergleichsmatrix).

## 🙏 Danksagungen

Danke an alle Entwickler der Python GUI-Frameworks, die dieses Vergleichsprojekt ermöglicht haben.

---

**Hinweis**: Dieses Projekt ist für Vergleichs- und Lernzwecke konzipiert. Für Produktionsanwendungen sollten Sie die spezifischen Dokumentationen der einzelnen Frameworks konsultieren.
