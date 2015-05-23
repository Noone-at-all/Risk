#AI-only risk
#Beginning part, the risk classes

#A rough tile class
class Tile:
    def __init__(self, coords, faction = "none", unitCount = "0"):
        self.coords = coords #coords is a list, so that when printed it comes out as [x, y]
        self.faction = faction #A string, until more edits are made will only have the factions R, G, and B
        self.unitCount = unitCount #An integer, the number of units on this tile
    def __repr__(): 
        #If the tile is at (1,1) and has 10 red units on it
        #it will print "Tile [1,1] has 10 red units"
        print "Tile %s has %s %s units" % (self.coords, self.unitCount, self.faction)
