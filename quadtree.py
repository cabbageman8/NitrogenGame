class leaf_node():
    def __init__(self, data = None):
        self.data = data
    def tree(self):
        print(self.data)
    def get_area(self, x, y, z, w, size, level):
        output = {}
        if self.data == None:
            return output
        else:
            if self.data[0]:
                output.update({(int(z + 0), int(w + 0)) : self.data[0]})
            if self.data[1]:
                output.update({(int(z + 1), int(w + 0)) : self.data[1]})
            if self.data[2]:
                output.update({(int(z + 0), int(w + 1)) : self.data[2]})
            if self.data[3]:
                output.update({(int(z + 1), int(w + 1)) : self.data[3]})
            return output
    def get_data(self, x, y, z, w, size):
        if self.data == None:
            return None
        else:
            if x > z:
                if y > w:
                    return self.data[3]
                else:
                    return self.data[1]
            else:
                if y > w:
                    return self.data[2]
                else:
                    return self.data[0]
    def set_data(self, x, y, data, z, w, size):
        if self.data == None:
            self.data = [None, None, None, None]
        if x > z:
            if y > w:
                self.data[3] = data
            else:
                self.data[1] = data
        else:
            if y > w:
                self.data[2] = data
            else:
                self.data[0] = data
class branch_node():
    def __init__(self, children = None):
        self.children = children
    def tree(self):
        if self.children != None:
            for c in self.children:
                c.tree()
    def get_area(self, x, y, z, w, size, level):
        output = {}
        if self.children == None:
            return output
        elif (2**level >= size):
            output.update(self.children[3].get_area(x, y, z+size/2, w+size/2, size/2, level))
            output.update(self.children[1].get_area(x, y, z+size/2, w-size/2, size/2, level))
            output.update(self.children[2].get_area(x, y, z-size/2, w+size/2, size/2, level))
            output.update(self.children[0].get_area(x, y, z-size/2, w-size/2, size/2, level))
            return output
        else:
            if x > z:
                if y > w:
                    return self.children[3].get_area(x, y, z+size/2, w+size/2, size/2, level)
                else:
                    return self.children[1].get_area(x, y, z+size/2, w-size/2, size/2, level)
            else:
                if y > w:
                    return self.children[2].get_area(x, y, z-size/2, w+size/2, size/2, level)
                else:
                    return self.children[0].get_area(x, y, z-size/2, w-size/2, size/2, level)
    def get_data(self, x, y, z, w, size):
        if self.children == None:
            return None
        else:
            if x > z:
                if y > w:
                    return self.children[3].get_data(x, y, z+size/2, w+size/2, size/2)
                else:
                    return self.children[1].get_data(x, y, z+size/2, w-size/2, size/2)
            else:
                if y > w:
                    return self.children[2].get_data(x, y, z-size/2, w+size/2, size/2)
                else:
                    return self.children[0].get_data(x, y, z-size/2, w-size/2, size/2)
    def set_data(self, x, y, data, z, w, size):
        if (size <= 2):
            if self.children == None:
                self.children = (leaf_node(), leaf_node(), leaf_node(), leaf_node())
            if x > z:
                if y > w:
                    self.children[3].set_data(x, y, data, z+size / 2, w+size / 2, size / 2)
                else:
                    self.children[1].set_data(x, y, data, z+size / 2, w-size / 2, size / 2)
            else:
                if y > w:
                    self.children[2].set_data(x, y, data, z-size / 2, w+size / 2, size / 2)
                else:
                    self.children[0].set_data(x, y, data, z-size / 2, w-size / 2, size / 2)
        else:
            if self.children == None:
                self.children = (branch_node(), branch_node(), branch_node(), branch_node())
            if x > z:
                if y > w:
                    self.children[3].set_data(x, y, data, z+size / 2, w+size / 2, size / 2)
                else:
                    self.children[1].set_data(x, y, data, z+size / 2, w-size / 2, size / 2)
            else:
                if y > w:
                    self.children[2].set_data(x, y, data, z-size / 2, w+size / 2, size / 2)
                else:
                    self.children[0].set_data(x, y, data, z-size / 2, w-size / 2, size / 2)
class root_node():
    def __init__(self):
        self.children = (branch_node(), branch_node(), branch_node(), branch_node())
        self.size = 2**4
        self.cache = {}
        self.save_buffer = {}
    def tree(self):
        for c in self.children:
            c.tree()
    def get_area(self, x, y, level):
        output = {}
        if (abs(x)>self.size or abs(y)>self.size):
            return output
        if (2**level >= self.size):
            output.update(self.children[3].get_area(x, y,  self.size,  self.size, self.size, level))
            output.update(self.children[1].get_area(x, y,  self.size, -self.size, self.size, level))
            output.update(self.children[2].get_area(x, y, -self.size,  self.size, self.size, level))
            output.update(self.children[0].get_area(x, y, -self.size, -self.size, self.size, level))
            return output
        if x > 0:
            if y > 0:
                result = self.children[3].get_area(x, y, self.size, self.size, self.size, level)
            else:
                result = self.children[1].get_area(x, y, self.size, -self.size, self.size, level)
        else:
            if y > 0:
                result = self.children[2].get_area(x, y, -self.size, self.size, self.size, level)
            else:
                result = self.children[0].get_area(x, y, -self.size, -self.size, self.size, level)
        return result
    def get_data(self, x, y):
        if (int(x), int(y)) in self.cache:
            return self.cache[(int(x), int(y))]
        if (abs(x)>self.size or abs(y)>self.size):
            return None
        if x > 0:
            if y > 0:
                result = self.children[3].get_data(x, y, self.size, self.size, self.size)
            else:
                result = self.children[1].get_data(x, y, self.size, -self.size, self.size)
        else:
            if y > 0:
                result = self.children[2].get_data(x, y, -self.size, self.size, self.size)
            else:
                result = self.children[0].get_data(x, y, -self.size, -self.size, self.size)
        self.cache_data(int(x), int(y), result)
        return result
    def cache_data(self, x, y, data):
        if len(self.cache) > 2**16:
            print("cleared cache")
            self.cache.clear()
        self.cache.update({(int(x), int(y)) : data})
    def apply_data(self, x, y, data):
        if self.get_data(int(x), int(y)) != data:
            if (abs(x)>self.size or abs(y)>self.size):
                self.size = 2*self.size
                print("world size now =", self.size)
                self.children = (branch_node((branch_node(), branch_node(), branch_node(), self.children[0])),
                                 branch_node((branch_node(), branch_node(), self.children[1], branch_node())),
                                 branch_node((branch_node(), self.children[2], branch_node(), branch_node())),
                                 branch_node((self.children[3], branch_node(), branch_node(), branch_node())))
                self.apply_data(x, y, data)
            else:
                self.cache_data(int(x), int(y), data)
                if x > 0:
                    if y > 0:
                        self.children[3].set_data(x, y, data, self.size, self.size, self.size)
                    else:
                        self.children[1].set_data(x, y, data, self.size, -self.size, self.size)
                else:
                    if y > 0:
                        self.children[2].set_data(x, y, data, -self.size, self.size, self.size)
                    else:
                        self.children[0].set_data(x, y, data, -self.size, -self.size, self.size)
    def set_data(self, x, y, data):
        if self.get_data(int(x), int(y)) != data:
            self.save_buffer.update({(int(x), int(y)): data})
            self.apply_data(x, y, data)