def planets(id):
    planetsdict = {
        1: 'Mercury',
        2: 'Venus',
        3: 'Earth',
        4: 'Mars',
        5: 'Jupiter',
        6: 'Saturn',
        7: 'Uranus',
        8: 'Neptune',
        9: 'Pluto'
    }

    if 0 < id < 10:
        return f"The planet corresponding to the id {id} is {planetsdict[id]}!"
    else:
        return "Planets ID should be in between 1 to 9!"


id = int(input("Enter the ID for the planets: "))
print(planets(id))