def planetsByID(planet_id):
    planetslist = [
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune',
        'Pluto'
    ]

    if 0 < planet_id < 10:
        return f"The planet corresponding to the ID {planet_id} is {planetslist[planet_id - 1]}!"
    return "Planets ID should be in between 1 to 9!"


try:
    planet_id = int(input("Enter the ID for the planet: "))
    print(planetsByID(planet_id))
except ValueError:
    print("Value Error: Planets ID should be in between 1 to 9!")
