from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from pulse.repository.database_connect import DatabaseConnect

Base = declarative_base()
class SP500_table(Base):
# Entity class for the DB table SP500 companies. 
# Manage all the operations like loading and fetching the data from the SP500 table.

    __tablename__ = 'sp500'
    id = Column(Integer)
    symbol = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)
    subSector = Column(String)
    headQuarter = Column(String)
    dateFirstAdded = Column(String)
    cik = Column(String)
    founded = Column(String)

    def load_data(self, data): 
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            for data_entry in data:
                existing_entry = session.query(SP500_table).filter_by(symbol=data_entry["symbol"]).first()
                if not existing_entry :
                    sp500_entry = SP500_table(
                        symbol=data_entry["symbol"],
                        name=data_entry["name"],
                        sector=data_entry["sector"],
                        subSector=data_entry["subSector"],
                        headQuarter=data_entry["headQuarter"],
                        dateFirstAdded=data_entry["dateFirstAdded"],
                        cik=data_entry["cik"],
                        founded=data_entry["founded"]
                    )
                    session.add(sp500_entry)
                    
                session.commit()
    
    def get_sectors(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            # Query the database for sectors
            sectors = session.query(SP500_table.sector).distinct().all()
            # Convert the data to a list of dictionaries
            data = [{"sector": sector} for sector, in sectors]
            return data
        
    def get_sectors_subsectors(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            sectors_and_subsectors = session.query(SP500_table.sector, SP500_table.subSector).distinct().all()
        # Convert the data to a list of dictionaries
            data = [{"sector": sector, "subSector": subsector} for sector, subsector in sectors_and_subsectors]
            return data


class NASDAQ_table(Base):
# Entity class for the DB table NASDAQ companies. 
# Manage all the operations like loading and fetching the data from the NASDAQ table.

    __tablename__ = 'nasdaq'
    id = Column(Integer)
    symbol = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)
    subSector = Column(String)
    headQuarter = Column(String)
    dateFirstAdded = Column(String)
    cik = Column(String)
    founded = Column(String)

    def load_data(self, data): 
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            for data_entry in data:
                existing_entry = session.query(NASDAQ_table).filter_by(symbol=data_entry["symbol"]).first()
                if not existing_entry :
                    nasdaq_entry = NASDAQ_table(
                        symbol=data_entry["symbol"],
                        name=data_entry["name"],
                        sector=data_entry["sector"],
                        subSector=data_entry["subSector"],
                        headQuarter=data_entry["headQuarter"],
                        dateFirstAdded=data_entry["dateFirstAdded"],
                        cik=data_entry["cik"],
                        founded=data_entry["founded"]
                    )
                    session.add(nasdaq_entry)
                    
                session.commit()

class DOWJONES_table(Base):
# Entity class for the DB table DOWJONES companies. 
# Manage all the operations like loading and fetching the data from the DOWJONES table.

    __tablename__ = 'dowjones'
    id = Column(Integer)
    symbol = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)
    subSector = Column(String)
    headQuarter = Column(String)
    dateFirstAdded = Column(String)
    cik = Column(String)
    founded = Column(String)

    def load_data(self, data): 
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            for data_entry in data:
                existing_entry = session.query(DOWJONES_table).filter_by(symbol=data_entry["symbol"]).first()
                if not existing_entry :
                    dowjones_entry = DOWJONES_table(
                        symbol=data_entry["symbol"],
                        name=data_entry["name"],
                        sector=data_entry["sector"],
                        subSector=data_entry["subSector"],
                        headQuarter=data_entry["headQuarter"],
                        dateFirstAdded=data_entry["dateFirstAdded"],
                        cik=data_entry["cik"],
                        founded=data_entry["founded"]
                    )
                    session.add(dowjones_entry)
                    
                session.commit()