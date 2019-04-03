class CityNetwork:
    def __init__(self):
        self.g = {}
        self.ch_port = {}

    def add_edge(self, vertex, destination, weight, ports=-1):
        if not self.g.has_key(vertex):
            self.g[vertex] = []
            if ports != -1:
                self.ch_port[vertex] = ports
        self.g[vertex].append((destination, weight))

    def add_network(self, g):
        self.g.update(g)

    def add_ports(self, vertex, ports):
        self.ch_port[vertex] = ports

    def add_multi_ports(self, network={}):
        self.ch_port.update(network)
