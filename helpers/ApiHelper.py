import logging

from config.Constants import Constants

logger = logging.getLogger("ratings")


def validateAddProductRequest(request):
    valid = True
    if not request or 'productId' not in request or 'productPrice' not in request or 'productName' not in request or 'productCategory' not in request:
        valid = False
    return valid


def validateRemoveProductRequest(request):
    if not request or 'productId' not in request:
        return False
    else:
        return True


def getFailureResponse(response_code=None):
    if response_code == 400:
        return {Constants.STATUS_KEY: Constants.STATUS_FAILURE, Constants.MESSAGE_KEY: Constants.REQUEST_ERROR}
    else:
        return {Constants.STATUS_KEY: Constants.STATUS_FAILURE, Constants.MESSAGE_KEY: Constants.GENERIC_ERROR}


