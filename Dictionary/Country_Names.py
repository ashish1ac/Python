countries = {}

for i in range(5):
    cname = input("Enter the name of the country: ")

    if cname[0] not in countries:
        countries[cname[0]] = [cname]
    else:
        countries[cname[0]].append(cname)

print(countries)
