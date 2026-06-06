"""JSON exporter"""
import json
from typing import Dict

class JsonExporter:
    """Export profiling data to JSON"""
    
    def export(self, report: 'ProfilerReport', output_path: str):
        """Export report to JSON"""
        data = report.to_json()
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
