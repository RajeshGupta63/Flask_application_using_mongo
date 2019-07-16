import unittest
import logging
import os
from services.ProductService import ProductService
logger = logging.getLogger("test.log")
ProductService = ProductService()


class TestUtils(unittest.TestCase):


    def test_insert_an_new_product(self):
            ProductService.removeProduct(100)
            response=ProductService.addProduct(100, 'Delphix', 100, 'software')
            self.assertEqual("Successfully saved product",response)

    def test_insert_an_already_existing_product(self):
        ProductService.addProduct(100, 'Delphix', 100, 'software')
        response = ProductService.addProduct(100, 'Delphix', 100, 'software')
        self.assertEqual("Product already exist",response)


    def test_delete_an_existing_product(self):
        ProductService.addProduct(100, 'Delphix', 100, 'software')
        response = ProductService.removeProduct(100)
        self.assertEqual("Successfully removed product: 100",response)

    def test_delete_an_non_existing_product(self):
        ProductService.removeProduct(100)
        response = ProductService.removeProduct(100)
        self.assertEqual("Product doesnot exist",response)

    def test_get_an_existing_product(self):
         ProductService.addProduct(100, 'Delphix', 100, 'software')
         response=ProductService.getProductDetails(100)
         self.assertEqual(response[0], 100)
         self.assertEqual(response[1], "Delphix")
         self.assertEqual(response[2], 100.0)
         self.assertEqual(response[3], "software")

    def test_get_an_non_existing_product(self):
         ProductService.removeProduct(100)
         response=ProductService.getProductDetails(100)
         self.assertEqual("Product doesnot exist",response)

    def test_download_data_from_a_file(self):
        if os.path.exists("delphix.csv"):
            os.remove("delphix.csv")
        else:
            print("Can not delete the file as it doesn't exists")
        response=ProductService.downloadProductToCSV("delphix.csv")
        self.assertEqual("Successfully downloaded data to file: delphix.csv",response)

    def test_upload_data_to_mongo(self):
        response = ProductService.uploadProductToMongo("upload.csv")
        self.assertEqual("Successfully uploaded data to MongoDB from file: upload.csv", response)

if __name__ == '__main__':
    unittest.main()
