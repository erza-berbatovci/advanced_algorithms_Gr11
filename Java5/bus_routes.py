from collections import defaultdict, deque

def numBusesToDestination(routes, source, target):
    if source == target:
        return 0

    # Map from stop -> list of bus routes containing that stop
    stop_to_routes = defaultdict(set)
    for route_index, stops in enumerate(routes):
        for stop in stops:
            stop_to_routes[stop].add(route_index)

    # BFS setup
    visited_routes = set()
    visited_stops = set([source])
    queue = deque()
    
    # Initialize queue with all routes that include the source stop
    for route_index in stop_to_routes[source]:
        queue.append((route_index, 1))  # (route_index, buses_taken)
        visited_routes.add(route_index)

    # BFS traversal
    while queue:
        route_index, buses_taken = queue.popleft()

        for stop in routes[route_index]:
            if stop == target:
                return buses_taken  # Found target stop
            
            if stop not in visited_stops:
                visited_stops.add(stop)
                # Add all connected routes (routes sharing this stop)
                for next_route in stop_to_routes[stop]:
                    if next_route not in visited_routes:
                        visited_routes.add(next_route)
                        queue.append((next_route, buses_taken + 1))
                        
    return -1
print(numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))  # Output: 2
print(numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))  # Output: -1
