import subprocess
import sys
import platform
from get_prompt import convert

#fetch host os
def get_os_info():
    host_os = platform.system()

#execute commands
def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Error executing command:\n", e.stderr.decode('utf-8'))

if __name__ == "__main__":
    #check number of arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <argument>")
        sys.exit(1)

    instructions = " ".join(sys.argv[1:])
    print(f"Instructions: {instructions}")

    #concat all arguments into single string
    full_command = " ".join(sys.argv[1:])

    execute_command(full_command)