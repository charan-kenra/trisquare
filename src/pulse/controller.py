from pulse.fmpapi.get_api import SP500
from pulse.fmpapi.get_api import Nasdaq
from pulse.fmpapi.get_api import Dowjones
from pulse.fmpapi.get_api import Stockprices
from pulse.repository.index_companies import SP500_table
from pulse.repository.index_companies import NASDAQ_table
from pulse.repository.index_companies import DOWJONES_table
from pulse.repository.stock_prices import Stock_prices_table

class Controller():
# Controller calls the FMPAPI and gets the JSON data. 
# This data is passed to the tables for loading. 
# Mainly focus on loading all the index companies from SP500, NASDAQ and DOWJONES

    def load_index_companies():
        sp500_api = SP500()
        sp500_json_data = sp500_api.fetch()
        print("Fetched sp500 json data from API")

        sp500_repo = SP500_table()
        sp500_repo.load_data(sp500_json_data)
        print("loaded sp500 API data into sp500 table")


        nasdaq_api = Nasdaq()
        nasdaq_json_data = nasdaq_api.fetch()
        print("Fetched Nasdaq json data from API")

        nasdaq_repo = NASDAQ_table()
        nasdaq_repo.load_data(nasdaq_json_data)
        print("loaded Nasdaq API data into Nasdaq table")

        dowjones_api = Dowjones()
        dowjones_json_data = dowjones_api.fetch()
        print("Fetched Dowjones json data from API")

        dowjones_repo = DOWJONES_table()
        dowjones_repo.load_data(dowjones_json_data)
        print("loaded Dowjones API data into Dowjones table")


        stock_price_api = Stockprices()
        stock_price_json_data = stock_price_api.fetch()
        print("Fetched stock price json data from API")

        stock_price_repo = Stock_prices_table()
        stock_price_repo.load_data(stock_price_json_data)
        print("loaded stock price API data into stockprices table")


