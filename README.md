# Project Title: asm

## One-line Tagline
A Python-based project leveraging Ghidra for binary analysis and decompilation.

## Architecture Overview
The `asm` repository is structured to handle binary analysis tasks using the Ghidra framework. The primary components include:
- **main.c**: A C program that checks if a person is allowed to drink based on age.
- **main.py**: A Python script that uses PyGhidra to load, analyze, and decompile a binary file (`check_age_bin`).
- **asm.asm, asm.def, code.asm, program.asm**: Assembly files likely used for various stages of the analysis or as part of the Ghidra project setup.

The interaction between these components is as follows:
1. The C program (`main.c`) is compiled into a binary file.
2. The Python script (`main.py`) uses PyGhidra to load this binary, perform auto-analysis, and decompile it into C code.
3. The decompiled output is then saved to `decompiled_output.c`.

## Tech Stack
- **Programming Languages**: Python, C
- **Libraries/Frameworks**:
  - **PyGhidra**: A Python interface for Ghidra, enabling automation of binary analysis tasks.
  - **Ghidra**: An open-source software reverse engineering framework developed by the NSA.

## Getting Started / Setup Guide

### Prerequisites
1. **Python**: Ensure you have Python installed (preferably version 3.6 or higher).
2. **Ghidra**: Download and install Ghidra from the [official website](https://ghidra-sre.org/).
3. **PyGhidra**: Install PyGhidra using pip:
   ```bash
   pip install pyghidra
   ```

### Steps to Run

1. **Compile the C Program**:
   - Navigate to the directory containing `main.c`.
   - Compile the program into a binary file named `check_age_bin`:
     ```bash
     gcc main.c -o check_age_bin
     ```

2. **Run the Python Script**:
   - Ensure that Ghidra is installed and accessible in your system's PATH.
   - Run the `main.py` script:
     ```bash
     python main.py
     ```
   - The script will load the binary, perform analysis, decompile it, and save the output to `decompiled_output.c`.

3. **Review the Output**:
   - After running the script, check the `decompiled_output.c` file for the decompiled C code.

### Troubleshooting
- If you encounter issues with PyGhidra initialization, ensure that Ghidra is correctly installed and accessible.
- Verify that the binary path specified in `main.py` (`check_age_bin`) matches the compiled binary's location.