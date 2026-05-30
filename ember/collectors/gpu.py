"""GPU metrics collector"""
import subprocess
import json
import re
from typing import Dict, Optional

class GpuCollector:
    """Collect GPU metrics"""
    
    def __init__(self, device_id: int = 0):
        self.device_id = device_id
        self._tool = self._detect_tool()
    
    def _detect_tool(self) -> Optional[str]:
        """Detect available GPU monitoring tool"""
        for tool in ['nvidia-smi', 'rocm-smi']:
            try:
                subprocess.run([tool, '--version'], capture_output=True, check=True)
                return tool
            except (FileNotFoundError, subprocess.CalledProcessError):
                continue
        return None
    
    def collect(self) -> Dict[str, float]:
        """Collect GPU metrics"""
        if self._tool == 'nvidia-smi':
            return self._collect_nvidia()
        elif self._tool == 'rocm-smi':
            return self._collect_rocm()
        return {'utilization': 0, 'memory_used': 0, 'temperature': 0}
    
    def _collect_nvidia(self) -> Dict[str, float]:
        """Collect via nvidia-smi"""
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=utilization.gpu,memory.used,temperature.gpu',
                 '--format=csv,noheader,nounits'],
                capture_output=True, text=True, timeout=5
            )
            parts = result.stdout.strip().split(', ')
            return {
                'utilization': float(parts[0]),
                'memory_used': float(parts[1]) * 1024**2,  # MB to bytes
                'temperature': float(parts[2]),
            }
        except Exception:
            return {'utilization': 0, 'memory_used': 0, 'temperature': 0}
    
    def _collect_rocm(self) -> Dict[str, float]:
        """Collect via rocm-smi"""
        try:
            result = subprocess.run(
                ['rocm-smi', '--showuse', '--json'],
                capture_output=True, text=True, timeout=5
            )
            data = json.loads(result.stdout)
            return {
                'utilization': data.get('gpu_use', 0),
                'memory_used': data.get('vram_used', 0),
                'temperature': data.get('temperature', 0),
            }
        except Exception:
            return {'utilization': 0, 'memory_used': 0, 'temperature': 0}
