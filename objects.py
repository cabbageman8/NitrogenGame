from math import pi, tau, sin, cos, tan, asin, acos, atan2, ceil, floor, sqrt, log
textures = [
            #special
            "None", "selection", "axe", "spade", "cloud", "sky", "hole", "moon",
            #materials
            "water", "planks", "dirt", "tiles", "weeds", "wall", "block", "hexpavers", "roughseedgrass",
            "stones", "lushundergrowth", "silkyoakdirt", "bottlebrushdirt", "sheoakdirt", "wattledirt", "lawn", "fossil", "sand", "freshwater",
            "glass", "eucalyptusdirt", "norfolkislandpinedirt", "wetdirt",
            #objects
            "grass", "treelog", "treestump", "treetrunk", "basil", "mushrooms",
            "fern", "bush", "tarragon", "silkyoak", "weepingbottlebrush", "norfolkislandpine", "cactus", "greencactus",
            "flytrap", "birchtreelog", "birchtreetrunk", "birchtreestump", "lillypad", "talldrygrass", "candle",
            "greymangrove", "silverwattle", "birdsnestfern", "papermulberry", "horsetailcasuarina", "horsetailcasuarinatrunk",
            "greymangrovetrunk", "blacktreefern", "blacktreeferntrunk", "breadpalm", "tasmaniantreefern", "bluegumeucalyptus", "truemulga", "australiangrasstree", "australiangrasstreetrunk", "australiangrasstreelog"
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
biome_map = ((4, 3, 2, 1, 1, 0),# cold
             (5, 5, 4, 4, 3, 3),
             (7, 6, 5, 3 , 3, 2),
             (6, 6, 6, 5, 5, 5))# hot
#             dry          wet

OBJ = {
             "grass": {
                 "substrate": ["weeds", "roughseedgrass", "stones", "lushundergrowth", "lawn", "sand", "freshwater"]+any_dirt,
                 "moisture": (5, 100),
                 "rootsize": "shallow",
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
                 "substrate": ("dirt", "weeds", "lushundergrowth", "silkyoakdirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (5, 50),
                 "rootsize": "moderate",
                 "nutreants": (10, 70),
                 "temperiture": (20, 40),
                 "salinity": (0, 50),
                 "lightlevel": "high",
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "mushrooms": {
                 "substrate": ["weeds", "lushundergrowth", "lawn"]+any_dirt,
                 "moisture": (40, 100),
                 "rootsize": "shallow",
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
                 "rootsize": "shallow",
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
                 "rootsize": "shallow",
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
                 "rootsize": "moderate",
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
                 "rootsize": "moderate",
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
                 "substrate": ["sand", "roughseedgrass",]+any_dirt,
                 "moisture": (5, 60),
                 "rootsize": "moderate",
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
                 "rootsize": "moderate",
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
                 "rootsize": "moderate",
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
                 "substrate": ("silkyoakdirt", ),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "creates": "silkyoakdirt",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "bluegumeucalyptus": {
                 "substrate": ("eucalyptusdirt", "roughseedgrass"),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "creates": "eucalyptusdirt",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.5+sin(x+y*y)/20
             },
             "weepingbottlebrush": {
                 "substrate": ("bottlebrushdirt", ),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "creates": "bottlebrushdirt",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "norfolkislandpine": {
                 "substrate": ("norfolkislandpinedirt", ),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "salinity": (0, 120),
                 "lightlevel": "any",
                 "creates": "sheoakdirt",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "doubletree",
                 "size": 8,
                 "height": lambda x,y: 0.5+sin(x+y*y)/20
             },
             "breadpalm": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "sheoakdirt"),
                 "moisture": (40, 75),
                 "rootsize": "deep",
                 "temperiture": (30, 80),
                 "salinity": (0, 60),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.3+sin(x+y*y)/20
             },
             "greymangrove": {
                 "substrate": ( "mangrovedirt", "dirt", "sand", "freshwater", "water", "roughseedgrass" ),
                 "moisture": (20, 50),
                 "rootsize": "deep",
                 "temperiture": (15, 80),
                 "salinity": (90, 130),
                 "lightlevel": "any",
                 "creates": "mangrovedirt",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "tree",
                 "trunk": "greymangrovetrunk",
                 "size": 8,
                 "height": lambda x,y: 0.1+sin(x+y*y)/20
             },
             "horsetailcasuarina": {
                 "substrate": ( "dirt", "sand", "sheoakdirt", "roughseedgrass" ),
                 "moisture": (20, 50),
                 "rootsize": "deep",
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
                 "substrate": ( "wattledirt", "roughseedgrass" ),
                 "moisture": (20, 80),
                 "rootsize": "deep",
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "creates": "wattledirt",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "papermulberry": {
                 "substrate": ( "dirt" ),
                 "moisture": (10, 90),
                 "rootsize": "deep",
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
                 "rootsize": "moderate",
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
                 "rootsize": "shallow",
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
                 "rootsize": "moderate",
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
                 "rootsize": "shallow",
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
                 "rootsize": "moderate",
                 "nutreants": (5, 70),
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
            "candle": {
                 "flags": {None,},
                 "model": "doubleobj",
                 "size": 1,
                 "height": 0.01,
                 "lightemit": lambda t,x,y: (0.08+(t/300+x/7+y/5)%1*0.02, 0.02+sin(x+y)*0.01, 0.0)
             },
}