# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'car_info_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_car_info_window(object):
    def setupUi(self, car_info_window):
        car_info_window.setObjectName("car_info_window")
        car_info_window.resize(772, 286)
        self.car_info_section = QtWidgets.QGroupBox(car_info_window)
        self.car_info_section.setGeometry(QtCore.QRect(10, 20, 741, 241))
        self.car_info_section.setObjectName("car_info_section")
        self.car_info_table = QtWidgets.QTableWidget(self.car_info_section)
        self.car_info_table.setGeometry(QtCore.QRect(20, 30, 701, 191))
        self.car_info_table.setObjectName("car_info_table")
        self.car_info_table.setColumnCount(5)
        self.car_info_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.car_info_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.car_info_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.car_info_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.car_info_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.car_info_table.setHorizontalHeaderItem(4, item)

        self.retranslateUi(car_info_window)
        QtCore.QMetaObject.connectSlotsByName(car_info_window)

    def retranslateUi(self, car_info_window):
        _translate = QtCore.QCoreApplication.translate
        car_info_window.setWindowTitle(_translate("car_info_window", "Información del carro"))
        self.car_info_section.setTitle(_translate("car_info_window", "Información del carro"))
        item = self.car_info_table.horizontalHeaderItem(0)
        item.setText(_translate("car_info_window", "Marca del carro"))
        item = self.car_info_table.horizontalHeaderItem(1)
        item.setText(_translate("car_info_window", "Tipo de carro"))
        item = self.car_info_table.horizontalHeaderItem(2)
        item.setText(_translate("car_info_window", "Placa"))
        item = self.car_info_table.horizontalHeaderItem(3)
        item.setText(_translate("car_info_window", "Fecha de ingreso"))
        item = self.car_info_table.horizontalHeaderItem(4)
        item.setText(_translate("car_info_window", "Tiempo elapsado"))
