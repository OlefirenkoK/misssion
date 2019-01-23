class Print(object):
    def __init__(self, category):
        self._category = category

    def log(self):
        for line in self._category.iter():
            print(line)
            yield line
