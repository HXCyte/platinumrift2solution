import sys
import math 
import random

# Class Zone represents a zone.
class Zone:
    def __init__ (self): # constructor
        self.owner = 0
        self.p0 = 0
        self.p1 = 0
        self.vis = 0
        self.plt = 0
    def upd(self, o, p1, p2, v, p): # update value
        self.owner = o
        self.p0 = p1
        self.p1 = p2
        self.vis = v
        self.plt = p

def strategy(my_pods, enemy_pods, z_id, neighbor): # strategy
    return 0

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
# zones: contains all information for zones
# neighborZones : ID of neighboring zones
player_count, my_id, zone_count, link_count = [int(i) for i in raw_input().split()]
zones = []
neighborZones = []
for i in xrange(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in raw_input().split()]
    zones.append(Zone())
    neighborZones.append([])
for i in xrange(link_count):
    zone_1, zone_2 = [int(j) for j in raw_input().split()]
    neighborZones[zone_1].append(zone_2)
    neighborZones[zone_2].append(zone_1)
    
# game loop
while True:
    comm = ""
    my_platinum = int(raw_input())  # your available Platinum
    for i in xrange(zone_count):
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in raw_input().split()]
        zones[z_id].upd(owner_id, pods_p0, pods_p1, visible, platinum)
        
    for i in xrange(zone_count):
        my_zone = zones[i]      # get zone
        if my_id == 0:          # owned pod in the zone
            my_pods = my_zone.p0
        else:
            my_pods = my_zone.p1
        if my_pods > 0:
            # execute command(s)
            comm += str(my_pods) + " "
            comm += str(i) + " "
            comm += str(neighborZones[i][random.randrange(len(neighborZones[i]))]) + " "

    print (comm)
    print "WAIT"
