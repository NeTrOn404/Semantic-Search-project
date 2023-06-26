from Server.Utils.pre_processor import Pre_Process, Format_Results
from Server.Utils.vdb import VectorDatabase
from Server.Utils.model import model
from flask import request, jsonify
from flask import Blueprint



#### Initiate the Vector Database
vdb = VectorDatabase()
vdb.connect()
vdb.load_papers()
vdb.load_videos()


search = Blueprint('seach', __name__)


@search.route('/videos/search')
def search_video():
    args = request.args
    query = args.get('query', None, str)
    offset = args.get('offset', 0 , int)
    processed_query = Pre_Process(query)

    encoded = model.encode(processed_query, show_progress_bar = True)

    results = vdb.search_videos([encoded], offset=offset)
    results = Format_Results(results)
    return jsonify(results)



@search.route('/papers/search')
def search_papers():
    args = request.args
    query = args.get('query', None, str)
    offset = args.get('offset', 0 , int)
    processed_query = Pre_Process(query)

    encoded = model.encode(processed_query, show_progress_bar = True)
    
    results = vdb.search_papers([encoded], offset=offset)
    results = Format_Results(results)
    return jsonify(results)