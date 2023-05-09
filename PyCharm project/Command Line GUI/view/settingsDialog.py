# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_settingDialog(object):
   def setupUi(self, settingDialog):
       settingDialog.setObjectName("settingDialog")
       settingDialog.resize(448, 230)
       self.buttonBox = QtWidgets.QDialogButtonBox(settingDialog)
       self.buttonBox.setGeometry(QtCore.QRect(80, 180, 341, 32))
       self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
       self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
       self.buttonBox.setObjectName("buttonBox")
       self.macPath = QtWidgets.QLineEdit(settingDialog)
       self.macPath.setGeometry(QtCore.QRect(180, 50, 241, 21))
       self.macPath.setObjectName("macPath")
       self.ubuntuPath = QtWidgets.QLineEdit(settingDialog)
       self.ubuntuPath.setGeometry(QtCore.QRect(180, 90, 241, 21))
       self.ubuntuPath.setObjectName("ubuntuPath")
       self.ubuntuName = QtWidgets.QLineEdit(settingDialog)
       self.ubuntuName.setGeometry(QtCore.QRect(180, 130, 241, 21))
       self.ubuntuName.setObjectName("ubuntuName")
       self.label = QtWidgets.QLabel(settingDialog)
       self.label.setGeometry(QtCore.QRect(30, 50, 111, 21))
       self.label.setObjectName("label")
       self.label_2 = QtWidgets.QLabel(settingDialog)
       self.label_2.setGeometry(QtCore.QRect(30, 90, 131, 20))
       self.label_2.setObjectName("label_2")
       self.label_3 = QtWidgets.QLabel(settingDialog)
       self.label_3.setGeometry(QtCore.QRect(30, 130, 111, 21))
       self.label_3.setObjectName("label_3")
       self.label_4 = QtWidgets.QLabel(settingDialog)
       self.label_4.setGeometry(QtCore.QRect(180, 10, 81, 31))
       font = QtGui.QFont()
       font.setPointSize(20)
       self.label_4.setFont(font)
       self.label_4.setObjectName("label_4")


       self.retranslateUi(settingDialog)
       self.buttonBox.accepted.connect(settingDialog.accept)
       self.buttonBox.rejected.connect(settingDialog.reject)
       QtCore.QMetaObject.connectSlotsByName(settingDialog)


   def retranslateUi(self, settingDialog):
       _translate = QtCore.QCoreApplication.translate
       settingDialog.setWindowTitle(_translate("settingDialog", "Dialog"))
       self.label.setText(_translate("settingDialog", "Mac vserver path"))
       self.label_2.setText(_translate("settingDialog", "Ubuntu vserver path"))
       self.label_3.setText(_translate("settingDialog", "Ubuntu hostname name"))
       self.label_4.setText(_translate("settingDialog", "Settings"))




if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   settingDialog = QtWidgets.QDialog()
   ui = Ui_settingDialog()
   ui.setupUi(settingDialog)
   settingDialog.show()
   sys.exit(app.exec_())
