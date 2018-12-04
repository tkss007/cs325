import time, itertools, math, exceptions

#Get distance between 2 cities
#Cities stored as [ident, x, y]
def getDistance(city1, city2):
    return 	math.sqrt((int(city2[1]) - int(city1[1]))**2 + (int(city2[2])-int(city1[2]))**2)

def num(s):
    try:
        return int(s)
    except exceptions.ValueError:
        return float(s)

#Get the cities from a specified city file
"""
def getCities(cityFile):
    for line in cityFile:
        try:
            #Lines split by white space will look like:
            #[ident, x-coord, y-coord]
            parts = line.split()
            if parts[0].isdigit():
                #Cities are just lists with values (almost a pseudo-class)
                #city = [num(ident), num(x), num(y), False]
                city = [num(parts[0]), num(parts[1]), num(parts[2].strip('\n')), False]
                cities.append(city)
        except Exception as e:
            #The ident was not an int so we skip (pass) it and move on to the next
            pass
"""
#A function to calculate the nearest neighbor of an abitrary node
def getNearestNeighbor(i):
    #Start at infinity
    nearest = [-1, float("inf")]

    #print '\n cities:' + str(cities)
    for index in range(len(cities)):
        #Skip if looking at itself or looking at a visited node
        if i == index or cities[index][3] == True:
            pass
        #Otherwise calculate distance and update nearest if necessary
        else:
            distance = getDistance(cities[i], cities[index])
            #print nearest
            if distance < nearest[1]:
                nearest = [index, distance]

    #Set nearest to visited and return
    cities[nearest[0]][3] = True
    return nearest

#A function to calculate the 'best' TSP tour on a given set of vertexes
def nearestNeighbor(cities):
    data = []
    tour = [[],0]
    first = getNearestNeighbor(0)
    data.append(first)
    next = first
    #Get the nearest neighbor and weight for every vertex and append to the list
    for index in range(1,len(cities)):
        cur = getNearestNeighbor(next[0])
        data.append(cur)
        next = cur

    #Once we have the path and weight, split into 2 arrays for ease of use
    for element in data:
        tour[1] += element[1]
        tour[0].append(element[0])
    #Account for weight of last node -> first node to complete the cycle
    tour[1] += getDistance(cities[tour[0][-1]],cities[tour[0][0]])
    #Return the tour
    return tour

cities = []
with open("tsp_example_1.txt","r") as fd:
    for line in fd:

        try:
            # Lines split by white space will look like:
            # [ident, x-coord, y-coord]
            parts = line.split()
            if parts[0].isdigit():
                # Cities are just lists with values (almost a pseudo-class)
                # city = [num(ident), num(x), num(y), False]
                city = [num(parts[0]), num(parts[1]), num(parts[2].strip('\n')), False]
                cities.append(city)
        #array=line.split(' ')
        #array = map(int, array)
        print nearestNeighbor(cities)
        #result = " \n".join(map(str,nearestNeighbor(cities)))
        #print result
        #with open("Results.txt","a") as f:
        #    f.write(result)
        #    f.write("\n")
fd.close()