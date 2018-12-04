import sys
import math
import exceptions

def algo_greedy_start(cities):
    route = [cities[0]]
    unvisited = cities[1:]
    #unvisited = _cities[0:]		#Again, make sure we have a local copy
    while unvisited:
        closest_dist = sys.maxint
        closest_idx = 0
        for i in unvisited:
            distance = add(math.pow(i[0] - route[-1][0], 2), math.pow((i[1] - route[-1][1]), 2))
            #distance = math.hypot(i[0] - route[-1][0], i[1] - route[-1][1])
            if distance < closest_dist:
                closest_dist = distance
                closest_idx = i
        route.append(closest_idx)
        unvisited.remove(closest_idx)

    route2 = []
    for i in route:
        route2.append(cities.index(i))

    return route2

def num(s):
	try:
		return int(s)
	except exceptions.ValueError:
		return float(s)
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
        except Exception as e:
            # The ident was not an int so we skip (pass) it and move on to the next
            pass
        #cities=line.split(' ')
        #cities = map(int, cities)
        result=",".join(map(str,algo_greedy_start(cities)))
        #print result
        with open("Results.txt","a") as f:
            f.write(result)
            f.write("\n")
fd.close()