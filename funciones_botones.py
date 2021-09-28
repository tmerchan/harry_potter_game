import tkinter as tk
import funciones_email as em
import mysql.connector
import re
import random
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.constants import E, LEFT, RIGHT, W
from typing import Text
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter import messagebox

# Make a regular expression
# for validating an Email
regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def duplicate(x):
    a = []
    for i in x:
        if i in a:
            pass
        else:
            a.append(i)
    return str(i)


# FUNCIONES PARA LOS BOTONES
def chequear_a_que_casa_corresponde(email_entered):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="entrega_final_hogwarts"
    )
    micursor = mibase.cursor()
    micursor.execute("SELECT rta FROM respuestas")
    resultado = micursor.fetchall()

    if duplicate(resultado) == "('Hufflepuff',)":
        em.send_email(email_entered, "Hufflepuff")
        messagebox.showinfo("Info", "Revisa tu correo ;)")
    if duplicate(resultado) == "('Gryffindor',)":
        em.send_email(email_entered, "Gryffindor")
        messagebox.showinfo("Info", "Revisa tu correo ;)")
    if duplicate(resultado) == "('Ravenclaw',)":
        em.send_email(email_entered, "Ravenclaw")
        messagebox.showinfo("Info", "Revisa tu correo ;)")
    if duplicate(resultado) == "('Slytherin',)":
        em.send_email(email_entered, "Slytherin")
        messagebox.showinfo("Info", "Revisa tu correo ;)")


def validate_entry(email_entered):
    if re.match(regex, email_entered):
        messagebox.showinfo("Info", "Genial! aguarde un instante por favor")
        chequear_a_que_casa_corresponde(email_entered)
    else:
        messagebox.showerror("Error", "Ingrese un correo valido por favor")


def guardar_respuesta_primer_frame(frame, controller, rta):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="entrega_final_hogwarts"
    )
    micursor = mibase.cursor()
    add_respuesta = "INSERT INTO respuestas " "(frame, rta) " "VALUES (%s, %s)"
    data_respuesta = ("Primer frame", rta)
    micursor.execute(add_respuesta, data_respuesta)
    mibase.commit()
    controller.show_frame(frame)


def guardar_respuesta_segundo_frame(frame, controller, rta):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="entrega_final_hogwarts"
    )
    micursor = mibase.cursor()
    add_respuesta = "INSERT INTO respuestas " "(frame, rta) " "VALUES (%s, %s)"
    data_respuesta = ("Segundo frame", rta)
    micursor.execute(add_respuesta, data_respuesta)
    mibase.commit()
    controller.show_frame(frame)


def guardar_respuesta_tercer_frame(frame, controller, rta):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="entrega_final_hogwarts"
    )
    micursor = mibase.cursor()
    add_respuesta = "INSERT INTO respuestas " "(frame, rta) " "VALUES (%s, %s)"
    data_respuesta = ("Tercer frame", rta)
    micursor.execute(add_respuesta, data_respuesta)
    mibase.commit()
    controller.show_frame(frame)


def guardar_respuesta_cuarto_frame(frame, controller, rta):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="entrega_final_hogwarts"
    )
    micursor = mibase.cursor()
    add_respuesta = "INSERT INTO respuestas " "(frame, rta) " "VALUES (%s, %s)"
    data_respuesta = ("Cuarto frame", rta)
    micursor.execute(add_respuesta, data_respuesta)
    mibase.commit()
    controller.show_frame(frame)


def iniciar_test(frame, controller):
    # PARA USAR LA BASE DE DATOS
    mibase = mysql.connector.connect(host="localhost", user="root", passwd="")
    micursor = mibase.cursor()
    micursor.execute("CREATE DATABASE IF NOT EXISTS entrega_final_hogwarts")

    create_rtas_table_query = """
    CREATE TABLE IF NOT EXISTS respuestas(
        id INT AUTO_INCREMENT PRIMARY KEY,
        frame VARCHAR(100),
        rta VARCHAR(100)
    )
    """
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="entrega_final_hogwarts"
    )
    micursor = mibase.cursor()
    micursor.execute(create_rtas_table_query)
    mibase.commit()
    controller.show_frame(frame)


def volver_a_empezar(frame, controller):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="entrega_final_hogwarts"
    )
    micursor = mibase.cursor()
    micursor.execute("DROP DATABASE entrega_final_hogwarts")
    mibase.commit()
    controller.show_frame(frame)


def ver_que_varita_toco(frame, controller):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="varitas"
    )
    micursor = mibase.cursor()
    select_varitas_query = "SELECT * FROM varitas"
    micursor.execute(select_varitas_query)

    varitas = micursor.fetchall()
    random_varita = random.choice(varitas)
    messagebox.showinfo(
        "Info",
        "Felicitaciones! Tu varita es de {} con nucleo de {}!".format(
            random_varita[1], random_varita[2]
        ),
    )
    controller.show_frame(frame)


# PARA LA AGENDA
def register(e1, e2, e3, e4):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="agenda"
    )
    micursor = mibase.cursor()
    dbFirst_Name = ""
    First_Name = e1.get()
    accion = "select count(*) from student where First_Name='%s'" % (First_Name)
    micursor.execute(accion)
    result = micursor.fetchall()
    for i in result:
        dbFirst_Name = i[0]
    if str(First_Name) != str(dbFirst_Name):
        Insert = "Insert into student(First_Name,Last_Name,Phone_Number,Age) values(%s,%s,%s,%s)"
        First_Name = e1.get()
        Last_Name = e2.get()
        Phone_Number = e3.get()
        Age = e4.get()
        if First_Name != "" and Last_Name != "" and Phone_Number != "" and Age != "":
            Value = (First_Name, Last_Name, Phone_Number, Age)
            micursor.execute(Insert, Value)
            mibase.commit()
            messagebox.askokcancel("Information", "Agendado")
        else:
            if (
                First_Name == ""
                and Last_Name == ""
                and Phone_Number == ""
                and Age == ""
            ):
                messagebox.askokcancel(
                    "Information", "Para agendar a alguien completa todos los campos"
                )
            else:
                messagebox.askokcancel("Information", "Dejaste cosas en blanco")
    else:
        messagebox.askokcancel("Information", "Ya existe ese contacto")


def showRecord(e1, T):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="agenda"
    )
    micursor = mibase.cursor()
    First_Name = e1.get()
    accion = "select * from student where First_Name='%s'" % (First_Name)
    micursor.execute(accion)
    result1 = micursor.fetchall()
    if result1:
        T.insert(tk.END, result1)
    else:
        messagebox.askokcancel("Information", "No hay nada para mostrar")


def delete(e1):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="agenda"
    )
    micursor = mibase.cursor()
    First_Name = e1.get()
    Delete = "delete from student where First_Name='%s'" % (First_Name)
    micursor.execute(Delete)
    mibase.commit()
    messagebox.showinfo("Information", "Borrado")
