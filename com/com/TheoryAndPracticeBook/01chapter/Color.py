
class Color(object):

    def __init__(self, red, green, blue):
        self.red = red;
        self.green = green;
        self.blue = blue;

    def __str__(self):
        return '(%s,%s,%s)' %(self.red, self.green, self.blue);

