import os
import pyghidra

# 1. Initialize PyGhidra JVM FIRST
pyghidra.start()

# 2. Import Ghidra modules after JVM startup
from ghidra.app.decompiler import DecompInterface
from ghidra.app.plugin.core.analysis import AutoAnalysisManager
from ghidra.util.task import TaskMonitor

binary_path = "check_age_bin"
output_path = "decompiled_output.c"

print(f"[-] Loading and analyzing {binary_path} from scratch...")

c_code_collection = []

# 3. Load the binary container
load_results = pyghidra.program_loader().source(binary_path).load()

program = None
for obj in load_results:
    program = obj.getDomainObject()
    break

if not program:
    raise RuntimeError("Failed to load program from binary.")

# 4. Force Ghidra to run deep Auto-Analysis with no prior knowledge
print("[-] Running Ghidra auto-analysis engine...")
analysis_manager = AutoAnalysisManager.getAnalysisManager(program)
analysis_manager.analyzeAll(TaskMonitor.DUMMY)

# 5. Decompile all discovered functions
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

print("[+] Independent decompilation complete and saved to", output_path)
