year_list = list(range(1981, 1987))
print ('Q1:', year_list)

print("Q2:", "I'm 2 years old in", year_list[2])

print("Q3:", "I'm %s yeas old in year %s which is my oldest age in the year list." %(max(year_list) - min(year_list), max(year_list)))

things = ['mozzarella', 'cinderella', 'salmonella']
print ("Q4:", things)

things[0] = things[0].title()
things[1] = things[1].title()
things[2] = things[2].title()
print ("Q5:", things)

things[0] = things[0].upper()
things[1] = things[1].upper()
things[2] = things[2].upper()
print ("Q6:", things)

del things[-1]
print ("Q7:", things)

surprise = ['Grouch', 'Chico', 'Harpo']
print ('Q8', surprise)

surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print ('Q9', surprise)

e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print ('Q10', e2f)

print ('Q11', 'walrus is', e2f['walrus'])

f2e = {}
for item in e2f.items():
    f2e[item[1]] = item[0]
print ('Q12', f2e)

print ('Q13', f2e['chien'])

print ('Q14', list(f2e.values()))

life = {
    'animals': {'cats':['Henri', 'Grumpy', 'Lucy'], 'octopi':{}, 'emus':{}},
    'plants': {},
    'others': {}
}  
print ('Q15', 'life created')

print ('Q16', life)

print ('Q17', life['animals'])

print ('Q18', life['animals']['cats'])