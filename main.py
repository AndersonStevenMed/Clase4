
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QWidget, QFormLayout, QLabel, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QMessageBox

import sys

class Ventana1 (QMainWindow):

    # Hacer el metodo de construcción de la ventana
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        #Poner el titulo
        self.setWindowTitle("Condicionales con operadores lógicos")

        # Establecemos las propiedades de ancho y alto
        self.ancho = 600
        self.alto = 400

        # Establecer el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # Estas lineas hacen que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Para fijar que la ventana no se pueda cambiar de tamaño
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos imagen de fondo para la ventana
        self.setStyleSheet("QMainWindow { background-image: url(imagenes/img.png);"
                           'background-repeat: no-repeat;'
                           "background-position: center;}")

        # Establecemos el fondo principal
        self.fondo = QWidget()

        # Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos de forms de formulario
        self.formulario = QFormLayout()

        # Consultar los tipos de letra del sistema
        for p in QFontDatabase().families():
            print(p)

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto
        self.letrero1.setText("Condicionales con operadores lógicos")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("BankGothic Lt BT", 17))

        # Centramos el texto
        self.letrero1.setAlignment(Qt.AlignCenter)

        # Le ponemos color de fondo color de texto y margenes al letrero
        self.letrero1.setStyleSheet("background-color:#pink; color:#pink; padding:30px;"
                                    "border:solid; border-width:3px; border-color:#pink;"
                                    "border-radius:5px; margin-bottom:50px;")

        # Agregamos el espacio para separar el titulo
        self.formulario.addRow(self.letrero1)

        # Hacemos el letrero del primer numero
        self.labelNumero1 = QLabel("Ingrese el primer numero: ")

        # Hacemos el campo para el primer numero
        self.numero1 = QLineEdit()

        # Definimos el ancho del campo en 60px
        self.numero1.setFixedWidth(60)

        # Establecemos que solo se ingrese un numero de 5 digitos
        self.numero1.setMaxLength(5)

        # Ponemos el letrero y ponemos el campo del primer numero en la segunda fila
        self.formulario.addRow(self.labelNumero1, self.numero1)

        # Hacemos el letrero del segundo numero
        self.labelNumero2 = QLabel("Ingrese el segundo numero: ")

        # Hacemos el campo para el segundo numero
        self.numero2 = QLineEdit()

        # Definimos el ancho del campo en 60px
        self.numero2.setFixedWidth(60)

        # Establecemos que solo se ingrese un numero de 5 digitos
        self.numero2.setMaxLength(5)

        # Ponemos el letrero y ponemos el campo del primer numero en la tercera fila
        self.formulario.addRow(self.labelNumero2, self.numero2)

        # Hacemos el letrero del tercer numero
        self.labelNumero3 = QLabel("Ingrese el tercer numero: ")

        # Hacemos el campo para el segundo numero
        self.numero3 = QLineEdit()

        # Definimos el ancho del campo en 60px
        self.numero3.setFixedWidth(60)

        # Establecemos que solo se ingrese un numero de 5 digitos
        self.numero3.setMaxLength(5)

        # Ponemos el letrero y ponemos el campo del primer numero en la cuarta fila
        self.formulario.addRow(self.labelNumero3, self.numero3)

        # Hacemos un boton para hacer calculos
        self.botonCalcular = QPushButton("Calcular")

        # Establecemos el ancho del boton
        self.botonCalcular.setFixedWidth(100)
        # Le ponemos color de fondo, color de texto y margenes del boton
        self.botonCalcular.setStyleSheet("background-color: #pink; color: #pink; padding: 10px;")
        # Ponemos el boton de 5 hacia abajo
        self.formulario.addWidget(self.botonCalcular)

        # Ponemos el bontonCalcular a funcionar
        self.botonCalcular.clicked.connect(self.accion_botonCalcular)

        # Poner de ultimo
        # Establecer que la ventana va a tener una distribución de fórmulario
        self.fondo.setLayout(self.formulario)

    def accion_botonCalcular(self):

        # Creamos una ventana de dialogo
        self.ventanaDialogo = QDialog()

        # Definimos el tamaño de la ventana
        self.ventanaDialogo.resize(300,200)

        # Creamos un boton para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opcionesBotones = QDialogButtonBox(self.botonAceptar)
        self.opcionesBotones.accepted.connect(self.ventanaDialogo.accept)

        # Establecemos el titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Mayor o menor de 3 numeros")

        # Configuramos la ventana para que sea modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos un layout vertical
        self.vertical = QVBoxLayout()

        self.mensaje = QLabel('')

        # Le ponemos estilos a label mensaje
        self.mensaje.setStyleSheet("background-color:#pink; color:#pink; padding:10px;"
                                   "border-radius:10px;")

        # Agregamos el label de mensaje
        self.vertical.addWidget(self.mensaje)

        # Agregar las opciones de los botones
        self.vertical.addWidget(self.opcionesBotones)

        # Poner de ultimo
        # Establecer que la ventana va a tener una distribución de fórmulario
        self.ventanaDialogo.setLayout(self.vertical)

        # Variable para controlar que se han ingresado los datos correctos
        self.datosCorrectos = True



        #Validamos si el número ingresado son espacios en blanco
        if (self.numero1.text().isspace()
                or self.numero2.text().isspace()
                or self.numero3.text().isspace()):
            # Cambiamos la variable datosCorrectos a False
            self.datosCorrectos = False
            QMessageBox.warning(self, "Datos incorrectos", "Ha ingresado espacios en blanco.")

        #
        if (self.numero1.text().isalpha()
                or self.numero2.text().isalpha()
                or self.numero3.text().isalpha()):
            # Cambiamos la variable datosCorrectos a False
            self.datosCorrectos = False
            QMessageBox.warning(self, "Datos incorrectos", "Ha ingresado letras.")

        if (self.numero1.text() == ''
                or self.numero2.text() == ''
                or self.numero3.text() == ''):
            # Cambiamos la variable datosCorrectos a False
            self.datosCorrectos = False
            QMessageBox.warning(self, "Datos incorrectos", "no ha ingresado nada.")

        if not(self.numero1.text().isalnum()
                or not self.numero2.text().isalnum()
                or not self.numero3.text().isalnum()):
            # Cambiamos la variable datosCorrectos a False
            self.datosCorrectos = False
            QMessageBox.warning(self, "Datos incorrectos", "Ha ingresado caracteres especiales.")



            self.mensaje.setText("Ha ingresado espacios en blanco")

            # Hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

        # Si los datos están correctos
        if self.datosCorrectos:


            try:

                # Convetimos a decimales todos los numeros
                self.n1 = float(self.numero1.text())
                self.n2 = float(self.numero2.text())
                self.n3 = float(self.numero3.text())

                # Creamos una varioable para guardar el numero mas peuqeño de los 3
                self.pequeño = 0

                # Cramos una variable para guardar el numero mas grande de los 3
                self.grande = 0

                # Buscamos el numero mas pequeño de  los 3
                if self.n1 < self.n2 and self.n1 < self.n3:
                    self.pequeño = self.n1
                else:
                    if self.n2 < self.n3:
                        self.pequeño = self.n2
                    else:
                        self.pequeño = self.n3

                # Buscamos el numero mas grande de  los 3
                if self.n1 > self.n2 and self.n1 > self.n3:
                    self.grande = self.n1
                else:
                    if self.n2 > self.n3:
                        self.grande = self.n2
                    else:
                        self.grande = self.n3

                self.respuesta = "De los 3 numeros: " + \
                                self.numero1.text() + ", " + self.numero2.text() + " y " + self.numero3.text() + \
                                "\nel menor de los 3 es: " + str(self.pequeño) + \
                                "\ny el mayor de los 3 es: " + str(self.grande) + "."

                # Escribimos el texto explicativo
                self.mensaje.setText(self.respuesta)

                # Hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

                # Reseteamos los campos de ingresos de los numeros
                self.numero1.setText("")
                self.numero2.setText("")
                self.numero3.setText("")

            except ValueError:

                # Escribimos el texto explicativo
                self.mensaje.setText("Ha ingresado un caraceter incorrecto\n vuelve a intentarlo")

                # Hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()



