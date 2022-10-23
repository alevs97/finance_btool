# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from src.app.app import App

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = App(symbol="MSFT", list_years=["2019","2020","2021"], list_ratios=['Current Ratio','Debt Ratio','Financial Leverage'])
    app2 = App(symbol="AAPL", list_years=["2019","2020","2021"], list_ratios=['Current Ratio','Debt Ratio','Financial Leverage'])



    print(app.get_result())
    print(app2.get_result())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
