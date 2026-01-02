"""
Export utilities for comparison data.
Supports CSV and JSON export formats.
"""

import csv
import json
import os
from comparison_data import FRAMEWORK_DATA, FEATURE_MATRIX

def export_to_csv(filename, frameworks_list):
    """
    Export comparison data to CSV file.
    
    Args:
        filename: Output CSV file path
        frameworks_list: List of (name, script) tuples to export
    """
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Header
        writer.writerow([
            "Framework", "Tech", "License", "Use Case", "Category",
            "Windows", "Linux", "macOS", "Mobile",
            "Learning Curve", "Python Version", "Install Difficulty",
            "Performance", "Community", "Documentation"
        ])
        
        # Data rows
        for name, script in frameworks_list:
            base_name = name.split(" (")[0]
            if base_name in FRAMEWORK_DATA:
                data = FRAMEWORK_DATA[base_name]
                platforms = data['platforms']
                writer.writerow([
                    name,
                    data['tech'],
                    data['license'],
                    data['use_case'],
                    data['category'],
                    "Yes" if platforms['windows'] else "No",
                    "Yes" if platforms['linux'] else "No",
                    "Yes" if platforms['macos'] else "No",
                    "Yes" if platforms['mobile'] else "No",
                    data['learning_curve'],
                    data['python_version'],
                    data['install_difficulty'],
                    data['performance'],
                    data['community'],
                    data['documentation']
                ])

def export_to_json(filename, frameworks_list):
    """
    Export comparison data to JSON file.
    
    Args:
        filename: Output JSON file path
        frameworks_list: List of (name, script) tuples to export
    """
    
    export_data = {
        "frameworks": {},
        "metadata": {
            "total_frameworks": len(frameworks_list),
            "export_format_version": "1.0"
        }
    }
    
    for name, script in frameworks_list:
        base_name = name.split(" (")[0]
        if base_name in FRAMEWORK_DATA:
            export_data["frameworks"][name] = {
                "script": script,
                **FRAMEWORK_DATA[base_name],
                "features": FEATURE_MATRIX.get(base_name, {})
            }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)

def export_features_to_csv(filename, frameworks_list):
    """
    Export feature matrix to CSV file.
    
    Args:
        filename: Output CSV file path
        frameworks_list: List of (name, script) tuples to export
    """
    from comparison_data import FEATURE_LABELS
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Header
        header = ["Framework"] + list(FEATURE_LABELS.values())
        writer.writerow(header)
        
        # Data rows
        for name, script in frameworks_list:
            base_name = name.split(" (")[0]
            if base_name in FEATURE_MATRIX:
                features = FEATURE_MATRIX[base_name]
                row = [name]
                for feature_key in FEATURE_LABELS.keys():
                    row.append("Yes" if features.get(feature_key, False) else "No")
                writer.writerow(row)
