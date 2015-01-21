# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    # your code here
	res = []
    path = graph[0]
    graph.remove(path)
    res.append(path[0])
    res.append(path[1])
    while(len(graph) > 0):
        l = len(res)

        
    return res

graph = [(1, 2), (2, 3), (3, 1)]
print find_eulerian_tour(graph)
