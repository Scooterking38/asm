import os
import pyghidra

# 1. Initialize PyGhidra JVM FIRST before any ghidra imports
pyghidra.start()

# 2. Import Ghidra modules AFTER the JVM has started
from ghidra.app.decompiler import DecompInterface

binary_path = "check_age_bin"
output_path = "decompiled_output.c"

print(f"[-] Loading and analyzing {binary_path}...")

c_code_collection = []

# 3. Load the binary using the modern program_loader API
load_results = pyghidra.program_loader().source(binary_path).load()

program = None
for obj in load_results:
    # Extract the actual Ghidra Program (DomainObject) instance
    program = obj.getDomainObject()
    break

if not program:
    raise RuntimeError("Failed to load program from binary.")

decompiler = DecompInterface()
decompiler.openProgram(program)

function_manager = program.getFunctionManager()
functions = function_manager.getFunctions(True)

for func in functions:
    func_name = func.getName()
    entry_point = func.getEntryPoint()
    
    header = f"// Function: {func_name} at {entry_point}\n"
    res = decompiler.decompileFunction(func, 30, None)
    
    if res and res.decompileCompleted():
        code = res.getDecompiledFunction().getC()
        c_code_collection.append(header + code + "\n\n")
    else:
        c_code_collection.append(header + "// Error: Could not decompile\n\n")
        
decompiler.dispose()

# Save output to a file for GitHub artifacts
with open(output_path, "w") as f:
    f.writelines(c_code_collection)

print("[+] Decompilation complete and saved to", output_path)
