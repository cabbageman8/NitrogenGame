from math import pi, tau, sin, cos, tan, asin, acos, atan2, ceil, floor, sqrt, log
textures = [
            #special
            "None", "selection", "selectionbot", "cloud", "sky", "hole", "moon",
            #materials
            "water", "planks", "dirt", "farmland", "tiles", "weeds", "wall", "block", "hexpavers", "roughseedgrass",
            "stones", "lushundergrowth", "silkyoakdirt", "bottlebrushdirt", "sheoakdirt", "wattledirt", "lawn", "fossil", "sand", "freshwater",
            "glass", "eucalyptusdirt", "norfolkislandpinedirt", "wetdirt",
            #objects
            "grass", "treelog", "treestump", "treetrunk", "basil", "mushrooms", "rock", "sharprock", "crab",
            "fern", "bush", "tarragon", "silkyoak", "weepingbottlebrush", "norfolkislandpine", "cactus", "greencactus",
            "flytrap", "birchtreelog", "birchtreetrunk", "birchtreestump", "lillypad", "talldrygrass", "candle",
            "greymangrove", "silverwattle", "birdsnestfern", "papermulberry", "horsetailcasuarina", "horsetailcasuarinatrunk",
            "greymangrovetrunk", "blacktreefern", "blacktreeferntrunk", "breadpalm", "tasmaniantreefern",
            "bluegumeucalyptus", "bluegumeucalyptussapling", "truemulga", "australiangrasstree", "australiangrasstreetrunk", "australiangrasstreelog",
            "oatgrass", "oats", "teabush", "teatree", "tealeaf", "chilibush",
            #items
            "axe", "spade", "chili", "chiliseeds", "wood", "oatmeal",
            ]

entities = ["charhands", "charhead", "charlegs"]
animated = {"water", "freshwater"}
difficult_terrain = {"water", "freshwater"}
any_dirt = [obj for obj in textures if "dirt" in obj]

#          biome name, material lists
biomes = (("alpinetundra", (("sheoakdirt", "weeds", "stones"),)),
          ("steppe", (("lawn", "lushundergrowth", "weeds", "stones"),)),
          ("wetforest", (("freshwater", "weeds", "freshwater"), ("freshwater", "wetdirt", "freshwater"), ("freshwater", "silkyoakdirt", "freshwater") )),
          ("moistforest", (("freshwater", "weeds", "wetdirt", "weeds", "wetdirt"),)),
          ("desertscrub", (("dirt", "sand", "roughseedgrass"),)),
          ("dryforest", (("silkyoakdirt", "roughseedgrass"), ("wattledirt", "roughseedgrass"), ("bottlebrushdirt", "roughseedgrass"), ("norfolkislandpinedirt","norfolkislandpinedirt", "dirt", "roughseedgrass"), ("eucalyptusdirt", "roughseedgrass"))),
          ("thornwoodland", (("roughseedgrass", "dirt", "roughseedgrass"),)),
          ("desert", (("sand", "fossil"),)),
          ("sea", (("water", "stones"),("water", "sand"),("water",),)))

#            temp over humidity
biome_map = ((4, 3, 2, 1, 2, 0),# cold
             (5, 5, 4, 4, 3, 3),
             (7, 6, 5, 3, 3, 2),
             (7, 6, 6, 5, 5, 5))# hot
#             dry          wet

