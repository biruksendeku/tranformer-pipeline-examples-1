from transformers import pipeline

classifier = pipeline("zero-shot-classification")
classification = classifier(
    "I have a problem with my order. It arrived damaged and I would like a refund.",
    candidate_labels=["complaint", "praise", "inquiry", "feedback"]
)
print(classification)
# Example output:
# {'sequence': 'I have a problem with my order. It arrived damaged and I would like a refund.',
#  'labels': ['complaint', 'feedback', 'inquiry', 'praise'],
#  'scores': [0.85, 0.08, 0.05, 0.02]}