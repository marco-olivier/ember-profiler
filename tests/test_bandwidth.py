"""Bandwidth analyzer tests"""
import pytest
from ember.bandwidth import BandwidthAnalyzer

class TestBandwidthAnalyzer:
    def test_benchmark(self):
        analyzer = BandwidthAnalyzer()
        result = analyzer.benchmark_bandwidth()
        assert result["host_to_device_gb_s"] > 0
    
    def test_record_transfer(self):
        analyzer = BandwidthAnalyzer()
        analyzer.record_transfer("htod", 1024**3, 0.1)
        summary = analyzer.get_summary()
        assert summary["host_to_device"]["count"] == 1
