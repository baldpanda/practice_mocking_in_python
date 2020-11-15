class Person:
    """ Person with a coin """
    def __init__(self, coin):
        self.coin = coin
    
    def observe_coins_face(self):
        return self.coin.get_face_showing()

    def flip_coin(self):
        self.coin.update_face_up_side_randomly()