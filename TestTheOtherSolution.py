import unittest
import TheOtherSolution
import os

class TestTheOtherSolution(unittest.TestCase):

    def test_generateReports_coveredContractsReport(self):
        solution = TheOtherSolution.TheOtherSolution('Input/deals.csv', 'Input/contract.json', 'Input/losses.csv')
        solution.generateReports()
        self.assertEqual(True, os.path.exists('Output/dealsCoveredByRenRe_TheOtherSolution.csv'))

    def test_generateReports_lossesReport(self):
        solution = TheOtherSolution.TheOtherSolution('Input/deals.csv', 'Input/contract.json', 'Input/losses.csv')
        solution.generateReports()
        self.assertEqual(True, os.path.exists('Output/lossesCoveredByRenRe_TheOtherSolution.csv'))

    def test_generateReports_exception_dealscsv(self):
        solution = TheOtherSolution.TheOtherSolution('Input/dealsssss.csv', 'Input/contract.json', 'Input/losses.csv')
        self.assertRaises(FileNotFoundError,
                          solution.generateReports())

    def test_generateReports_exception_contractJson(self):
        solution = TheOtherSolution.TheOtherSolution('Input/deals.csv', 'Input/contractttt.json', 'Input/losses.csv')
        self.assertRaises(FileNotFoundError,
                          solution.generateReports())

    def test_generateReports_exception_lossesCSV(self):
        solution = TheOtherSolution.TheOtherSolution('Input/deals.csv', 'Input/contract.json', 'Input/losseseee.csv')
        self.assertRaises(FileNotFoundError,
                          solution.generateReports())

    if __name__ == '__main__':
        unittest.main()