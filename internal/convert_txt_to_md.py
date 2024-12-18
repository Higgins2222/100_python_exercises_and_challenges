import re
import os

def convert_to_md(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # Split the content by the separator marker
    questions = content.split('#----------------------------------------#')

    # Ask to overwrite if file exists
    overwrite = 'n'
    if os.path.exists(output_file):
        overwrite = input(f"The file {output_file} exists. Overwrite? (y/n): ")
    if overwrite.lower() == 'y':
        # Open output markdown file
        cont = ''
        with open(output_file, 'w') as md_file:
            #i = -1 # stupid header
            i = 0 # removed the header for now
            for question in questions:
                question = question.strip()
                # print(question)
                # if cont != 's':
                #     cont = input()
                # if cont == 't':
                #     break
                if question:
                    i += 1
                    question_pattern = r"(?:[Qq]uestion ?)?\n( \d+)?\s*(?:[Ll]evel )?(\d+)?\s*(?:\n?[Qq]uestion.*?\n)?(.*?)\n(?:[Hh]ints?:? *)+?\n(.*?)\n(?:[Ss]olutions?:? *)+?\n(.*?)$"

                    match = re.search(question_pattern, question, re.DOTALL)
                    print(f'{i}: {match}')
                    if match:
                        # Extract matched data if it follows the structure
                        question_number, level, question_text, hints, solution = match.groups()

                        # Handle missing data
                        question_number = question_number if question_number else str(i)
                        question_text = question_text if question_text else 'no text'
                        hints = hints.strip() if hints else "No hints provided."
                        solution = solution.strip() if solution else "No solution provided."

                        # Write formatted markdown content
                        md_file.write(f"## Question {question_number} (Level {level})\n\n")
                        md_file.write(f"**Question:**\n{question_text.strip()}\n\n")
                        md_file.write(f"**Hints:**\n{hints}\n\n")
                        md_file.write(f"**Solution:**\n```\n{solution}\n```\n\n")
                    else:
                        # If it doesn't match the expected structure, output raw text
                        md_file.write(f"### Raw Question Block (No structured match):\n\n")
                        md_file.write(f"```\n{question}\n```\n\n")

    else:
        print("File not overwritten.")

# Usage example
convert_to_md('100plus_python_exercises.txt', '..\\100plus_python_exercises.md')
