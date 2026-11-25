from transformers import pipeline

ner = pipeline('ner', grouped_entities=True)
results = ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
print(results)
# Example output:
# [{'entity_group': 'PER', 'score': 0.998, 'word': 'Sylvain', 'start': 11, 'end': 18},
#  {'entity_group': 'ORG', 'score': 0.975, 'word': 'Hugging Face', 'start': 33, 'end': 45},
#  {'entity_group': 'LOC', 'score': 0.998, 'word': 'Brooklyn', 'start': 49, 'end': 57}]