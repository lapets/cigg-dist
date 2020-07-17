"""Load and confirm compatibility of CIGG for current environment."""

# Check that the object file can be loaded and invoked.
import canaries

lib = canaries.load({
    'Linux': ['./cigg.linux.64.so', './cigg.linux.32.so'],
    'Darwin': ['./cigg.macos.64.so', './cigg.macos.32.so'],
    'Windows': ['./cigg.win.64.dll', './cigg.win.32.dll']
})

assert(lib is not None)
