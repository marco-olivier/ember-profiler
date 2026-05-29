"""Profiler report"""
from dataclasses import dataclass, field
from typing import Dict, List, Any
from enum import Enum

@dataclass
class ProfilerConfig:
    """Profiler configuration"""
    sample_interval: float = 0.1  # seconds
    enable_gpu: bool = True
    enable_cpu: bool = True
    enable_memory: bool = True

class ReportFormat(Enum):
    TEXT = "text"
    JSON = "json"
    CHROME_TRACE = "chrome_trace"

@dataclass
class ProfilerReport:
    """Profiler results"""
    duration_seconds: float = 0.0
    num_samples: int = 0
    gpu_utilization: float = 0.0
    gpu_memory_used: float = 0.0
    cpu_utilization: float = 0.0
    memory_used: float = 0.0
    samples: List[Dict] = field(default_factory=list)
    
    @property
    def gpu_memory_gb(self) -> float:
        return self.gpu_memory_used / (1024**3)
    
    @property
    def memory_gb(self) -> float:
        return self.memory_used / (1024**3)
    
    def summary(self) -> str:
        """Get text summary"""
        return f"""
Profiler Report
===============
Duration: {self.duration_seconds:.2f}s
Samples: {self.num_samples}
GPU Utilization: {self.gpu_utilization:.1f}%
GPU Memory: {self.gpu_memory_gb:.2f}GB
CPU Utilization: {self.cpu_utilization:.1f}%
System Memory: {self.memory_gb:.2f}GB
"""
    
    def to_json(self) -> Dict:
        """Convert to JSON"""
        return {
            'duration': self.duration_seconds,
            'samples': self.num_samples,
            'gpu': {
                'utilization': self.gpu_utilization,
                'memory_used': self.gpu_memory_used,
            },
            'cpu': {
                'utilization': self.cpu_utilization,
            },
            'memory': {
                'used': self.memory_used,
            }
        }
