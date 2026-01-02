import webview
import threading
import time

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>PyWebView Ultimate CRM</title>
    <style>
        body { font-family: sans-serif; background: #eef2f3; margin: 0; padding: 20px; }
        .tab-box { display: flex; border-bottom: 2px solid #ccc; margin-bottom: 20px; }
        .tab { padding: 10px 20px; cursor: pointer; background: #ddd; margin-right: 5px; }
        .tab.active { background: white; border: 2px solid #ccc; border-bottom: none; }
        .view { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .hidden { display: none; }
        input, select, textarea { display: block; width: 100%; margin: 10px 0; padding: 10px; border: 1px solid #ccc; box-sizing: border-box; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #eee; padding: 10px; text-align: left; }
        .btn { padding: 12px 24px; background: #2c3e50; color: white; border: none; border-radius: 4px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="tab-box">
        <div class="tab active" onclick="sh('d', this)">Overview</div>
        <div class="tab" onclick="sh('l', this)">Database</div>
        <div class="tab" onclick="sh('a', this)">Administration</div>
    </div>

    <div id="d" class="view">
        <h1>Global Operations Hub</h1>
        <div style="display:flex; gap: 20px;">
            <div style="flex:1; border: 1px solid blue; padding: 20px; border-radius: 8px;"><h4>Total Assets</h4><h2>$21.4M</h2></div>
            <div style="flex:1; border: 1px solid green; padding: 20px; border-radius: 8px;"><h4>New Contracts</h4><h2>54</h2></div>
            <div style="flex:1; border: 1px solid red; padding: 20px; border-radius: 8px;"><h4>Pending Issues</h4><h2>12</h2></div>
        </div>
        <p>System Sync State: <span id="sync">65%</span></p>
        <progress value="65" max="100" style="width: 100%"></progress>
    </div>

    <div id="l" class="view hidden">
        <h1>Portfolio Manager (15 Groups)</h1>
        <table>
            <thead><tr><th>ID</th><th>Legal Entity</th><th>Risk</th><th>Value</th></tr></thead>
            <tbody id="tb"></tbody>
        </table>
    </div>

    <div id="a" class="view hidden">
        <h1>Internal Account Setup</h1>
        <!-- 1. Text Input -->
        <label>Account Subject:</label><input id="name" type="text">
        <!-- 2. Text Area -->
        <label>Case Narrative:</label><textarea id="narrative"></textarea>
        <!-- 3. Dropdown -->
        <label>Vertical Sector:</label><select id="sector"><option>Legal</option><option>IT</option><option>Finance</option><option>Healthcare</option></select>
        <!-- 4. Radio Buttons -->
        <label>Account Type:</label>
        <div>
            <input type="radio" name="type" id="b2b" value="B2B" checked> <label for="b2b">B2B Enterprise</label>
            <input type="radio" name="type" id="b2c" value="B2C"> <label for="b2c">B2C Consumer</label>
        </div>
        <!-- 5. Checkbox -->
        <label>Permissions:</label>
        <input type="checkbox" id="marketing"> <label for="marketing">Marketing Automation</label>
        <!-- 6. Switch (using checkbox styled) -->
        <input type="checkbox" id="active" checked> <label for="active">ACCOUNT ACTIVE</label>
        <!-- 7. Slider -->
        <label>Priority Weight:</label><input type="range" id="priority" min="0" max="100" value="50">
        <!-- 8. Number Input (SpinBox) -->
        <label>Seat Count:</label><input type="number" id="seats" min="0" max="1000" value="10">
        <!-- 9. Date Picker -->
        <label>Effective Date:</label><input type="date" id="date">
        <!-- 10. Progress Bar -->
        <label>Sync Progress:</label><progress id="progress" value="65" max="100" style="width: 100%"></progress>
        <!-- 11. Buttons -->
        <div style="margin-top: 20px;">
            <button class="btn" onclick="pywebview.api.save(document.getElementById('name').value)">Finalize Data</button>
            <button class="btn" onclick="resetForm()" style="background: #95a5a6;">Reset Form</button>
        </div>
    </div>

    <script>
        function sh(id, el) {
            document.querySelectorAll('.view').forEach(v => v.classList.add('hidden'));
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.getElementById(id).classList.remove('hidden');
            el.classList.add('active');
        }
        
        let h = "";
        for(let i=1; i<=15; i++) {
            h += `<tr><td>${100+i}</td><td>Holding Group ${i}</td><td>Low</td><td>$${i*20}k</td></tr>`;
        }
        document.getElementById('tb').innerHTML = h;
        
        function resetForm() {
            document.getElementById('name').value = '';
            document.getElementById('narrative').value = '';
            document.getElementById('sector').value = 'Legal';
            document.getElementById('b2b').checked = true;
            document.getElementById('marketing').checked = false;
            document.getElementById('active').checked = true;
            document.getElementById('priority').value = 50;
            document.getElementById('seats').value = 10;
            document.getElementById('date').value = '';
        }
    </script>
</body>
</html>
"""

class API:
    def save(self, name):
        print(f"API: Persisting record {name}")

def main():
    api = API()
    window = webview.create_window('PyWebView Ultimate CRM', html=html_content, js_api=api, width=1100, height=800)
    webview.start()

if __name__ == '__main__':
    main()
