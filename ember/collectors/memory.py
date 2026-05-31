"""Memory metrics collector"""
import psutil
from typing import Dict

class MemoryCollector:
    """Collect memory metrics"""
    
    def collect(self) -> Dict[str, float]:
        """Collect memory metrics"""
        mem = psutil.virtual_memory()
        return {
            'total': mem.total,
            'used': mem.used,
            'available': mem.available,
            'percent': mem.percent,
        }
    
    def collect_swap(self) -> Dict[str, float]:
        """Collect swap metrics"""
        swap = psutil.swap_memory()
        return {
            'total': swap.total,
            'used': swap.used,
            'percent': swap.percent,
        }
    
    def collect_process(self, pid: int = None) -> Dict[str, float]:
        """Collect process memory"""
        proc = psutil.Process(pid)
        mem = proc.memory_info()
        return {
            'rss': mem.rss,
            'vms': mem.vms,
        }
