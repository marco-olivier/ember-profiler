"""Collector tests"""
import pytest
from ember.collectors import GpuCollector, CpuCollector, MemoryCollector

class TestCpuCollector:
    def test_collect(self):
        collector = CpuCollector()
        data = collector.collect()
        assert 'utilization' in data
    
    def test_load(self):
        collector = CpuCollector()
        data = collector.collect_load()
        assert 'load_1m' in data

class TestMemoryCollector:
    def test_collect(self):
        collector = MemoryCollector()
        data = collector.collect()
        assert 'total' in data
        assert 'used' in data
