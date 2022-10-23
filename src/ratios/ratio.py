import numpy as np

class Ratio:

    def __init__(self):
        self.dict_ratios = self.set_dic_ratios()

    def calculate_ratio(self, list_years, ratio, financial_data):
        dict_results_ratio = dict()
        for year in list_years:
            dict_results_ratio[year] = self.dict_ratios[ratio](year, financial_data)

        return dict_results_ratio

    def get_list_ratios_avalable(self):
        return {
            "Current Ratio",
            "Debt Ratio",
            "Financial Leverage",
            "Return of Equity(ROE)",
            "Net Profit Margin",
            "Operating Margin",
        }

    def get_ratios_description(self):
        return {
            "Current Ratio": "Description",
            "Debt Ratio": "Description",
            "Financial Leverage": "Description",
            "Return of Equity(ROE)": "Description",
            "Net Profit Margin": "Description",
            "Operating Margin": "Description",
        }

    def set_dic_ratios(self):
        return {
            "Current Ratio": self.calculate_current_ratio,
            "Debt Ratio": self.calculate_debt_ratio,
            "Financial Leverage": self.calculate_financial_leverage,
            "Return of Equity(ROE)": self.calculate_return_equity,
            "Net Profit Margin": self.calculate_net_profit_margin,
            "Operating Margin": self.calculate_operating_margin,
        }

    def calculate_current_ratio(self, year, financial_data):
        balance = financial_data["balance"]
        result = np.divide(balance[year]['Total Current Assets'],balance[year]['Total Current Liabilities'])
        return result

    def calculate_debt_ratio(self, year, financial_data):
        balance = financial_data["balance"]
        result = np.divide(balance[year]['Total Liab'], balance[year]['Total Assets'])
        return result

    def calculate_financial_leverage(self, year, financial_data):
        balance = financial_data["balance"]
        result = np.divide(balance[year]['Total Liab'], balance[year]['Total Stockholder Equity'])
        return result

    def calculate_return_equity(self, year, financial_data):
        pass

    def calculate_net_profit_margin(self, year, financial_data):
        pass

    def calculate_operating_margin(self, year, financial_data):
        pass


