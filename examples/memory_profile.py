#!/usr/bin/env python3
"""Memory profiling example"""
import time
from ember.memory import MemoryProfiler, MemoryTracker

def main():
    profiler = MemoryProfiler()
    tracker = MemoryTracker(leak_threshold_seconds=1)
    
    # Simulate allocations
    for i in range(100):
        addr = 0x1000 + i * 0x1000
        profiler.record_allocation(addr, 1024 * 1024)  # 1MB
        tracker.register(addr, 1024 * 1024)
    
    print(f"Current: {profiler.current_usage / 1024**2:.0f} MB")
    print(f"Peak: {profiler.peak_usage / 1024**2:.0f} MB")
    
    # Free some
    for i in range(0, 100, 2):
        addr = 0x1000 + i * 0x1000
        profiler.record_free(addr)
        tracker.unregister(addr)
    
    print(f"After free: {profiler.current_usage / 1024**2:.0f} MB")

if __name__ == "__main__":
    main()
