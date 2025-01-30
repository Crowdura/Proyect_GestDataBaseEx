class MappingExcel:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    __update = update

class MappingSubclass(MappingExcel):        
    def update(self, keys, value):
        for item in zip(keys, value):
            self.items_list.append(item)