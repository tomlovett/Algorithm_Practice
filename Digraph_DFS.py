# build nodes, edges, digraph

# build DFS; add dynamic programming
# two-way graph

class Digraph(object):
	def __init__(self):
		self.nodes = []
		self.all_paths     = {}
		self.optimum_paths = {}

	def add_node(self, node):
		self.nodes.append(node)

	def add_edge(self, node_a, node_b, edge):
		node_a.edges[node_b.name] = edge
		node_b.edges[node_a.name] = edge

	def depth_first_search(self, src, dest, path):
		if src == dest:
			return path
			# record path
		for child in src.edges:
			print child
			if child in path:
				continue
			path.append(child)
			# total_weight  += src.edges[child].weight
			# total_outside += src.edges[child].outside_weight
			self.depth_first_search(child, dest, path)
			path.pop()
		return 		# redundant? 

	def record_path(self, path):
		src  = path[0]
		dest = path[-1]
		if (src, dest) in self.paths:
			other = self.paths

class Node(object):
	def __init__(self, name):
		self.name  = str(name)
		self.edges = {}

class Edge(object):
	def __init__(self, outside_weight, weight):
		self.weight         = weight
		self.outside_weight = outside_weight

class Path(object):
	def __init__(self, src, dest):
		self.src  = src
		self.dest = dest
		self.weight         = weight
		self.outside_weight = outside_weight
