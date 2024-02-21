

planet_list = ["Mercury", "Mars"]
rocky_planets = slice(0, 4)

last_two_planets = ["Uranus", "Neptune"]



planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(last_two_planets)
planet_list.insert(1,"Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")
del planet_list[8]


print(planet_list)
print(planet_list[rocky_planets])


spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
]

for planet in planet_list:
    for tuple in spacecraft:
        if planet is tuple[1]:

            print(f'{tuple[0]} has visited {planet}')