if __name__ == '__main__':
    # Hacer que la aplicación se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo Ventana1 con el nombre de ventana1
    ventana1 = Ventana1()
    # Hacer que el objeto ventana1  se vea
    ventana1.show()

    sys.exit(app.exec_())









































# def programa1():
#
#     sueldo = input("Ingresar sueldo: ")
#
#     if int(sueldo) > 3000000:
#         # Operaciones
#         print("esta persona debe pagar impuestos")
#     print ("Por aqui continua el programa")
#
# def programa2():
#     numero1 = input("Ingrese primer numero: ")
#     numero2 = input("Ingrese segundo numero: ")
#
#     if int(numero1) > int(numero2):
#         print("el valor mayor es numero1 " + numero1)
#     else:
#         print("el valor mayor es numero2 " + numero2)
#
# def programa3():
#     parcial1 = float(input("ingrese nota primer parcial: "))
#     parcial2 = float(input("ingrese nota segundo parcial: "))
#     parcial3 = float(input("ingrese nota tercer parcial: "))
#
#     promedio = (parcial1 + parcial2 + parcial3) / 3
#     print("promedio: " + str(promedio))
#     if promedio >= 4:
#         print("Paso muy bien el curso")
#     else:
#
#         if promedio >=3 and promedio <4:
#             print("Paso regular")
#
#         else:
#             print("Perdio el curso")
#
#
#
# if __name__ == "__main__":
#     programa1()
#     print()
#     programa2()
#     print()
#     programa3()