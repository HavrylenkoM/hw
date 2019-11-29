def down(s):
    return s.lower()


def up(s):
    return s.upper()

s = 'HeLlO GooDbye MaLenKiy SloVARNiy ZapaS'


print(down(s))
print(up(s))




slova1 = ['HeLlO', 'GooDbye', 'MaLenKiy', 'SloVARNiy', 'ZapaS']

slova2 = list(map(lambda x: x.upper(), slova1))
slova3 = list(map(lambda x: x.lower(), slova1))

print(slova2)
print(slova3)


