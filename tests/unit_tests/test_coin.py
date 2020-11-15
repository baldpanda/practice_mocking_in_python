from coin import Coin
class TestCoin:
    """ """

    def setup_method(self):
        self.sut = Coin()

    def test_coins_face_showing_is_heads_or_tails(self):
        assert self.sut.get_face_showing() in ["Heads", "Tails"]

    def test_randomly_choosing_face(self):
        self.sut.update_face_up_side_randomly()
        assert self.sut.get_face_showing() in ["Heads", "Tails"]