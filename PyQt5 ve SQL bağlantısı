from PyQt5 import QtCore, QtGui, QtWidgets
import pypyodbc
#from anaform import Ui_MainWindow
import anaform


class Ui_Dialog(object):


    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = anaform.Ui_MainWindow()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()


    def hatamesaji(self,hatabaslik = "Uyarı",hatamesaj= "SQL bağlantısı sağlanamadı"):
        hata = QtWidgets.QMessageBox()

        hata.setWindowTitle(hatabaslik)
        hata.setText(hatamesaj)
        hata.setStandardButtons(QtWidgets.QMessageBox.Ok)
        hata.exec_()

    def baglantimesaji(self,baslik = "Uyarı", mesaj="Bağlantı Sağlandı, Lütfen Bekleyin"):
        baglantimesaji = QtWidgets.QMessageBox()

        baglantimesaji.setWindowTitle(baslik)
        baglantimesaji.setText(mesaj)
        baglantimesaji.exec_()
        self.openwindow()


    def baglan(self):
        try:
            self.db_server = self.lineEdit.text()
            self.db_adi = self.lineEdit_2.text()
            self.db_kadi = self.lineEdit_3.text()
            self.db_sifre = self.lineEdit_4.text()

            self.baglanti_yolu = ('Driver=SQL Server;'
                             'Server='+self.db_server+';'
                             'Database='+self.db_adi+';'
                             'UID='+self.db_kadi+';'
                             'PWD='+self.db_sifre+';')

            self.baglanti = pypyodbc.connect(self.baglanti_yolu)

            self.imlec = self.baglanti.cursor()

            #self.openwindow()
            self.baglantimesaji()

        except:
            self.hatamesaji()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 207)
        self.btn_1 = QtWidgets.QPushButton(Dialog)
        self.btn_1.setGeometry(QtCore.QRect(70,140,241,32))
        self.btn_1.setObjectName("btn_1")
        self.btn_1.setText("Bağlan")
        self.btn_1.clicked.connect(lambda: self.baglan())
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 161, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 20, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 50, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 80, 141, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 110, 141, 20))
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bağlantı Kur"))
        self.label.setText(_translate("Dialog", "SERVER NAME"))
        self.label_2.setText(_translate("Dialog", "VERİTABANI ADI"))
        self.label_3.setText(_translate("Dialog", "VERİTABANI KULLANICI ADI"))
        self.label_4.setText(_translate("Dialog", "VERİTABANI KULLANICI ŞİFRE"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
