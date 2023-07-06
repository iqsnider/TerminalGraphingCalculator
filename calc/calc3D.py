import re 


class Surface:

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self):
        return f"x = {self.__x}\ny = {self.__y}\nz = {self.__z}"
    
    def makemath(self, t_1, t_2):
        self.__x


    def makeframe(self, step):
        pass



def decimal_range(start, stop, increment):
        while start < stop:
            yield start
            start += increment

    