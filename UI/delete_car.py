# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_car.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from controllers import controller_cars, controller_parking_lot


class Ui_car_delete_form(object):
    def setupUi(self, car_delete_form):
        car_delete_form.setObjectName("car_delete_form")
        car_delete_form.resize(335, 107)
        self.instructions_delete_car = QtWidgets.QLabel(car_delete_form)
        self.instructions_delete_car.setGeometry(QtCore.QRect(10, 10, 211, 16))
        self.instructions_delete_car.setObjectName("instructions_delete_car")
        self.text_id = QtWidgets.QLabel(car_delete_form)
        self.text_id.setGeometry(QtCore.QRect(10, 40, 31, 16))
        self.text_id.setObjectName("text_id")
        self.id = QtWidgets.QLineEdit(car_delete_form)
        self.id.setGeometry(QtCore.QRect(50, 40, 241, 20))
        self.id.setObjectName("id")
        self.button_delete_car = QtWidgets.QPushButton(car_delete_form)
        self.button_delete_car.setGeometry(QtCore.QRect(250, 80, 71, 23))
        self.button_delete_car.setObjectName("button_delete_car")
        self.button_delete_car.clicked.connect(self.delete_car)

        self.retranslateUi(car_delete_form)
        QtCore.QMetaObject.connectSlotsByName(car_delete_form)

    def retranslateUi(self, car_delete_form):
        _translate = QtCore.QCoreApplication.translate
        car_delete_form.setWindowTitle(_translate("car_delete_form", "Eliminar carro"))
        self.instructions_delete_car.setText(_translate("car_delete_form", "Por favor ingresa la placa del carro a eliminar:"))
        self.text_id.setText(_translate("car_delete_form", "Placa"))
        self.button_delete_car.setText(_translate("car_delete_form", "Eliminar"))

    def show_message(self, message, type_message):
        msg = QMessageBox()
        msg.setText(message)
        msg.setIcon(type_message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    def delete_car(self):
        car_id = self.id.text().strip()
        if not car_id:
            self.show_message("El carro no pudo ser eliminado, intente de nuevo!", QMessageBox.Critical)
        else:
            self.show_message("El carro ha sido eliminado!", QMessageBox.Information)
            self.id.clear()
            total = controller_cars.payout(car_id)
            self.show_message("El total a pagar es de: " + str(total) + "!", QMessageBox.Information)
            controller_cars.delete_car(car_id)
            controller_parking_lot.add_money(total)
