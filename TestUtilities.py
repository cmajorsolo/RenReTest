import unittest
import Utilities

class TestUtilities(unittest.TestCase):
    def test_extract_contract_info(self):
        inputList = [{'test':'location', 'Include':['Location1', 'Location2']},
                      {'test2':'peril', 'Exclude':['Peril2']},
                      {'test3':'some-other-condition', 'Include':['condition3', 'condition4'], 'Exclude':['condition5']}]
        outputIncludeList1 = ['Location1', 'Location2', 'condition3', 'condition4']
        outputExcludeList2 = ['Peril2', 'condition5']
        expectedOutputResult = (outputIncludeList1, outputExcludeList2)
        result = Utilities.extract_contract_info(inputList)
        self.assertEqual(expectedOutputResult, result)

    def test_processClaim_with_claim_value_bigger_than_3000(self):
        claimValue = 4000
        expectedResult = 3000
        result = Utilities.process_claim(claimValue, 3000)
        self.assertEqual(expectedResult, result)

    def test_processClaim_with_claim_value_smaller_than_3000(self):
        claimValue = 1500
        expectedResult = 1500
        result = Utilities.process_claim(claimValue, 3000)
        self.assertEqual(expectedResult, result)

    def test_processClaim_with_claim_value_equal_to_3000(self):
        claimValue = 3000
        expectedResult = 3000
        result = Utilities.process_claim(claimValue, 3000)
        self.assertEqual(expectedResult, result)




if __name__ == '__main__':
    unittest.main()