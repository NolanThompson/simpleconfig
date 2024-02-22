import sys
import platform
from execute import execute_command
from convert import convert_instructions
from output_valid import validate_output

if __name__ == "__main__":    
    #check number of arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <argument>")
        sys.exit(1)

    #fetch host os
    #host_os = platform.system()
    host_os = "Linux"

    #parse user input
    instructions = " ".join(sys.argv[1:])

    #invoke conversion
    prompt = "Your job is to accept instructions as input and convert them to the necessary commands to make the specified changes to iptables. The only thing you should return as output is commands that will achieve the specified result. These commands should follow proper syntax and be immediately executable with no editing required. Additionally, please verify that the commands are for iptables. Do not include any unnecessary commands or additional commentary, just the necessary command required and nothing more. If the operating system is incompatible, please don't include any other commentary except for this message, Error: unavailable on this OS. Please assume the operating system is: " + host_os + ". Here is what the commands should do: " + instructions
    command = convert_instructions(prompt + " " + instructions)



    validate_output(command)