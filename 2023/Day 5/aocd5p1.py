with open("seeds.txt", "r") as seedsf:
    seeds = seedsf.readline().strip().split(" ")


soilsq = []
with open("seed to soil.txt", "r") as soilsf:
    for m in soilsf:
        soilsq.append(m.strip())
soils = []
for seed in seeds:
    found = False
    for soil in soilsq:
        fgfd = soil.split(" ")
        interval = int(seed) - int(fgfd[1]) 
        if 0 <= interval <= int(fgfd[2]):
            found = True
            soils.append(int(fgfd[0]) + interval)
            break
    if not found:
        soils.append(seed)


fertilizersq = []
with open("soil to fertilizer.txt", "r") as fertilizersf:
    for m in fertilizersf:
        fertilizersq.append(m.strip())
fertilizers = []
for soil in soils:
    found = False
    for fertilizer in fertilizersq:
        fgfg = fertilizer.split(" ")
        interval = int(soil) - int(fgfg[1]) 
        if 0 <= interval <= int(fgfg[2]):
            found = True
            fertilizers.append(int(fgfg[0]) + interval)
            break
    if not found:
        fertilizers.append(soil)


watersq = []
with open("fertilizer to water.txt", "r") as watersf:
    for m in watersf:
        watersq.append(m.strip())
waters = []
for fertilizer in fertilizers:
    found = False
    for water in watersq:
        asdf = water.split(" ")
        interval = int(fertilizer) - int(asdf[1]) 
        if 0 <= interval <= int(asdf[2]):
            found = True
            waters.append(int(asdf[0]) + interval)
            break
    if not found:
        waters.append(fertilizer)


lightsq = []
with open("water to light.txt", "r") as lightsf:
    for m in lightsf:
        lightsq.append(m.strip())
lights = []
for water in waters:
    found = False
    for light in lightsq:
        hjks = light.split(" ")
        interval = int(water) - int(hjks[1]) 
        if 0 <= interval <= int(hjks[2]):
            found = True
            lights.append(int(hjks[0]) + interval)
            break
    if not found:
        lights.append(water)


temperaturesq = []
with open("light to temperature.txt", "r") as temperaturesf:
    for m in temperaturesf:
        temperaturesq.append(m.strip())
temperatures = []
for light in lights:
    found = False
    for temperature in temperaturesq:
        hjks = temperature.split(" ")
        interval = int(light) - int(hjks[1]) 
        if 0 <= interval <= int(hjks[2]):
            found = True
            temperatures.append(int(hjks[0]) + interval)
            break
    if not found:
        temperatures.append(light)


humiditysq = []
with open("temperature to humidity.txt", "r") as humiditysf:
    for m in humiditysf:
        humiditysq.append(m.strip())
humiditys = []
for temperature in temperatures:
    found = False
    for humidity in humiditysq:
        ewgc = humidity.split(" ")
        interval = int(temperature) - int(ewgc[1]) 
        if 0 <= interval <= int(ewgc[2]):
            found = True
            humiditys.append(int(ewgc[0]) + interval)
            break
    if not found:
        humiditys.append(temperature)


locationsq = []
with open("humidity to location.txt", "r") as locationsf:
    for m in locationsf:
        locationsq.append(m.strip())
locations = []
for humidity in humiditys:
    found = False
    for location in locationsq:
        adsr = location.split(" ")
        interval = int(humidity) - int(adsr[1]) 
        if 0 <= interval <= int(adsr[2]):
            found = True
            locations.append(int(adsr[0]) + interval)
            break
    if not found:
        locations.append(humidity)

print(min(locations))