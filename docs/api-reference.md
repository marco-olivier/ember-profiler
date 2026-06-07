# API Reference

## Profiler

### `Profiler(config=None)`
Create profiler instance.

### `profiler.start()`
Start profiling.

### `profiler.stop() -> ProfilerReport`
Stop profiling and return report.

## ProfilerReport

### `report.summary() -> str`
Get text summary.

### `report.to_json() -> Dict`
Export to JSON dict.

## GpuCollector

### `collector.collect() -> Dict`
Collect GPU metrics.

## KernelProfiler

### `profiler.start_kernel(name, grid, block)`
Start timing kernel.

### `profiler.stop_kernel()`
Stop timing kernel.

### `profiler.get_summary() -> Dict`
Get per-kernel summary.

## MemoryProfiler

### `profiler.record_allocation(addr, size)`
Record allocation.

### `profiler.record_free(addr)`
Record deallocation.

### `profiler.get_summary() -> Dict`
Get memory summary.
