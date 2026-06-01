"""Kernel execution profiler"""
from typing import Dict, List, Optional
from dataclasses import dataclass
import time

@dataclass
class KernelExecution:
    """Single kernel execution record"""
    name: str
    start_time: float
    end_time: float
    grid_size: tuple
    block_size: tuple
    shared_memory: int = 0
    
    @property
    def duration_ms(self) -> float:
        return (self.end_time - self.start_time) * 1000

class KernelProfiler:
    """Profile GPU kernel executions"""
    
    def __init__(self):
        self._executions: List[KernelExecution] = []
        self._current: Optional[KernelExecution] = None
    
    def start_kernel(self, name: str, grid: tuple, block: tuple, shared_mem: int = 0):
        """Start timing kernel"""
        self._current = KernelExecution(
            name=name,
            start_time=time.perf_counter(),
            end_time=0,
            grid_size=grid,
            block_size=block,
            shared_memory=shared_mem
        )
    
    def stop_kernel(self):
        """Stop timing kernel"""
        if self._current:
            self._current.end_time = time.perf_counter()
            self._executions.append(self._current)
            self._current = None
    
    def get_summary(self) -> Dict[str, dict]:
        """Get per-kernel summary"""
        from collections import defaultdict
        kernel_times = defaultdict(list)
        
        for exec in self._executions:
            kernel_times[exec.name].append(exec.duration_ms)
        
        import numpy as np
        summary = {}
        for name, times in kernel_times.items():
            times = np.array(times)
            summary[name] = {
                'count': len(times),
                'total_ms': float(times.sum()),
                'mean_ms': float(times.mean()),
                'min_ms': float(times.min()),
                'max_ms': float(times.max()),
            }
        
        return summary
    
    @property
    def total_executions(self) -> int:
        return len(self._executions)
    
    @property
    def total_time_ms(self) -> float:
        return sum(e.duration_ms for e in self._executions)
