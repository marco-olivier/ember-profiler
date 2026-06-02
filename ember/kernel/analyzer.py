"""Kernel performance analyzer"""
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Bottleneck:
    """Performance bottleneck"""
    category: str
    description: str
    severity: str  # low, medium, high
    recommendation: str

class KernelAnalyzer:
    """Analyze kernel performance"""
    
    def __init__(self):
        self._bottlenecks: List[Bottleneck] = []
    
    def analyze(self, executions: list) -> List[Bottleneck]:
        """Analyze kernel executions for bottlenecks"""
        self._bottlenecks = []
        
        # Check for occupancy issues
        self._check_occupancy(executions)
        
        # Check for memory issues
        self._check_memory(executions)
        
        # Check for launch overhead
        self._check_launch_overhead(executions)
        
        return self._bottlenecks
    
    def _check_occupancy(self, executions: list):
        """Check GPU occupancy"""
        for exec in executions:
            block_size = exec.block_size[0] * exec.block_size[1] * exec.block_size[2]
            if block_size < 128:
                self._bottlenecks.append(Bottleneck(
                    category="occupancy",
                    description=f"Low block size {block_size} for kernel {exec.name}",
                    severity="medium",
                    recommendation="Increase block size to 256 or 512"
                ))
    
    def _check_memory(self, executions: list):
        """Check memory usage"""
        for exec in executions:
            if exec.shared_memory > 48000:
                self._bottlenecks.append(Bottleneck(
                    category="memory",
                    description=f"High shared memory usage ({exec.shared_memory} bytes)",
                    severity="medium",
                    recommendation="Reduce shared memory usage to avoid bank conflicts"
                ))
    
    def _check_launch_overhead(self, executions: list):
        """Check kernel launch overhead"""
        if len(executions) > 100:
            self._bottlenecks.append(Bottleneck(
                category="launch_overhead",
                description=f"Many kernel launches ({len(executions)})",
                severity="low",
                recommendation="Consider kernel fusion to reduce launch overhead"
            ))
    
    def get_recommendations(self) -> List[str]:
        """Get optimization recommendations"""
        return [b.recommendation for b in self._bottlenecks]
