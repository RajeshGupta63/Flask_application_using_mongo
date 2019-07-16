# app.py - a minimal flask api using flask_restful
import logging
from flask import Flask, render_template, request, jsonify
from api.v1.urlMappings import api_v1 as api_blueprint
from config.Config import Config
from config.Endpoints import Endpoints
from services.ProductService import ProductService
from core.models.Product import Product


app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix=Endpoints.PRODUCT_URL_PREFIX)
logger = logging.getLogger("products")

ProductService = ProductService()

def initializeLogging():
    logging.basicConfig(filename=Config.LOG_FILE, level=logging.DEBUG,
                        format=Config.LOG_PATTERN)
    logger.setLevel(logging.INFO)


@app.route('/get_product')
def get():
   return render_template('product.html')


@app.route('/product_search_result',  methods=['GET', 'POST', 'DELETE', 'PATCH'])
def getProduct(productId=None):
   if request.method == 'POST':
       productId = request.form['product_id']
       data = ProductService.getProductDetails(productId)
       return jsonify(data), 200

@app.route('/add_product', methods=['GET'])
def addProduct():
    return render_template('addProduct.html')

@app.route('/add_product_detail',  methods=['POST'])
def addProductDetails(productId=None):
   if request.method == 'POST':
       product_id = request.form['product_id']
       product_name=request.form['product_name']
       product_price=request.form['product_price']
       product_category=request.form['product_category']
       data = ProductService.addProduct(product_id, product_name, product_price, product_category)
       return jsonify(data), 200

@app.route('/delete_product')
def delete():
   return render_template('deleteProduct.html')


@app.route('/delete_product_detail',  methods=['GET', 'POST', 'DELETE', 'PATCH'])
def deleteProduct(productId=None):
   if request.method == 'POST':
       product_id = request.form['product_id']
       data = ProductService.removeProduct(product_id)
       return jsonify(data), 200


@app.route('/download_to_csv')
def download():
   return render_template('downloadToCSV.html')


@app.route('/download_product_detail',  methods=['GET', 'POST', 'DELETE', 'PATCH'])
def downloadProduct(file_path=None):
   if request.method == 'POST':
       file_name = request.form['file_path']
       return jsonify(ProductService.downloadProductToCSV(file_name))


@app.route('/upload_to_mongo')
def upload():
   return render_template('uploadToMongo.html')


@app.route('/upload_product_detail',  methods=['GET', 'POST', 'DELETE', 'PATCH'])
def uploadProduct(file_path=None):
   if request.method == 'POST':
       file_name = request.form['file_path']
       return jsonify(ProductService.uploadProductToMongo(file_name))

if __name__ == '__main__':
    initializeLogging()
    app.run(debug=True, host='localhost')
