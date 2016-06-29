# build nodes, edges, digraph

# build DFS; add dynamic programming
# two-way graph

class Digraph(object):
	def __init__(self):
		self.nodes = {}
		self.all_paths     = {}
		self.optimum_paths = {}

	def add_node(self, node):
		self.nodes[node.name] = node

	def add_edge(self, node_a, node_b, edge):
		node_a.edges[node_b.name] = edge  # assigning weight instead
		node_b.edges[node_a.name] = edge

	def calc_weight(self, path):
		if len(path) < 2:
			return 0
		weight = 0
		for i in range(len(path)-1):
			src, dest = path[i], path[i+1]
			edge = src.edges[dest]
			weight += edge.weight
		return weight

	def depth_first_search(self, src, dest, path, max_total):
		if (src, dest) in self.memo:
			return self.memo[(src, dest)]
		elif src == dest:
			return path

		weight = self.calc_weight(path) # ready to expand to outside weight
		if weight > max_total:
			return

		trials = []
		for child in src.edges:
			if child in path:
				continue
			path.append(child)
			if self.depth_first_search(child, dest, path):
				trials.append(path)
			path.pop()

		if len(trials) > 0:
			shortest = trials[0]
			for other in trials:
				if self.calc_weight(other) < self.calc_weight(shortest):
					shortest = other
			self.memo[(src, dest)] = shortest
			# careful, it might go around
				# there may be a faster way that utilizes a node already in the path?
				# my brain is farting
			return shortest
		else:
			return

class Node(object):
	def __init__(self, name):
		self.name  = str(name)
		self.edges = {}

class Edge(object):
	def __init__(self, weight, outside_weight=0):
		self.weight         = weight
		# self.outside_weight = outside_weight

