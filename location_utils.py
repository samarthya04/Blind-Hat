import osmnx as ox
import geocoder
from math import radians, sin, cos, sqrt, atan2

def get_location_coordinates(location_name):
    g = geocoder.osm(f"{location_name}, Bhubaneswar, India")
    return g.latlng if g.ok else None

def calculate_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (sin(dlat/2)**2 + cos(radians(lat1)) * 
         cos(radians(lat2)) * sin(dlon/2)**2)
    return 2 * R * atan2(sqrt(a), sqrt(1-a)) * 1000  # Meters

def get_bhubaneswar_graph():
    return ox.graph_from_place("Bhubaneswar, India", network_type='walk')

def find_walking_route(G, start_point, end_point):
    start_node = ox.nearest_nodes(G, start_point[1], start_point[0])
    end_node = ox.nearest_nodes(G, end_point[1], end_point[0])
    route = ox.shortest_path(G, start_node, end_node, weight='length')
    return [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

def plot_route(G, route):
    fig, ax = ox.plot_graph_route(G, route, route_color='r', route_linewidth=4, node_size=0)
    return fig
