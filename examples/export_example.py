#!/usr/bin/env python3
"""Export example"""
import time
from ember import Profiler
from ember.export import JsonExporter, CsvExporter

def main():
    profiler = Profiler()
    profiler.start()
    time.sleep(1)
    report = profiler.stop()
    
    # Export to JSON
    exporter = JsonExporter()
    exporter.export(report, "profile.json")
    print("Exported to profile.json")
    
    # Export to CSV
    csv_exporter = CsvExporter()
    csv_exporter.export(report.samples, "profile.csv")
    print("Exported to profile.csv")

if __name__ == "__main__":
    main()
