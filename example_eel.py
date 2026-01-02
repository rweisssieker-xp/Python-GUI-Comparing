import eel
import os
import random

# Exposing Python to JS
@eel.expose
def add_lead_to_db(name):
    print(f"Staging lead: {name}")
    return f"Success: {name} added to pipeline."

def main():
    # Create web folder if it doesn't exist (simulated for comparative purposes)
    web_path = os.path.join(os.path.dirname(__file__), 'eel_web')
    if not os.path.exists(web_path):
        os.makedirs(web_path)
    
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Eel Ultimate CRM</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #f4f7f6; margin: 0; display: flex; }
            #sidebar { width: 200px; background: #2c3e50; color: white; height: 100vh; padding: 20px; }
            #content { flex: 1; padding: 30px; overflow-y: auto; height: 100vh; }
            .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }
            table { width: 100%; border-collapse: collapse; }
            th, td { border-bottom: 1px solid #eee; padding: 12px; text-align: left; }
            .hidden { display: none; }
            .btn { background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; }
        </style>
    </head>
    <body>
        <div id="sidebar">
            <h2 onclick="show('dash')">CRM Hub</h2>
            <div onclick="show('dash')">Dashboard</div>
            <div onclick="show('list')">Accounts</div>
            <div onclick="show('admin')">New Entry</div>
        </div>
        <div id="content">
            <!-- DASHBOARD -->
            <div id="dash" class="view">
                <h1>Executive Intelligence</h1>
                <div style="display: flex; gap: 20px;">
                    <div class="card" style="flex:1"><h3>Revenue</h3><h2 style="color: #27ae60">$1.8M</h2></div>
                    <div class="card" style="flex:1"><h3>Active Leads</h3><h2>324</h2></div>
                    <div class="card" style="flex:1"><h3>Pending Issues</h3><h2 style="color: #e74c3c">8</h2></div>
                </div>
                <div class="card">
                    <h3>Syncing Statistics...</h3>
                    <progress value="72" max="100" style="width: 100%;"></progress>
                </div>
            </div>

            <!-- CUSTOMER LIST -->
            <div id="list" class="view hidden">
                <h1>Active Portfolio</h1>
                <div class="card">
                    <table>
                        <thead><tr><th>ID</th><th>Company</th><th>Status</th><th>Value</th></tr></thead>
                        <tbody id="table-body"></tbody>
                    </table>
                </div>
            </div>

            <!-- ADMIN FORM -->
            <div id="admin" class="view hidden">
                <h1>Add New Opportunity</h1>
                <div class="card">
                    <!-- 1. Text Input -->
                    <label>Lead Entity:</label><br><input type="text" id="name" style="width:100%"><br><br>
                    <!-- 2. Text Area -->
                    <label>Internal Bio:</label><br><textarea id="bio" style="width:100%; height:100px;"></textarea><br><br>
                    <!-- 3. Dropdown -->
                    <label>Vertical:</label><br><select id="vertical" style="width:100%"><option>Tech</option><option>Retail</option><option>Finance</option><option>Healthcare</option></select><br><br>
                    <!-- 4. Radio Buttons -->
                    <label>Category:</label><br>
                    <input type="radio" name="cat" id="cat_b2b" value="B2B" checked> <label for="cat_b2b">B2B Enterprise</label>
                    <input type="radio" name="cat" id="cat_b2c" value="B2C"> <label for="cat_b2c">B2C Consumer</label><br><br>
                    <!-- 5. Checkbox -->
                    <input type="checkbox" id="newsletter" checked> <label for="newsletter">Newsletter Active</label><br>
                    <!-- 6. Switch (using checkbox styled) -->
                    <input type="checkbox" id="active" checked> <label for="active">ACCOUNT ACTIVE STATUS</label><br><br>
                    <!-- 7. Slider -->
                    <label>Relationship Score:</label><br><input type="range" id="score" min="0" max="100" value="50" style="width:100%"><br><br>
                    <!-- 8. Number Input (SpinBox) -->
                    <label>Seat Count:</label><br><input type="number" id="seats" min="0" max="1000" value="10" style="width:100%"><br><br>
                    <!-- 9. Date Picker -->
                    <label>Target Date:</label><br><input type="date" id="target_date"><br><br>
                    <!-- 10. Progress Bar -->
                    <label>Sync Progress:</label><br><progress id="sync_progress" value="65" max="100" style="width:100%"></progress><br><br>
                    <!-- 11. Buttons -->
                    <button class="btn" onclick="save()">Persist Entry</button>
                    <button class="btn" onclick="resetForm()" style="background: #95a5a6;">Reset Form</button>
                </div>
            </div>
        </div>

        <script>
            function show(id) {
                document.querySelectorAll('.view').forEach(v => v.classList.add('hidden'));
                document.getElementById(id).classList.remove('hidden');
            }
            
            function save() {
                let n = document.getElementById('name').value;
                eel.add_lead_to_db(n)(function(res) { alert(res); });
            }
            
            function resetForm() {
                document.getElementById('name').value = '';
                document.getElementById('bio').value = '';
                document.getElementById('vertical').value = 'Tech';
                document.getElementById('cat_b2b').checked = true;
                document.getElementById('newsletter').checked = true;
                document.getElementById('active').checked = true;
                document.getElementById('score').value = 50;
                document.getElementById('seats').value = 10;
                document.getElementById('target_date').value = '';
            }

            // Populate 15 rows
            let html = "";
            for(let i=1; i<=15; i++) {
                html += `<tr><td>${100+i}</td><td>Global Co ${i}</td><td>Active</td><td>$${i*5}k</td></tr>`;
            }
            document.getElementById('table-body').innerHTML = html;
        </script>
    </body>
    </html>
    """
    
    with open(os.path.join(web_path, 'index.html'), 'w') as f:
        f.write(html_content)

    eel.init(web_path)
    eel.start('index.html', size=(1100, 800))

if __name__ == "__main__":
    main()
