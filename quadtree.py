class root_node():
    def __init__(self):
        self.cache = {}
        self.save_buffer = {}
    def get_data(self, x, y):
        if (int(x), int(y)) in self.cache:
            return self.cache[(int(x), int(y))]
        return None
    def cache_data(self, x, y, data):
        self.cache.update({(int(x), int(y)) : data})
    def apply_data(self, x, y, data):
        self.cache_data(int(x), int(y), data)
    def set_data(self, x, y, data):
        if self.get_data(int(x), int(y)) != data:
            self.save_buffer.update({(int(x), int(y)): data})
            self.apply_data(x, y, data)