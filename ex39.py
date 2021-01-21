#creates a mapping of the state to abbrevation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("Michigan's abbrevation is:", states['Michigan'])
print("Florida's abbrevation is:", states['Florida'])

#print some states
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every states abbrevation
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbrevated as {abbrev}")

#print every city in state 
print('-' * 10)
for abberv ,city in list(cities.items()):
	print(f"{abberv} has  the city {city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbrevated {abbrev}")
	print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get a abbrevation by the state that might not be there
state = states.get('Texas')

if not states:
	print("Sorry, no Texas.")


#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"THe city for the state 'TX' is :{city}")