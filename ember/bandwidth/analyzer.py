"""Memory bandwidth analyzer"""
from typing import Dict, List
from dataclasses import dataclass
import time
import numpy as np

@dataclass
class TransferRecord:
    """Memory transfer record"""
    direction: str  # "htod" or "dtoh"
    size_bytes: int
    duration_seconds: float
    
    @property
    def bandwidth_gb_s(self) -> float:
        if self.duration_seconds == 0:
            return 0
        return (self.size_bytes / (1024**3)) / self.duration_seconds

class BandwidthAnalyzer:
    """Analyze memory bandwidth"""
    
    def __init__(self):
        self._transfers: List[TransferRecord] = []
    
    def record_transfer(self, direction: str, size_bytes: int, duration: float):
        """Record memory transfer"""
        self._transfers.append(TransferRecord(
            direction=direction,
            size_bytes=size_bytes,
            duration_seconds=duration
        ))
    
    def benchmark_bandwidth(self, size_mb: int = 256, iterations: int = 100) -> Dict:
        """Benchmark memory bandwidth"""
        # Simulated benchmark
        return {
            'host_to_device_gb_s': 12.4,
            'device_to_host_gb_s': 12.1,
            'device_local_gb_s': 890.5,
            'theoretical_max_gb_s': 900.0,
        }
    
    def get_summary(self) -> Dict:
        """Get transfer summary"""
        htod = [t for t in self._transfers if t.direction == 'htod']
        dtoh = [t for t in self._transfers if t.direction == 'dtoh']
        
        return {
            'total_transfers': len(self._transfers),
            'host_to_device': {
                'count': len(htod),
                'total_bytes': sum(t.size_bytes for t in htod),
                'avg_bandwidth': np.mean([t.bandwidth_gb_s for t in htod]) if htod else 0,
            },
            'device_to_host': {
                'count': len(dtoh),
                'total_bytes': sum(t.size_bytes for t in dtoh),
                'avg_bandwidth': np.mean([t.bandwidth_gb_s for t in dtoh]) if dtoh else 0,
            },
        }
