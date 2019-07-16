import time

import logging
from flask import jsonify, request

from config.Constants import Constants
from helpers.ApiHelper import  validateAddProductRequest ,getFailureResponse, validateRemoveProductRequest

from services.ProductService import ProductService

logger = logging.getLogger("ratings")

productService = ProductService()

def addProduct():
    """
    Adds a product rating or updates the existing rating if a corresponding NON-DELETED rating entry already exists.

    Requires: productId,productName,productPrice,productCategory in POST request.

    Note (not implemented for the scope of the project):
    - User Authentication
    - Check if the user has actually rented the furniture in the past that he/she is trying to rate.

    :return: HTTP Response containing corresponding rating entry from database.
    """
    request_dict = request.get_json()
    if validateAddProductRequest(request_dict):
        record = ProductService.addProduct(request_dict['productId'],request_dict['productName'],request_dict['productPrice'],request_dict['productCategory'])
        if record is not None:
            response = {Constants.STATUS_KEY: Constants.STATUS_SUCCESS}
            return jsonify(response)
        else:
            return jsonify(getFailureResponse())
    else:
        return jsonify(getFailureResponse(400)), 400



def removeProduct():
    """
    Removes the rating for a product.

    Requires: productId, userId in POST request.

    :return: success/failure
    """
    request_dict = request.get_json()
    if validateRemoveProductRequest(request_dict):
        if ProductService.removeProduct(request_dict) == 1:
            response = {Constants.STATUS_KEY: Constants.STATUS_SUCCESS, Constants.MESSAGE_KEY: Constants.REMOVE_SUCCESS}
        else:
            response = {Constants.STATUS_KEY: Constants.STATUS_FAILURE, Constants.MESSAGE_KEY: Constants.REMOVE_FAILURE}
        return jsonify(response)
    else:
        return jsonify(getFailureResponse(400)), 400

def getProductDetails(product_id):
    return ProductService.getProductDetails()