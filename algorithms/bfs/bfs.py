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

# Ορισμός της συνάρτησης BFS
def bfs(graph, start, end):
    # Δημιουργία ουράς για το BFS
    queue = deque()
    # Εισαγωγή του κόμβου εκκίνησης και της απόστασής του
    queue.append((start, 0))
    # Δημιουργία συνόλου για να κρατάμε τους επισκεπτόμενους κόμβους
    visited = set()
    # Επανάληψη μέχρι η ουρά να είναι άδεια
    while queue:
        # Αφαίρεση του κόμβου και της απόστασής του από την αρχή της ουράς
        print(f"Ουρά: {queue}")
        node, distance = queue.popleft()
        print(f"Επισκέπτομαι τον κόμβο {node} σε απόσταση {distance}")
        print(f"ουρά: {queue}")
        # Αν ο κόμβος είναι ο κόμβος προορισμού, επιστροφή της απόστασης
        if node == end:
            return distance
        # Αν ο κόμβος δεν έχει επισκεφθεί, σημειώνεται ως επισκεπτόμενος
        if node not in visited:
            visited.add(node)
            print(f"Οι επισκεπτόμενοι κόμβοι είναι {visited}")
            # Εισαγωγή όλων των γειτόνων του κόμβου στην ουρά
            for neighbor in graph[node]:
                queue.append((neighbor, distance + 1))
                print(f"Εισάγω στην ουρά τον γείτονα {neighbor} σε απόσταση {distance + 1}")
    # Αν ο κόμβος προορισμού δεν είναι προσβάσιμος, επιστροφή -1
    return -1

# Εκτέλεση της συνάρτησης BFS
start = 'A'
end = 'F'
distance = bfs(graph, start, end)
if distance != -1:
    print(f"Η συντομότερη απόσταση ανάμεσα σε {start} και {end} είναι {distance}")
else:
    print(f"Ο κόμβος {end} δεν είναι προσβάσιμος από τον κόμβο {start}")