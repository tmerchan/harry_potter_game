import tkinter as tk
import funciones_email as em
import funciones_botones as fb
import mysql.connector
import re
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.constants import E, LEFT, RIGHT, W
from typing import Text
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter import messagebox

LARGEFONT = ("Times New Roman", 48)
SIMPLETEXT = ("Times New Roman", 20)
WIDTH, HEIGHT = 1200, 750


class tkinterApp(tk.Tk):
    # __init__ function para la clase tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function para la clase Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creando un container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # inicializando frames en un array vacio
        self.frames = {}

        for F in (
            StartPage,
            Page1,
            Page2,
            Page3,
            Page4,
            Page5,
            Page6,
            Page7,
            Page8,
            Page9,
            Page10,
        ):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # para mostrar el frame que se pasa por parametro
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# primera ventana - startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Display image on a Label widget.
        img = ImageTk.PhotoImage(
            Image.open("img/hola.png").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        )
        label = tk.Label(self, image=img)
        label.img = img  # Keep a reference in case this code put is in a function.
        label.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Place label in center of parent.

        label2 = tk.Label(
            self, text="Bienvenido", background="#1A1A20", fg="#EBC34E", font=LARGEFONT
        )
        label2.pack(side=LEFT, expand=False, anchor="nw")

        label3 = tk.Label(
            self,
            text="Que deseas hacer?",
            background="#1A1A20",
            fg="#EBC34E",
            font=SIMPLETEXT,
        )
        label3.place(x=30, y=260)

        button1 = tk.Button(
            self,
            text="Descubrir a que casa pertenezco",
            command=lambda: fb.iniciar_test(Page1, controller),
            background="#1A1A20",
            fg="#EBC34E",
            font=("Times New Roman", 14),
        )
        button1.place(x=80, y=350)

        button2 = tk.Button(
            self,
            text="Ir a buscar mi varita",
            font=("Times New Roman", 14),
            background="#1A1A20",
            fg="#EBC34E",
            command=lambda: controller.show_frame(Page7),
        )
        button2.place(x=80, y=430)

        button3 = tk.Button(
            self,
            text="Me hice un amigo en el camino a Hogwarts, y quiero guardar su contacto",
            command=lambda: controller.show_frame(Page10),
            background="#1A1A20",
            fg="#EBC34E",
            font=("Times New Roman", 14),
        )
        button3.place(x=80, y=510)


