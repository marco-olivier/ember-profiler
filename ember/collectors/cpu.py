"""CPU metrics collector"""
import psutil
from typing import Dict

class CpuCollector:
    """Collect CPU metrics"""
    
    def collect(self) -> Dict[str, float]:
        """Collect CPU metrics"""
        return {
            'utilization': psutil.cpu_percent(interval=0),
            'frequency': psutil.cpu_freq().current if psutil.cpu_freq() else 0,
            'cores': psutil.cpu_count(),
        }
    
    def collect_per_core(self) -> list:
        """Collect per-core metrics"""
        return psutil.cpu_percent(percpu=True)
    
    def collect_load(self) -> Dict[str, float]:
        """Get system load averages"""
        load1, load5, load15 = psutil.getloadavg()
        return {
            'load_1m': load1,
            'load_5m': load5,
            'load_15m': load15,
        }
