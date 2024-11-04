import unittest


def skip_if_frozen(test_func):
    """Декоратор для пропуска теста, если атрибут is_frozen установлен в True."""

    def wrapper(*args, **kwargs):
        instance = args[0]
        if getattr(instance, 'is_frozen', False):
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return test_func(*args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run(self):
        self.assertEqual(2 * 2, 4)

    @skip_if_frozen
    def test_walk(self):
        self.assertTrue(True)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(3 - 1, 2)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertEqual(5 // 1, 5)

    @skip_if_frozen
    def test_third_tournament(self):
        # ваш тест
        self.assertFalse(False)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
