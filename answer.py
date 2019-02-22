import sys
import math 
import random

# Class Zone represents a zone.
class Zone:
    def __init__ (self): # constructor
        self.owner = 0 # ID of the zone's owner
        self.mp = 0 # number of player's pod
        self.ep = 0 # number of enemy pod
        self.vis = 0 # visibility of the zone
        self.plt = 0 # number of platinum sources
        self.visited = 0 # higher value means the zone has been visited recently
    def upd(self, o, p0, p1, v, p, my_id): # update value
        self.owner = o
        self.vis = v
        self.plt = p
        if my_id == 0:
            self.mp = p0
            self.ep = p1
        else:
            self.mp = p1
            self.ep = p0
        if self.visit > 0:
            self.visited -= 1
    def visit(self): # mark zone as visited
        self.visited = random.randrange(3, 6)
        
def strategy(my_id, enemy_id, my_pods, enemy_pods, z_id, neighbor): # strategy
    # favored zones and how much they are favored
    mfavored_zone1 = -1 
    mfavored_zone2 = -1
    mfavor_value1 = -1000
    mfavor_value2 = -1000
    # eff_pods: pods to move
    # pod_split: if true, pods in the zone splits in 
    # two teams and go to two different zones
    eff_pods = my_pods
    pod_split = False
    comm = ""
    # pods have a chance to split if there are more than 20 of them
    if my_pods > 20 and len(neighbor) > 1 and random.randrange(100) > 90:
        pod_split = True
        eff_pods = my_pods // 2
    # check if the neighboring zones are favored
    for z in neighbor:
        nz = zones[z]
        favor_value = 0
        # pods will most likely go to neutral/enemy zones with platinums
        if nz.plt > 0 and nz.owner != my_id:
            favor_value += nz.plt * 10
        # pods prefer to capture neutral/enemy zones
        if nz.owner == enemy_id:
            favor_value += 20
        if nz.owner == -1:
            favor_value += 10
        #if nz.mp > 0:
            #favor_value += 5
        # pods will confront enemy pods if they outnumber the enemy pods
        if nz.ep > 0:
            favor_value += (eff_pods - nz.ep) * 2
        # pods do not feel like going to recently visited zones
        if nz.visited > 0:
            favor_value -= nz.visited * 5
        # checks if this zone is the most favored one
        if favor_value > mfavor_value1:
            mfavor_value2 = mfavor_value1
            mfavor_value1 = favor_value
            mfavored_zone2 = mfavored_zone1
            mfavored_zone1 = z
        elif favor_value == mfavor_value1 and random.randrange(100) > 50:
            mfavor_value2 = mfavor_value1
            mfavor_value1 = favor_value
            mfavored_zone2 = mfavored_zone1
            mfavored_zone1 = z
    
    # output
    if pod_split:
        comm += str(eff_pods) + " "
        comm += str(z_id) + " "
        comm += str(mfavored_zone1) + " "
        zones[mfavored_zone1].visit()
        comm += str(my_pods - eff_pods) + " "
        comm += str(z_id) + " "
        comm += str(mfavored_zone2) + " "
        zones[mfavored_zone2].visit()
    elif my_pods > 0:
        comm += str(my_pods) + " "
        comm += str(z_id) + " "
        comm += str(mfavored_zone1) + " "
        zones[mfavored_zone1].visit()
    return comm
        
# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
# zones: contains all information for zones
# neighborZones : ID of neighboring zones
player_count, my_id, zone_count, link_count = [int(i) for i in raw_input().split()]
enemy_id = 1 - my_id
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
    # get zones data
    for i in xrange(zone_count):
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in raw_input().split()]
        zones[z_id].upd(owner_id, pods_p0, pods_p1, visible, platinum, my_id)
    # move pods in every zone
    for i in xrange(zone_count):
        my_zone = zones[i]      # get zone
        my_pods = my_zone.mp
        enemy_pods = my_zone.ep
        if my_pods > 0:
            comm += strategy(my_id, enemy_id, my_pods, enemy_pods, i, neighborZones[i]) # apply strategy

    print (comm)
    print "WAIT"
