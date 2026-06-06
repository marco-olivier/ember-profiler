"""CSV exporter"""
import csv
from typing import List, Dict

class CsvExporter:
    """Export profiling data to CSV"""
    
    def export(self, samples: List[Dict], output_path: str):
        """Export samples to CSV"""
        if not samples:
            return
        
        fieldnames = ['timestamp', 'gpu_utilization', 'gpu_memory', 'cpu_utilization', 'memory_used']
        
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for sample in samples:
                row = {
                    'timestamp': sample.get('timestamp', 0),
                    'gpu_utilization': sample.get('gpu', {}).get('utilization', 0),
                    'gpu_memory': sample.get('gpu', {}).get('memory_used', 0),
                    'cpu_utilization': sample.get('cpu', {}).get('utilization', 0),
                    'memory_used': sample.get('memory', {}).get('used', 0),
                }
                writer.writerow(row)
