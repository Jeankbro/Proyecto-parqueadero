# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'car_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_car_form(object):
    def setupUi(self, add_car_form):
        add_car_form.setObjectName("add_car_form")
        add_car_form.resize(364, 223)
        self.car_info = QtWidgets.QGroupBox(add_car_form)
        self.car_info.setGeometry(QtCore.QRect(10, 10, 341, 201))
        self.car_info.setObjectName("car_info")
        self.instructions_add_doctor = QtWidgets.QLabel(self.car_info)
        self.instructions_add_doctor.setGeometry(QtCore.QRect(10, 20, 191, 16))
        self.instructions_add_doctor.setObjectName("instructions_add_doctor")
        self.text_car_brand = QtWidgets.QLabel(self.car_info)
        self.text_car_brand.setGeometry(QtCore.QRect(20, 60, 81, 20))
        self.text_car_brand.setObjectName("text_car_brand")
        self.text_car_type = QtWidgets.QLabel(self.car_info)
        self.text_car_type.setGeometry(QtCore.QRect(30, 90, 71, 16))
        self.text_car_type.setObjectName("text_car_type")
        self.text_id = QtWidgets.QLabel(self.car_info)
        self.text_id.setGeometry(QtCore.QRect(65, 120, 31, 20))
        self.text_id.setObjectName("text_id")
        self.car_brand = QtWidgets.QLineEdit(self.car_info)
        self.car_brand.setGeometry(QtCore.QRect(100, 60, 201, 20))
        self.car_brand.setObjectName("car_brand")
        self.car_type = QtWidgets.QLineEdit(self.car_info)
        self.car_type.setGeometry(QtCore.QRect(100, 90, 201, 20))
        self.car_type.setObjectName("car_type")
        self.id = QtWidgets.QLineEdit(self.car_info)
        self.id.setGeometry(QtCore.QRect(100, 120, 201, 20))
        self.id.setObjectName("id")
        self.button_add_car = QtWidgets.QPushButton(self.car_info)
        self.button_add_car.setGeometry(QtCore.QRect(240, 170, 91, 23))
        self.button_add_car.setObjectName("button_add_car")

        self.retranslateUi(add_car_form)
        QtCore.QMetaObject.connectSlotsByName(add_car_form)

    def retranslateUi(self, add_car_form):
        _translate = QtCore.QCoreApplication.translate
        add_car_form.setWindowTitle(_translate("add_car_form", "Añadir carro"))
        self.car_info.setTitle(_translate("add_car_form", "Información del carro"))
        self.instructions_add_doctor.setText(_translate("add_car_form", "Por favor ingrese los datos del carro:"))
        self.text_car_brand.setText(_translate("add_car_form", "Marca del carro"))
        self.text_car_type.setText(_translate("add_car_form", "Tipo de carro"))
        self.text_id.setText(_translate("add_car_form", "Placa"))
        self.button_add_car.setText(_translate("add_car_form", "Añadir carro"))
