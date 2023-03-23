import softest


class soft_assert(softest.TestCase):
    a = 5
    b = 10
    c = 30

    def f(self, yogesh):
        return 3

    def test_function_01(self):
        self.soft_assert(self.assertTrue,
                         self.f() == 3,
                         "3 is not equal to f")
        print('success')
        self.soft_assert(self.assertTrue,
                         self.a == 1,
                         "a is snot equal to 5")
        print('success')

        self.soft_assert(self.assertTrue,
                         self.b == 10,
                         "b is is not equal to 10")
        print('success')

        self.soft_assert(self.assertTrue,
                         self.c == 30,
                         "c is not equal to 30")
        print('success')
        self.assert_all()

# Hard assertion does not runs after assertion failed
# soft assertion runs after assertion failed or passed
