import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in raw_input().split()]
availableLinks = []
links = []
for i in xrange(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in raw_input().split()]
    availableLinks.append([])
for i in xrange(link_count):
    zone_1, zone_2 = [int(j) for j in raw_input().split()]
    links.append([zone_1, zone_2])
    availableLinks[zone_1].append(i)
    availableLinks[zone_2].append(i)
# game loop
while True:
    comm = ""
    my_platinum = int(raw_input())  # your available Platinum
    for i in xrange(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in raw_input().split()]
        if my_id == 0:
            my_pods = pods_p0
        else:
            my_pods = pods_p1
        if my_pods > 0:
            comm += str(my_pods)
            selectedLink = links[availableLinks[i][random.randrange(0, len(availableLinks[i]))]]
            if selectedLink[0] == i:
                comm += " " + str(selectedLink[0]) + " " + str(selectedLink[1]) + " "
            else:
                comm += " " + str(selectedLink[1]) + " " + str(selectedLink[0]) + " " 
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."


    # first line for movement commands, second line no longer used (see the protocol in the statement for details)

    print (comm)
    print "WAIT"
