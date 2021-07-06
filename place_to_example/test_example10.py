class TestExample10:
    def test_check_length(self):

        phrase = input("Set a phrase: ")

        assert len(phrase) <= 15, "Length is more than 15 characters"