
def add_edge(adj, src, dest):

	adj[src].append(dest);
	adj[dest].append(src);


def BFS(adj, src, dest, v, pred, dist):

	
	queue = []

	
	visited = [False for i in range(v)];

	
	for i in range(v):

		dist[i] = 1000000
		pred[i] = -1;
	
	
	visited[src] = True;
	dist[src] = 0;
	queue.append(src);

	# standard BFS algorithm
	while (len(queue) != 0):
		u = queue[0];
		queue.pop(0);
		for i in range(len(adj[u])):
		
			if (visited[adj[u][i]] == False):
				visited[adj[u][i]] = True;
				dist[adj[u][i]] = dist[u] + 1;
				pred[adj[u][i]] = u;
				queue.append(adj[u][i]);

				# We stop BFS when we find
				# destination.
				if (adj[u][i] == dest):
					return True;

	return False;


def printShortestDistance(adj, s, dest, v):
	
	
	pred=[0 for i in range(v)]
	dist=[0 for i in range(v)];

	if (BFS(adj, s, dest, v, pred, dist) == False):
		print("Given source and destination are not connected")

	# vector path stores the shortest path
	path = []
	crawl = dest;
	path.append(crawl);
	
	while (pred[crawl] != -1):
		path.append(pred[crawl]);
		crawl = pred[crawl];
	

	# distance from source is in distance array
	print("Shortest path length is : " + str(dist[dest]), end = '')

	# printing path from source to destination
	print("\nPath is : : ")
	
	for i in range(len(path)-1, -1, -1):
		print(path[i], end=' ')
		
# Driver program to test above functions
if __name__=='__main__':
	
	# no. of vertices
	v = 8;

	# array of vectors is used to store the graph
	# in the form of an adjacency list
	adj = [[] for i in range(v)];

	# Creating graph given in the above diagram.
	# add_edge function takes adjacency list, source
	# and destination vertex as argument and forms
	# an edge between them.
	add_edge(adj, 0, 1);
	add_edge(adj, 0, 3);
	add_edge(adj, 1, 2);
	add_edge(adj, 3, 4);
	add_edge(adj, 3, 7);
	add_edge(adj, 4, 5);
	add_edge(adj, 4, 6);
	add_edge(adj, 4, 7);
	add_edge(adj, 5, 6);
	add_edge(adj, 6, 7);
	source = 0
	dest = 7
	printShortestDistance(adj, source, dest, v)


