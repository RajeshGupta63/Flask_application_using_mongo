from flask import Blueprint

from api.v1.CatalogueController import addProduct , removeProduct , getProductDetails

from config.Endpoints import Endpoints

api_v1 = Blueprint('api.v1', __name__)

api_v1.add_url_rule(Endpoints.GET_PRODUCT, view_func=getProductDetails, methods=['GET'])
api_v1.add_url_rule(Endpoints.ADD_PRODUCT, view_func=addProduct, methods=['POST'])
api_v1.add_url_rule(Endpoints.REMOVE_PRODUCT, view_func=removeProduct, methods=['POST'])