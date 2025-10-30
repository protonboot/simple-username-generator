import os
import fitz
import re
import pyphen
from collections import defaultdict

class Deconstructor:
    def __init__(self, lang):
        self.lang = lang
        self.dic = pyphen.Pyphen(lang=self.lang)

    def _extract_text(self, path: str):
        full_text = ""
        if os.path.exists(path):
            filename, ext = os.path.splitext(path)
            if ext == ".pdf":
                with open(path, "rb") as file:
                    pdf_bytes = file.read()
                doc = fitz.open(stream=pdf_bytes, filetype="pdf")
                full_text = " ".join(page.get_text() for page in doc)
                return full_text
            elif ext == ".txt":
                with open(path, "r") as file:
                    full_text = " ".join(file.read().split()) # split and join to have all words on one line
                    return full_text
            raise ValueError(f"'{ext}' filetype is not supported for text extraction")
        else:
            raise ValueError("Cannot extract text: the inputted path doesn't exist.")

    def _deconstruct(self, path: str):
        if os.path.exists(path):
            filename, _ = os.path.splitext(path)
            deconstructed_path = path + "_deconstructed" + ".txt"
            text = self._extract_text(path)
            normalized_text = re.findall(r"\b[a-zA-Z]+\b", text)
            return normalized_text
        else:
            raise ValueError("Cannot deconstruct: the inputted path doesn't exist.")
        
    def syllabyze(self, path: str):
        if os.path.exists(path):
            normalized_text = self._deconstruct(path)
            syllable_lists = [self.dic.inserted(word).split("-") for word in normalized_text]

            transitions = defaultdict(list)

            for syllables in syllable_lists:
                for i in range(len(syllables) - 1):
                    current_syllable = syllables[i]
                    next_syllable = syllables[i + 1]
                    transitions[current_syllable].append(next_syllable)

            return transitions