import os
import pyghidra

# Set Ghidra install directory from environment variable
pyghidra.start()

binary_path = "check_age_bin"  # Name of the compiled binary
output_path = "decompiled_output.c"

print(f"[-] Loading and analyzing {binary_path}...")

with pyghidra.program_loader(binary_path) as flat_api:
    program = flat_api.getCurrentProgram()
    
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
