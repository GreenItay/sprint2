import networkx as nx
import typing
from algorithmics.utils.coordinate import Coordinate
from algorithmics.enemy.radar import Radar
from algorithmics.enemy import Enemy
def create_radar_graph(source: Coordinate, target :Coordinate, radar : Radar):
    """
    :param: source - Coordinate of beginning on the radar
    :param: target - Coordinate inside the radar or on edge
    :param: radar - Radar object
    :return: g - nx.Graph object with legal lines between neighbors inside the grid
    """
    division_parameter = 100
    radius = radar.radius
    grid = [[0 for i in range(division_parameter)] for j in range(division_parameter)]
    center_of_radar: Coordinate = radar.center
    start_of_grid: Coordinate = Coordinate(center_of_radar.x - radar.radius, center_of_radar.y - radar.radius)
    division_ratio = 2 * radius/division_parameter

    for i in range(division_parameter):
        for j in range(division_parameter):
            grid[i][j] = Coordinate(start_of_grid.x + i *division_ratio, start_of_grid.y + j * division_ratio)
    g = nx.Graph()
    g.add_nodes_from(grid)
    g.add_node(source)
    g.add_node(target)
  
    return g 

def optimal_path_in_radar(g: nx.Graph, source: Coordinate, target: Coordinate):
    return nx.shortest_path(g, source, target, 'dist')

def get_edges_to_neighbors(i, j, distance, grid, enemies: list['Enemy']):
    """return a list - edges"""
    edges = [] # (start, end, weight)
    current = grid[i][j]
    for neighbor in find_neighbors(grid, i, j, distance):
            edges.append((current, neighbor, current.distance_to(neighbor)))
    
    return edges

def find_neighbors(grid, _i, _j, distance) -> list[Coordinate]:
    neighbors = []

    for i in range(_i, _i + distance + 1): # out of bounds
        for j in range(_j, _j + distance + 1):
            if i != _i or j != _j:
                neighbors.append(grid[i][j])
    return neighbors


def is_legal_line(n1: Coordinate, n2: Coordinate, enemies: list[Enemy]):


    return True

def find_location_of_point_on_grid(c: Coordinate):
    ...

