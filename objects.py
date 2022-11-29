from math import pi, tau, sin, cos, tan, asin, acos, atan2, ceil, floor, sqrt, log
textures = [
            #special
            "None", "selection", "selectionbot", "cloud", "sky", "hole", "moon", "birds", "rain",
            #materials
            "seawater", "planks", "dirt", "farmland", "tiles", "weeds", "hexpavers", "roughseedgrass",
            "stones", "lushundergrowth", "silkyoakdirt", "bottlebrushdirt", "wattledirt", "lawn", "sand", "freshwater",
            "glass", "eucalyptusdirt", "norfolkislandpinedirt", "wetdirt", "banksiadirt", "mossdirt",
            #objects
            "grass", "treelog", "treestump", "treetrunk", "mushrooms", "rock", "crab",
            "fern", "silkyoak", "weepingbottlebrush", "weepingbottlebrushsapling", "norfolkislandpine", "cactus", "greencactus",
            "whitetreelog", "whitetreetrunk", "whitetreestump", "lillypad", "talldrygrass", "candle",
            "greymangrove", "silverwattle", "silverwattlesapling", "birdsnestfern", "papermulberry", "horsetailcasuarina", "horsetailcasuarinatrunk",
            "greymangrovetrunk", "greymangrovepropagules", "greymangrovesapling", "blacktreefern", "blacktreeferntrunk", "breadpalm", "tasmaniantreefern",
            "bluegumeucalyptus", "bluegumeucalyptussapling", "mulgabush", "mulgatree", "australiangrasstree", "australiangrasstreetrunk", "australiangrasstreelog",
            "sawtoothbanksiasapling", "sawtoothbanksia",
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
            "axe", "spade", "wood", "hoe", "sharprock", "leafrake"
            ]

item_type_map = {0 :"Floor tile", 1 :"Object", 2 :"Item", 3 :"Roof tile"}

entities = ["charhands", "charhead", "charlegs"]
animated = {"seawater", "freshwater"}
difficult_terrain = {"seawater", "freshwater"}
any_dirt = [obj for obj in textures if "dirt" in obj]+["farmland", "roughseedgrass"]
tools = ["axe", "sharprock", "spade", "hoe", "leafrake"]

#          biome name, material lists
biomes = (("alpinetundra", (("sheoakdirt", "mossdirt", "stones"),)),
          ("steppe", (("lawn", "lushundergrowth", "weeds", "stones"),)),
          ("wetforest", (("freshwater", "mossdirt", "freshwater"), ("freshwater", "wetdirt", "freshwater"), ("freshwater", "silkyoakdirt", "freshwater") )),
          ("moistforest", (("freshwater", "mossdirt", "wetdirt", "mossdirt", "wetdirt"),)),
          ("desertscrub", (("dirt", "sand", "roughseedgrass"),)),
          ("dryforest", (("silkyoakdirt", "roughseedgrass"), ("wattledirt", "roughseedgrass"), ("bottlebrushdirt", "roughseedgrass"), ("banksiadirt", "roughseedgrass"), ("norfolkislandpinedirt","norfolkislandpinedirt", "dirt", "roughseedgrass"), ("eucalyptusdirt", "roughseedgrass"))),
          ("thornwoodland", (("roughseedgrass", "dirt", "roughseedgrass"),)),
          ("desert", (("sand", "dirt"),)),
          ("sea", (("seawater", "stones"),("seawater", "sand"),)))

#            temp over humidity
biome_map = ((4, 3, 2, 1, 2, 0),# cold
             (5, 5, 4, 4, 3, 3),
             (7, 6, 5, 3, 3, 2),
             (7, 6, 6, 5, 5, 5))# hot
#             dry          wet

