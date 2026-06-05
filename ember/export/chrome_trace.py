"""Chrome Trace format exporter"""
import json
from typing import List, Dict

class ChromeTraceExporter:
    """Export profiling data to Chrome Trace format"""
    
    def export(self, samples: List[Dict], output_path: str):
        """Export to Chrome Trace JSON"""
        events = []
        
        for sample in samples:
            if 'gpu' in sample and sample['gpu']:
                events.append({
                    'name': 'gpu_utilization',
                    'ph': 'C',
                    'ts': sample['timestamp'] * 1000000,
                    'pid': 0,
                    'tid': 0,
                    'args': {'utilization': sample['gpu'].get('utilization', 0)}
                })
        
        with open(output_path, 'w') as f:
            json.dump({'traceEvents': events}, f)
