import os
import smtplib
import imghdr
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage


def read_creds():
    user = passw = ""
    with open("credentials.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw


def send_email(email, casa):
    sender, password = read_creds()
    msgRoot = MIMEMultipart("related")
    msgRoot["Subject"] = "Desición final del Sombrero Seleccionador"
    msgRoot["From"] = sender
    msgRoot["To"] = email
    msgRoot.preamble = "Multi-part message in MIME format."

    msgAlternative = MIMEMultipart("alternative")
    msgRoot.attach(msgAlternative)

    msgText = MIMEText("Alternative plain text message.")
    msgAlternative.attach(msgText)

    if casa == "Hufflepuff":
        msgText = MIMEText(
            '<b>Felicidades!! Eres un <i>Hufflepuff</i>.</b><br><img src="cid:image1"><br>La Sala Común de Hufflepuff se encuentra en una bodega en el mismo pasillo subterráneo que la cocina. Inicialmente, Hufflepuff buscaba alumnos que simplemente quisieran pertenecer a esa casa, aunque actualmente busca alumnos leales, honestos y que no teman el trabajo pesado. La fundadora es nada menos que la bruja Helga Hufflepuff, amiga desde la infancia de Rowena Ravenclaw. Helga fue una bruja muy noble, amigable y la principal impulsora de que Hogwarts aceptase a alumnos nacidos de muggles. La principal reliquia de la casa es la copa de Helga Hufflepuff. El símbolo de la casa es un tejón negro y sus colores representativos son el amarillo y el negro carbón. Los estudiantes de esta casa son conocidos por ser trabajadores, amigables, leales, humildes y sin prejuicios. Debido a sus valores, los Hufflepuffs no son tan competitivos como las otras casas, o son más modestos con respecto a sus logros..',
            "html",
        )
        msgAlternative.attach(msgText)

        # Attach Image
        fp = open("img/hufflepuff.png", "rb")  # Read image
        msgImage = MIMEImage(fp.read())
        fp.close()
    if casa == "Gryffindor":
        msgText = MIMEText(
            '<b>Felicidades!! Eres un <i>Gryffindor</i>.</b><br><img src="cid:image1"><br>La Casa Gryffindor fue fundada por el célebre mago Godric Gryffindor. Godric sólo aceptaba en su casa a aquellos magos y brujas que tenían valentía, disposición, coraje y caballerosidad, ya que éstas son las cualidades de un auténtico Gryffindor. Los colores de esta casa son el dorado y el escarlata y su símbolo es un león. La reliquia más preciada de la casa es la espada de Godric Gryffindor, perteneciente, como su nombre indica, al fundador de la casa. La Casa de Gryffindor estima el coraje, así como la osadía y el temple, así, sus miembros se caracterizan por ser valientes aunque a veces hasta el punto de ser imprudentes. Gryffindor ha aportado numerosos miembros al Ejército de Dumbledore y a la Orden del Fénix. Los estudiantes de esta casa pasan la mayor parte del tiempo en la Torre de Gryffindor, ubicada en el séptimo piso del Castillo de Hogwarts. Existen dos escaleras, cada una dirige al dormitorio de los hombres y las mujeres respectivamente. Las escaleras de los dormitorios de las chicas están encantados para convertirse en un tobogán si un chico intenta subir por ellas, esto no pasa en las otras escaleras, puesto que se entendió que las chicas eran más de fiar que los chicos, por lo que Hermione podía subir al dormitorio de los chicos..',
            "html",
        )
        msgAlternative.attach(msgText)

        # Attach Image
        fp = open("img/gryffindor.png", "rb")  # Read image
        msgImage = MIMEImage(fp.read())
        fp.close()
    if casa == "Ravenclaw":
        msgText = MIMEText(
            '<b>Felicidades!! Eres un <i>Ravenclaw</i>.</b><br><img src="cid:image1"><br>La Casa Ravenclaw se encuentra en una torre en el ala oeste del castillo. En la entrada se encuentra una estatua con forma de águila que dice acertijos y sólo te deja entrar si los resuelves. De seguro eres un alumno académico, estudioso y que siempre sabe lo que hay que hacer. No te preocupes, nunca te quedarás fuera de tu dormitorio. Ravenclaw fue fundada por la bruja, nacida en las cañadas de Escocia, Rowena Ravenclaw. Supuestamente es la principal inventora del nombre, lugar y formato de Hogwarts. También es la causante de que las escaleras se muevan. La casa Ravenclaw premia el aprendizaje, la sabiduría, el ingenio, y el intelecto de sus miembros. Por ello, muchos Ravenclaw tienden a tener talento académico y a ser estudiantes motivados. Los Ravenclaw también se enorgullecen de ser originales en sus ideas y métodos. No es raro encontrar a estudiantes de Ravenclaw que practiquen diferentes tipos de magia que otras casas podrían tratar de evitar..',
            "html",
        )
        msgAlternative.attach(msgText)

        # Attach Image
        fp = open("img/ravenclaw.png", "rb")  # Read image
        msgImage = MIMEImage(fp.read())
        fp.close()
    if casa == "Slytherin":
        msgText = MIMEText(
            '<b>Felicidades!! Eres un <i>Slytherin</i>.</b><br><img src="cid:image1"><br>La Casa Slytherin está caracterizada principalmente por la ambición y la astucia. Fue fundada por el mago Salazar Slytherin. La Sala Común está situada en las mazmorras, pasando por un serie de numerosos pasillos subterráneos. Específicamente se encuentra debajo del Lago Negro, haciendo que la sala común sea fría y con una tonalidad verdosa, ya que hay ventanas que dan a las aguas. Se accede a ella por una puerta altamente disimulada en un muro de piedra, diciendo una contraseña requerida. La única conocida es "Sangre Pura". Su principal reliquia es el guardapelo de Salazar Slytherin. El animal representativo es la serpiente, sus colores son verde y plateado y el elemento es el agua, asociada con la astucia y la frialdad. Los Slytherin tienden a ser líderes ambiciosos, astutos y fuertes, orientados a los logros. Según Albus Dumbledore, las cualidades que Salazar valoraba en los estudiantes que había elegido incluían inteligencia, ingenio, determinación y "un cierto desdén por las reglas". Los Slytherin tienden a hacerse cargo y poseen fuertes habilidades de liderazgo, a menudo son seguros de sí mismos y confían en su propia competencia y pueden ser muy leales..',
            "html",
        )
        msgAlternative.attach(msgText)

        # Attach Image
        fp = open("img/slytherin.png", "rb")  # Read image
        msgImage = MIMEImage(fp.read())
        fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header("Content-ID", "<image1>")
    msgRoot.attach(msgImage)

    import smtplib

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)  # Username and Password of Account
        smtp.sendmail(sender, email, msgRoot.as_string())
        smtp.quit()
