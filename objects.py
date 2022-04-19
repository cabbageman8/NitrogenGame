from math import pi, tau, sin, cos, tan, asin, acos, atan2, ceil, floor, sqrt, log
textures = [
            #special
            "None", "selection", "axe", "spade", "cloud", "sky", "hole",
            #materials
            "water", "planks", "dirt", "tiles", "weeds", "wall", "block", "hexpavers", "roughseedgrass",
            "stones", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn", "fossil", "sand", "freshwater",
            "glass",
            #objects
            "grass", "deadtree", "normaltree", "treelog", "treestump", "treetrunk", "basil", "mushrooms",
            "fern", "bush", "tarragon", "gravilearobustatree", "bottlebrushtree", "sheoaktree", "cactus", "greencactus",
            "flytrap", "birchtreelog", "birchtreetrunk", "birchtreestump", "lillypad", "talldrygrass",
            ]

entities = ["charhands","charhandstouch", "charhead", "charlegs"]
animated = {"water", "freshwater"}
difficult_terrain = {"water", "flytrap", "freshwater"}

#          biome name, material lists
biomes = (("alpinetundra", (("sheoakdirt", "weeds", "stones"),)),
          ("steppe", (("lawn", "lushundergrowth", "weeds", "stones"),)),
          ("wetforest", (("freshwater", "weeds", "freshwater"), ("freshwater", "dirt", "freshwater"), ("freshwater", "gravillearobustadirt", "freshwater") )),
          ("moistforest", (("freshwater", "weeds", "dirt", "weeds", "dirt"),)),
          ("desertscrub", (("dirt", "sand", "roughseedgrass"),)),
          ("dryforest", (("gravillearobustadirt", "roughseedgrass"), ("bottlebrushdirt", "roughseedgrass"), ("sheoakdirt", "roughseedgrass"))),
          ("thornwoodland", (("roughseedgrass",),)),
          ("desert", (("sand", "fossil"),)))

#            temp over humidity
biome_map = ((3, 2, 2, 1, 1, 0),# cold
             (5, 5, 4, 4, 3, 3),
             (7, 6, 5, 4, 3, 2),
             (6, 6, 6, 5, 5, 5))# hot
#             dry          wet

OBJ = {
             "grass": {
                 "substrate": ("dirt", "weeds", "roughseedgrass", "stones", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn", "sand", "freshwater"),
                 "moisture": (5, 100),
                 "rootsize": "shallow",
                 "nutreants": (10, 70),
                 "temperiture": (0, 35),
                 "lightlevel": "high",
                 "flags": {"plant", "native", "flip"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "deadtree": {
                 "substrate": ("dirt", "weeds", "roughseedgrass", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (0, 50),
                 "rootsize": "deep",
                 "nutreants": (0, 100),
                 "temperiture": (0, 80),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "normaltree": {
                 "substrate": ("dirt", "weeds", "roughseedgrass"),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "lightlevel": "any",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "basil": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (5, 50),
                 "rootsize": "moderate",
                 "nutreants": (10, 70),
                 "temperiture": (20, 40),
                 "lightlevel": "high",
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "mushrooms": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (40, 100),
                 "rootsize": "shallow",
                 "nutreants": (0, 50),
                 "temperiture": (10, 30),
                 "lightlevel": "low",
                 "flags": {"plant", "native", "flip"},
                 "model": "singleshrub",
                 "size": 1,
                 "height": 0.01,
                 "lightemit": (0.05, 0.0, 0.08)
             },
             "fern": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (40, 90),
                 "rootsize": "shallow",
                 "nutreants": (10, 70),
                 "temperiture": (20, 40),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip"},
                 "model": "doubleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "bush": {
                 "substrate": ("dirt", "weeds", "roughseedgrass", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (40, 90),
                 "rootsize": "moderate",
                 "nutreants": (10, 70),
                 "temperiture": (20, 40),
                 "lightlevel": "moderate",
                 "flags": {"plant", "native", "flip", "slow"},
                 "model": "doubleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "tarragon": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (20, 50),
                 "rootsize": "moderate",
                 "nutreants": (50, 70),
                 "temperiture": (20, 40),
                 "lightlevel": "high",
                 "flags": {"plant", "flip"},
                 "model": "doubleshrub",
                 "size": 2,
                 "height": 0.05
             },
             "gravilearobustatree": {
                 "substrate": ("gravillearobustadirt", ),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "lightlevel": "any",
                 "creates": "gravillearobustadirt",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "bottlebrushtree": {
                 "substrate": ("bottlebrushdirt", ),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "lightlevel": "any",
                 "creates": "bottlebrushdirt",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "sheoaktree": {
                 "substrate": ("sheoakdirt", ),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "lightlevel": "any",
                 "creates": "sheoakdirt",
                 "flags": {"plant", "native", "flip", "solid"},
                 "model": "tree",
                 "size": 8,
                 "height": lambda x,y: 0.4+sin(x+y*y)/20
             },
             "cactus": {
                 "substrate": ("roughseedgrass", "sand"),
                 "moisture": (20, 60),
                 "rootsize": "moderate",
                 "nutreants": (5, 70),
                 "temperiture": (20, 50),
                 "lightlevel": "high",
                 "flags": {"plant", "flip", "solid"},
                 "model": "singleshrub",
                 "size": 2,
                 "height": 0.03
             },
             "flytrap": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (50, 90),
                 "rootsize": "shallow",
                 "nutreants": (10, 60),
                 "temperiture": (30, 40),
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
                 "lightlevel": "high",
                 "flags": {"plant", "native", "flip"},
                 "model": "singleshrub",
                 "size": 1.5,
                 "height": 0.001
             },
             "talldrygrass": {
                 "substrate": ("dirt", "weeds", "roughseedgrass", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (70, 100),
                 "rootsize": "shallow",
                 "nutreants": (10, 70),
                 "temperiture": (0, 45),
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
                 "height": 0.15
             },
}