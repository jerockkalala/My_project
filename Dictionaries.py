alain={'non': 'kalala', 'position': 3}
print(alain)
alain['niveau']= 'licencie'
print(alain)

famille={}
famille['papa']='Mutombo'
famille['Maman']='Veronique'
famille['garcons']=5
famille['filles']= 3
famille['Total enfant']= 8
print(famille)
famille['papa']='Jean Paul'

print(famille)
mutombo_kid={
    'elvis':'fufu',
    'Maria':'riz',
    'jerock': 'Banane',
    }
print(mutombo_kid)
favori=mutombo_kid['elvis']
print(f"Le repas varifi de Elka c'est le {favori.title()}")
prefere = mutombo_kid.get('Esther', 'No value assigned')
print(favori)
print(prefere)

for key, value in mutombo_kid.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")