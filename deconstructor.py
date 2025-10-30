import os
import fitz
import re
import pyphen

class Deconstructor:
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

    def deconstruct(self, path: str):
        if os.path.exists(path):
            filename, _ = os.path.splitext(path)
            deconstructed_path = path + "_deconstructed" + ".txt"
            text = self._extract_text(path)
            normalized_text = re.findall(r"\b[a-zA-Z]+\b", text)
            with open(deconstructed_path, "w") as file:
                if len(normalized_text) <= 1000:
                    update_index = 100
                elif len(normalized_text) <= 100:
                    update_index = 10
                elif len(normalized_text) <= 10000:
                    update_index = 1000
                else:
                    update_index = 10000
                for i, word in enumerate(normalized_text, start=1):
                    file.write(word + "\n")
                    if i % update_index == 0:
                        print(f"Wrote {i} words to file")      
        else:
            raise ValueError("Cannot deconstruct: the inputted path doesn't exist.")