import os
import subprocess
import sys

def run_synthesis(file_name, top_module):
    if not os.path.exists(file_name):
        print(f"Error: {file_name} not found")
        return
    
    yosys_commands = f"""
    read_verilog {file_name}
    hierarchy -check -top {top_module}
    proc; opt; fsm; opt; memory; opt
    techmap; opt
    dfflibmap -liberty LIBS/asap7sc7p5t_SEQ_RVT_TT_nldm_220123.lib
    abc -liberty LIBS/asap7sc7p5t_SIMPLE_RVT_TT_nldm_211120.lib -liberty LIBS/asap7sc7p5t_INVBUF_RVT_TT_nldm_220122.lib -script +strash;map
    clean
    stat -liberty LIBS/asap7sc7p5t_SIMPLE_RVT_TT_nldm_211120.lib
    write_verilog -noattr {top_module}_synth.v
    show -format dot -prefix {top_module}_diag {top_module}
    """
    try:
        print(f"Starting synthesis for {top_module}")
        subprocess.run(["yosys", "-p", yosys_commands], check=True)
        dot_file = f"{top_module}_diag.dot"
        png_file = f"{top_module}_diag.png"

        if os.path.exists(dot_file):
            print(f"Converting {dot_file} to {png_file}")
            subprocess.run(["dot", "-Tpng", dot_file, "-o", png_file], check=True)
            print(f"Success! Diagram saved as {png_file}")

        print(f"Synthesis finished! Result: {top_module}_synth.v")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during synthesis: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 run_synth.py <file.v> <top_module>")
    else:
        run_synthesis(sys.argv[1], sys.argv[2])
