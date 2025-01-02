class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def run(self):
        self.distance += self.speed

    def walk(self):
        self.distance += self.speed // 2

class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        while any(runner.distance < self.distance for runner in self.runners):
            for runner in self.runners:
                runner.run()
                if runner.distance >= self.distance and runner.name not in results.values():
                    results[len(results) + 1] = runner.name
        return results



import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_tournament_usain_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        result = tournament.start()
        self.all_results[1] = result
        self.assertTrue(result[max(result)] == "Ник")

    def test_tournament_andrey_nik(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(result[max(result)] == "Ник")

    def test_tournament_usain_andrey_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        result = tournament.start()
        self.all_results[3] = result
        self.assertTrue(result[max(result)] == "Ник")

if __name__ == "__main__":
    unittest.main()