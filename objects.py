
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

solids = {"deadtree", "normaltree", "gravilearobustatree", "bottlebrushtree", "sheoaktree", "treelog", "birchtreelog", "treestump", "birchtreestump", "wall", "cactus", "greencactus"}
entities = ["charhands","charhandstouch", "charhead", "charlegs"]
animated = {"water", "freshwater"}
blocks = {"block", "wall"}
roofing = {"tiles", "planks", "glass"}
difficult_terrain = {"water", "flytrap", "freshwater"}

#          biome name, material lists
biomes = (("alpinetundra", (("sheoakdirt", "weeds", "stones"),)),
          ("steppe", (("lawn", "lushundergrowth", "weeds", "stones"),)),
          ("wetforest", (("freshwater", "weeds", "freshwater"),)),
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
                 "lightlevel": "high"
             },
             "deadtree": {
                 "substrate": ("dirt", "weeds", "roughseedgrass", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (0, 50),
                 "rootsize": "deep",
                 "nutreants": (0, 100),
                 "temperiture": (0, 80),
                 "lightlevel": "any"
             },
             "normaltree": {
                 "substrate": ("dirt", "weeds", "roughseedgrass"),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "lightlevel": "any"
             },
             "basil": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (5, 50),
                 "rootsize": "moderate",
                 "nutreants": (10, 70),
                 "temperiture": (20, 40),
                 "lightlevel": "high"
             },
             "mushrooms": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (40, 100),
                 "rootsize": "shallow",
                 "nutreants": (0, 50),
                 "temperiture": (10, 30),
                 "lightlevel": "low"
             },
             "fern": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (40, 90),
                 "rootsize": "shallow",
                 "nutreants": (10, 70),
                 "temperiture": (20, 40),
                 "lightlevel": "moderate"
             },
             "bush": {
                 "substrate": ("dirt", "weeds", "roughseedgrass", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (40, 90),
                 "rootsize": "moderate",
                 "nutreants": (10, 70),
                 "temperiture": (20, 40),
                 "lightlevel": "moderate"
             },
             "tarragon": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (20, 50),
                 "rootsize": "moderate",
                 "nutreants": (50, 70),
                 "temperiture": (20, 40),
                 "lightlevel": "high"
             },
             "gravilearobustatree": {
                 "substrate": ("gravillearobustadirt", ),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "lightlevel": "any",
                 "creates": "gravillearobustadirt",
             },
             "bottlebrushtree": {
                 "substrate": ("bottlebrushdirt", ),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "lightlevel": "any",
                 "creates": "bottlebrushdirt",
             },
             "sheoaktree": {
                 "substrate": ("sheoakdirt", ),
                 "moisture": (20, 75),
                 "rootsize": "deep",
                 "nutreants": (20, 75),
                 "temperiture": (15, 80),
                 "lightlevel": "any",
                 "creates": "sheoakdirt",
             },
             "cactus": {
                 "substrate": ("roughseedgrass", "sand"),
                 "moisture": (20, 60),
                 "rootsize": "moderate",
                 "nutreants": (5, 70),
                 "temperiture": (20, 50),
                 "lightlevel": "high"
             },
             "flytrap": {
                 "substrate": ("dirt", "weeds", "lushundergrowth", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (50, 90),
                 "rootsize": "shallow",
                 "nutreants": (10, 60),
                 "temperiture": (30, 40),
                 "lightlevel": "high"
             },
             "lillypad": {
                 "substrate": ("freshwater", ),
                 "moisture": (50, 100),
                 "rootsize": "moderate",
                 "nutreants": (10, 60),
                 "temperiture": (30, 40),
                 "lightlevel": "high"
             },
             "talldrygrass": {
                 "substrate": ("dirt", "weeds", "roughseedgrass", "gravillearobustadirt", "bottlebrushdirt", "sheoakdirt", "lawn"),
                 "moisture": (70, 100),
                 "rootsize": "shallow",
                 "nutreants": (10, 70),
                 "temperiture": (0, 45),
                 "lightlevel": "high"
             },
            "greencactus": {
                 "substrate": ("roughseedgrass", "sand"),
                 "moisture": (10, 50),
                 "rootsize": "moderate",
                 "nutreants": (5, 70),
                 "temperiture": (20, 50),
                 "lightlevel": "high"
             },
}