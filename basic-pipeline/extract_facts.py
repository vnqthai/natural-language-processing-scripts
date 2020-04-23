import sys
import spacy
import textacy.extract

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# The text we want to examine
file = open('data/' + sys.argv[1], 'r')
text = file.read()
file.close()

# Parse the document with spaCy
doc = nlp(text)

# Extract semi-structured statements
subject = sys.argv[2]
statements = textacy.extract.semistructured_statements(doc, subject)

# Print the results
print(f"Here are the things I know about {subject}:")

for statement in statements:
    subject, verb, fact = statement
    print(f" - {fact}")
