tube_network = {
    "Hammersmith": ["Goldhawk Road"],
    "Goldhawk Road": ["Hammersmith", "Shepherd's Bush Market"],
    "Shepherd's Bush Market": ["Goldhawk Road", "Wood Lane"],
    "Wood Lane": ["Shepherd's Bush Market", "Latimer Road"],
    "Latimer Road": ["Wood Lane", "Ladbroke Grove"],
    "Ladbroke Grove": ["Latimer Road", "Westbourne Park"],
    "Westbourne Park": ["Ladbroke Grove", "Royal Oak"],
    "Royal Oak": ["Westbourne Park", "Paddington (Suburban)"],
    "Paddington (Suburban)": ["Royal Oak", "Paddington (Praed Street)", "Edgware Road"],
    "Paddington (Praed Street)": ["Paddington (Suburban)", "Bayswater"],
    "Bayswater": ["Paddington (Praed Street)", "Notting Hill Gate"],
    "Notting Hill Gate": ["Bayswater", "High Street Kensington"],
    "High Street Kensington": ["Notting Hill Gate", "Gloucester Road"],
    "Gloucester Road": ["High Street Kensington", "South Kensington"],
    "South Kensington": ["Gloucester Road", "Sloane Square"],
    "Sloane Square": ["South Kensington", "Victoria"],
    "Victoria": ["Sloane Square", "St James's Park"],
    "St James's Park": ["Victoria", "Westminster"],
    "Westminster": ["St James's Park", "Embankment"],
    "Embankment": ["Westminster", "Temple"],
    "Temple": ["Embankment", "Blackfriars"],
    "Blackfriars": ["Temple", "Mansion House"],
    "Mansion House": ["Blackfriars", "Cannon Street"],
    "Cannon Street": ["Mansion House", "Monument"],
    "Monument": ["Cannon Street", "Tower Hill"],
    "Tower Hill": ["Monument", "Aldgate"],
    "Aldgate": ["Tower Hill", "Liverpool Street"],
    "Liverpool Street": ["Aldgate", "Moorgate"],
    "Moorgate": ["Liverpool Street", "Barbican"],
    "Barbican": ["Moorgate", "Farringdon"],
    "Farringdon": ["Barbican", "King's Cross"],
    "King's Cross": ["Farringdon", "Euston Square"],
    "Euston Square": ["King's Cross", "Great Portland Street"],
    "Great Portland Street": ["Euston Square", "Baker Street"],
    "Baker Street": ["Great Portland Street", "Edgware Road"],
    "Edgware Road": ["Baker Street", "Paddington (Suburban)", "Paddington (Praed Street)"],
    "Amersham": ["Chalfont & Latimer"],
    "Chalfont & Latimer": ["Chesham", "Amersham", "Chorleywood"],
    "Chorleywood": ["Chalfont & Latimer", "Rickmansworth"],
    "Rickmansworth": ["Moor Park"],
    "Moor Park": ["Croxley", "Rickmansworth", "Northwood"],
    "Croxley": ["Watford", "Moor Park"],
    "Watford": ["Croxley"],
    "Northwood": ["Moor Park", "Northwood Hills"],
    "Northwood Hills": ["Northwood", "Pinner"],
    "Pinner": ["Northwood Hills", "North Harrow"],
    "North Harrow": ["Pinner", "Harrow-on-the-Hill"],
    "Harrow-on-the-Hill": ["North Harrow", "Northwick Park", "West Harrow"],
    "West Harrow": ["Rayners Lane", "Harrow-on-the-Hill"],
    "Rayners Lane": ["Eastcote", "West Harrow"],
    "Eastcote": ["Ruislip Manor", "Rayners Lane"],
    "Ruislip Manor": ["Ruislip", "Eastcote"],
    "Ruislip": ["Ickenham", "Ruislip Manor"],
    "Ickenham": ["Hillingdon", "Ruislip"],
    "Hillingdon": ["Uxbridge", "Ickenham"],
    "Uxbridge": ["Hillingdon"],
    "Northwick Park": ["Harrow-on-the-Hill", "Preston Road"],
    "Preston Road": ["Northwick Park", "Wembley Park"],
    "Wembley Park": ["Preston Road", "Finchley Road"],
    "Finchley Road": ["Wembley Park", "Baker Street"],
    "Baker Street": ["Finchley Road", "Euston Square"],
    "Euston Square": ["Great Portland Street", "King's Cross"],
    "King's Cross": ["Euston Square", "Farringdon"],
    "Farringdon": ["King's Cross", "Barbican"],
    "Barbican": ["Farringdon", "Moorgate"],
    "Moorgate": ["Barbican", "Aldgate"], 
    "Aldgate": ["Moorgate"],
}

# Example usage:
start_station = "Tower Hill"
goal_station = "Notting Hill Gate"


def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == goal:
        return path

    for station in graph[start]:
        if station not in path:
            new_path = dfs(graph, station, goal, path)
            if new_path:
                return new_path

    return None

result_path_dfs = dfs(tube_network, start_station, goal_station)

if result_path_dfs:
    print(f"DFS path from {start_station} to {goal_station}: {result_path_dfs}")
else:
    print(f"No path found from {start_station} to {goal_station}")

#BFS

def bfs(graph, start, goal):
        queue = [[start]]
        visited = set()

        while queue: 
                #Gets the first path in the queue
                path = queue.pop(0)

                #Gets the last node in the path
                vertex = path[-1]

                #Checks if arrived at the end
                if vertex == goal:
                    return path
                #Checks to see if current node has already been visited 
                elif vertex not in visited: 
                        #enumerate all adjacent nodes, 
                        #costruct a new path, and push it into the queue
                        for current_neighbour in graph.get(vertex, []):
                             new_path = list(path)
                             new_path.append(current_neighbour)
                             queue.append(new_path)

                             #Marks vertex as visited
                             visited.add(vertex)
       
result_path_bfs = bfs(tube_network, start_station, goal_station)

if result_path_bfs:
    print(f"BFS path from {start_station} to {goal_station}: {result_path_bfs}")
else:
    print(f"No path found from {start_station} to {goal_station}")
