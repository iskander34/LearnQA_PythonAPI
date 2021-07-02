class TestExample:
    def test_chek_math(self):
        a,b = 5,9
        expected_sum = 14
        assert a+b == expected_sum, f"Sum of variables a and b is not equal to {expected_sum}"

    def test_chek_math2(self):
        a,b = 5,11
        expected_sum = 14
        assert a+b == expected_sum, f"Sum of variables a and b is not equal to {expected_sum}"