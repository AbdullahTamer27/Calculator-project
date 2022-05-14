class Calculator:
    def __init__(self, string):
        self.string = string
        self.my_list = list()
        self.x = 0
        self.y = 0

    def order_of_operations(self):
        self.my_list = self.string.split()
        while "X" in self.my_list:
            if "/" not in self.my_list:
                i = self.my_list.index("X")
                self.x = int(self.my_list[i-1])
                self.y = int(self.my_list[i+1])
                self.multiply(i)
            else:
                i = self.my_list.index("X")
                k = self.my_list.index("/")
                if i < k:
                    i = self.my_list.index("X")
                    self.x = self.my_list[i - 1]
                    self.y = self.my_list[i + 1]
                    self.multiply(i)
                else:
                    i = self.my_list.index("/")
                    self.x = self.my_list[i - 1]
                    self.y = self.my_list[i + 1]
                    self.divide(i)
        while "/" in self.my_list:
            if "X" not in self.my_list:
                i = self.my_list.index("/")
                self.x = self.my_list[i-1]
                self.y = self.my_list[i+1]
                self.divide(i)
            else:
                i = self.my_list.index("/")
                k = self.my_list.index("X")
                if i < k:
                    i = self.my_list.index("/")
                    self.x = self.my_list[i - 1]
                    self.y = self.my_list[i + 1]
                    self.divide(i)
                else:
                    i = self.my_list.index("X")
                    self.x = self.my_list[i - 1]
                    self.y = self.my_list[i + 1]
                    self.multiply(i)
        while "+" in self.my_list:
            if "-" not in self.my_list:
                i = self.my_list.index("+")
                self.x = self.my_list[i-1]
                self.y = self.my_list[i+1]
                self.add(i)
            else:
                i = self.my_list.index("+")
                k = self.my_list.index("-")
                if i < k:
                    i = self.my_list.index("+")
                    self.x = self.my_list[i - 1]
                    self.y = self.my_list[i + 1]
                    self.add(i)
                else:
                    i = self.my_list.index("-")
                    self.x = self.my_list[i - 1]
                    self.y = self.my_list[i + 1]
                    self.subtract(i)
        while "-" in self.my_list:
            if "+" not in self.my_list:
                i = self.my_list.index("-")
                self.x = self.my_list[i-1]
                self.y = self.my_list[i+1]
                self.subtract(i)
            else:
                i = self.my_list.index("-")
                k = self.my_list.index("+")
                if i < k:
                    i = self.my_list.index("-")
                    self.x = self.my_list[i - 1]
                    self.y = self.my_list[i + 1]
                    self.subtract(i)
                else:
                    i = self.my_list.index("+")
                    self.x = self.my_list[i - 1]
                    self.y = self.my_list[i + 1]
                    self.add(i)
        return self.my_list

    def add(self, i):
        z = self.x + self.y
        self.my_list.remove(self.x)
        self.my_list.remove(self.y)
        self.my_list[i-1] = z

    def subtract(self, i):
        z = self.x - self.y
        self.my_list.remove(self.x)
        self.my_list.remove(self.y)
        self.my_list[i-1] = z

    def multiply(self, i):
        z = self.x * self.y
        self.my_list.remove(self.x)
        self.my_list.remove(self.y)
        self.my_list[i-1] = z

    def divide(self, i):
        z = self.x / self.y
        self.my_list.remove(self.x)
        self.my_list.remove(self.y)
        self.my_list[i-1] = z
