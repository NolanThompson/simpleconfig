import sys
import platform
from execute import execute_command
from convert import convert_instructions

if __name__ == "__main__":    
    #check number of arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <argument>")
        sys.exit(1)

    #fetch host os
    host_os = platform.system()

    #parse user input
    instructions = " ".join(sys.argv[1:])

    #invoke conversion
    prompt = "Your job is to accept instructions as input and convert them to the necessary commands to make the specified changes to iptables. The only thing you should return as output is commands that will achieve the specified result. These commands should follow proper syntax and be immediately executable with no editing required. Do not include any unnecessary commands or additional commentary, just the necessary command required and nothing more. Please assume the operating system is: " + host_os + ". Here is what the commands should do: " + instructions
    command = convert_instructions(prompt + " " + instructions)

    print("\n" + prompt)
    print("\n" + command)

    #execute_command(command)

    #process:
    #main(get input)-->convert(create commands)-->simpleconfig(execute commands)