# Getting Started

## Installation

```bash
pip install ember-profiler
```

## Basic Profiling

```python
from ember import Profiler

with Profiler() as profiler:
    # Your GPU code here
    pass

report = profiler.stop()
print(report.summary())
```

## Kernel Profiling

```python
from ember.kernel import KernelProfiler

profiler = KernelProfiler()

# Profile each kernel
profiler.start_kernel("my_kernel", grid, block)
# ... run kernel ...
profiler.stop_kernel()

print(profiler.get_summary())
```
