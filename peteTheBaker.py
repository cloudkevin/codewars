import math

def cakes(recipe, available):
    required = list(recipe.keys())
    ratios = []
    for r in required:
        if available.get(r, 'null') == 'null':
            return 0
    for i in recipe:
        ratios.append(math.floor(available[i] / recipe[i]))
    ratios.sort()
    return ratios[:1][0]
