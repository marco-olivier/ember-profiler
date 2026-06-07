#!/usr/bin/env python3
"""Basic profiling example"""
import time
from ember import Profiler

def main():
    profiler = Profiler()
    profiler.start()
    
    # Simulate GPU workload
    time.sleep(2)
    
    report = profiler.stop()
    print(report.summary())

if __name__ == "__main__":
    main()
