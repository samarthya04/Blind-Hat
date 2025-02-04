from speech_utils import say_text, get_audio_input
from location_utils import get_location_coordinates, find_walking_route, get_bhubaneswar_graph, plot_route
from obstacle_detection import detect_obstacles
from navigation import navigate
import matplotlib.pyplot as plt

def main():
    # Get Bhubaneswar graph
    G = get_bhubaneswar_graph()
    say_text("Bhubaneswar map loaded")

    # Get source location
    source_name = None
    for _ in range(5):
        source_name = get_audio_input("Please say your current location in Bhubaneswar")
        if source_name:
            source_coords = get_location_coordinates(source_name)
            if source_coords:
                break
            else:
                say_text("Location not found in Bhubaneswar. Please try again.")
        if _ == 4:
            say_text("Failed to get source location. Exiting.")
            return

    # Get destination location
    destination_name = None
    for _ in range(5):
        destination_name = get_audio_input("Please say your destination in Bhubaneswar")
        if destination_name:
            destination_coords = get_location_coordinates(destination_name)
            if destination_coords:
                break
            else:
                say_text("Location not found in Bhubaneswar. Please try again.")
        if _ == 4:
            say_text("Failed to get destination location. Exiting.")
            return

    say_text(f"Navigating from {source_name} to {destination_name} in Bhubaneswar")
    
    route = find_walking_route(G, source_coords, destination_coords)
    
    # Plot and save the route
    fig = plot_route(G, route)
    plt.savefig('bhubaneswar_route.png')
    plt.close(fig)
    say_text("Route map saved as bhubaneswar_route.png")

    navigate(route, source_coords, destination_coords)

if __name__ == "__main__":
    main()
