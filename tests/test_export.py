"""Export tests"""
import pytest
import tempfile
from ember.export import JsonExporter, CsvExporter
from ember.report import ProfilerReport

class TestJsonExporter:
    def test_export(self):
        exporter = JsonExporter()
        report = ProfilerReport(duration_seconds=1.0)
        with tempfile.NamedTemporaryFile(suffix=".json", mode="w") as f:
            exporter.export(report, f.name)

class TestCsvExporter:
    def test_export(self):
        exporter = CsvExporter()
        samples = [{"timestamp": 1, "gpu": {"utilization": 50}, "cpu": {"utilization": 25}, "memory": {"used": 1024}}]
        with tempfile.NamedTemporaryFile(suffix=".csv", mode="w") as f:
            exporter.export(samples, f.name)
