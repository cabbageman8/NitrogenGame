from math import pi, tau, sin, cos, tan, asin, acos, atan2, ceil, floor, sqrt, log
textures = [
            #special
            "None", "selection", "selectionbot", "cloud", "sky", "hole", "moon", "birds", "rain",
            #materials
            "water", "planks", "dirt", "farmland", "tiles", "weeds", "wall", "block", "hexpavers", "roughseedgrass",
            "stones", "lushundergrowth", "silkyoakdirt", "bottlebrushdirt", "wattledirt", "lawn", "sand", "freshwater",
            "glass", "eucalyptusdirt", "norfolkislandpinedirt", "wetdirt",
            #objects
            "grass", "treelog", "treestump", "treetrunk", "mushrooms", "rock", "sharprock", "crab",
            "fern", "silkyoak", "weepingbottlebrush", "weepingbottlebrushsapling", "norfolkislandpine", "cactus", "greencactus",
            "flytrap", "birchtreelog", "birchtreetrunk", "birchtreestump", "lillypad", "talldrygrass", "candle",
            "greymangrove", "silverwattle", "silverwattlesapling", "birdsnestfern", "papermulberry", "horsetailcasuarina", "horsetailcasuarinatrunk",
            "greymangrovetrunk", "greymangrovepropagules", "greymangrovesapling", "blacktreefern", "blacktreeferntrunk", "breadpalm", "tasmaniantreefern",
            "bluegumeucalyptus", "bluegumeucalyptussapling", "truemulga", "australiangrasstree", "australiangrasstreetrunk", "australiangrasstreelog",
            #crops
            "oatgrassseedling", "oatgrassfilling", "oatgrassmature", "oats", "oatmeal", "oatbread",
            "teabush", "teatree", "tealeaf",
            "chilibush", "chili", "chiliseeds",
            "coffeebush", "coffeetree", "coffeecherries", "coffeebeans",
            "artichoke", "artichokehead",
            "strawberryplant", "strawberry", "strawberryseeds",
            "soybeanseedling", "soybeanfilling", "soybeanmature", "soybeanmaturestem", "edamame", "soybeans",
            "cottonseedling", "cottonjointing", "cottonflowering", "cottonfilling", "cottonmature", "cottonseeds", "cottonbolls",
            "ricegrassseedling", "ricegrassfilling", "ricegrassmature", "rice",
            "barleygrassseedling", "barleygrassfilling", "barleygrassmature", "barley",
            #items
            "axe", "spade", "wood"
            ]

item_type_map = {0 :"Floor tile", 1 :"Object", 2 :"Item", 3 :"Roof tile"}

entities = ["charhands", "charhead", "charlegs"]
animated = {"water", "freshwater"}
difficult_terrain = {"water", "freshwater"}
any_dirt = [obj for obj in textures if "dirt" in obj]+["farmland",]

