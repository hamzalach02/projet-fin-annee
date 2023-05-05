import tkinter as tk
import mysql.connector
import io
from PIL import Image, ImageTk


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
        query = "SELECT nom_p,Q_stock,prix_u,image FROM produit"
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
            name_label = tk.Label(self.inner_frame, text=product[0], width=20, anchor="w")
            name_label.grid(row=row, column=col, padx=10, pady=5)
            price_label = tk.Label(self.inner_frame, text="${:.2f}".format(product[1]), width=10, anchor="w")
            price_label.grid(row=row, column=col+1, padx=10, pady=5)
            quantity_label = tk.Label(self.inner_frame, text=str(product[2]), width=10, anchor="w")
            quantity_label.grid(row=row, column=col+2, padx=10, pady=5)
           
            
            
        

            # Display the image
            img = Image.open(io.BytesIO(product[3]))
            img = img.resize((100, 100))
            photo = ImageTk.PhotoImage(img)
            image_label = tk.Label(self.inner_frame, image=photo)
            image_label.image = photo
            image_label.grid(row=row, column=col+3, padx=10, pady=5)

            col += 4
            if col > 3:
                col = 0
                row += 1

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def search_callback(self, *args):
        global search_term
        search_term = self.search_var.get()

    def search_callback_button(self, *args):
        search_trm = search_term
        self.filtered_products = [product for product in self.products if search_trm.lower() in product[0].lower()]
        self.display_products()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500")
    app = ProductWindow(root)
    root.mainloop()
