"""Core profiler"""
import time
import threading
from typing import Optional, Dict, Any
from .report import ProfilerReport, ProfilerConfig
from .collectors import GpuCollector, CpuCollector, MemoryCollector

class Profiler:
    """Main profiler interface"""
    
    def __init__(self, config: Optional[ProfilerConfig] = None):
        self.config = config or ProfilerConfig()
        self._running = False
        self._start_time = 0
        self._gpu_collector = GpuCollector()
        self._cpu_collector = CpuCollector()
        self._memory_collector = MemoryCollector()
        self._samples = []
        self._thread: Optional[threading.Thread] = None
    
    def start(self):
        """Start profiling"""
        if self._running:
            return
        
        self._running = True
        self._start_time = time.time()
        
        # Start collection thread
        self._thread = threading.Thread(target=self._collect_loop)
        self._thread.start()
    
    def stop(self) -> ProfilerReport:
        """Stop profiling and return report"""
        self._running = False
        if self._thread:
            self._thread.join(timeout=5)
        
        return self._generate_report()
    
    def _collect_loop(self):
        """Background collection loop"""
        while self._running:
            sample = {
                'timestamp': time.time(),
                'gpu': self._gpu_collector.collect(),
                'cpu': self._cpu_collector.collect(),
                'memory': self._memory_collector.collect(),
            }
            self._samples.append(sample)
            time.sleep(self.config.sample_interval)
    
    def _generate_report(self) -> ProfilerReport:
        """Generate profiler report"""
        duration = time.time() - self._start_time
        
        gpu_util = [s['gpu']['utilization'] for s in self._samples if s['gpu']]
        memory_used = [s['memory']['used'] for s in self._samples if s['memory']]
        
        return ProfilerReport(
            duration_seconds=duration,
            num_samples=len(self._samples),
            gpu_utilization=sum(gpu_util) / max(len(gpu_util), 1),
            gpu_memory_used=sum(memory_used) / max(len(memory_used), 1),
            samples=self._samples
        )
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, *args):
        self.stop()
