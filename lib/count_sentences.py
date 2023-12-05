#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            return("The value must be a string.")
        else: self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if not self.value:
            return 0
        # Split the string using regular expression to handle various punctuation marks
        sentences = re.split(r'[.!?]+', self.value)
        # Filter out empty strings from the list
        non_empty_sentences = [s.strip() for s in sentences if s.strip()]
        return len(non_empty_sentences)

