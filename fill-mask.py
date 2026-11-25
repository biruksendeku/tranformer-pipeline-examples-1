from transformers import pipeline

unmasker = pipeline('fill-mask', top_k=2)
result = unmasker("This course will teach you all about <mask> models.")
print(result)
# Example output:
# [{'score': 0.15, 'token_str': 'machine', 'sequence': 'This course will teach you all about machine models.'},
#  {'score': 0.10, 'token_str': 'computer', 'sequence': 'This course will teach you all about computer models.'}]