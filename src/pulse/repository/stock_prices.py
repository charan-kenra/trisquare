from sqlalchemy import Column, String, DateTime, Float, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from pulse.repository.database_connect import DatabaseConnect
from datetime import datetime

Base = declarative_base()

class Stock_prices_table(Base):
    __tablename__ = 'stockprices'
    symbol = Column(String, primary_key=True)
    timestamp = Column(DateTime, primary_key=True)  # Change the data type to DateTime
    name = Column(String)
    price = Column(Float)
    changes_percentage = Column(Float)
    change = Column(Float)
    day_low = Column(Float)
    day_high = Column(Float)
    year_high = Column(Float)
    year_low = Column(Float)
    market_cap = Column(BigInteger)
    price_avg_50 = Column(Float)
    price_avg_200 = Column(Float)
    exchange = Column(String)
    volume = Column(Integer)
    avg_volume = Column(Integer)
    open_price = Column(Float)
    previous_close = Column(Float)
    eps = Column(Float)
    pe = Column(Float)
    earnings_announcement = Column(DateTime)
    shares_outstanding = Column(BigInteger)

    def load_data(self, json_data):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            for element in json_data:
                timestamp = datetime.fromtimestamp(element["timestamp"])
                existing_entry = session.query(Stock_prices_table).filter_by(symbol=element["symbol"], timestamp=timestamp).first()
                if not existing_entry :
                    stock_entry = Stock_prices_table(
                        symbol=element["symbol"],
                        timestamp = timestamp,
                        name=element["name"],
                        price=element["price"],
                        changes_percentage=element["changesPercentage"],
                        change=element["change"],
                        day_low=element["dayLow"],
                        day_high=element["dayHigh"],
                        year_high=element["yearHigh"],
                        year_low=element["yearLow"],
                        market_cap=element["marketCap"],
                        price_avg_50=element["priceAvg50"],
                        price_avg_200=element["priceAvg200"],
                        exchange=element["exchange"],
                        volume=element["volume"],
                        avg_volume=element["avgVolume"],
                        open_price=element["open"],
                        previous_close=element["previousClose"],
                        eps=element["eps"],
                        pe=element["pe"],
                        earnings_announcement=element["earningsAnnouncement"],
                        shares_outstanding=element["sharesOutstanding"]
                    )
                    session.add(stock_entry)

                session.commit()