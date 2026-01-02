import subprocess
import sys
import os

mock_script = os.path.join(os.path.dirname(__file__), "mock_template.py")
reason = "PyGUI is a legacy native wrapper project that is largely deprecated or difficult to install on modern 64-bit Windows environments. It focused on a thin wrapper around native widgets."

subprocess.Popen([sys.executable, mock_script, "PyGUI", reason])
