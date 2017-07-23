import sys, os
import pandas as pd
import Utilities

class FindDealsCoveredByRenRe():

    def __init__(self, dealsFilePath, contractFilePath, lossesFilePath, maxCoverageValue = 0):
        self.dealsFilePath = dealsFilePath
        self.contractFilePath = contractFilePath
        self.lossesFilePath = lossesFilePath
        self.maxCoverageValue = maxCoverageValue

    def get_max_coverage_value(self):
        try:
            contract_df = pd.read_json(self.contractFilePath)
            self.maxCoverageValue = contract_df['MaxAmount'].iloc[0]
        except Exception:
            self.get_exception_details()

    def generate_contracts_covered_by_RenRe(self, coveredContractFilePath):
        if os.path.exists(coveredContractFilePath):
            os.remove(coveredContractFilePath)
        try:
            contract_df = pd.read_json(self.contractFilePath)
            contractConstrains = Utilities.extract_contract_info(contract_df['Coverage'])
            chunkSize = 1000
            for chunk in pd.read_csv(self.dealsFilePath, chunksize=chunkSize):
                chunk = chunk.loc[chunk['Location'].isin(contractConstrains[0]) & ~chunk['Peril'].isin(contractConstrains[1])]
                chunk.to_csv(coveredContractFilePath, mode='a', index=False)
        except Exception:
            self.get_exception_details()

    def generate_loss_report(self, coveredContractFilePath, lossReportFilePath):
        self.get_max_coverage_value()
        if os.path.exists(lossReportFilePath):
            os.remove(lossReportFilePath)
        try:
            if(not os.path.exists(coveredContractFilePath)):
                self.generate_contracts_covered_by_RenRe(coveredContractFilePath)
            loss_df = pd.read_csv(self.lossesFilePath)
            chunkSize = 1000
            for chunk in pd.read_csv(coveredContractFilePath, chunksize=chunkSize):
                covered_chunk = pd.merge(loss_df, chunk, on=['DealId'])[['Loss', 'Peril']]
                covered_chunk['Loss'] = covered_chunk.apply(
                    lambda row: Utilities.process_claim(row['Loss'], self.maxCoverageValue), axis=1)
                covered_chunk = covered_chunk.groupby('Peril').agg(sum)
                covered_chunk.to_csv(lossReportFilePath, mode='a')
        except Exception:
            self.get_exception_details()

    def get_exception_details(self):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

if __name__ == '__main__':
    example = FindDealsCoveredByRenRe('Input/deals.csv', 'Input/contract.json', 'Input/losses.csv')
    example.generate_loss_report('Output/contractCoveredByRenRe.csv', 'Output/lossReport.csv')
