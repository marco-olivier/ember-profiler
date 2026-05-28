# Ember Profiler

Real-time performance monitoring and profiling toolkit for GPU workloads.

## Features

- **GPU Monitoring**: Utilization, memory, temperature tracking
- **Kernel Profiling**: Per-kernel execution analysis
- **Memory Tracking**: Allocation patterns and leaks
- **Bandwidth Analysis**: Host↔Device transfer metrics
- **Timeline Visualization**: Event timeline rendering
- **Export**: Chrome Trace, JSON, CSV formats

## Quick Start

```python
from ember import Profiler

# Start profiling
profiler = Profiler()
profiler.start()

# ... your GPU code ...

# Stop and get results
report = profiler.stop()
print(f"GPU Utilization: {report.gpu_utilization:.1f}%")
print(f"Memory Used: {report.memory_used / 1024**3:.1f}GB")
```

## Requirements

- Python 3.9+
- GPU monitoring tools (nvidia-smi, rocm-smi)

## Installation

```bash
pip install ember-profiler
```

## License

MIT License
