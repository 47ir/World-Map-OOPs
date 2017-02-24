#WORLD MAP
import sys
class Room():
    def __init__(self, name, desc, N,S,E,W,NE,NW,SE,SW, items = None):
        self.name = name
        self.desc = desc
        self.north = N
        self.south = S
        self.east = E
        self.west  = W
        self.northeast = NE
        self.northwest = NW
        self.southeast = SE
        self.southwest = SW
        self.items = items
    def move(self, direction):
        global node
        node = globals()[getattr(self, direction)]
    #def loot_item(self, item):
        
ffg = Room('Fresno Fair Gate','You are at the entrance of the Fresno Fair.','log',None,None,None,None,None,None,None, 'Tickets')

log = Room('White Water Lodge Flume','There is a line of logs with two seats, floating on clear water.','ex','ffg','fb','ws',None,None,None,None)

ex = Room('Ex Scream Machine','There are 6 cars each capable of holding up to 4 people.','me','log',None, None,None,None,'tg',None)

me = Room('Music Express', 'There are four trailers, each one has an unforgettable size, scenery, lights, and music coming from the ride.',None,'ex',None,None,None,None,None,None)

tv = Room('The Viper', 'You see a humongous green viper themed ride with a giant arm holding two part seating clusters.','ppc','ws',None,None,None,None,None,None)

ws = Room('Wave Swinger', 'Over twenty chairs are hanging from chains connected to an enormous tower.', 'tv','cw','log','one',None,None,None,None)

one = Room('1001 Nachts','There is a platform ride that goes completely up and over in a circular fashion.','mg','tz','ws',None,None,None,None,None)

tz = Room('The Zipper','There are ten cages, each holding two passengers, connected to a vertically spinning tower.','one','cw',None,None,None,None,None,None)

cw = Room('Century Wheel', 'A sixty-seven foot tall ferris wheel slowly rotates.','ws',None,None,'tz',None,None,None,None)

mg = Room('Mardi Gras','A tall structure stands, with a variety of attractions inside.','tgc','one',None,None,None,None,None,None)

tgc = Room('The Grand Carousel','There is a thirty-eight foot carousel with thirty-six jumping horses and two chariots.',None,'mg',None,None,None,None,None,None)

rof = Room('Ring of Fire','There is a train of cars at the base of a huge loop.','ver','fl',None,'fb',None,None,None,None)

tg = Room('The Gravitron','You see a UFO shaped ride titled "Gravitron" that spins and flashes colorful lights.','gw','fb','ver',None,'ex',None,None,None)

ver = Room('Vertigo','There is a on-hundred foot tower with twenty-four seats hung by thin chains.','e16','rof',None,'tg',None,None,None,None)

e16 = Room('Eagle 16','A sixty foot ferris wheel stands tall and spins steadily.',None,'ver',None,None,None,None,None,'gw')

fl = Room('Footloose','There are two axe like structures that swing it\'s passengers.','rof',None,'gs','hof',None,None,None,None)

ppc = Room('Pole Position Coaster','A confusing track and a circular coaster make up this ride.',None,'tv',None,None,None,None,None,None)

gs = Room('Giant Scooters','There is a long track, twenty cars, smoke machines, music videos, and a 100 amp music system.','fb',None,None,'fl',None,None,None,None)

fb = Room('Fireball','An arm holding a cluster of seats swings vertically stands.','tg','gs','rof','log',None,None,None,None)

gw = Room('Giant Wheel','A huge ferris wheel turns slowly.',None,'tg',None,None,'e16',None,None,None)

hof = Room('The Hall of Mirrors','You see a complex maze of confusing mirrors that don\'t seem to lead anywhere.',None,None,'fl','m1',None,None,None,None)

m1 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.','m2','m7','hof','m6',None,None,None,None)

m2 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.','m3','m1',None,'m5',None,None,None,None)

m3 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.','m4','m2','m11',None,None,None,None,None)

m4 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.','de','m3',None,None,None,None,None,None)

m5 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.',None,None,'m2',None,None,None,None,None)

m6 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.',None,'m9','m1',None,None,None,None,None)

m7 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.','m1','m8','m9',None,None,None,None,None)

m8 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.','m7',None,None,'m10',None,None,None,None)

m9 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.','m6',None,None,'m7',None,None,None,None)

m10 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.',None,None,'m8',None,None,None,None,None)

m11 = Room('The Hall of Mirrors','There is a cracked mirror that seems to have a small room behind it.','m12','m13',None,'m3',None,None,None,None)

m12 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.',None,'m11','m14',None,None,None,None,None)

m13 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.','m11',None,None,None,None,None,None,None)

m14 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.',None,'m15',None,'m12',None,None,None,None)

m15 = Room('The Hall of Mirrors','You are on a path of confusing mirrors.','m14',None,'m16',None,None,None,None,None)

m16 = Room('The Hall of Mirrors','There seems to be a room titled "Maintenence" to the north.','bt','hof',None,'m15',None,None,None,None)

###########################

###########################

node = ffg
directions = ['north','west','south','east','up','down']
short_directions = ['n','w','s','e','u','d']
#controller
is_alive = True
while is_alive:
    print node.name
    print node.desc
    
    inp = raw_input('> ')
    if inp in ['q','quit','exit']:
        sys.exit(0)
    if inp in short_directions:
        inp = directions[short_directions.index(inp)]
        
    try:
        node.move(inp)
    except: 
        print 'You can\'t do that.'