## Bitcoinkernel Pybind

These are experimental python bindings directly on Bitcoin Core's c++ code.

### Build instructions

Build the bitcoinkernel library:

```
cd bitcoin
cmake -B build -DBUILD_KERNEL_LIB=ON
cmake --build build --parallel
cd ..
```

Build the python bindings with pybind:
```
python -m venv. env
source .venv/bin/activate
pip install -e.
```

Run the example:
```
python example.py
```

