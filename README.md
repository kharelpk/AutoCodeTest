# Code Healers

Code Healers is a debugging tool that utilizes OpenAI's GPT-3.5 Turbo model to efficiently identify and resolve errors in your Python code.

## Features

- AI-driven error identification and resolution
- Iterative error checking and code improvement
- User-controlled execution
- Time-efficient debugging process

## Installation

To use Code Healers, you'll need to install the required Python libraries:

```bash
pip install openai termcolor
```

## Setup

You'll need an API key from OpenAI to use their GPT-3.5 Turbo model. Set the `OPENAI_API_KEY` environment variable to your OpenAI API key:

```bash
export OPENAI_API_KEY="your_api_key"
```

Replace `your_api_key` with your actual API key.

## Usage

1. Save your Python code with errors as `test.py` in the same directory as the Code Healers script.

2. Run the Code Healers script:

```bash
python code_healer.py
```

3. The script will run your code, identify errors, and consult the GPT-3.5 Turbo model for solutions. The updated code will be saved as `test_update1.py`, `test_update2.py`, and so on.

4. The script will prompt you to continue checking for errors. Enter 'y' to continue or 'n' to stop the execution.

5. Once the code is error-free, the script will display a "Code is healed" message along with the output of the error-free code.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
