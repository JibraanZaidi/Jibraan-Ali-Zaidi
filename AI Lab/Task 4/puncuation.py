punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def remove_punctuation(text):
    return ''.join(char for char in text if char not in punctuations)

sample = "Hello, Jibraan Zaidi kas'a ho! bha'i? kia kry/// ho?"
result = remove_punctuation(sample)
print(result)
