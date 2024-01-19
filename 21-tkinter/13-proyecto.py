from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk

ventana = Tk()
ventana.minsize(500, 300)
# ventana.geometry("500x300")
ventana.title("Proyecto tkinter")
ventana.resizable(False, False)


# pantallas
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)
    products_box.grid(row=1)

    # listar
    # for product in products:
    #     if len(product) == 3:
    #         product.append('added')
    #         Label(products_box, text=product[0]).grid()
    #         Label(products_box, text=product[1]).grid()
    #         Label(products_box, text=product[2]).grid()
    #         Label(products_box, text="--------------------").grid()
    for product in products:
        if len(product) == 3:
            product.append('added')
            products_box.insert('', 0, text=product[0], values=(product[1]))

    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True


def add():
    # encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=110,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=12)
    # Campos
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=10, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=10, sticky=E)

    add_price_label.grid(row=1, column=3, padx=5, pady=10, sticky=E)
    add_price_entry.grid(row=1, column=4, padx=5, pady=10, sticky=E)

    add_description_label.grid(row=2, column=0, padx=5, pady=10, sticky=NE)
    add_description_entry.config(width=40, height=3, padx=4, pady=5, )
    add_description_entry.grid(row=2, column=1, columnspan=4, sticky=NE)

    add_boton.grid(row=3, column=1, columnspan=2, padx=0, pady=10, sticky=E)
    add_boton.config(
        fg="white",
        bg="green",
        bd=0,
        font=("Arial", 10),
        width=17
    )
    # Ocultar
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()
    return True


def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=150,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()
    return True


def add_product():
    try:
        price_float = float(price_data.get())
        products.append([
            name_data.get(),
            price_float,
            add_description_entry.get("1.0", "end-1c")
        ])
        name_data.set("")
        price_data.set("")
        add_description_entry.delete("1.0", END)
        home()
    except:
        MessageBox.showerror("Ingrese valores validos", "Ingrese valores validos para el precio")


# variables
products = []
name_data = StringVar()
price_data = StringVar()

# campos home
home_label = Label(ventana, text="Inicio")
# products_box = Frame(ventana)

products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)

# campos add
add_label = Label(ventana, text="Añadir producto")
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Nombre:")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción:")
add_description_entry = Text(add_frame)

add_boton = Button(add_frame, text="Guardar", command=add_product)
# campos info
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por: Edwin Ariza")

home()

menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

ventana.config(menu=menu_superior)

ventana.mainloop()
