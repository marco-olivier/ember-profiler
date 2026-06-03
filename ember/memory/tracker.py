"""Memory leak tracker"""
from typing import List, Dict
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class LeakCandidate:
    """Potential memory leak"""
    address: int
    size: int
    age_seconds: float
    allocation_site: str = ""

class MemoryTracker:
    """Track and detect memory leaks"""
    
    def __init__(self, leak_threshold_seconds: float = 60):
        self.leak_threshold = leak_threshold_seconds
        self._active: Dict[int, dict] = {}
    
    def register(self, address: int, size: int):
        """Register allocation"""
        import time
        self._active[address] = {
            'size': size,
            'timestamp': time.time(),
        }
    
    def unregister(self, address: int):
        """Register deallocation"""
        self._active.pop(address, None)
    
    def detect_leaks(self) -> List[LeakCandidate]:
        """Detect potential memory leaks"""
        import time
        leaks = []
        
        for addr, info in self._active.items():
            age = time.time() - info['timestamp']
            if age > self.leak_threshold:
                leaks.append(LeakCandidate(
                    address=addr,
                    size=info['size'],
                    age_seconds=age
                ))
        
        return leaks
    
    @property
    def active_count(self) -> int:
        return len(self._active)
    
    @property
    def active_bytes(self) -> int:
        return sum(info['size'] for info in self._active.values())