#          biome name, material lists
biomes = (("alpinetundra", (("sheoakdirt", "weeds", "stones"),)),
          ("steppe", (("lawn", "lushundergrowth", "weeds", "stones"),)),
          ("wetforest", (("freshwater", "weeds", "freshwater"), ("freshwater", "wetdirt", "freshwater"), ("freshwater", "silkyoakdirt", "freshwater") )),
          ("moistforest", (("freshwater", "weeds", "wetdirt", "weeds", "wetdirt"),)),
          ("desertscrub", (("dirt", "sand", "roughseedgrass"),)),
          ("dryforest", (("silkyoakdirt", "roughseedgrass"), ("wattledirt", "roughseedgrass"), ("bottlebrushdirt", "roughseedgrass"), ("norfolkislandpinedirt","norfolkislandpinedirt", "dirt", "roughseedgrass"), ("eucalyptusdirt", "roughseedgrass"))),
          ("thornwoodland", (("roughseedgrass", "dirt", "roughseedgrass"),)),
          ("desert", (("sand", "dirt"),)),
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
                 "height": 0.02
             },
             "ricegrassmature": {
                 "alias": "Rice Grass",
                 "drops": (4, "rice", 1),
                 "substrate": ("farmland", "freshwater"),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.07
             },
             "ricegrassfilling": {
                 "alias": "Rice Grass",
                 "becomes": "ricegrassmature",
                 "drops": None,
                 "substrate": ("farmland", "freshwater"),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "ricegrassseedling": {
                 "alias": "Rice Grass",
                 "becomes": "ricegrassfilling",
                 "drops": None,
                 "substrate": ("farmland", "freshwater"),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 1,
                 "height": 0.03
             },
             "rice": {
                 "alias": "Rice",
                 "becomes": "ricegrassseedling",
                 "drops": None,
                 "substrate": ("farmland", "freshwater"),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.01
             },
             "barleygrassmature": {
                 "alias": "Barley Grass",
                 "drops": (4, "barley", 1),
                 "substrate": ("farmland", ),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.07
             },
             "barleygrassfilling": {
                 "alias": "Barley Grass",
                 "becomes": "barleygrassmature",
                 "drops": None,
                 "substrate": ("farmland", ),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "barleygrassseedling": {
                 "alias": "Barley Grass",
                 "becomes": "barleygrassfilling",
                 "drops": None,
                 "substrate": ("farmland", ),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.03
             },
             "barley": {
                 "alias": "Barley",
                 "becomes": "barleygrassseedling",
                 "drops": None,
                 "substrate": ("farmland", ),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.01
             },
             "oatgrassmature": {
                 "alias": "Oat Grass",
                 "drops": (4, "oats", 1),
                 "substrate": ("farmland",),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "oatgrassfilling": {
                 "alias": "Oat Grass",
                 "becomes": "oatgrassmature",
                 "drops": None,
                 "substrate": ("farmland",),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "oatgrassseedling": {
                 "alias": "Oat Grass",
                 "becomes": "oatgrassfilling",
                 "drops": None,
                 "substrate": ("farmland",),
                 "moisture": (5, 50),
                 "temperiture": (5, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 1,
                 "height": 0.05
             },
             "oats": {
                 "becomes": "oatgrassseedling",
                 "drops": None,
                 "substrate": ("farmland",),
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
                 "substrate": ("farmland",),
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
                 "substrate": ("farmland",),
                 "moisture": (40, 100),
                 "temperiture": (30, 50),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 4,
                 "height": lambda x,y: 0.1+sin(x+y*y)/20
             },
             "coffeebush": {
                 "alias": "Coffee Bush",
                 "drops": None,
                 "becomes": "coffeetree",
                 "substrate": ("farmland",),
                 "moisture": (0, 40),
                 "temperiture": (30, 50),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "coffeetree": {
                 "alias": "Coffee Tree",
                 "drops": None,
                 "leaves": "coffeecherries",
                 "creates": (1, "coffeecherries"),
                 "substrate": ("farmland",),
                 "moisture": (0, 40),
                 "temperiture": (30, 50),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 4,
                 "height": lambda x,y: 0.1+sin(x+y*y)/20
             },
             "coffeecherries": {
                 "alias": "Coffee Cherries",
                 "description": "Fruit if the coffee plant, contains two coffee seeds",
                 "drops": None,
                 "becomes": "coffeebush",
                 "substrate": ("farmland",),
                 "moisture": (0, 40),
                 "temperiture": (30, 50),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.02
             },
             "chilibush": {
                 "alias": "Chilli Bush",
                 "creates": (2, "chili"),
                 "drops": None,
                 "substrate": ("farmland",),
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
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperiture": (30, 50),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.02
             },
             "strawberryplant": {
                 "alias": "Strawberry Plant",
                 "creates": (3, "strawberry"),
                 "drops": None,
                 "substrate": ("farmland",),
                 "moisture": (50, 100),
                 "temperiture": (20, 35),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 1,
                 "height": 0.02
             },
             "strawberryseeds": {
                 "alias": "Strawberry",
                 "drops": None,
                 "becomes": "strawberryplant",
                 "substrate": ("farmland",),
                 "moisture": (50, 100),
                 "temperiture": (20, 35),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.02
             },
             "soybeans": {
                 "drops": None,
                 "becomes": "soybeanseedling",
                 "substrate": ("farmland",),
                 "moisture": (50, 100),
                 "temperiture": (20, 35),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.02
             },
             "soybeanseedling": {
                 "drops": None,
                 "becomes": "soybeanfilling",
                 "substrate": ("farmland",),
                 "moisture": (50, 100),
                 "temperiture": (20, 35),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.04
             },
             "soybeanfilling": {
                 "drops": (4, "edamame", 2),
                 "becomes": "soybeanmature",
                 "substrate": ("farmland",),
                 "moisture": (50, 100),
                 "temperiture": (20, 35),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 2,
                 "height": 0.06
             },
             "soybeanmature": {
                 "drops": (12, "soybeans", 1),
                 "substrate": ("farmland",),
                 "moisture": (50, 100),
                 "temperiture": (20, 35),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "qtree",
                 "trunk": "soybeanmaturestem",
                 "size": 1,
                 "height": lambda x,y: 0.06+sin(x*+y*y)/50
             },
             "cottonseedling": {
                 "drops": None,
                 "becomes": "cottonjointing",
                 "substrate": ("farmland",),
                 "moisture": (50, 100),
                 "temperiture": (20, 35),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 0.5,
                 "height": 0.04
             },
             "cottonseeds": {
                 "drops": None,
                 "becomes": "cottonseedling",
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperiture": (25, 50),
                 "salinity": (0, 100),
                 "flags": {"plant", "flip"},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.01
             },
             "cottonjointing": {
                 "drops": None,
                 "becomes": "cottonflowering",
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperiture": (25, 50),
                 "salinity": (0, 100),
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 1,
                 "height": 0.03
             },
             "cottonflowering": {
                 "drops": None,
                 "becomes": "cottonfilling",
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperiture": (25, 50),
                 "salinity": (0, 100),
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 1,
                 "height": 0.03
             },
             "cottonfilling": {
                 "drops": None,
                 "leaves": "cottonseeds",
                 "becomes": "cottonmature",
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperiture": (25, 50),
                 "salinity": (0, 100),
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 1,
                 "height": 0.04
             },
             "cottonmature": {
                 "drops": (6, "cottonbolls", 2),
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperiture": (25, 50),
                 "salinity": (0, 100),
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 1,
                 "height": 0.05
             },
             "artichoke": {
                 "alias": "Artichoke",
                 "creates": (1, "artichokehead"),
                 "drops": None,
                 "substrate": ("farmland",),
                 "moisture": (30, 60),
                 "temperiture": (20, 30),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "artichokehead": {
                 "alias": "Artichoke Head",
                 "becomes": "artichoke",
                 "substrate": ("farmland",),
                 "moisture": (30, 60),
                 "temperiture": (20, 30),
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
                 "height": lambda x,y: 0.4+sin(x*+y*y)/15
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
             "silkyoak": {
                 "leaves": "treestump",
                 "drops": (4, "wood", 2),
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
                 "drops": (2, "wood", 2),
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
                 "drops": (6, "wood", 2),
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
                 "drops": (4, "wood", 2),
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
             "weepingbottlebrushsapling": {
                 "leaves": "treestump",
                 "drops": (1, "wood", 2),
                 "sheds": "bottlebrushdirt",
                 "substrate": ("bottlebrushdirt", ),
                 "moisture": (20, 75),
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 4,
                 "height": lambda x,y: 0.2+sin(x+y*y)/20
             },
             "norfolkislandpine": {
                 "leaves": "treestump",
                 "drops": (6, "wood", 2),
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
                 "drops": (3, "wood", 2),
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
                 "drops": (1, "wood", 2),
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
             "greymangrovesapling": {
                 "drops": (1, "wood", 2),
                 "substrate": ( "mangrovedirt", "dirt", "sand", "freshwater", "water", "roughseedgrass" ),
                 "moisture": (20, 50),
                 "temperiture": (15, 80),
                 "salinity": (90, 130),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "tree",
                 "trunk": "greymangrovetrunk",
                 "size": 4,
                 "height": lambda x,y: 0.075+sin(x+y*y)/20
             },
             "greymangrovepropagules": {
                 "drops": (1, "wood", 2),
                 "substrate": ( "mangrovedirt", "dirt", "sand", "freshwater", "water", "roughseedgrass" ),
                 "moisture": (20, 50),
                 "temperiture": (15, 80),
                 "salinity": (90, 130),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.1
             },
             "horsetailcasuarina": {
                 "drops": (1, "wood", 2),
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
                 "drops": (4, "wood", 2),
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
             "silverwattlesapling": {
                 "leaves": "treestump",
                 "drops": (4, "wood", 2),
                 "sheds": "wattledirt",
                 "substrate": ( "wattledirt", "roughseedgrass" ),
                 "moisture": (20, 80),
                 "temperiture": (15, 80),
                 "salinity": (0, 90),
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 4,
                 "height": lambda x,y: 0.2+sin(x+y*y)/20
             },
             "papermulberry": {
                 "leaves": "treestump",
                 "drops": (4, "wood", 2),
                 "substrate": ( "dirt" ),
                 "moisture": (10, 90),
                 "temperiture": (15, 60),
                 "salinity": (0, 80),
                 "flags": {"plant", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.3+sin(x+y*y)/20
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
            "planks": {
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
                 "drops": (1, "wood", 2),
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

ITEMS = {
            "sharprock": {
                 "alias": "Sharp Rock",
                 "description": "Sharper than other rocks",
            },
            "oatmeal": {
                 "alias": "Oatmeal",
                 "description": "Rolled oat seeds",
            },
            "oatbread": {
                 "alias": "Oatmeal Bread",
                 "description": "Delicous source of carbs",
            },
            "coffeebeans": {
                 "alias": "Coffee Beans",
                 "description": "Roasted seeds, high in caffeine",
            },
            "chiliseeds": {
                 "alias": "Chilli Seeds",
                 "description": "Used to grow chillies",
            },
            "strawberryseeds": {
                 "alias": "Strawberry Seeds",
                 "description": "Used to grow strawberries",
            }
}

TILES = {
            "planks": {
                 "alias": "Wooden Planks",
                 "description": "Used to build flooring, walls, and roofing",
            },
}

crafting = {
    (2, "sharprock", 2): {
        "materials": ((2, "rock", ),)},
    (1, "chiliseeds", 1): {
        "materials": ((4, "chili"), (1, "sharprock"))},
    (1, "strawberryseeds", 1): {
        "materials": ((3, "strawberry"), (1, "sharprock"))},
    (1, "oatmeal", 2): {
        "materials": ((4, "oats"), ),
        "workstation": (("windmill",), ("watermill", "water"))},
    (1, "oatbread", 2): {
        "materials": ((6, "oatmeal"), ),
        "workstation": (("oven",), ("campfire",))},
    (1, "coffeebeans", 2): {
        "materials": ((4, "coffeecherries"), (1, "rock")),
        "workstation": (("oven",), ("campfire",))},
    (1, "planks", 0): {
        "materials": ((4, "wood"),)},
    (1, "planks", 1): {
        "materials": ((8, "wood"),)},
    (2, "cottonseeds", 1): {
        "materials": ((1, "cottonbolls"),)},

}