import itertools
def get_pins(pin):
    adjacent = {
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '6'],
        '4': ['1', '5', '7'],
        '5': ['2', '4', '6', '8'],
        '6': ['3', '5', '9'],
        '7': ['4', '8'],
        '8': ['5', '7', '9', '0'],
        '9': ['6', '8'],
        '0': ['8'],
    }
    combos=[[p]+adjacent[p] for p in pin]
    return [''.join(c) for c in list(itertools.product(*combos))]