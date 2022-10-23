import yfinance as yf
import pandas as pd

from src.ratios.ratio import Ratio

class App:

    def __init__(self, list_years=[], list_ratios=[], symbol=""):
        self.ratio = Ratio()
        self.symbol = symbol
        self.list_years = self.validate_list_years(list_years)
        self.list_ratios = self.validate_list_ratios(list_ratios)
        self.dic_result_calculations = dict()

    def validate_list_ratios(self, list_ratios):
        ratios = self.ratio.get_list_ratios_avalable()
        for ratio in list_ratios:
            if ratio not in ratios:
                raise Exception(f"{ratio} is not recognize this ratio, check your type")
        return list_ratios

    def validate_list_years(self, list_years):
        dates_availables = self.make_petition_to_test_dates()
        for year in list_years:
            if year not in dates_availables:
                raise Exception(f"{year} is not available, the dataset only have {dates_availables}")
        return sorted(list_years, reverse=True)

    def make_petition_to_test_dates(self):
        symbol_test = "MSFT"
        stock_data = yf.Ticker(symbol_test)
        balance = stock_data.balance_sheet.copy()
        dates_available = self.change_format_dates_columns(balance.columns)
        return dates_available


    def request_data(self):
        symbol = self.symbol
        stock_data = yf.Ticker(symbol)
        balance_sheet = stock_data.balance_sheet.copy()
        result_sheet = stock_data.financials.copy()
        cash_flow_sheet = stock_data.cashflow.copy()

        if cash_flow_sheet.size == 0:
            raise Exception(f"{symbol} doesn't have data, verify your symbol or may information no available")

        return self.change_format_columns_dataframe(balance_sheet,result_sheet,cash_flow_sheet)

    def get_result(self):
        financial_data = self.request_data()
        for ratio in self.list_ratios:
            self.dic_result_calculations[ratio] = self.ratio.calculate_ratio(self.list_years, ratio, financial_data)
        return self.dic_result_calculations


    def change_format_dates_columns(self, dates_DateTimeIndex):
        return set(map(lambda x: str(x.strftime("%Y")), dates_DateTimeIndex))

    def change_format_columns_dataframe(self, balance_sheet, result_sheet, cash_flow_sheet):
        balance_sheet.columns = sorted(self.change_format_dates_columns(balance_sheet.columns), reverse=True)
        result_sheet.columns = sorted(self.change_format_dates_columns(result_sheet.columns), reverse=True)
        cash_flow_sheet.columns = sorted(self.change_format_dates_columns(cash_flow_sheet.columns), reverse=True)
        return {
            "balance": balance_sheet,
            "result": result_sheet,
            "cash_flow": cash_flow_sheet
        }