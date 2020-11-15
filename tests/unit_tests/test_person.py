import mock
from person import Person

class TestPerson:

    @mock.patch("coin.Coin")
    def test_person_gets_face_of_coin(self, mock_coin):
        """ Test the person can get the face of the coin OK """
        mock_coin().get_face_showing.return_value = "Test face"
        self.sut = Person(mock_coin())
        assert self.sut.observe_coins_face() == "Test face"

    @mock.patch("coin.Coin")
    def test_flipping_coin(self, mock_coin):
        """ Test flipping the coin updates the face of the coin """
        mocked_coin = mock_coin()
        self.sut = Person(mocked_coin)
        self.sut.flip_coin()
        mocked_coin.update_face_up_side_randomly.assert_called()
        

        