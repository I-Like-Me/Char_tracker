class CharSpawn:

    def __init__(self, name, x_pos=0, y_pos=0):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        print(f"{self.name} starting at {self.x_pos},{self.y_pos}")

    def move_char(self, new_x, new_y):
        print(f"{self.name} moved from {self.x_pos},{self.y_pos} to {new_x},{new_y}")
        self.x_pos = new_x
        self.y_pos = new_y

    def where_am_i(self):
        print(f"{self.name} currently at {self.x_pos},{self.y_pos}")

kevin = CharSpawn("Kevin", 3, 7)
kevin.move_char(5,2)
kevin.where_am_i()
