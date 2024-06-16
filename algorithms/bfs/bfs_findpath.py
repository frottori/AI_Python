from collections import deque

# Ορισμός του γράφου ως λεξικό λιστών
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['E']
}

# Ορισμός της συνάρτησης BFS για να επιστρέφει το συντομότερο μονοπάτι
def bfs_shortest_path(graph, start, end):
    # Δημιουργία ουράς για το BFS
    queue = deque()
    # Εισαγωγή του κόμβου εκκίνησης και της απόστασής του
    queue.append(([start], 0))
    # Δημιουργία συνόλου για να κρατάμε τους επισκεπτόμενους κόμβους
    visited = set()
    # Επανάληψη μέχρι η ουρά να είναι άδεια
    while queue:
        # Αφαίρεση του μονοπατιού και της απόστασής του από την αρχή της ουράς
        print(queue)
        path, distance = queue.popleft()
        print (path, distance)
        print(queue)
        # Πάρτε τον τελευταίο κόμβο στο μονοπάτι
        node = path[-1]
        # Αν ο κόμβος είναι ο κόμβος προορισμού, επιστροφή του μονοπατιού και της απόστασης του
        if node == end:
            return (path, distance)
        # Αν ο κόμβος δεν έχει επισκεφθεί, σημειώνεται ως επισκεπτόμενος
        if node not in visited:
            visited.add(node)
            print(visited)
            # Εισαγωγή όλων των γειτόνων του κόμβου στην ουρά με τα μονοπάτια τους
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append((new_path, distance + 1))
                print(new_path, distance + 1)
    # Αν ο κόμβος προορισμού δεν είναι προσβάσιμος, επιστροφή None
    return None

# Εκτέλεση της συνάρτησης BFS για να εκτυπώσει το συντομότερο μονοπάτι
start = 'A'
end = 'F'
path = bfs_shortest_path(graph, start, end)
if path:
    print(f"Το συντομότερο μονοπάτι από τον κόμβο {start} στον κόμβο {end} είναι {' -> '.join(path[0])}, Απόσταση: {path[1]}")
else:
    print(f"Ο κόμβος {end} δεν είναι προσβάσιμος από τον κόμβο {start}")
