
class data_node():
    def __init__(self, children = None):
        self.children = children
        self.data = None
    def get_data(self, x, y, z, w, size):
        if self.children == None:
            return self.data
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
        if (size < 1):
            self.data = data
            return True
        if self.children == None:
            self.children = (data_node(), data_node(), data_node(), data_node())
        else:
            if x > z:
                if y > w:
                    return self.children[3].set_data(x, y, data, z+size / 2, w+size / 2, size / 2)
                else:
                    return self.children[1].set_data(x, y, data, z+size / 2, w-size / 2, size / 2)
            else:
                if y > w:
                    return self.children[2].set_data(x, y, data, z-size / 2, w+size / 2, size / 2)
                else:
                    return self.children[0].set_data(x, y, data, z-size / 2, w-size / 2, size / 2)
class root_node():
    def __init__(self):
        self.children = (data_node(), data_node(), data_node(), data_node())
        self.size = 2**1
        self.cache = {}
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
        self.cache_data(x, y, result)
        return result
    def cache_data(self, x, y, data):
        if len(self.cache) > 2**16:
            print("cleared cache")
            self.cache = {}
        self.cache.update({(int(x), int(y)): data})
    def set_data(self, x, y, data):
        self.cache_data(x, y, data)
        if (abs(x)>self.size or abs(y)>self.size):
            self.size = 2*self.size
            print("world size now =", self.size)
            self.children = (data_node((data_node(), data_node(), data_node(), self.children[0])),
                             data_node((data_node(), data_node(), self.children[1], data_node())),
                             data_node((data_node(), self.children[2], data_node(), data_node())),
                             data_node((self.children[3], data_node(), data_node(), data_node())))
            return self.set_data(x, y, data)
        if x > 0:
            if y > 0:
                return self.children[3].set_data(x, y, data, self.size, self.size, self.size)
            else:
                return self.children[1].set_data(x, y, data, self.size, -self.size, self.size)
        else:
            if y > 0:
                return self.children[2].set_data(x, y, data, -self.size, self.size, self.size)
            else:
                return self.children[0].set_data(x, y, data, -self.size, -self.size, self.size)