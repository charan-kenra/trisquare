from flask import Blueprint, jsonify
from pulse.repository.index_companies import SP500_table

# Sectors calls the methods that query from DB and creating API routes
sectors = Blueprint("sectors", __name__)

@sectors.route('/sectors', methods=['GET'])
def get_sectors():
    sp500_repo = SP500_table()
    return jsonify(sp500_repo.get_sectors())

@sectors.route('/sectors/subsectors', methods=['GET'])
def get_sectors_subsectors():
    sp500_repo = SP500_table()
    return jsonify(sp500_repo.get_sectors_subsectors())
