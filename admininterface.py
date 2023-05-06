import tkinter as tk
import mysql.connector
import io
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import subprocess



class ProductWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Product Window")
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill="both", expand=True)


        
        

        # create search bar
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.search_callback)
        self.search_entry = tk.Entry(self.frame, textvariable=self.search_var, width=20)
        self.search_entry.pack(side="top", padx=10, pady=5)
        self.search_button = tk.Button(self.frame, text="Search", command=self.search_callback_button)
        self.search_button.pack(side="top", padx=10, pady=5)
        self.search_button = tk.Button(self.frame, text="ajouter un produit", command=self.ajouterproduit)
        self.search_button.pack(side="top", padx=10, pady=5)

        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.inner_frame = tk.Frame(self.canvas,bg="#369E98")
        self.canvas.create_window((50, 0), window=self.inner_frame, anchor="nw")
       

        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_stock"
        )
        cursor = cnx.cursor()
        query = "SELECT * FROM produit"
        cursor.execute(query)
        self.products = cursor.fetchall()

        # add the products to the window
        self.filtered_products = self.products[:]
        self.display_products()
       

    def display_products(self):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        row = 0
        col = 0
        
        
        for i, product in enumerate(self.filtered_products):
            
            id_label = tk.Label(self.inner_frame, text=product[0], width=20, anchor="w")
            id_label.grid(row=row, column=col, padx=10, pady=5)
            
            name_label = tk.Label(self.inner_frame, text=product[1], width=20, anchor="w")
            name_label.grid(row=row, column=col+1, padx=10, pady=5)

            desc_label= tk.Label(self.inner_frame, text=product[2], width=20, anchor="w")
            desc_label.grid(row=row, column=col+2, padx=10, pady=5)

            price_label = tk.Label(self.inner_frame, text="${:.2f}".format(product[3]), width=10, anchor="w")
            price_label.grid(row=row, column=col+3, padx=10, pady=5)


            quantity_label = tk.Label(self.inner_frame, text=str(product[4]), width=10, anchor="w")
            quantity_label.grid(row=row, column=col+4, padx=10, pady=5)
            


            dde_label= tk.Label(self.inner_frame, text=str(product[5]), width=10, anchor="w")
            dde_label.grid(row=row, column=col+5, padx=10, pady=5)


            dds_label= tk.Label(self.inner_frame, text=str(product[6]), width=10, anchor="w")
            dds_label.grid(row=row, column=col+6, padx=10, pady=5)
          



            

            rembuttons=tk.Button(self.inner_frame, width=10, text="remove",anchor="w",bg="red", command=lambda id=product[0]: self.remove_product(id))

            rembuttons.grid(row=row, column=col+8, padx=10, pady=5)
            editbutton=tk.Button(self.inner_frame, width=10, text="edit",anchor="w",bg="skyblue", command=lambda id=product[0]: self.modifier_p(id))

            editbutton.grid(row=row, column=col+9, padx=10, pady=5)
            
            
            

            # Display the image
            img = Image.open(io.BytesIO(product[7]))
            img = img.resize((100, 100))
            photo = ImageTk.PhotoImage(img)
            image_label = tk.Label(self.inner_frame, image=photo)
            image_label.image = photo
            image_label.grid(row=row, column=col+7, padx=10, pady=5)
           
            col += 10
            if col > 9:
                col = 0
                row += 1


           


           
    def remove_product(self, product_id):
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_stock"
        )
        cursor = cnx.cursor()
        query = "DELETE FROM produit WHERE id_p = %s"
        cursor.execute(query, (product_id,))
        cnx.commit()
        cursor.close()
        cnx.close()

        # Update the list of products and redisplay them
        self.products = [product for product in self.products if product[0] != product_id]
        self.filtered_products = self.products[:]
        self.display_products()

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def search_callback(self, *args):
        global search_term
        search_term = self.search_var.get()

    def search_callback_button(self, *args):
        search_trm = search_term
        self.filtered_products = [product for product in self.products if search_trm.lower() in product[1].lower()]
        self.display_products()

    def ajouterproduit(self):
         self.frame.destroy()
         
         
         self.frame2= tk.Frame(self.master,bg="#369E98")
         self.frame2.pack(fill="both", expand=True)
        

         self.id_label = tk.Label(self.frame2, text="Product ID:")
         self.id_label.pack(side="top", padx=10, pady=10)
         self.id_entry = tk.Entry(self.frame2)
         self.id_entry.pack(side="top", padx=10, pady=10)
            
         self.name_label = tk.Label(self.frame2, text="Product Name:")
         self.name_label.pack(side="top", padx=10, pady=10)
         self.name_entry = tk.Entry(self.frame2)
         self.name_entry.pack(side="top", padx=10, pady=10)

         self.desc_label = tk.Label(self.frame2, text="Product Description:")
         self.desc_label.pack(side="top", padx=10, pady=10)
         self.desc_entry = tk.Entry(self.frame2)
         self.desc_entry.pack(side="top", padx=10, pady=10)

         self.price_label = tk.Label(self.frame2, text="Product Price:")
         self.price_label.pack(side="top", padx=10, pady=10)
         self.price_entry = tk.Entry(self.frame2)
         self.price_entry.pack(side="top", padx=10, pady=10)

         self.qty_label = tk.Label(self.frame2, text="Product Quantity:")
         self.qty_label.pack(side="top", padx=10, pady=10)
         self.qty_entry = tk.Entry(self.frame2)
         self.qty_entry.pack(side="top", padx=10, pady=10)

         self.select_file_button = tk.Button(self.frame2, text="Select Image", command=self.select_file)
         self.select_file_button.pack(side="top", padx=10, pady=10)

         self.image_label = tk.Label(self.frame2)
         self.image_label.pack(side="top", padx=10, pady=10)

         self.add_button = tk.Button(self.frame2, text="Add Product", command=self.add_product)
         self.add_button.pack(side="top", padx=10, pady=10)

         self.add_button_back= tk.Button(self.frame2, text="back to products",command=self.back)
         self.add_button_back.pack(side="top", padx=10, pady=10)


                # Connect to the MySQL database
         self.cnx = mysql.connector.connect(user='root', password='', host='localhost', database='gestion_stock')
         self.cursor = self.cnx.cursor()


         

    def select_file(self):
                self.file_path = filedialog.askopenfilename()
                if self.file_path:
                    with open(self.file_path, 'rb') as file:
                        self.file_data = file.read()
                    image = Image.open(self.file_path)
                    image.thumbnail((30, 30), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(image)
                    self.image_label.config(image=photo)
                    self.image_label.image = photo
    def add_product(self):
                try:
                    insert_query = "INSERT INTO produit (id_p,nom_p, desc_p, prix_u, Q_stock, image) VALUES (%s,%s, %s, %s, %s, %s)"
                    values = (self.id_entry.get(),self.name_entry.get(), self.desc_entry.get(), self.price_entry.get(), self.qty_entry.get(), self.file_data)
                    self.cursor.execute(insert_query, values)
                    self.cnx.commit()
                    print("Product added to database")
                except mysql.connector.Error as error:
                    print("Failed to add product to database: {}".format(error))


    def modifier_p(self,product_id):
         
         self.frame.destroy()
         self.p_id=product_id
         
         self.frame3= tk.Frame(self.master,bg="#369E98")
         self.frame3.pack(fill="both", expand=True)
            
         self.name_label = tk.Label(self.frame3, text="Product Name:")
         self.name_label.pack(side="top", padx=10, pady=10)
         self.name_entry = tk.Entry(self.frame3)
         self.name_entry.pack(side="top", padx=10, pady=10)

         self.desc_label = tk.Label(self.frame3, text="Product Description:")
         self.desc_label.pack(side="top", padx=10, pady=10)
         self.desc_entry = tk.Entry(self.frame3)
         self.desc_entry.pack(side="top", padx=10, pady=10)

         self.price_label = tk.Label(self.frame3, text="Product Price:")
         self.price_label.pack(side="top", padx=10, pady=10)
         self.price_entry = tk.Entry(self.frame3)
         self.price_entry.pack(side="top", padx=10, pady=10)

         self.qty_label = tk.Label(self.frame3, text="Product Quantity:")
         self.qty_label.pack(side="top", padx=10, pady=10)
         self.qty_entry = tk.Entry(self.frame3)
         self.qty_entry.pack(side="top", padx=10, pady=10)

         self.add_edit= tk.Button(self.frame3, text="edit product",command=self.edit)
         self.add_edit.pack(side="top", padx=10, pady=10)
         self.add_button_back= tk.Button(self.frame3, text="back to products",command=self.back)
         self.add_button_back.pack(side="top", padx=10, pady=10)

    def edit(self):
         cnx = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="",
                     database="gestion_stock"
                     )
         cursor = cnx.cursor()
         query = "UPDATE produit SET nom_p = %s, prix_u = %s,desc_p= %s ,Q_stock = %s WHERE id_p = %s"
         values = (self.name_entry.get(), self.price_entry.get(),self.desc_entry.get() ,self.qty_entry.get(),self.p_id)
         cursor.execute(query, values)
         cnx.commit()
         cursor.close()
         cnx.close()

        # Update the list of products and redisplay them
         self.master.destroy()    
         subprocess.call(["python", "admininterface.py"])

         

        
         

         

         

         



    def back(self):
         self.master.destroy()    
         subprocess.call(["python", "admininterface.py"])

    
        
 

       
  

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1300x600")
    app = ProductWindow(root)
    root.mainloop()