OBJ = {
             "grass": {
                 "substrate": ["weeds", "roughseedgrass", "stones", "lushundergrowth", "lawn", "sand", "freshwater"]+any_dirt,
                 "moisture": (5, 100),
                 "nutreants": (10, 70),
                 "temperiture": (0, 35),
                 "salinity": (0, 100),
                 "lightlevel": "high",
                 "flags": {"plant", "native", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "basil": {
                 "substrate": ("dirt", "weeds", "lushundergrowth"),
                 "moisture": (5, 50),
                 "nutreants": (10, 70),
                 "temperiture": (20, 40),
                 "salinity": (0, 50),
                 "lightlevel": "high",
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "oatgrass": {
                 "alias": "Oat Grass",
                 "creates": (1, "oats"),
                 "drops": None,
                 "substrate": ("dirt", "weeds", "lushundergrowth", "farmland",),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "oats": {
                 "becomes": "oatgrass",
                 "drops": None,
                 "substrate": ("dirt", "weeds", "lushundergrowth", "farmland",),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.02
             },
             "teabush": {
                 "alias": "Tea Bush",
                 "becomes": "teatree",
                 "creates": (1,"tealeaf"),
                 "drops": (4, "tealeaf", 2),
                 "substrate": ("dirt", "weeds", "lushundergrowth", "farmland",),
                 "moisture": (40, 100),
                 "temperiture": (30, 50),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "teatree": {
                 "alias": "Tea Tree",
                 "leaves": "teabush",
                 "drops": (1, "teabush", 1),
                 "creates": (1, "tealeaf"),
                 "substrate": ("dirt", "weeds", "lushundergrowth", "farmland",),
                 "moisture": (40, 100),
                 "temperiture": (30, 50),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 4,
                 "height": lambda x,y: 0.1+sin(x+y*y)/20
             },
             "chilibush": {
                 "alias": "Chilli Bush",
                 "creates": (2, "chili"),
                 "drops": None,
                 "substrate": ("dirt", "weeds", "lushundergrowth", "farmland",),
                 "moisture": (10, 50),
                 "temperiture": (30, 50),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 1,
                 "height": 0.05
             },
             "chiliseeds": {
                 "alias": "Chilli Seeds",
                 "drops": None,
                 "becomes": "chilibush",
                 "substrate": ("dirt", "weeds", "lushundergrowth", "farmland",),
                 "moisture": (10, 50),
                 "temperiture": (30, 50),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.02
             },
             "mushrooms": {
                 "substrate": ["weeds", "lushundergrowth", "lawn", "farmland",]+any_dirt,
                 "moisture": (40, 100),
                 "nutreants": (0, 50),
                 "temperiture": (10, 30),
                 "salinity": (0, 50),
                 "lightlevel": "low",
                 "flags": {"plant", "native", "flip"},
                 "model": "singleshrub",
                 "size": 1,
                 "height": 0.01,
                 "lightemit": lambda t,x,y: (0.05+sin(t/600+x+y)*0.01, 0.02+sin(x+y)*0.02, 0.08+sin(t/600+x+y)*0.01)
             },
             "fern": {
                 "substrate": ["weeds", "lushundergrowth", "lawn"]+any_dirt,
                 "moisture": (40, 90),
                 "temperiture": (20, 40),
                 "salinity": (0, 50),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip"},
                 "model": "doubleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "birdsnestfern": {
                 "substrate": ["weeds", "lushundergrowth", "lawn"]+any_dirt,
                 "moisture": (40, 90),
                 "temperiture": (20, 40),
                 "salinity": (0, 50),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip"},
                 "model": "doubleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "blacktreefern": {
                 "substrate": ("wetdirt", "weeds", "lushundergrowth", "sheoakdirt"),
                 "moisture": (60, 100),
                 "temperiture": (0, 40),
                 "salinity": (0, 40),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "blacktreeferntrunk",
                 "size": 4,
                 "height": lambda x,y: 0.4+sin(x*+y*y)/5
             },
             "tasmaniantreefern": {
                 "substrate": ("wetdirt", "weeds", "lushundergrowth", "sheoakdirt"),
                 "moisture": (60, 100),
                 "temperiture": (0, 40),
                 "salinity": (0, 40),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "blacktreeferntrunk",
                 "size": 4,
                 "height": lambda x,y: 0.3+sin(x+y*y)/15
             },
             "australiangrasstree": {
                 "leaves": "australiangrasstreelog",
                 "drops": None,
                 "substrate": ["sand", "roughseedgrass",]+any_dirt,
                 "moisture": (5, 60),
                 "temperiture": (10, 45),
                 "salinity": (40, 80),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "qtree",
                 "trunk": "australiangrasstreetrunk",
                 "log": "australiangrasstreelog",
                 "stump": "australiangrasstreelog",
                 "size": 3,
                 "height": lambda x,y: 0.1+sin(x+y*y)/15
             },
             "truemulga": {
                 "substrate": ["weeds", "roughseedgrass",]+any_dirt,
                 "moisture": (40, 90),
                 "nutreants": (10, 70),
                 "temperiture": (30, 45),
                 "salinity": (0, 100),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "doubleshrub",
                 "size": 3,
                 "height": 0.1
             },
             "tarragon": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "silkyoakdirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (20, 50),
                 "nutreants": (50, 70),
                 "temperiture": (20, 40),
                 "salinity": (0, 60),
                 "lightlevel": "high",
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "silkyoak": {
                 "leaves": "treestump",
                 "drops": (4, "wood"),
                 "sheds": "silkyoakdirt",
                 "substrate": ("silkyoakdirt", ),
                 "moisture": (20, 75),
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "bluegumeucalyptussapling": {
                 #"becomes": "bluegumeucalyptus",
                 "drops": (2, "wood"),
                 "sheds": "eucalyptusdirt",
                 "substrate": ("eucalyptusdirt", "roughseedgrass"),
                 "moisture": (20, 75),
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 4,
                 "height": lambda x,y: 0.3+sin(x+y*y)/20
             },
             "bluegumeucalyptus": {
                 "leaves": "treestump",
                 "drops": (6, "wood"),
                 "sheds": "eucalyptusdirt",
                 "substrate": ("eucalyptusdirt", "roughseedgrass"),
                 "moisture": (20, 75),
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "doubletree",
                 "size": 9,
                 "height": lambda x,y: 0.5+sin(x+y*y)/20
             },
             "weepingbottlebrush": {
                 "leaves": "treestump",
                 "drops": (4, "wood"),
                 "sheds": "bottlebrushdirt",
                 "substrate": ("bottlebrushdirt", ),
                 "moisture": (20, 75),
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "norfolkislandpine": {
                 "leaves": "treestump",
                 "drops": (6, "wood"),
                 "sheds": "norfolkislandpinedirt",
                 "substrate": ("norfolkislandpinedirt", ),
                 "moisture": (20, 75),
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "salinity": (0, 120),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "doubletree",
                 "size": 8,
                 "height": lambda x,y: 0.5+sin(x+y*y)/20
             },
             "breadpalm": {
                 "leaves": "treestump",
                 "drops": (3, "wood"),
                 "substrate": ("dirt", "weeds", "lushundergrowth", "sheoakdirt"),
                 "moisture": (40, 75),
                 "temperiture": (30, 80),
                 "salinity": (0, 60),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.3+sin(x+y*y)/20
             },
             "greymangrove": {
                 "drops": (1, "wood"),
                 "substrate": ( "mangrovedirt", "dirt", "sand", "freshwater", "water", "roughseedgrass" ),
                 "moisture": (20, 50),
                 "temperiture": (15, 80),
                 "salinity": (90, 130),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "tree",
                 "trunk": "greymangrovetrunk",
                 "size": 8,
                 "height": lambda x,y: 0.1+sin(x+y*y)/20
             },
             "horsetailcasuarina": {
                 "drops": (1, "wood"),
                 "substrate": ( "dirt", "sand", "sheoakdirt", "roughseedgrass" ),
                 "moisture": (20, 50),
                 "temperiture": (15, 80),
                 "salinity": (60, 130),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "silverwattle": {
                 "leaves": "treestump",
                 "drops": (4, "wood"),
                 "sheds": "wattledirt",
                 "substrate": ( "wattledirt", "roughseedgrass" ),
                 "moisture": (20, 80),
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "papermulberry": {
                 "drops": (1, "wood"),
                 "substrate": ( "dirt" ),
                 "moisture": (10, 90),
                 "temperiture": (15, 60),
                 "salinity": (0, 80),
                 "flags": {"plant", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "cactus": {
                 "substrate": ("roughseedgrass", "sand"),
                 "moisture": (20, 60),
                 "temperiture": (20, 50),
                 "salinity": (0, 100),
                 "lightlevel": "high",
                 "flags": {"plant", "flip", "solid"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.03
             },
             "flytrap": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "silkyoakdirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (50, 90),
                 "nutreants": (10, 60),
                 "temperiture": (30, 40),
                 "salinity": (0, 40),
                 "lightlevel": "high",
                 "flags": {"plant", "flip", "slow"},
                 "model": "singleshrub",
                 "size": 1.5,
                 "height": 0.03
             },
             "lillypad": {
                 "substrate": ("freshwater", ),
                 "moisture": (50, 100),
                 "nutreants": (10, 60),
                 "temperiture": (30, 40),
                 "salinity": (0, 50),
                 "lightlevel": "high",
                 "flags": {"plant", "native", "flip"},
                 "model": "singleshrub",
                 "size": 1.5,
                 "height": 0.001
             },
             "talldrygrass": {
                 "substrate": ("dirt", "weeds", "roughseedgrass", "silkyoakdirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (0, 20),
                 "nutreants": (10, 70),
                 "temperiture": (30, 45),
                 "salinity": (0, 100),
                 "lightlevel": "high",
                 "flags": {"plant", "native", "flip"},
                 "model": "singleshrub",
                 "size": 1,
                 "height": 0.05
             },
            "greencactus": {
                 "substrate": ("roughseedgrass", "sand"),
                 "moisture": (10, 50),
                 "temperiture": (20, 50),
                 "salinity": (0, 50),
                 "lightlevel": "high",
                 "flags": {"plant", "flip", "solid"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.03
             },
            "wall": {
                 "flags": {"solid",},
                 "model": "block",
                 "size": 1,
                 "height": 0.1
             },
            "hexpavers": {
                 "flags": {"solid",},
                 "model": "block",
                 "size": 1,
                 "height": 0.1
             },
            "candle": {
                 "flags": {None,},
                 "model": "doubleobj",
                 "size": 1,
                 "height": 0.01,
                 "lightemit": lambda t,x,y: (0.08+(t/300+x/7+y/5)%1*0.02, 0.02+sin(x+y)*0.01, 0.0)
             },
            "rock": {
                 "substrate": ["roughseedgrass", "stones", "sand"]+any_dirt,
                 "flags": { "flip",},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.02
             },
            "crab": {
                 "substrate": ["stones", "sand"],
                 "salinity": (100, 200),
                 "flags": { "flip",},
                 "model": "singleshrub",
                 "size": 1,
                 "height": 0.02
             },
            "treestump": {
                 "drops": (1, "wood"),
                 "flags": { "solid",},
                 "model": "doubleobj",
                 "bot": "treelog",
                 "size": 1,
                 "height": 0.03
             },
            "australiangrasstreelog": {
                 "drops": None,
                 "flags": { "solid",},
                 "model": "doubleobj",
                 "size": 1,
                 "height": 0.02
             },
}

ITEMS ={
            "sharprock": {
                 "alias": "Sharp Rock",
                 "description": "Sharper than other rocks",
            }
}

crafting = {
    "sharprock" : ((2, "rock", ),),
    "chiliseeds" : ((4, "chili"), (1, "sharprock")),
    "oatmeal" : ((4, "oats"), (2, "rock", )),
}