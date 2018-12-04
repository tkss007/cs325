from sys import argv
from math import sqrt
from file_reader import get_vertices_from_file
import datetime


def calculate_distance(point1, point2):
    dx = point1[1] - point2[1]
    dy = point1[2] - point2[2]
    return int(sqrt(dx * dx + dy * dy) + .5)


def total_distance(points):
    tot_1 = calculate_distance(points[0], points[len(points) - 1])
    tot_2 = sum([calculate_distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])
    tot_dist = tot_1 + tot_2
    return tot_dist


def find_nearest_neighbor(current_vertex, unvisited_vertices):
    nearest_neighbor = unvisited_vertices[0]
    minimum_distance = calculate_distance(current_vertex, nearest_neighbor)

    for neighbor in unvisited_vertices[1:]:
        distance = calculate_distance(current_vertex, neighbor)
        if distance < minimum_distance:
            nearest_neighbor = neighbor
            minimum_distance = distance

    return nearest_neighbor


def tsp(vertices):
    if len(vertices) < 1000:
        min_dist = float('inf')
        for i in range(0, len(vertices)):
            dist = 0
            start_vertex = vertices[i]
            unvisited_vertices = vertices[:]
            unvisited_vertices.remove(start_vertex)
            tour = [start_vertex]
            while len(unvisited_vertices) > 0:
                nearest_neighbor = find_nearest_neighbor(tour[-1], unvisited_vertices)
                unvisited_vertices.remove(nearest_neighbor)
                tour.append(nearest_neighbor)
            dist = int(total_distance(tour))
            if (dist < min_dist):
                min_tour = tour
                min_dist = dist
        return min_tour 
    else:
        start_vertex = vertices[0]
        unvisited_vertices = vertices[1:]
        tour = [start_vertex]
        while len(unvisited_vertices) > 0:
            nearest_neighbor = find_nearest_neighbor(tour[-1], unvisited_vertices)
            unvisited_vertices.remove(nearest_neighbor)
            tour.append(nearest_neighbor)
        return tour

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    
    vertices = get_vertices_from_file(argv[1])
    path = tsp(vertices)
    distance = int(total_distance(path))
    
    with open('{}.tour'.format(argv[1]), 'w') as f:
        f.write('{}\n'.format(distance))
        for vertex in path:
            f.write('{}\n'.format(vertex[0]))

    endtime = datetime.datetime.now()
    print (endtime - starttime)



