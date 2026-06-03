"""Memory usage profiler"""
from typing import Dict, List
from dataclasses import dataclass
import time

@dataclass
class AllocationRecord:
    """Memory allocation record"""
    address: int
    size: int
    timestamp: float
    freed: bool = False
    free_time: float = 0
    
    @property
    def lifetime(self) -> float:
        end = self.free_time if self.freed else time.time()
        return end - self.timestamp

class MemoryProfiler:
    """Track GPU memory allocations"""
    
    def __init__(self):
        self._allocations: Dict[int, AllocationRecord] = {}
        self._history: List[AllocationRecord] = []
        self._total_allocated = 0
        self._total_freed = 0
        self._peak_usage = 0
    
    def record_allocation(self, address: int, size: int):
        """Record memory allocation"""
        record = AllocationRecord(
            address=address,
            size=size,
            timestamp=time.time()
        )
        self._allocations[address] = record
        self._total_allocated += size
        self._update_peak()
    
    def record_free(self, address: int):
        """Record memory free"""
        if address in self._allocations:
            record = self._allocations.pop(address)
            record.freed = True
            record.free_time = time.time()
            self._history.append(record)
            self._total_freed += record.size
    
    def _update_peak(self):
        """Update peak memory usage"""
        current = self._total_allocated - self._total_freed
        if current > self._peak_usage:
            self._peak_usage = current
    
    @property
    def current_usage(self) -> int:
        """Current memory usage"""
        return self._total_allocated - self._total_freed
    
    @property
    def peak_usage(self) -> int:
        return self._peak_usage
    
    def get_summary(self) -> Dict:
        """Get memory summary"""
        return {
            'current': self.current_usage,
            'peak': self.peak_usage,
            'total_allocated': self._total_allocated,
            'total_freed': self._total_freed,
            'active_allocations': len(self._allocations),
        }
