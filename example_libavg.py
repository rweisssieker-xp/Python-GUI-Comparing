import subprocess
import sys
import os

mock_script = os.path.join(os.path.dirname(__file__), "mock_template.py")
reason = "Libavg is a high-performance multimedia engine. It usually requires specialized C++ binaries and is notoriously difficult to install via standard 'pip' on Windows without a dedicated build environment."

subprocess.Popen([sys.executable, mock_script, "Libavg", reason])
