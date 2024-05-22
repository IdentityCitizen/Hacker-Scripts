# Overwriting the PTrace function

This is useful when a binary has debugging detection logic built in.

The code is essentially an empty function, so when it is called, it doesn't return anything. This tricks the binary into thinking it is not being traced.

Compile accordingly:
`gcc -shared ptrace.cpp -o ptrace.so`

Run the following from within GDB (if you're debugging there) to tell it to use your ptrace.so file instead of the OS one:

`set environment LD_PRELOAD ./ptrace.so`


# Alternative

Patching the binary could also work, but I'm sure this would ultimately change the hash of the binary if a secondary check was also performed.