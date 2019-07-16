Tech stack used:
 
1. Flask
2. MongoDB



API documentation

### Product search page
Once the application has started successfully and database has been seeded with test data, open up your favorite web browser and go to http://127.0.0.1:5000/get_product.

Enter the product id you want to search


Screenshot
![Screenshot of Product Page](https://pasteboard.co/Ioc6crB.png)

Output screen shot

![Screenshot of Product Search Page](https://pasteboard.co/Ioc7awQ.png)



### Product add page
Once the application has started successfully and database has been seeded with test data, open up your favorite web browser and go to http://127.0.0.1:5000/add_product.

Enter the product description you want to add

a. Unique product code
b. Product Name
c. Product Price
d. Product category


Screenshot
![Screenshot of Product Add Page](https://pasteboard.co/Ioc8j6T.png)

Output screen shot

![Screenshot of Product Add output Page](https://pasteboard.co/Ioc8EHs.png)




### Product remove page
Once the application has started successfully and database has been seeded with test data, open up your favorite web browser and go to http://127.0.0.1:5000/delete_product.

Enter the product id which user want to remove

Screenshot
![Screenshot of Product Delete Page](https://pasteboard.co/Ioc9Fsi.png)

Output screen shot

![Screenshot of Product Delete output Page](https://pasteboard.co/Ioc9T44.png)




### Product catalogue upload page
Once the application has started successfully and database has been seeded with test data, open up your favorite web browser and go to http://127.0.0.1:5000/delete_product.

Enter the file from which user want to upload data to catalogue

File content should be in the below format

productId,productName,productPrice,productCategory

Screenshot
![Screenshot of Product catalogue upload Page](https://pasteboard.co/IocaxRp.png)

Output screen shot

![Screenshot of Product catalogue upload output Page](https://pasteboard.co/IocbjDs.png)


**After upload, connect to mongo and verify documents are uploaded to mongoDB

------------------------------------
> db.product.find()
{ "_id" : ObjectId("5d2c7cd4981b51b94eafae07"), "product_category" : "fashion", "product_id" : 2, "product_name" : "Jeans", "product_price" : 2 }
{ "_id" : ObjectId("5d2c7cd4981b51b94eafae09"), "product_category" : "fashion", "product_id" : 1, "product_name" : "Shirt", "product_price" : 100 }
{ "_id" : ObjectId("5d2c7cd4981b51b94eafae0b"), "product_category" : "logistics", "product_id" : 3, "product_name" : "rivigo", "product_price" : 500 }
{ "_id" : ObjectId("5d2c80c6981b51b94eafaeef"), "product_category" : "fashion", "product_id" : 200, "product_name" : "Jeans", "product_price" : 100 }
{ "_id" : ObjectId("5d2c8eed981b51b94eafb25f"), "product_category" : "dummy", "product_id" : 2000, "product_name" : "DummyProduct", "product_price" : 0 }
{ "_id" : ObjectId("5d2d56ca981b51b94eafb5be"), "product_category" : "hardware", "product_id" : 200, "product_name" : "Laptop", "product_price" : 300000 }
{ "_id" : ObjectId("5d2d56ca981b51b94eafb5c0"), "product_category" : "hardware", "product_id" : 201, "product_name" : "Mobile", "product_price" : 20000 }
{ "_id" : ObjectId("5d2d56ca981b51b94eafb5c2"), "product_category" : "stationary", "product_id" : 202, "product_name" : "Pen", "product_price" : 200 }
{ "_id" : ObjectId("5d2d5749981b51b94eafb5f8"), "product_category" : "software", "product_id" : 100, "product_name" : "Delphix", "product_price" : 100 }

---------------------------------------


### Product catalogue download page
Once the application has started successfully and database has been seeded with test data, open up your favorite web browser and go to http://127.0.0.1:5000/delete_product.

Enter the file name to which user want to download catalogue

File content will be in the below format

productId,productName,productPrice,productCategory

Screenshot
![Screenshot of Product catalogue download Page](https://pasteboard.co/IocdmNK.png)

Output screen shot

![Screenshot of Product catalogue download output Page](https://pasteboard.co/IocdIeY.png)


**After download open the file and verify the content

-----------------------------------
cat catalogue_16_jul.csv 
2,Jeans,2.0,fashion
1,Shirt,100.0,fashion
3,rivigo,500.0,logistics
2000,DummyProduct,0.0,dummy
201,Mobile,20000.0,hardware
202,Pen,200.0,stationary
100,Delphix,100.0,software
500,pencil,2.0,Stationary
-------------------------------------



------------
------------

