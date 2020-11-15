import random

class Coin:
    """ Regular unbias coin with two sides """
    def __init__(self):
        self.faces = {"Heads", "Tails"}
        self.face_showing = self._randomly_choose_face_showing()

    def _randomly_choose_face_showing(self):
        return random.sample(self.faces, 1)[0]

    def get_face_showing(self):
        """ Return the side of the coin showing """
        return self.face_showing
    
    def update_face_up_side_randomly(self):
        """ Update the side of the coin randomly """
        print(1234)
        self.face_showing = self._randomly_choose_face_showing()

    