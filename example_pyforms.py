import subprocess
import sys
import os

mock_script = os.path.join(os.path.dirname(__file__), "mock_template.py")
reason = "PyForms is primarily used in scientific research. While powerful (especially with PyQt), it often requires complex dependency chains (OpenCV, etc.) that make it less suitable for a quick standalone demo on this platform."

subprocess.Popen([sys.executable, mock_script, "PyForms", reason])
