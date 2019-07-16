import logging

from flask import jsonify

from services.DatabaseService import database

logger = logging.getLogger("product")


class ProductService:
    def __init__(self):
        self.database = database

    def addProduct(self, product_id, product_name, product_price, product_category):

        if self.productDoesNotExist(product_id):
            saved_record = self.database.addProduct(product_id,product_name,product_price,product_category)
            if False:
                return "Error occured while saving"
            else:
                return "Successfully saved product"
        else:
            logger.error("Product already exist.")
            return "Product already exist"

    def productDoesNotExist(self, product_id):
        product = self.database.getProduct(product_id)
        print product
        if product is None:
            return True
        else:
            return False

    def getProductDetails(self,product_id) :
        if self.productDoesNotExist(product_id):
            logger.error("Product doesnot exist.")
            return "Product doesnot exist"
        else:
            product = self.database.getProduct(product_id)
            return product

    def removeProduct(self, product_id):
        if self.productDoesNotExist(product_id):
            logger.error("Product doesnot exist.")
            return "Product doesnot exist"
        else:
            self.database.removeProduct(product_id)
            return "Successfully removed product: {}".format(product_id)

    def downloadProductToCSV(self, file_name):
         return self.database.downloadProductToCSV(file_name)


    def uploadProductToMongo(self, file_name):
         return self.database.uploadProductToMongo(file_name)
