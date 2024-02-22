from execute import execute_command
from convert import convert_instructions

def validate_output(output):
    validation_prompt = "Please analyze the following input. If the input is only iptables commands, return the commands and nothing else. If the input contains anything other than iptables commands, remove everything but the iptables commands. If the input contains no iptables commands at all, return the following message: Error: Unable to convert. Here is the input: "
    command = convert_instructions(validation_prompt + " " + output)

    summary_prompt = "Please analyze the following input. If the input is only iptables commands, please return a summary of the changes the commands are making. Make the summary as short as possible and make it easy to understand. There is no need to restate the commands either, just summarize them. If the input contains anything other than iptables commands, disregard everything but the iptables commands and then summarize the changes being made by the commands. If the input contains no iptables commands at all, return the following message: Error: Unable to convert. Here is the input: "
    summary = convert_instructions(summary_prompt + " " + command)

    user_input = input(f"\n{summary}\n\n{command}\n\nEnter 'y' to accept or 'n' to reject: ").lower()
    
    while user_input not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n'.")
        user_input = input(f"\n{summary}\n\n{command}\n\nEnter 'y' to accept or 'n' to reject changes: ").lower()

    if user_input == 'y':
        #invoke commands
        print("\nAccepted, changes have been made.\n")
    else:
        print("\nRejected, no change was made.\n")
        exit

    return command