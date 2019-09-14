phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
# first_half = int(len(phrase)/2) calculates a half of the sentence as int
first_half = phrase[:int(len(phrase)/2)]
print(first_half)
