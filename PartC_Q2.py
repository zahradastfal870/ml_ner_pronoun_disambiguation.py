# Task: Named Entity Recognition + Pronoun ambiguity warning
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Chris met Alex at Apple headquarters in California. He told him about the new iPhone launch."

# Process text
doc = nlp(text)

# 1️⃣ Named Entity Recognition (NER)
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")

# 2️⃣ Pronoun ambiguity detection
pronouns = {"he", "she", "they", "him", "her", "them"}
found_pronouns = [token.text.lower() for token in doc if token.text.lower() in pronouns]

if found_pronouns:
    print("\n⚠️ Warning: Possible pronoun ambiguity detected!")
    print("Pronouns found:", found_pronouns)
else:
    print("\nNo pronoun ambiguity detected.")
