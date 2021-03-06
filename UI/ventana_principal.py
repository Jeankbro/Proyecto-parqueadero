# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox

from UI import parking_lot_form, car_form, search_car_id, fees_info, delete_car, cars_info_window
from controllers import controller_parking_lot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.text_welcome = QtWidgets.QLabel(self.centralwidget)
        self.text_welcome.setGeometry(QtCore.QRect(10, 10, 771, 71))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.text_welcome.setFont(font)
        self.text_welcome.setObjectName("text_welcome")

        self.text_instructions = QtWidgets.QLabel(self.centralwidget)
        self.text_instructions.setGeometry(QtCore.QRect(160, 520, 471, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.text_instructions.setFont(font)
        self.text_instructions.setObjectName("text_instructions")

        self.img_parking_symbol = QtWidgets.QLabel(self.centralwidget)
        self.img_parking_symbol.setGeometry(QtCore.QRect(200, 90, 401, 391))
        self.img_parking_symbol.setAutoFillBackground(False)
        self.img_parking_symbol.setText("")
        self.img_parking_symbol.setPixmap(QtGui.QPixmap("parking_lot_symbol.jpg"))
        self.img_parking_symbol.setObjectName("img_parking_symbol")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menu_parking_lot = QtWidgets.QMenu(self.menubar)
        self.menu_parking_lot.setObjectName("menu_parking_lot")

        self.menu_cars = QtWidgets.QMenu(self.menubar)
        self.menu_cars.setObjectName("menu_cars")
        MainWindow.setMenuBar(self.menubar)

        self.action_add_parking_lot = QtWidgets.QAction(MainWindow)
        self.action_add_parking_lot.setObjectName("action_add_parking_lot")
        self.action_add_parking_lot.triggered.connect(self.show_add_parking_lot_form)

        self.action_add_car = QtWidgets.QAction(MainWindow)
        self.action_add_car.setObjectName("action_add_car")
        self.action_add_car.triggered.connect(self.show_add_car_form)

        self.action_search_car = QtWidgets.QAction(MainWindow)
        self.action_search_car.setObjectName("action_search_car")
        self.action_search_car.triggered.connect(self.show_car_search_id_form)

        self.action_view_cars = QtWidgets.QAction(MainWindow)
        self.action_view_cars.setObjectName("action_add_cars")
        self.action_view_cars.triggered.connect(self.show_cars)

        self.action_view_fees = QtWidgets.QAction(MainWindow)
        self.action_view_fees.setObjectName("action_view_fees")
        self.action_view_fees.triggered.connect(self.show_fees)

        self.action_delete_car = QtWidgets.QAction(MainWindow)
        self.action_delete_car.setObjectName("action_delete_car")
        self.action_delete_car.triggered.connect(self.show_car_delete_form)

        self.action_view_gains = QtWidgets.QAction(MainWindow)
        self.action_view_gains.setObjectName("action_view_gains")
        self.action_view_gains.triggered.connect(self.show_gains)

        self.menu_parking_lot.addAction(self.action_add_parking_lot)
        self.menu_parking_lot.addAction(self.action_view_fees)


        self.menu_cars.addAction(self.action_add_car)
        self.menu_cars.addAction(self.action_search_car)
        self.menu_cars.addAction(self.action_view_cars)
        self.menu_cars.addAction(self.action_delete_car)
        self.menu_cars.addAction(self.action_view_gains)


        self.menubar.addAction(self.menu_parking_lot.menuAction())
        self.menubar.addAction(self.menu_cars.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de parqueadero"))
        self.text_welcome.setText(_translate("MainWindow", "Bienvenido al sistema de parqueadero"))
        self.text_instructions.setText(_translate("MainWindow", "Porfavor seleccione una de las pesta??as en la esquina superior"))
        self.menu_parking_lot.setTitle(_translate("MainWindow", "Parqueadero"))
        self.menu_cars.setTitle(_translate("MainWindow", "Carros"))
        self.action_add_parking_lot.setText(_translate("MainWindow", "A??adir parqueadero"))
        self.action_add_car.setText(_translate("MainWindow", "A??adir carro"))
        self.action_search_car.setText(_translate("MainWindow", "Buscar carro"))
        self.action_view_cars.setText(_translate("MainWindow", "Mostrar carros"))
        self.action_view_fees.setText(_translate("MainWindow", "Ver tarifas"))
        self.action_delete_car.setText(_translate("MainWindow", "Eliminar carro"))
        self.action_view_gains.setText(_translate("MainWindow", "Ver ganancias"))


    def show_add_parking_lot_form(self):
        self.add_parking_lot_window = QtWidgets.QMainWindow()
        self.ui_parking_lot = parking_lot_form.Ui_add_parking_lot_form()
        self.ui_parking_lot.setupUi(self.add_parking_lot_window)
        self.add_parking_lot_window.show()

    def show_add_car_form(self):
        self.add_car_window = QtWidgets.QMainWindow()
        self.ui_car = car_form.Ui_add_car_form()
        self.ui_car.setupUi(self.add_car_window)
        self.add_car_window.show()

    def show_car_search_id_form(self):
        self.search_car_id_window = QtWidgets.QMainWindow()
        self.ui_search_car_id = search_car_id.Ui_car_search_form()
        self.ui_search_car_id.setupUi(self.search_car_id_window)
        self.search_car_id_window.show()

    def show_cars(self):
        self.show_cars_window = QtWidgets.QMainWindow()
        self.ui_show_cars = cars_info_window.Ui_cars_info_window()
        self.ui_show_cars.setupUi(self.show_cars_window)
        self.ui_show_cars.load_cars()
        self.show_cars_window.show()

    def show_fees(self):
        self.fees_window = QtWidgets.QMainWindow()
        self.ui_fees = fees_info.Ui_fees_info()
        self.ui_fees.setupUi(self.fees_window)
        self.fees_window.show()

    def show_car_delete_form(self):
        self.car_delete_window = QtWidgets.QMainWindow()
        self.ui_car_delete = delete_car.Ui_car_delete_form()
        self.ui_car_delete.setupUi(self.car_delete_window)
        self.car_delete_window.show()

    def show_gains(self):
        self.show_message("Las ganancias hasta ahora son de: " + str(controller_parking_lot.parking_lot.money), QMessageBox.Information)

    def show_message(self, message, type_message):
        msg = QMessageBox()
        msg.setText(message)
        msg.setIcon(type_message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
