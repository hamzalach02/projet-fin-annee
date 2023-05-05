#======create database and table=======
import mysql.connector
import io
from PIL import Image

# #Connect to the new database
# cnx = mysql.connector.connect(
#     host="localhost",
#     user="yourusername",
#     password="yourpassword",
#     database="gestion_stock"
# )
# cursor = cnx.cursor()

# # Create a table named "produit" with columns for product name, description, unit price, stock quantity, and image
# create_table_query = """
# CREATE TABLE produit (
#     id_p INT(11) NOT NULL AUTO_INCREMENT,
#     nom_p VARCHAR(255) NOT NULL,
#     desc_p VARCHAR(255),
#     prix_u DECIMAL(10, 2) NOT NULL,
#     Q_stock INT(11) NOT NULL,
#     image LONGBLOB NOT NULL,
#     PRIMARY KEY (id_p)
# )"""
# cursor.execute(create_table_query)

# #Commit the changes and close the cursor and database connection
# cnx.commit()
# cursor.close()
# cnx.close()





#=======insert to data base========= 


# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestion_stock"
)
cursor = cnx.cursor()

# Insert 20 products with their respective keys and images
for i in range(1, 21):
    # Read the image file
    image_file_path = f"product_img/img_{i}.jpg"
    with open(image_file_path, 'rb') as f:
        image_binary_data = f.read()

    # Insert the product data
    insert_query = "INSERT INTO produit (nom_p, desc_p, prix_u, Q_stock, image) VALUES (%s, %s, %s, %s, %s)"
    product_data = (f"Product {i}", f"Description of Product {i}", i* 10.00, i* 100, image_binary_data)
    cursor.execute(insert_query, product_data)

# Commit the changes and close the cursor and database connection
cnx.commit()
cursor.close()
cnx.close()