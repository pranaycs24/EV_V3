class DemandCar:
    def __init__(self):
        pass
        self.demand = {}

    def add_demand(self, demand_info, demand_node=-1):
        if demand_node != -1:
            self.demand[demand_node] = demand_info
        else:
            self.demand.update(demand_info)

    def number_demand(self, demand_node):
        return len(self.demand[demand_node])

    def number_demand_time(self, time):
        """

        :rtype: int
        """
        count = 0
        for key, value in self.demand.iteritems():
            for x in value:
                if x[1] == time:
                    count += 1
        return count
