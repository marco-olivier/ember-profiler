#!/usr/bin/env python3
"""Kernel profiling example"""
import time
from ember.kernel import KernelProfiler

def main():
    profiler = KernelProfiler()
    
    # Simulate kernel executions
    for i in range(10):
        profiler.start_kernel(f"kernel_{i}", (64, 1, 1), (256, 1, 1))
        time.sleep(0.01)  # Simulate execution
        profiler.stop_kernel()
    
    summary = profiler.get_summary()
    for name, stats in summary.items():
        print(f"{name}: {stats['count']} calls, {stats['mean_ms']:.2f}ms avg")

if __name__ == "__main__":
    main()
