ML NER Pronoun Disambiguation

Author: Zahra Dastfal
Student Number:700777425
Course: DSA 5600 — Machine Learning
Assignment: Homework 4 — Part C (Coding)

Description

This project demonstrates Named Entity Recognition (NER) and pronoun ambiguity detection using spaCy. It identifies named entities in a text (like people, organizations, and locations) and checks for possible pronoun-related ambiguity.
The code file: ml_ner_pronoun_disambiguation.py

Input Example

"Chris met Alex at Apple headquarters in California. He told him about the new iPhone launch."

Expected Output

Named Entities:
Chris -> PERSON
Alex -> PERSON
Apple -> ORG
California -> GPE
iPhone -> ORG
⚠️ Warning: Possible pronoun ambiguity detected!
Pronouns found: ['he', 'him']

How to Run

1-Install spaCy
pip install spacy
python -m spacy download en_core_web_sm
2-Run the script
python ml_ner_pronoun_disambiguation.py

Notes

This code is part of Homework 4 – Part C (Q2) for DSA 5600. It prints all detected named entities and shows a warning if pronouns are found. The code is well-commented and meets the assignment submission requirements
