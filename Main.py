from collections import defaultdict
from math import ceil, floor

from data_str import CityNetwork
from data_str.DemandCar import DemandCar
from data_str.Mapping import Mapping
from heapq import *


# from ortools.constraint_solver import pywrapcp


def d_sort(graph, f, t, wait_time, d_t, carc):
    g = defaultdict(list)
    for key, value in graph.items():
        for r, c in graph[key]:
            g[key].append((c, r))

    q, seen, mins = [(d_t, f, (), 0)], set(), {f: 0}
    elapsed = {f: 0}

    while q:
        (cost, v1, path, wt) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = ([v1, cost], path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                print str(path) + " " + str(v2)
                next = cost + c / 4
                print next
                wt_time = 0
                if wait_time[v2][0] <= next <= wait_time[v2][1]:
                    dis = (next - elapsed[v1]) * 4 + min(g.get(v2, ()), key=lambda first: first[0])[0]
                    print "Cummulative waiting time " + str(elapsed[v1]) + " " + str(v2)+" "+str(v1)
                    # if dis > carc:
                    # print "Path: " + str(path) + "  " + str(v1)
                    wt_time = wait_time[v2][1] - next
                    print wt_time
                    if wt_time>wt:
                            print "cost "+str(cost)
                            wt_time -= floor((((cost - elapsed[v1]) * 4) % carc) / 3)
                            wt_time=max(wt_time, 0)

                next += wt_time
                # print next
                if prev is None or next < prev:
                    mins[v2] = next
                    elapsed[v2] = elapsed[v1] + wt_time
                    heappush(q, (next, v2, path, wt_time))
        print elapsed
    return float("inf")


d = DemandCar()
d.add_demand([(2, 0), (5, 1), (6, 1)], 1)
di = {2: [(5, 0), (6, 1)]}
d.add_demand(di)

print d.number_demand(2)
print d.number_demand_time(1)

cn = CityNetwork.CityNetwork()
cn.add_edge(1, 5, 32)
cn.add_edge(1, 7, 67)
cn.add_edge(2, 6, 90)
cn.add_network({3: [(2, 6), (6, 9)], 4: [(7, 8)]})
print cn.g

cn.add_multi_ports({1: 3, 2: 5})
cn.add_ports(6, 5)

print cn.ch_port

m = Mapping()
m.add_car('D1', 'C1', 0, 10)
print m.demand_map
print m.car_map

graph = {0: [(1, 32), (2, 12)], 1: [(4, 12)], 2: [(3, 16)], 3: [(4, 20)]}
wait_time = [(0, 0), (8, 12), (0, 0), (7, 12), (0, 0)]
d_t = 0
print 'x'
p = d_sort(graph, 0, 4, wait_time, d_t, 33)
print p
a = []

while p:
    a.append(p[0])
    p = p[1]
a = a[1:]
x= [0]*len(a)
i=0
for x1 in a:
    x[i]=x1[0]
    i+=1
x.reverse()
print x[0]