OBJ = {
             "grass": {
                 "alias": "Grass",
                 "drops": None,
                 "substrate": ["weeds", "roughseedgrass", "stones", "lushundergrowth", "lawn", "sand", "freshwater"]+any_dirt,
                 "moisture": (5, 100),
                 "nutreants": (10, 70),
                 "temperature": (0, 35),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (5, 30),
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
                 "temperature": (30, 50),
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
                 "temperature": (30, 50),
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
                 "temperature": (30, 50),
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
                 "temperature": (30, 50),
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
                 "temperature": (30, 50),
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
                 "temperature": (30, 50),
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
                 "temperature": (30, 50),
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
                 "temperature": (20, 35),
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
                 "temperature": (20, 35),
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
                 "temperature": (20, 35),
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
                 "temperature": (20, 35),
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
                 "temperature": (20, 35),
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
                 "temperature": (20, 35),
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
                 "temperature": (20, 35),
                 "salinity": (0, 50),
                 "flags": {"plant", "flip"},
                 "model": "singleshrub",
                 "size": 0.5,
                 "height": 0.04
             },
             "cottonseeds": {
                 "alias": "Cotton Seeds",
                 "drops": None,
                 "becomes": "cottonseedling",
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperature": (25, 50),
                 "salinity": (0, 100),
                 "flags": {"plant", "flip"},
                 "model": "singleobj",
                 "size": 1,
                 "height": 0.01
             },
             "cottonjointing": {
                 "alias": "Cotton (jointing)",
                 "drops": None,
                 "becomes": "cottonflowering",
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperature": (25, 50),
                 "salinity": (0, 100),
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 1,
                 "height": 0.03
             },
             "cottonflowering": {
                 "alias": "Cotton (flowering)",
                 "drops": None,
                 "becomes": "cottonfilling",
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperature": (25, 50),
                 "salinity": (0, 100),
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 1,
                 "height": 0.03
             },
             "cottonfilling": {
                 "alias": "Cotton (filling)",
                 "drops": None,
                 "leaves": "cottonseeds",
                 "becomes": "cottonmature",
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperature": (25, 50),
                 "salinity": (0, 100),
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 1,
                 "height": 0.04
             },
             "cottonmature": {
                 "alias": "Cotton (mature)",
                 "drops": (6, "cottonbolls", 2),
                 "substrate": ("farmland",),
                 "moisture": (10, 50),
                 "temperature": (25, 50),
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
                 "temperature": (20, 30),
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
                 "temperature": (20, 30),
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
                 "temperature": (10, 30),
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
                 "moisture": (40, 100),
                 "temperature": (20, 40),
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
                 "temperature": (20, 40),
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
                 "temperature": (0, 40),
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
                 "temperature": (0, 40),
                 "salinity": (0, 40),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "blacktreeferntrunk",
                 "size": 4,
                 "height": lambda x,y: 0.3+sin(x+y*y)/15
             },
             "australiangrasstree": {
                 "alias": "Australian Grass Tree",
                 "leaves": "australiangrasstreelog",
                 "drops": None,
                 "substrate": ["sand", "roughseedgrass",]+any_dirt,
                 "moisture": (5, 60),
                 "temperature": (10, 45),
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
             "mulgabush": {
                 "alias": "Mulga (bush)",
                 "drops": (2, "wood", 2),
                 "substrate": ["weeds", "roughseedgrass", "sand"]+any_dirt,
                 "moisture": (40, 90),
                 "nutreants": (10, 70),
                 "temperature": (30, 45),
                 "salinity": (0, 100),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "doubleshrub",
                 "size": 3,
                 "height": 0.1
             },
             "mulgatree": {
                 "alias": "Mulga (tree)",
                 "drops": (4, "wood", 2),
                 "substrate": ["weeds", "roughseedgrass", "sand"]+any_dirt,
                 "moisture": (40, 90),
                 "nutreants": (10, 70),
                 "temperature": (30, 45),
                 "salinity": (0, 100),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 6,
                 "height": lambda x,y: 0.3+sin(x+y*y)/20
             },
             "sawtoothbanksiasapling": {
                 "alias": "Sawtooth Banksia (sapling)",
                 "drops": (2, "wood", 2),
                 "substrate": ["banksiadirt",],
                 "moisture": (20, 90),
                 "nutreants": (10, 70),
                 "temperature": (15, 80),
                 "salinity": (0, 100),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 3,
                 "height": lambda x,y: 0.2+sin(x+y*y)/20
             },
             "sawtoothbanksia": {
                 "alias": "Sawtooth Banksia",
                 "leaves": "treestump",
                 "drops": (4, "wood", 2),
                 "substrate": ["banksiadirt",],
                 "moisture": (20, 90),
                 "nutreants": (10, 70),
                 "temperature": (15, 80),
                 "salinity": (0, 100),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 7,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "silkyoak": {
                 "alias": "Silky Oak",
                 "leaves": "treestump",
                 "drops": (4, "wood", 2),
                 "sheds": "silkyoakdirt",
                 "substrate": ("silkyoakdirt", ),
                 "moisture": (20, 75),
                 "nutreants": (20, 75),
                 "temperature": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "bluegumeucalyptussapling": {
                 "alias": "Bluegum Eucalyptus (sapling)",
                 #"becomes": "bluegumeucalyptus",
                 "drops": (2, "wood", 2),
                 "sheds": "eucalyptusdirt",
                 "substrate": ("eucalyptusdirt", "roughseedgrass"),
                 "moisture": (20, 75),
                 "temperature": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 4,
                 "height": lambda x,y: 0.3+sin(x+y*y)/20
             },
             "bluegumeucalyptus": {
                 "alias": "Bluegum Eucalyptus",
                 "leaves": "whitetreestump",
                 "drops": (6, "wood", 2),
                 "sheds": "eucalyptusdirt",
                 "substrate": ("eucalyptusdirt", "roughseedgrass"),
                 "moisture": (20, 75),
                 "temperature": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "doubletree",
                 "trunk": "whitetreetrunk",
                 "log": "whitetreelog",
                 "stump": "whitetreestump",
                 "size": 9,
                 "height": lambda x,y: 0.5+sin(x+y*y)/20
             },
             "weepingbottlebrush": {
                 "alias": "Weeping Bottlebrush",
                 "leaves": "treestump",
                 "drops": (4, "wood", 2),
                 "sheds": "bottlebrushdirt",
                 "substrate": ("bottlebrushdirt", ),
                 "moisture": (20, 75),
                 "nutreants": (20, 75),
                 "temperature": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "weepingbottlebrushsapling": {
                 "alias": "Weeping Bottlebrush (sapling)",
                 "leaves": "treestump",
                 "drops": (1, "wood", 2),
                 "sheds": "bottlebrushdirt",
                 "substrate": ("bottlebrushdirt", ),
                 "moisture": (20, 75),
                 "nutreants": (20, 75),
                 "temperature": (15, 80),
                 "salinity": (0, 90),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 4,
                 "height": lambda x,y: 0.2+sin(x+y*y)/20
             },
             "norfolkislandpine": {
                 "alias": "Norfolk Island Pine",
                 "leaves": "treestump",
                 "drops": (6, "wood", 2),
                 "sheds": "norfolkislandpinedirt",
                 "substrate": ("norfolkislandpinedirt", ),
                 "moisture": (20, 75),
                 "nutreants": (20, 75),
                 "temperature": (15, 80),
                 "salinity": (0, 120),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "doubletree",
                 "size": 8,
                 "height": lambda x,y: 0.5+sin(x+y*y)/20
             },
             "breadpalm": {
                 "alias": "Bread Palm",
                 "leaves": "treestump",
                 "drops": (3, "wood", 2),
                 "substrate": ("dirt", "weeds", "lushundergrowth", "sheoakdirt"),
                 "moisture": (40, 75),
                 "temperature": (30, 80),
                 "salinity": (0, 60),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.3+sin(x+y*y)/20
             },
             "greymangrove": {
                 "alias": "Grey Mangrove",
                 "drops": (1, "wood", 2),
                 "creates": (1, "greymangrovepropagules"),
                 "substrate": ( "mangrovedirt", "dirt", "sand", "freshwater", "seawater", "roughseedgrass", "stones" ),
                 "moisture": (20, 50),
                 "temperature": (15, 80),
                 "salinity": (90, 130),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "tree",
                 "trunk": "greymangrovetrunk",
                 "size": 8,
                 "height": lambda x,y: 0.1+sin(x+y*y)/20
             },
             "greymangrovesapling": {
                 "alias": "Grey Mangrove (sapling)",
                 "drops": (1, "wood", 2),
                 "substrate": ( "mangrovedirt", "dirt", "sand", "freshwater", "seawater", "roughseedgrass", "stones" ),
                 "moisture": (20, 50),
                 "temperature": (15, 80),
                 "salinity": (90, 130),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "tree",
                 "trunk": "greymangrovetrunk",
                 "size": 4,
                 "height": lambda x,y: 0.075+sin(x+y*y)/20
             },
             "greymangrovepropagules": {
                 "alias": "Grey Mangrove (propagules)",
                 "drops": (1, "wood", 2),
                 "substrate": ( "mangrovedirt", "dirt", "sand", "freshwater", "seawater", "roughseedgrass", "stones" ),
                 "moisture": (20, 50),
                 "temperature": (15, 80),
                 "salinity": (90, 130),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.1
             },
             "horsetailcasuarina": {
                 "alias": "Horsetail Casuarina",
                 "drops": (1, "wood", 2),
                 "substrate": ( "dirt", "sand", "sheoakdirt", "roughseedgrass" ),
                 "moisture": (20, 50),
                 "temperature": (15, 80),
                 "salinity": (60, 130),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "silverwattle": {
                 "alias": "Silver Wattle",
                 "leaves": "treestump",
                 "drops": (4, "wood", 2),
                 "sheds": "wattledirt",
                 "substrate": ( "wattledirt", "roughseedgrass" ),
                 "moisture": (20, 80),
                 "temperature": (15, 80),
                 "salinity": (0, 90),
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "silverwattlesapling": {
                 "alias": "Silver Wattle (sapling)",
                 "drops": (4, "wood", 2),
                 "sheds": "wattledirt",
                 "substrate": ( "wattledirt", "roughseedgrass" ),
                 "moisture": (20, 80),
                 "temperature": (15, 80),
                 "salinity": (0, 90),
                 "flags": {"plant", "native", "flip"},
                 "model": "tree",
                 "trunk": "horsetailcasuarinatrunk",
                 "size": 4,
                 "height": lambda x,y: 0.2+sin(x+y*y)/20
             },
             "papermulberry": {
                 "alias": "Paper Mulberry",
                 "leaves": "treestump",
                 "drops": (4, "wood", 2),
                 "substrate": ( "dirt" ),
                 "moisture": (10, 90),
                 "temperature": (15, 60),
                 "salinity": (0, 80),
                 "flags": {"plant", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.3+sin(x+y*y)/20
             },
             "cactus": {
                 "substrate": ("roughseedgrass", "sand"),
                 "moisture": (20, 60),
                 "temperature": (20, 50),
                 "salinity": (0, 100),
                 "lightlevel": "high",
                 "flags": {"plant", "flip", "solid"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.03
             },
             "lillypad": {
                 "substrate": ("freshwater", ),
                 "moisture": (50, 100),
                 "nutreants": (10, 60),
                 "temperature": (30, 40),
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
                 "temperature": (30, 45),
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
                 "temperature": (20, 50),
                 "salinity": (0, 50),
                 "lightlevel": "high",
                 "flags": {"plant", "flip", "solid"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.03
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
            "whitetreestump": {
                 "drops": (1, "wood", 2),
                 "flags": { "solid",},
                 "model": "doubleobj",
                 "bot": "whitetreelog",
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

ANY_TREE = [key for key, value in OBJ.items() if "tree" in value["model"]]

ITEMS = {
            "sharprock": {
                 "alias": "Sharp Rock",
                 "description": "Sharper than other rocks, can be used to cut trees",
            },
            "hoe": {
                 "alias": "Hoe",
                 "description": "Can till dirt into farmland",
            },
            "leafrake": {
                 "alias": "Leaf Rake",
                 "description": "Can clean up leaf litter",
            },
            "axe": {
                 "alias": "Axe",
                 "description": "Can cut trees without breaking",
            },
            "oatmeal": {
                 "alias": "Oatmeal",
                 "description": "Rolled oat seeds",
            },
            "oatbread": {
                 "alias": "Oatmeal Bread",
                 "description": "Delicous source of carbs",
            },
            "coffeecherries": {
                 "alias": "Coffee Cherries",
                 "description": "Used to grow Coffee Tree or roasted into Coffee Beans",
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
            },
            "tealeaf": {
                 "alias": "Tea Leaf",
                 "description": "Used to brew Tea",
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
    (1, "candle", 1): {
        "materials": ((1, "wood", ),)},
    (1, "hoe", 2): {
        "materials": ((1, "rock"), (4, "wood"),)},
    (1, "leafrake", 2): {
        "materials": ((8, "wood"),)},
    (1, "spade", 2): {
        "materials": ((8, "wood"),)},
    (1, "axe", 2): {
        "materials": ((1, "sharprock"), (4, "wood"),)},
    (1, "chiliseeds", 1): {
        "materials": ((4, "chili"), (1, "sharprock"))},
    (1, "strawberryseeds", 1): {
        "materials": ((3, "strawberry"), (1, "sharprock"))},
    (1, "oatmeal", 2): {
        "materials": ((4, "oats"), ),
        "workstation": (("windmill",), ("watermill", "seawater"))},
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
    (1, "planks", 3): {
        "materials": ((8, "wood"),)},
    (2, "cottonseeds", 1): {
        "materials": ((1, "cottonbolls"),)},

}