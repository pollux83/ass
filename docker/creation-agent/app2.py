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

    # Extract relevant information from the NLU processed instructions
    # You can add your logic here to handle different NLU tasks (e.g., named entity recognition, part-of-speech tagging)

    # Example: Extracting verbs from the instructions
    verbs = [token.lemma_ for token in doc if token.pos_ == 'VERB']

    # Example: Extracting named entities from the instructions
    entities = [ent.text for ent in doc.ents]

    # Example: Print the extracted verbs and named entities
    print("Extracted verbs:", verbs)
    print("Extracted entities:", entities)

    # Return a response to indicate the successful extraction of information
    return "NLU processing completed"

if __name__ == '__main__':
    app.run()
