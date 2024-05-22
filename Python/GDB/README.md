# Python GDB Scripts

Some scripts that have proven useful in CTF/hacking.

## iterate_registers.py

This script will break on a specific function (in this example, `welcome`). It will step through the function, spitting out the register values to an extract.txt file, removing any empty registers or ones populated by different functions.

It will also step 30 places forwards and backwards in memory and spit out any useful values there too, in case I've missed anything when analysing the assembly code.