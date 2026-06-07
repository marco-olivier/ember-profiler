"""Profiler tests"""
import pytest
import time
from ember.profiler import Profiler
from ember.report import ProfilerReport

class TestProfiler:
    def test_start_stop(self):
        profiler = Profiler(config=None)
        profiler.config.sample_interval = 0.01
        profiler.start()
        time.sleep(0.1)
        report = profiler.stop()
        assert isinstance(report, ProfilerReport)
        assert report.duration_seconds > 0
    
    def test_context_manager(self):
        with Profiler() as p:
            p.config.sample_interval = 0.01
            time.sleep(0.05)
        # No assertion needed, just ensure no crash
    
    def test_report_summary(self):
        report = ProfilerReport(duration_seconds=1.0, gpu_utilization=50.0)
        summary = report.summary()
        assert "50.0%" in summary
