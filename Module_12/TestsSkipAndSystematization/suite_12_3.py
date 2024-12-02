import tests_12_3
import unittest


test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

test_run = unittest.TextTestRunner(verbosity=2)
test_run.run(test_suite)
