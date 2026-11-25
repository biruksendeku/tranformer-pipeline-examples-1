from transformers import pipeline

classifier = pipeline("zero-shot-classification")
classification = classifier(
    "I have a problem with my order. It arrived damaged and I would like a refund.",
    candidate_labels=["complaint", "praise", "inquiry", "feedback"]
)
print(classification)