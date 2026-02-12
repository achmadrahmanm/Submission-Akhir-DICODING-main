import json
import sys

notebook_path = r'c:\laragon\www\Submission-Akhir-DICODING-main\[Clustering]_Submission_Akhir_BMLP_Achmad_Rahman_M.ipynb'

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Extract all code from code cells
    all_code = ""
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            all_code += source + "\n\n"

    # Save to a temporary script
    with open('run_verification.py', 'w', encoding='utf-8') as f:
        f.write(all_code)

    print("Extracted code to run_verification.py")

    # Now execute it
    import subprocess
    result = subprocess.run([sys.executable, 'run_verification.py'], capture_output=True, text=True)

    print("--- STDOUT ---")
    print(result.stdout)
    print("--- STDERR ---")
    print(result.stderr)

    if result.returncode == 0:
        print("Execution successful!")
    else:
        print(f"Execution failed with return code {result.returncode}")

except Exception as e:
    print(f"Error: {e}")
