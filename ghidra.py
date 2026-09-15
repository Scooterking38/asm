import os
import pyghidra

# Initialize PyGhidra JVM
pyghidra.start()

binary_path = "check_age_bin"
output_path = "decompiled_output.c"

print(f"[-] Loading and analyzing {binary_path}...")

# Load the binary using the builder pattern and get the loaded program
load_results = pyghidra.program_loader().source(binary_path).load()

# Depending on the pyghidra version, retrieve the program object safely:
# If load_results acts as a context manager yielding the flat API or domain object:
program = load_results.getProgram() if hasattr(load_results, "getProgram") else load_results

from ghidra.app.decompiler import DecompInterface

decompiler = DecompInterface()
decompiler.openProgram(program)

function_manager = program.getFunctionManager()
functions = function_manager.getFunctions(True)

c_code_collection = []

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
