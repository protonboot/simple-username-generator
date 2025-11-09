import json
import random

class Generator:
    def _predict_syllable(self, model, temperature, last_syllable):
        items = list(model[last_syllable].keys())
        weights = [float(p) ** (1/temperature) for p in list(model[last_syllable].values())] # adjusted with temperature

        syl = random.choices(items, weights=weights, k=1)

        if len(syl) == 1:
            syl = syl[0]
        else:
            raise Exception("The syl dictionary contains more then 1 keys")
        
        return syl
    
    def generate(self, length: int, modelfile_path: str, temperature: float):
        modelfile = open(modelfile_path, "r")
        model = json.load(modelfile)

        username = ""
        last_syllable = ""

        for i in range(length):
            if i == 0:
                username = random.choice(list(model.keys()))
                last_syllable = username
            else:
                if last_syllable in model:
                    syl = self._predict_syllable(model=model, temperature=temperature, last_syllable=last_syllable)
                    username += syl
                    last_syllable = syl
                    
                else:
                    print(f"model['{last_syllable}'] doesn't exist in the model file. Retrying username generation.")
                    i = 0
                

        return username