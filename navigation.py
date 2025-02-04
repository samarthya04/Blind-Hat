import time
from speech_utils import say_text
from location_utils import calculate_distance
from obstacle_detection import detect_obstacles

def navigate(route, current_pos, destination):
    current_step = 0
    
    try:
        while True:
            if obstacles := detect_obstacles():
                say_text(f"Caution ahead: {', '.join(obstacles)}")
            
            target = route[current_step]
            distance = calculate_distance(current_pos, target)
            
            if distance < 10:
                if current_step >= len(route) - 1:
                    say_text("Destination reached")
                    break
                current_step += 1
                say_text(f"Reached waypoint {current_step} of {len(route)}")
            else:
                say_text(f"Continue for {int(distance)} meters to waypoint {current_step + 1}")
            
            time.sleep(10)
            # In a real scenario, update current_pos here with GPS data
            # For simulation, we'll move along the route
            current_pos = route[current_step]

    except KeyboardInterrupt:
        say_text("Navigation stopped")
