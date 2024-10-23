import heapq

# Function to perform Dijkstra's Algorithm
def dijkstra(graph, start):
    # Initialize the priority queue (min heap)
    priority_queue = []
    
    # Distances dictionary (to store the shortest distance to each node)
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # The distance to the start node is 0
    
    # Push the start node into the priority queue
    heapq.heappush(priority_queue, (0, start))  # (distance, node)
    
    while priority_queue:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the distance of the current node is greater than the stored distance, skip processing
        if current_distance > distances[current_node]:
            continue
        
        # Process the neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Update the shortest distance
                heapq.heappush(priority_queue, (distance, neighbor))  # Push the neighbor into the queue
    
    return distances

# Example Graph as an Adjacency List
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def main():
    # Take user input for start node
    start_node = input("Enter the start node: ").upper()
    
    # Perform Dijkstra's Algorithm
    distances = dijkstra(graph, start_node)
    
    # Print the shortest distances from the start node to all other nodes
    print("\nShortest distances from node", start_node, ":")
    for node, distance in distances.items():
        print(f"Distance to {node}: {distance}")

if __name__ == "__main__":
    main()
