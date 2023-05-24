import spacy
from flask import Flask, request

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route('/create_task', methods=['POST'])
def create_task():
    # Receive instructions or requests from users or external systems
    instructions = request.form.get('instructions')

    # Perform Natural Language Understanding (NLU) on the received instructions
    doc = nlp(instructions)

    # Task Extraction and structuring
    task_objective = None
    required_inputs = []
    constraints = []
    dependencies = []

    # Example: Extracting the task's objective
    for sentence in doc.sents:
        if "task" in sentence.text.lower():
            task_objective = sentence.text
            break

    # Example: Extracting required inputs
    for token in doc:
        if token.pos_ == 'NOUN':
            required_inputs.append(token.text)

    # Example: Extracting constraints
    for token in doc:
        if token.dep_ == 'aux':
            constraints.append(token.text)

    # Example: Extracting dependencies
    for token in doc:
        if token.dep_ == 'prep':
            dependencies.append(token.text)

    # Task Specification
    task_specification = {
        "task_objective": task_objective,
        "required_inputs": required_inputs,
        "constraints": constraints,
        "dependencies": dependencies
        # Add more fields as needed: due date, priority level, required resources, etc.
    }

    # Example: Print the task specification
    print("Task Specification:", task_specification)

    # Return a response to indicate the successful task specification creation
    return "Task specification created successfully"

if __name__ == '__main__':
    app.run()
