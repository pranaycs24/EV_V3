class Mapping:
    def __init__(self):
        self.demand_map = {}
        self.car_map = {}

    def add_car(self, demand, car, ts, tu):
        if not self.demand_map.has_key(demand):
            self.demand_map[demand] = []
        self.demand_map[demand].append([car, ts, tu])
        if not self.car_map.has_key(car):
            self.car_map[car] = []
        self.car_map[car].append([demand, ts, tu, 'R'])
