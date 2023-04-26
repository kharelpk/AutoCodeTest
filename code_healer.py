import os
import subprocess
import openai
from termcolor import colored

def run_script(script_path):
    result = subprocess.run(['python', script_path], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout, result.stderr

def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file_contents(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def ask_openai_gpt35_turbo(question, code):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Question: {question}\n\nCode:\n{code}\n\nPlease provide the corrected code snippet only:"}
        ]
    )

    return completion.choices[0].message['content'].strip()

def main():
    script_path = 'test.py'
    iteration = 1

    while True:
        stdout, stderr = run_script(script_path)
        code_contents = read_file_contents(script_path)

        if stderr:
            print(colored(f"Error encountered while running {script_path}:", 'red'))
            print(colored(stderr, 'red'))
            question = f"How can I fix the following error in Python code?\n{stderr}"
            print(colored("Thinking...", 'green'))
            suggestion = ask_openai_gpt35_turbo(question, code_contents)
            print(colored("Suggestion from OpenAI GPT-3.5 Turbo:", 'cyan'))
            print(colored(suggestion, 'cyan'))

            # Save the suggested code to a new file
            new_script_path = f"test_update{iteration}.py"
            write_file_contents(new_script_path, suggestion)
            script_path = new_script_path
            iteration += 1

            # Prompt user to continue or stop execution
            user_input = input("Do you want to continue checking for errors? (y/n): ")
            if user_input.lower() != 'y':
                break
        else:
            print(colored("Code is healed.", 'green'))
            print(colored(f"Output of {script_path}:", 'green'))
            print(colored(stdout, 'green'))
            break

if __name__ == '__main__':
    main()