# segunda ventana
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Display image on a Label widget.
        img = ImageTk.PhotoImage(
            Image.open("img/dinning_room.png").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        )
        label = tk.Label(self, image=img)
        label.img = img  # Keep a reference in case this code put is in a function.
        label.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Place label in center of parent.

        label2 = tk.Label(
            self,
            text="Permita al Sombrero Seleccionador colocarlo en su legítima casa de Hogwarts.",
            background="#1A1A20",
            fg="#EBC34E",
            font=("Times New Roman", 20),
        )
        label2.pack()
        label2.place(x=180, y=150)

        button = tk.Button(
            self,
            text="Ok! Comencemos",
            command=lambda: controller.show_frame(Page2),
            background="#1A1A20",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button.pack()
        button.place(x=490, y=290)


# tercera ventana
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        img = ImageTk.PhotoImage(
            Image.open("img/fondo3.png").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        )
        label = tk.Label(self, image=img)
        label.img = img  # Keep a reference in case this code put is in a function.
        label.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Place label in center of parent.

        label1 = tk.Label(
            self,
            text="¿Qué es lo que más esperas aprender en Hogwarts?",
            font=SIMPLETEXT,
            background="#000000",
            fg="#CEA10C",
        )
        label1.pack()
        label1.place(x=300, y=75)

        self.photo = PhotoImage(file="img/animales.png")
        self.photoimage = self.photo.subsample(2, 2)
        button = tk.Button(
            self,
            text="Todo sobre criaturas mágicas y cómo hacerse cuidar de ellas",
            image=self.photoimage,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_primer_frame(
                Page3, controller, "Hufflepuff"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button.pack()
        button.place(x=100, y=150)

        self.photo1 = PhotoImage(file="img/aparicion.png")
        self.photoimage1 = self.photo1.subsample(4, 4)
        button1 = tk.Button(
            self,
            text="Aparición y desaparición (poder materializarse\n y desmaterializarse a voluntad)",
            image=self.photoimage1,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_primer_frame(
                Page3, controller, "Ravenclaw"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button1.pack()
        button1.place(x=590, y=150)

        self.photo2 = PhotoImage(file="img/secretos.png")
        self.photoimage2 = self.photo2.subsample(3, 3)
        button2 = tk.Button(
            self,
            text="Secretos sobre el castillo",
            image=self.photoimage2,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_primer_frame(
                Page3, controller, "Slytherin"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button2.pack()
        button2.place(x=180, y=450)

        self.photo3 = PhotoImage(file="img/transformacion.png")
        self.photoimage3 = self.photo3.subsample(4, 4)
        button3 = tk.Button(
            self,
            text="Transformación (convertir un objeto en otro objeto) ",
            image=self.photoimage3,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_primer_frame(
                Page3, controller, "Gryffindor"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button3.pack()
        button3.place(x=590, y=450)


# cuarta ventana
class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        img = ImageTk.PhotoImage(
            Image.open("img/fondo3.png").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        )
        label = tk.Label(self, image=img)
        label.img = img  # Keep a reference in case this code put is in a function.
        label.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Place label in center of parent.

        label1 = tk.Label(
            self,
            text="Se colocan cuatro copas ante ti. ¿Cuál elegirías para beber?",
            font=SIMPLETEXT,
            background="#000000",
            fg="#CEA10C",
        )
        label1.pack()
        label1.place(x=300, y=75)

        self.photo = PhotoImage(file="img/bebidapurpura.png")
        self.photoimage = self.photo.subsample(2, 2)
        button = tk.Button(
            self,
            text="La bebida suave, espesa y de un color púrpura intenso\n que desprende un delicioso olor a chocolate y ciruelas",
            image=self.photoimage,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_segundo_frame(
                Page4, controller, "Ravenclaw"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button.pack()
        button.place(x=100, y=150)

        self.photo1 = PhotoImage(file="img/bebidanegra.png")
        self.photoimage1 = self.photo1.subsample(4, 4)
        button1 = tk.Button(
            self,
            text="El misterioso líquido negro que reluce como tinta y \ndesprende vapores que te hacen ver extrañas visiones",
            image=self.photoimage1,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_segundo_frame(
                Page4, controller, "Gryffindor"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button1.pack()
        button1.place(x=590, y=150)

        self.photo2 = PhotoImage(file="img/bebidaplateada.png")
        self.photoimage2 = self.photo2.subsample(2, 2)
        button2 = tk.Button(
            self,
            text="El líquido espumoso y plateado que\n brilla como si tuviera diamantes molidos",
            image=self.photoimage2,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_segundo_frame(
                Page4, controller, "Slytherin"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button2.pack()
        button2.place(x=100, y=450)

        self.photo3 = PhotoImage(file="img/bebidadorada.png")
        self.photoimage3 = self.photo3.subsample(3, 3)
        button3 = tk.Button(
            self,
            text="El líquido dorado tan brillante que duele la vista\n y que hace bailar las manchas solares por toda la habitación",
            image=self.photoimage3,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_segundo_frame(
                Page4, controller, "Hufflepuff"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button3.pack()
        button3.place(x=590, y=450)


# quinta ventana
class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        img = ImageTk.PhotoImage(
            Image.open("img/fondo2.png").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        )
        label = tk.Label(self, image=img)
        label.img = img  # Keep a reference in case this code put is in a function.
        label.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Place label in center of parent.

        label1 = tk.Label(
            self,
            text="¿Cuál de las siguientes opciones odiaría más que la gente lo llamara?",
            font=SIMPLETEXT,
            background="#000000",
            fg="#CEA10C",
        )
        label1.pack()
        label1.place(x=200, y=75)

        button = tk.Button(
            self,
            text="Ignorante",
            command=lambda: fb.guardar_respuesta_tercer_frame(
                Page5, controller, "Ravenclaw"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 40),
        )
        button.pack()
        button.place(x=100, y=150)

        button1 = tk.Button(
            self,
            text="Egoísta",
            command=lambda: fb.guardar_respuesta_tercer_frame(
                Page5, controller, "Hufflepuff"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 40),
        )
        button1.pack()
        button1.place(x=590, y=150)

        button2 = tk.Button(
            self,
            text="Ordinario",
            command=lambda: fb.guardar_respuesta_tercer_frame(
                Page5, controller, "Slytherin"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 40),
        )
        button2.pack()
        button2.place(x=100, y=450)

        button3 = tk.Button(
            self,
            text="Cobarde",
            command=lambda: fb.guardar_respuesta_tercer_frame(
                Page5, controller, "Gryffindor"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 40),
        )
        button3.pack()
        button3.place(x=590, y=450)


# septima ventana
class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        img = ImageTk.PhotoImage(
            Image.open("img/fondo3.png").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        )
        label = tk.Label(self, image=img)
        label.img = img  # Keep a reference in case this code put is in a function.
        label.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Place label in center of parent.

        label1 = tk.Label(
            self,
            text="¿Que camino te tienta más?",
            font=SIMPLETEXT,
            background="#000000",
            fg="#CEA10C",
        )
        label1.pack()
        label1.place(x=300, y=75)

        self.photo = PhotoImage(file="img/bosque.png")
        self.photoimage = self.photo.subsample(7, 7)
        button = tk.Button(
            self,
            text="El camino retorcido y cubierto de hojas a través del bosque",
            image=self.photoimage,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_cuarto_frame(
                Page6, controller, "Gryffindor"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button.pack()
        button.place(x=100, y=150)

        self.photo1 = PhotoImage(file="img/carril.png")
        self.photoimage1 = self.photo1.subsample(3, 3)
        button1 = tk.Button(
            self,
            text="El carril ancho, soleado y cubierto de hierba",
            image=self.photoimage1,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_cuarto_frame(
                Page6, controller, "Hufflepuff"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button1.pack()
        button1.place(x=590, y=150)

        self.photo2 = PhotoImage(file="img/callejon.png")
        self.photoimage2 = self.photo2.subsample(4, 4)
        button2 = tk.Button(
            self,
            text="El callejón estrecho, oscuro e iluminado por linternas",
            image=self.photoimage2,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_cuarto_frame(
                Page6, controller, "Slytherin"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button2.pack()
        button2.place(x=100, y=450)

        self.photo3 = PhotoImage(file="img/adoquines.png")
        self.photoimage3 = self.photo3.subsample(3, 3)
        button3 = tk.Button(
            self,
            text="La calle adoquinada bordeada de edificios antiguos",
            image=self.photoimage3,
            compound=BOTTOM,
            command=lambda: fb.guardar_respuesta_cuarto_frame(
                Page6, controller, "Ravenclaw"
            ),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button3.pack()
        button3.place(x=590, y=445)


# octava ventana
class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Display image on a Label widget.
        img = ImageTk.PhotoImage(
            Image.open("img/fondo3.png").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        )
        label = tk.Label(self, image=img)
        label.img = img  # Keep a reference in case this code put is in a function.
        label.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Place label in center of parent.

        label2 = tk.Label(
            self,
            text='"Oh, podrás pensar que no soy bonito, pero no juzgues por lo que ves. \n Me comeré a mi mismo si puedes encontrar un sombrero más inteligente que yo. \nPuedes tener bombines negros, sombreros altos y elegantes. \nPero yo soy el Sombrero Seleccionador de Hogwarts y puedo superar a todos. \nNo hay nada escondido en tu cabeza que el Sombrero Seleccionador no pueda ver. \nAsí que pruébeme y te diré dónde debes estar"',
            background="#000000",
            fg="#EBC34E",
            font=("Times New Roman", 25),
        )
        label2.pack()
        label2.place(x=80, y=40)

        self.photo = PhotoImage(file="img/Sombrero.png")
        self.photoimage = self.photo.subsample(2, 2)
        button = tk.Button(
            self,
            image=self.photoimage,
            compound=TOP,
            text="CLIC AQUI PARA CONOCER SU CASA",
            command=lambda: fb.validate_entry(name.get()),
            background="#000000",
            fg="#CEA10C",
            font=("Times New Roman", 14),
        )
        button.pack()
        button.place(x=400, y=390)

        label3 = tk.Label(
            self,
            text="Ingrese aquí su correo electrónico por favor:",
            background="#000000",
            fg="#EBC34E",
            font=("Times New Roman", 18),
        )
        label3.pack()
        label3.place(x=160, y=290)

        name = tk.StringVar()
        nameEntered = ttk.Entry(self, width=80, textvariable=name)
        nameEntered.pack()
        nameEntered.place(x=600, y=299)

        button1 = tk.Button(
            self,
            text="Volver",
            command=lambda: fb.volver_a_empezar(StartPage, controller),
            font=("Times New Roman", 14),
        )
        button1.place(x=1100, y=690)


# novena ventana
class Page7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mibase = mysql.connector.connect(host="localhost", user="root", passwd="")
        micursor = mibase.cursor()
        micursor.execute("CREATE DATABASE IF NOT EXISTS varitas")

        create_table_query = """
        CREATE TABLE IF NOT EXISTS varitas(
            id INT AUTO_INCREMENT PRIMARY KEY,
            madera VARCHAR(255),
            nucleo VARCHAR(255)
        )
        """
        mibase = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="varitas"
        )
        micursor = mibase.cursor()
        micursor.execute(create_table_query)
        mibase.commit()

        create_inventario_query = """
        INSERT INTO
        `varitas` (`madera`, `nucleo`)
        VALUES
        ('Arce', 'Pelo de dragón'),
        ('Alamo', 'Pluma de fenix'),
        ('Espino', 'Diente de unicornio'),
        ('Fresno', 'Pelo de unicornio'),
        ('Arce', 'Fibra de corazón de dragón'),
        ('Alamo', 'Pelo de cola de thestral'),
        ('Espino', 'Bigotes de trol'),
        ('Fresno', 'Pelo de veela')
        """
        micursor = mibase.cursor()
        micursor.execute(create_inventario_query)
        mibase.commit()

        # Display image on a Label widget.
        img = ImageTk.PhotoImage(
            Image.open("img/olivander2.png").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        )
        label = tk.Label(self, image=img)
        label.img = img  # Keep a reference in case this code put is in a function.
        label.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Place label in center of parent.

        label2 = tk.Label(
            self,
            text="La mayoría de los magos y brujas compran sus varitas en la tienda de varitas de Ollivander \nen el Callejón Diagon, donde pueden probar varias varitas hasta que encuentran la que más\n les conviene, o mejor dicho, la varita encuentra la bruja o mago que más le convenga.\n A continuación, entraras a Ollivander's, la mejor tienda fabricante de varitas.",
            background="#1A1A20",
            fg="#EBC34E",
            font=("Times New Roman", 20),
        )
        label2.pack()
        label2.place(x=90, y=150)

        button = tk.Button(
            self,
            text="Muy bien",
            command=lambda: controller.show_frame(Page8),
            background="#1A1A20",
            fg="#CEA10C",
            font=("Times New Roman", 16),
        )
        button.pack()
        button.place(x=550, y=350)


# octava ventana
class Page8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Display image on a Label widget.
        img = ImageTk.PhotoImage(
            Image.open("img/varitas.png").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        )
        label = tk.Label(self, image=img)
        label.img = img  # Keep a reference in case this code put is in a function.
        label.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Place label in center of parent.

        label2 = tk.Label(
            self,
            text="Una varita es un instrumento mágico casi sensible a través del cual una bruja o mago canaliza \nsu poder mágico para centralizar los efectos para obtener resultados más complejos.\n Cada varita individual es única y su carácter dependerá del tipo de árbol y de la \ncriatura mágica de la que deriva sus materiales. Además, cada varita, desde el momento \nen que encuentra a su dueño ideal, comenzará a aprender y a enseñar a su compañero humano.",
            background="#1A1A20",
            fg="#EBC34E",
            font=("Times New Roman", 20),
        )
        label2.pack()
        label2.place(x=90, y=150)

        label3 = tk.Label(
            self,
            text="Al ingresar al local, sientes una sensación de calidez. En tu interior, sabes que estás próximo\n a conocer a tu varita definitiva. ",
            background="#1A1A20",
            fg="#EBC34E",
            font=("Times New Roman", 20),
        )
        label3.pack()
        label3.place(x=90, y=350)

        button = tk.Button(
            self,
            text="Quiero saber cual es mi varita!",
            command=lambda: fb.ver_que_varita_toco(Page9, controller),
            background="#1A1A20",
            fg="#CEA10C",
            font=("Times New Roman", 16),
        )
        button.pack()
        button.place(x=490, y=590)


class Page9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Display image on a Label widget.
        img = ImageTk.PhotoImage(
            Image.open("img/olivander1.png").resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        )
        label = tk.Label(self, image=img)
        label.img = img  # Keep a reference in case this code put is in a function.
        label.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Place label in center of parent.

        label2 = tk.Label(
            self,
            text="En casi todos los casos documentados, la varita elige al mago que coincide con su personalidad,\n porque el mago puede tener dificultades o no al realizar magia si las características de la varita entran en \nconflicto, o la magia puede ser inferior a la magia realizada con una varita correspondiente.\n Aunque Ollivander dice que los magos pueden canalizar sus poderes a través de casi cualquier cosa, \nlos resultados óptimos solo se pueden lograr con aquellos con los que tienen una afinidad natural. \nAl probar varitas diferentes, una varita que no es adecuada para su portador generalmente no hará nada en absoluto.\n Sin embargo, un sentimiento cálido es una indicación de haber elegido la varita correcta, \ny la varita a veces emite algunas chispas o hace algún signo similar de magia.",
            background="#1A1A20",
            fg="#EBC34E",
            font=("Times New Roman", 18),
        )
        label2.pack()
        label2.place(x=30, y=150)

        button1 = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(StartPage),
            font=("Times New Roman", 14),
        )
        button1.pack()
        button1.place(x=1100, y=690)


class Page10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mibase = mysql.connector.connect(host="localhost", user="root", password="")
        micursor = mibase.cursor()
        micursor.execute("CREATE DATABASE IF NOT EXISTS agenda")

        create_table_query = """
        CREATE TABLE IF NOT EXISTS student(
            id INT AUTO_INCREMENT PRIMARY KEY,
            First_Name VARCHAR(255),
            Last_Name VARCHAR(255),
            Phone_Number VARCHAR(255),
            Age VARCHAR(255)
        )
        """
        mibase = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="agenda"
        )
        micursor = mibase.cursor()
        micursor.execute(create_table_query)
        mibase.commit()

        label1 = tk.Label(self, text="Primer nombre", width=20, height=2)
        label1.grid(row=1, column=0)
        label2 = tk.Label(self, text="Apellido", width=20, height=2)
        label2.grid(row=2, column=0)
        label3 = tk.Label(self, text="Telefono", width=20, height=2)
        label3.grid(row=3, column=0)
        label4 = tk.Label(self, text="Edad", width=20, height=2)
        label4.grid(row=4, column=0)
        label8 = tk.Label(self, width=10, height=2)
        label8.grid(row=7, column=2)
        label9 = tk.Label(self, width=10, height=2)
        label9.grid(row=7, column=4)

        e1 = tk.StringVar()
        e1entered = ttk.Entry(self, width=30, textvariable=e1)
        e1entered.grid(row=1, column=2)

        e2 = tk.StringVar()
        e2entered = ttk.Entry(self, width=30, textvariable=e2)
        e2entered.grid(row=2, column=2)

        e3 = tk.StringVar()
        e3entered = ttk.Entry(self, width=30, textvariable=e3)
        e3entered.grid(row=3, column=2)

        e4 = tk.StringVar()
        e4entered = ttk.Entry(self, width=30, textvariable=e4)
        e4entered.grid(row=4, column=2)

        T = tk.Text(self, height=20, width=100)
        T.grid(row=10, column=2)

        button1 = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(StartPage),
            font=("Times New Roman", 14),
        )
        button1.grid(row=5, column=8)

        button1 = tk.Button(
            self,
            text="Registrar",
            width=10,
            height=2,
            command=lambda: fb.register(e1, e2, e3, e4),
        )
        button1.grid(row=5, column=1)
        button2 = tk.Button(
            self, text="Borrar", width=10, height=2, command=lambda: fb.delete(e1)
        )
        button2.grid(row=5, column=0)
        button4 = tk.Button(
            self,
            text="Mostrar record",
            width=10,
            height=2,
            command=lambda: fb.showRecord(e1, T),
        )
        button4.grid(row=5, column=2)


# Driver Code
app = tkinterApp()
app.geometry("{}x{}".format(WIDTH, HEIGHT))
app.mainloop()
