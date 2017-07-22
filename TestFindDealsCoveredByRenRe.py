import unittest
import FindDealsCoveredByRenRe
import os

class TestFindDealsCoveredByRenRe(unittest.TestCase):
    def test_get_max_coverage_value(self):
        solution = FindDealsCoveredByRenRe.FindDealsCoveredByRenRe('Input/deals.csv', 'Input/contract.json',
                                                                   'Input/losses.csv')
        expectedValue = 3000
        solution.get_max_coverage_value()
        self.assertEqual(expectedValue, solution.maxCoverageValue)

    def test_get_max_coverage_value_FileNotFoundException(self):
        solution = FindDealsCoveredByRenRe.FindDealsCoveredByRenRe('Input/deals.csv', 'Input/contract1111.json',
                                                                   'Input/losses.csv')
        self.assertRaises(FileNotFoundError, solution.get_max_coverage_value())

    def test_generate_contracts_covered_by_RenRe(self):
        solution = FindDealsCoveredByRenRe.FindDealsCoveredByRenRe('Input/deals.csv', 'Input/contract.json',
                                                                   'Input/losses.csv')
        solution.generate_contracts_covered_by_RenRe('Output/Test/testContracts.csv')
        self.assertEqual(True, os.path.exists('Output/Test/testContracts.csv'))

    def test_generate_contracts_covered_by_RenRe_FileNotFoundException_1stFile(self):
        solution = FindDealsCoveredByRenRe.FindDealsCoveredByRenRe('Input/deals2222.csv', 'Input/contract.json',
                                                                   'Input/losses.csv')
        self.assertRaises(FileNotFoundError,
                          solution.generate_contracts_covered_by_RenRe('Output/Test/testContracts.csv'))

    def test_generate_contracts_covered_by_RenRe_FileNotFoundException_2ndFile(self):
        solution = FindDealsCoveredByRenRe.FindDealsCoveredByRenRe('Input/deals.csv', 'Input/contractsss.json',
                                                                   'Input/losses.csv')
        self.assertRaises(FileNotFoundError,
                          solution.generate_contracts_covered_by_RenRe('Output/Test/testContracts.csv'))

    def test_generate_contracts_covered_by_RenRe_FileNotFoundException_3rdFile(self):
        solution = FindDealsCoveredByRenRe.FindDealsCoveredByRenRe('Input/deals.csv', 'Input/contractsss.json',
                                                                   'Input/losses.csv')
        self.assertRaises(FileNotFoundError,
                          solution.generate_contracts_covered_by_RenRe('Output/Testeee/testContracts.csv'))

    def test_generate_loss_report(self):
        solution = FindDealsCoveredByRenRe.FindDealsCoveredByRenRe('Input/deals.csv', 'Input/contract.json',
                                                                   'Input/losses.csv')
        solution.generate_loss_report('Output/Test/testContracts.csv', 'Output/Test/testLossReport.csv')
        self.assertEqual(True, os.path.exists('Output/Test/testLossReport.csv'))

    def test_generate_loss_report_FileNotFound_lossFilePath(self):
        solution = FindDealsCoveredByRenRe.FindDealsCoveredByRenRe('Input/deals.csv', 'Input/contractsss.json',
                                                                   'Input/losseseeee.csv')
        self.assertRaises(FileNotFoundError,
                          solution.generate_loss_report('Output/Testeee/testContracts.csv',
                                                        'Output/Test/testLossReport.csv'))


if __name__ == '__main__':
    unittest.main()