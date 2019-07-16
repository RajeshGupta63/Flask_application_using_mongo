import csv
import logging
from flask import jsonify
from mongoengine import *

from core.models.Product import Product

logger = logging.getLogger("ratings")


class DatabaseService:
    def __init__(self):
        try:

            # self.connection = connect("delphix", host=os.environ['DB_PORT_27017_TCP_ADDR'], port=27017)

            self.connection = connect("delfix", host='127.0.0.1', port=27017)
        except MongoEngineConnectionError:
            logger.exception("Fatal Error. Connection to the database can not be established.")

    @staticmethod
    def addProduct(product_id,product_name,product_price,product_category):
        try:
            record = Product.objects(product_id=product_id,product_name=product_name,product_price=product_price, product_category=product_category)
            record.update_one(set__product_id=product_id , upsert=True)
            return jsonify(record.first()['product_id'])
        except Exception:
            logger.exception("Error occurred while saving record")
            return False

    @staticmethod
    def removeProduct(product_id):
        try:
            dropped = Product.objects(product_id=product_id).delete()
            return dropped
        except Exception:
            logger.exception("Error occurred while removing product")
            return "Error while deleting product: {}".format(product_id)

    @staticmethod
    def downloadProductToCSV(file_path):
        count=0
        for e in Product.objects.all():
            l=[e.product_id, e.product_name, e.product_price, e.product_category]
            writer = csv.writer(open(file_path, 'a'), delimiter=',')
            writer.writerows([l])
            count += 1
        if count>0:
            return "Successfully downloaded data to file: {}".format(file_path)
        else:
            return "No data downloaded to file: {}".format(file_path)

    @staticmethod
    def uploadProductToMongo(file_path):
        count = 0
        reader = csv.reader(open(file_path, 'r'), delimiter=',')
        for raw in reader:
            record= Product.objects(product_id=raw[0], product_name=raw[1], product_price=raw[2],product_category=raw[3])
            record.update_one(set__product_id=raw[0], upsert=True)
            count += 1
        if count>0:
            return "Successfully uploaded data to MongoDB from file: {}".format(file_path)
        else:
            return "No data uploaded to MongoDB from file: {}".format(file_path)

    @staticmethod
    def getProduct(product_id):
        try:
            product = Product.objects(product_id=product_id).first()
            return product['product_id'], product['product_name'], product['product_price'], product['product_category']
        except Exception:
            logger.exception("Error while fetching product: {}".format(product_id))
            return None


# Initializing a singleton instance
database = DatabaseService()
