# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\vk_api\widget_get_users.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Get_Users(object):
    def setupUi(self, MainWindow_Get_Users):
        MainWindow_Get_Users.setObjectName("MainWindow_Get_Users")
        MainWindow_Get_Users.resize(300, 160)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow_Get_Users.sizePolicy().hasHeightForWidth())
        MainWindow_Get_Users.setSizePolicy(sizePolicy)
        MainWindow_Get_Users.setMinimumSize(QtCore.QSize(300, 160))
        MainWindow_Get_Users.setMaximumSize(QtCore.QSize(300, 160))
        self.centralwidget = QtWidgets.QWidget(MainWindow_Get_Users)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_get_users = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_get_users.setGeometry(QtCore.QRect(10, 10, 281, 141))
        self.groupBox_get_users.setObjectName("groupBox_get_users")
        self.lineEdit_get_users_id = QtWidgets.QLineEdit(self.groupBox_get_users)
        self.lineEdit_get_users_id.setGeometry(QtCore.QRect(120, 27, 151, 20))
        self.lineEdit_get_users_id.setText("")
        self.lineEdit_get_users_id.setObjectName("lineEdit_get_users_id")
        self.pushButton_get_users_save = QtWidgets.QPushButton(self.groupBox_get_users)
        self.pushButton_get_users_save.setGeometry(QtCore.QRect(200, 110, 71, 23))
        self.pushButton_get_users_save.setObjectName("pushButton_get_users_save")
        self.lineEdit_get_users_status = QtWidgets.QLineEdit(self.groupBox_get_users)
        self.lineEdit_get_users_status.setEnabled(False)
        self.lineEdit_get_users_status.setGeometry(QtCore.QRect(160, 60, 111, 21))
        self.lineEdit_get_users_status.setObjectName("lineEdit_get_users_status")
        self.lineEdit_get_users_file_name = QtWidgets.QLineEdit(self.groupBox_get_users)
        self.lineEdit_get_users_file_name.setGeometry(QtCore.QRect(10, 110, 181, 21))
        self.lineEdit_get_users_file_name.setText("")
        self.lineEdit_get_users_file_name.setObjectName("lineEdit_get_users_file_name")
        self.pushButton_get_users_load = QtWidgets.QPushButton(self.groupBox_get_users)
        self.pushButton_get_users_load.setGeometry(QtCore.QRect(10, 60, 71, 23))
        self.pushButton_get_users_load.setObjectName("pushButton_get_users_load")
        self.pushButton_get_users_clear = QtWidgets.QPushButton(self.groupBox_get_users)
        self.pushButton_get_users_clear.setGeometry(QtCore.QRect(80, 60, 71, 23))
        self.pushButton_get_users_clear.setObjectName("pushButton_get_users_clear")
        self.radioButton_group = QtWidgets.QRadioButton(self.groupBox_get_users)
        self.radioButton_group.setGeometry(QtCore.QRect(10, 32, 82, 21))
        self.radioButton_group.setObjectName("radioButton_group")
        self.radioButton_user = QtWidgets.QRadioButton(self.groupBox_get_users)
        self.radioButton_user.setGeometry(QtCore.QRect(10, 20, 111, 17))
        self.radioButton_user.setObjectName("radioButton_user")
        self.label = QtWidgets.QLabel(self.groupBox_get_users)
        self.label.setGeometry(QtCore.QRect(10, 92, 61, 20))
        self.label.setObjectName("label")
        MainWindow_Get_Users.setCentralWidget(self.centralwidget)
        self.action_6 = QtWidgets.QAction(MainWindow_Get_Users)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow_Get_Users)
        self.action_7.setObjectName("action_7")

        self.retranslateUi(MainWindow_Get_Users)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Get_Users)

    def retranslateUi(self, MainWindow_Get_Users):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Get_Users.setWindowTitle(_translate("MainWindow_Get_Users", "MainWindow"))
        self.groupBox_get_users.setTitle(_translate("MainWindow_Get_Users", "Получение списка подписчиков"))
        self.pushButton_get_users_save.setText(_translate("MainWindow_Get_Users", "Сохранить"))
        self.lineEdit_get_users_status.setText(_translate("MainWindow_Get_Users", "Данных нет"))
        self.pushButton_get_users_load.setText(_translate("MainWindow_Get_Users", "Загрузка"))
        self.pushButton_get_users_clear.setText(_translate("MainWindow_Get_Users", "Сброс"))
        self.radioButton_group.setText(_translate("MainWindow_Get_Users", "ID Группы"))
        self.radioButton_user.setText(_translate("MainWindow_Get_Users", "ID Пользователя"))
        self.label.setText(_translate("MainWindow_Get_Users", "Имя файла"))
        self.action_6.setText(_translate("MainWindow_Get_Users", "Создать новую базу"))
        self.action_7.setText(_translate("MainWindow_Get_Users", "Загрузить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Get_Users = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Get_Users()
    ui.setupUi(MainWindow_Get_Users)
    MainWindow_Get_Users.show()
    sys.exit(app.exec_())
