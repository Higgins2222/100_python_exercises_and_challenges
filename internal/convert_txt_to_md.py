import re
import os
from dataclasses import dataclass
from typing import Optional


SEPARATOR = '#----------------------------------------#'

source = '100plus_python_exercises.txt'
md_dest = '..\\100plus_python_exercises_and_solutions.md'
questions_dest = '..\\100plus_python_exercises.md'

@dataclass
class Question:
    number: str
    chapter: Optional[str]
    level: Optional[str]
    text: str
    hints: str
    solution: str

def read_content(input_file):
    with open(input_file, 'r') as file:
        return file.read()

def parse_questions(content):
    # Split the content by the separator marker
    questions = content.split(SEPARATOR)
    # A list of Question objects
    parsed_questions = []

    # Our regex, works for the specific original file that was provided, grabs the text for all questions even those that are malformed, basically as long as the block has the word 'question' in it followed by a newline char and some text, the text will be captured as a question, solution and hints are optional and will be given default no-entry values if not present.
    question_pattern = r"(\d*\.\d*)?(?:(?:[Qq]uestion[\n ]?)(\d+))?\s*(?:[Ll]evel )?(\d+)?\s*(?:\n?[Qq]uestion.*?\n)?(.*?)\n(?:[Hh]ints?:? *)+?\n(.*?)\n(?:[Ss]olutions?:? *)?\n(.*?)$"

    # Questions output counter
    i = 0
    for question in questions:
        question = question.strip()
        if question:
            i += 1 # Update counter if section is not blank
            match = re.search(question_pattern, question, re.DOTALL)
            print(f'{i}: {match}')
            if match:
                # Extract matched data if it follows the structure
                chapter, question_number, level, question_text, hints, solution = match.groups()
                # Handle missing data
                # Apply escape chars to special markdown chars
                parsed_questions.append(Question(
                    number = question_number or str(i),
                    chapter = chapter if chapter else None,
                    level = level if level else None,
                    text = question_text.replace('*', '\\*') if question_text else "no text",
                    hints = hints.strip() if hints else "No hints provided.",
                    solution = solution.strip() if solution else "No solution provided."
                ))
            else:
                # Output the raw text if the structure cannot be decoded
                parsed_questions.append(Question(
                    number=str(i),
                    chapter=None,
                    level=None,
                    text="Raw Question Block",
                    hints="No hints provided.",
                    solution=question
                ))
    return parsed_questions

def write_markdown(output_file, questions):
    # Ask to overwrite if file exists
    if os.path.exists(output_file):
        overwrite = input(f"The file {output_file} exists. Overwrite? (y/n): ").strip().lower()
        if not overwrite.lower().startswith('y'):
            print("File not overwritten.")
            return

    # Open output markdown file
    with open(output_file, 'w') as md_file:
        for question in questions:
            if question.text == "Raw Question Block":
                md_file.write(f"### Raw Question Block (No structured match):\n\n")
                md_file.write(f"```\n{question.solution}\n```\n\n")
            else:
                md_file.write(f"## Question {question.number} {'(Level '+str(question.level)+')' if question.level else ''} {'('+question.chapter+')' if question.chapter else ''}\n\n")
                md_file.write(f"{question.text}\n\n")
                md_file.write(f"**Hints:**\n{question.hints}\n\n")
                md_file.write(f"**Solution**\n\n")
                md_file.write(f"```python\n{question.solution}\n```\n\n")

def write_markdown_questions_only(output_file, questions):
    # Ask to overwrite if file exists
    if os.path.exists(output_file):
        overwrite = input(f"The file {output_file} exists. Overwrite? (y/n): ").strip().lower()
        if not overwrite.startswith('y'):
            print("File not overwritten.")
            return

    with open(output_file, 'w') as md_file:
        for question in questions:
            if question.text == "Raw Question Block":
                md_file.write(f"### Raw Question Block (No structured match):\n\n")
                md_file.write(f"```\n{question.solution}\n```\n\n")
            else:
                md_file.write(f"**Question {question.number}**\n\n")
                md_file.write(f"{question.text}\n\n")


if __name__ == '__main__':
    content = read_content(source)
    questions = parse_questions(content)
    write_markdown(md_dest, questions)
    write_markdown_questions_only(questions_dest, questions)
