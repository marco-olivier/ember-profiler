"""Memory profiler tests"""
import pytest
from ember.memory import MemoryProfiler, MemoryTracker

class TestMemoryProfiler:
    def test_allocation(self):
        profiler = MemoryProfiler()
        profiler.record_allocation(4096, 1024)
        assert profiler.current_usage == 1024
    
    def test_free(self):
        profiler = MemoryProfiler()
        profiler.record_allocation(4096, 1024)
        profiler.record_free(4096)
        assert profiler.current_usage == 0
    
    def test_peak(self):
        profiler = MemoryProfiler()
        profiler.record_allocation(4096, 2048)
        profiler.record_free(4096)
        profiler.record_allocation(8192, 1024)
        assert profiler.peak_usage == 2048

class TestMemoryTracker:
    def test_leak_detection(self):
        tracker = MemoryTracker(leak_threshold_seconds=0)
        tracker.register(4096, 1024)
        leaks = tracker.detect_leaks()
        assert len(leaks) == 1
