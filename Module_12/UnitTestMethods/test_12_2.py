import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = list()

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner("Усэйн", 10)
        self.runner2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner3 = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        [print(item) for item in cls.all_results]

    def test_tournamet1(self):
        tournamet = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.all_results.append({key: str(item) for key, item in tournamet.start().items()})
        self.assertTrue(self.all_results[[max(item.keys()) - 1 for item in self.all_results][0] - 1], "Ник")

    def test_tournamet2(self):
        tournamet = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.all_results.append({key: str(item) for key, item in tournamet.start().items()})
        self.assertTrue(self.all_results[[max(item.keys()) - 1 for item in self.all_results][0] - 1], "Ник")

    def test_tournamet3(self):
        tournamet = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results.append({key: str(item) for key, item in tournamet.start().items()})
        self.assertTrue(self.all_results[[max(item.keys()) - 1 for item in self.all_results][0] - 1], "Ник")


if __name__ == "__main__":
    unittest.main()
