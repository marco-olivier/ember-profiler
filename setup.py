from setuptools import setup, find_packages

setup(
    name="ember-profiler",
    version="0.1.0",
    author="Marco Olivier",
    description="GPU performance monitoring and profiling toolkit",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=["psutil>=5.9.0", "pydantic>=2.0.0"],
    extras_require={"dev": ["pytest"]},
)
