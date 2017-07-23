import pandas as pd
import Utilities
import sys, os

class TheOtherSolution():

    def __init__(self, dealsFilePath, contractFilePath, lossesFilePath):
        self.dealsFilePath = dealsFilePath
        self.contractFilePath = contractFilePath
        self.lossesFilePath = lossesFilePath

    def generateReports(self):
        try:
            contract = pd.read_json(self.contractFilePath)
            coverages = contract['Coverage']
            maxAmount = contract['MaxAmount'][0]
            includes = {}
            excludes = {}
            for coverage in coverages:
                if 'Include' in coverage:
                    includes[coverage['Attribute']] = coverage['Include']
                if 'Exclude' in coverage:
                    excludes[coverage['Attribute']] = coverage['Exclude']

            includesData = pd.DataFrame(includes, columns=['Location'])
            excludesData = pd.DataFrame(excludes, columns=['Peril'])

            deals = pd.read_csv(self.dealsFilePath)
            includedDeals = pd.merge(includesData, deals)
            excludedDeals = pd.merge(excludesData, deals)
            dealsCoveredByRenRe = includedDeals[~includedDeals.DealId.isin(excludedDeals.DealId)]\
                .sort_values(['DealId'], ascending=True)
            dealsCoveredByRenRe = dealsCoveredByRenRe[['DealId', 'Company', 'Peril', 'Location']]
            dealsCoveredByRenRe.to_csv('Output/dealsCoveredByRenRe_TheOtherSolution.csv', index=False)

            losses = pd.read_csv(self.lossesFilePath)
            lossesCoveredByRenRe = pd.merge(dealsCoveredByRenRe, losses)[['Peril', 'Loss']]
            lossesCoveredByRenRe['Loss'] = lossesCoveredByRenRe.apply(
                lambda row: Utilities.process_claim(row['Loss'], maxAmount), axis=1)
            lossesCoveredByRenRe = lossesCoveredByRenRe.groupby('Peril').agg(sum)
            lossesCoveredByRenRe.to_csv('Output/lossesCoveredByRenRe_TheOtherSolution.csv')
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
