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
        try:
            deals_df = pd.read_csv(self.dealsFilePath)
            contract_df = pd.read_json(self.contractFilePath)
            contractConstrains = Utilities.extract_contract_info(contract_df['Coverage'])
            deals_df = deals_df.loc[deals_df['Location'].isin(contractConstrains[0])
                                    & ~deals_df['Peril'].isin(contractConstrains[1])]
            deals_df.to_csv(coveredContractFilePath, index=False)
        except Exception:
            self.get_exception_details()

    def generate_loss_report(self, coveredContractFilePath, lossReportFilePath):
        self.get_max_coverage_value()

        try:
            loss_df = pd.read_csv(self.lossesFilePath)
            if(not os.path.exists(coveredContractFilePath)):
                self.generate_contracts_covered_by_RenRe(coveredContractFilePath)
            covered_contract_df = pd.read_csv(coveredContractFilePath)
            loss_covered_by_RenRe_df = pd.merge(loss_df, covered_contract_df, on=['DealId'])[['Loss', 'Peril']]
            loss_covered_by_RenRe_df['Loss'] = loss_covered_by_RenRe_df.apply(
                lambda row: Utilities.process_claim(row['Loss'], self.maxCoverageValue), axis=1)
            loss_covered_by_RenRe_df = loss_covered_by_RenRe_df.groupby('Peril').agg(sum)
            loss_covered_by_RenRe_df.to_csv(lossReportFilePath)
        except Exception:
            self.get_exception_details()

    def get_exception_details(self):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

if __name__ == '__main__':
    example = FindDealsCoveredByRenRe('Input/deals.csv', 'Input/contract.json', 'Input/losses.csv')
    example.generate_loss_report('Output/contractCoveredByRenRe.csv', 'Output/lossReport.csv')
