# -*- coding: utf-8 -*-

# Elementy Analizy Numerycznej
# 3.4 Rozwiązywanie układu równań liniowych metodą Doolittle'a

# 108605 Piotr Bajsarowicz

from PyQt4 import QtCore, QtGui
import numpy as np
import random

#tempX = np.array(0.0,np.float64)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(383, 174)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 130, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.dialogLabel = QtGui.QLabel(Dialog)
        self.dialogLabel.setGeometry(QtCore.QRect(20, 20, 341, 111))
        self.dialogLabel.setObjectName(_fromUtf8("dialogLabel"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Błąd", "Błąd", None))
        self.dialogLabel.setText(_translate("Dialog", "TextLabel", None))

    def lab(self,x):
        self.dialogLabel.setText(x)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(760, 456)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.rozwiazPushButton = QtGui.QPushButton(self.centralwidget)
        self.rozwiazPushButton.setGeometry(QtCore.QRect(30, 300, 75, 23))
        self.rozwiazPushButton.setObjectName(_fromUtf8("rozwiazPushButton"))
        self.wymiarLabel = QtGui.QLabel(self.centralwidget)
        self.wymiarLabel.setGeometry(QtCore.QRect(30, 30, 181, 16))
        self.wymiarLabel.setObjectName(_fromUtf8("wymiarLabel"))
        self.zatwierdzPushButton = QtGui.QPushButton(self.centralwidget)
        self.zatwierdzPushButton.setGeometry(QtCore.QRect(330, 30, 75, 23))
        self.zatwierdzPushButton.setObjectName(_fromUtf8("zatwierdzPushButton"))
        self.daneTableWidget = QtGui.QTableWidget(self.centralwidget)
        self.daneTableWidget.setGeometry(QtCore.QRect(30, 121, 701, 161))
        self.daneTableWidget.setObjectName(_fromUtf8("daneTableWidget"))
        self.daneTableWidget.setColumnCount(0)
        self.daneTableWidget.setRowCount(0)
        self.wymiarTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.wymiarTextEdit.setGeometry(QtCore.QRect(220, 30, 104, 21))
        self.wymiarTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wymiarTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wymiarTextEdit.setObjectName(_fromUtf8("wymiarTextEdit"))
        self.daneLabel = QtGui.QLabel(self.centralwidget)
        self.daneLabel.setGeometry(QtCore.QRect(30, 60, 361, 16))
        self.daneLabel.setObjectName(_fromUtf8("daneLabel"))
        self.przykladTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.przykladTextEdit.setGeometry(QtCore.QRect(480, 30, 251, 61))
        self.przykladTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.przykladTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.przykladTextEdit.setReadOnly(True)
        self.przykladTextEdit.setObjectName(_fromUtf8("przykladTextEdit"))
        self.wynikTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.wynikTextEdit.setGeometry(QtCore.QRect(120, 300, 611, 101))
        self.wynikTextEdit.setObjectName(_fromUtf8("wynikTextEdit"))
        self.losoweLabel = QtGui.QLabel(self.centralwidget)
        self.losoweLabel.setGeometry(QtCore.QRect(30, 90, 71, 16))
        self.losoweLabel.setObjectName(_fromUtf8("losoweLabel"))
        self.losoweOdLabel = QtGui.QLabel(self.centralwidget)
        self.losoweOdLabel.setGeometry(QtCore.QRect(110, 90, 16, 16))
        self.losoweOdLabel.setObjectName(_fromUtf8("losoweOdLabel"))
        self.losoweDoLabel = QtGui.QLabel(self.centralwidget)
        self.losoweDoLabel.setGeometry(QtCore.QRect(220, 90, 20, 16))
        self.losoweDoLabel.setObjectName(_fromUtf8("losoweDoLabel"))
        self.losowoOdTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.losowoOdTextEdit.setGeometry(QtCore.QRect(130, 90, 81, 21))
        self.losowoOdTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.losowoOdTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.losowoOdTextEdit.setObjectName(_fromUtf8("losowoOdTextEdit"))
        self.losowoDoTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.losowoDoTextEdit.setGeometry(QtCore.QRect(240, 90, 81, 21))
        self.losowoDoTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.losowoDoTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.losowoDoTextEdit.setObjectName(_fromUtf8("losowoDoTextEdit"))
        self.losowoPushButton = QtGui.QPushButton(self.centralwidget)
        self.losowoPushButton.setGeometry(QtCore.QRect(330, 90, 75, 23))
        self.losowoPushButton.setObjectName(_fromUtf8("losowoPushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.zatwierdzPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.wymiar)
        QtCore.QObject.connect(self.rozwiazPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.wynik)
        QtCore.QObject.connect(self.losowoPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.losuj)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.rozwiazPushButton.setText(_translate("MainWindow", "Rozwiąż", None))
        self.wymiarLabel.setText(_translate("MainWindow", "Wpisz wymiar macierzy/równania (N)", None))
        self.zatwierdzPushButton.setText(_translate("MainWindow", "Zatwierdź", None))
        self.daneLabel.setText(_translate("MainWindow", "Wprowadź dane (w przykładzie pierwszym wierszem będzie  3  -4  2  15):", None))
        self.przykladTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Przykład:          Wymiar macierzy/równania: N = 3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3x - 4y + 2z = 15</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">x + 2y - z = 5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2x - y + z = 13</span></p></body></html>", None))
        self.losoweLabel.setText(_translate("MainWindow", "Losowe dane: ", None))
        self.losoweOdLabel.setText(_translate("MainWindow", "od", None))
        self.losoweDoLabel.setText(_translate("MainWindow", "do", None))
        self.losowoPushButton.setText(_translate("MainWindow", "Losuj", None))

    def wymiar(self):
        try:
            N = int(self.wymiarTextEdit.toPlainText())+1
            if N<3:
                raise Exception
            self.daneTableWidget.setColumnCount(N)
            self.daneTableWidget.setRowCount(N)

            """item = self.daneTableWidget.horizontalHeaderItem(N-1)
            item.setText(_translate("MainWindow", "b", None))
            """
            #self.daneTableWidget.setHorizontalHeaderItem(1,"la")



        except Exception:
            Dialog = QtGui.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.lab("Podales zla wartosc! Podaj liczbe calkowita wieksza od 1")
            Dialog.exec_()
        #Dialog.setText("what")

    def losuj(self):
        #global tempX
        try:
            N = int(self.wymiarTextEdit.toPlainText())
            od = float(self.losowoOdTextEdit.toPlainText())
            do = float(self.losowoDoTextEdit.toPlainText())
            tempX = np.array([random.uniform(od,do) for x in range(N)],np.float64) #losowanie wartosci zmiennych równań
            for y in range(N):
                 self.daneTableWidget.setItem(N,y,QtGui.QTableWidgetItem(str(tempX[y])))
            self.daneTableWidget.setItem(N,N,QtGui.QTableWidgetItem("EMPTY"))

            if od == "" or do == "":
                raise Exception
            for x in range(N):
                for y in range(N):
                    self.daneTableWidget.setItem(x,y,QtGui.QTableWidgetItem(str(random.uniform(od,do))))

            A = np.array([[float(self.daneTableWidget.item(y,x).text()) for x in range(N)] for y in range(N)],np.float64)


            B = np.array([0.0 for x in range(N)],np.float64) #macierz wyliczonych b (ax=b)
            #print "tempX " + str(tempX)

            for y in range(N):
                sum = 0.0
                for x in range(N):
                    #print A[y][x],"*",tempX[x]
                    sum += A[y][x]*tempX[x]
                #print sum
                self.daneTableWidget.setItem(y,N,QtGui.QTableWidgetItem(str(sum))) #row,column

            #print tempX
        except Exception:
            Dialog = QtGui.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.lab("Sprawdz:*czy zatwierdziles wymiar tablicy; *podane dane do generacji!")
            Dialog.exec_()


    def wynik(self):
        #a = float(self.tableWidget.item(0,0).text())
        data_type = 'fff'
        N = int(self.wymiarTextEdit.toPlainText())
        """ AA = np.array([[5,4,2],     #00 01 02 03
                       [1,2,0],     #10 11 12 13
                       [3,0,4]])    #20 21 22 23"""


        A = np.array([[float(self.daneTableWidget.item(y,x).text()) for x in range(N)] for y in range(N)],np.float64)
        B = np.array([float(self.daneTableWidget.item(x,N).text()) for x in range(N)],np.float64)
        #print A
        #print B

        if self.daneTableWidget.item(N,0) != None:
            tempX = np.array([float(self.daneTableWidget.item(N,y).text()) for y in range(N)],np.float64)

        L = np.array([[0.0 for x in range(N)] for x in range(N)],np.float64)
        U = np.array([[0.0 for x in range(N)] for x in range(N)],np.float64)
        X = np.array([0.0 for x in range(N)],np.float64)
        Y = np.array([0.0 for x in range(N)],np.float64)

        #1.0 na przekatnej L
        for i in range(N):
            L[i][i] = 1.0

        #L i U
        for i in range(N):
            #i-ty wiersz U
            for j in range(N):
                suma = 0.0
                for k in range(i):
                    suma += L[i][k]*U[k][j]
                U[i][j] = A[i][j] - suma
            #i-ta kolumna L
            for j in range(i+1,N):
                suma = 0.0
                for k in range(i):
                    suma += L[j][k]*U[k][i]
                L[j][i] = (A[j][i] - suma) / U[i][i]

        #wektor Y
        for i in range(N):
            suma = 0.0
            for k in range(i):
                suma += L[i][k]*Y[k]
            Y[i] = B[i] - suma

        #wektor X
        for i in np.arange(N-1,-1,-1):
            suma = 0.0
            for k in range(i+1,N):
                suma += U[i][k]*X[k]
            X[i] = np.float64((Y[i] - suma) / U[i][i])

        #print X
        self.wynikTextEdit.setText("")

        if self.daneTableWidget.item(N,0) != None:
            bladBezwzgledny = np.array([abs(tempX[x]-X[x]) for x in range(N)],np.float64)
            bladWzgledny = np.array([abs(tempX[x]-X[x])/tempX[x] for x in range(N)],np.float64)

        if self.daneTableWidget.item(N,0) != None:
            self.wynikTextEdit.append("Sredni blad bezwgledny = " + str(np.average(bladBezwzgledny)))
            self.wynikTextEdit.append("Max blad bezwgledny = " + str(np.max(bladBezwzgledny)))
            self.wynikTextEdit.append("Min blad bezwgledny = " + str(np.min(bladBezwzgledny)))
            self.wynikTextEdit.append("Sredni blad wgledny = " + str((np.average(bladWzgledny)*100.0)) + "%")
            self.wynikTextEdit.append("Max blad wgledny = " + str((np.max(bladWzgledny)*100.0)) + "%")
            self.wynikTextEdit.append("Min blad wgledny = " + str((np.min(bladWzgledny)*100.0)) + "%")

        if self.daneTableWidget.item(N,0) != None:
            for id in range(len(X)):
                 self.wynikTextEdit.append("x" + str(id+1) + " = " + str(X[id]) + "   wylosowane " + str(tempX[id]))
        else:
            for id in range(len(X)):
                 self.wynikTextEdit.append("x" + str(id+1) + " = " + str(X[id]))
        #print result
        #self.wymiarTextEdit.setText(result)

        """ print "tempX" + str(tempX)
        print "bladBezwzgledny" + str(bladBezwzgledny)
        print "bladWzgledny" + str(bladWzgledny)
        print "abs(tempX[0]-X[0]) " + str(tempX[0]-X[0])
        sth = tempX[0]-X[0]
        print str(sth)
        print "tempX[0] " + str(tempX[0])
        print "X[0] " + str(X[0])"""

        if self.daneTableWidget.item(N,0) != None:
            with open('result.csv', 'a') as f:
                f.writelines("\r"+str(N)+";"
                        +self.losowoOdTextEdit.toPlainText()+";"
                        +self.losowoDoTextEdit.toPlainText()+";"
                        +str(np.max(bladBezwzgledny))+";"
                        +str(np.min(bladBezwzgledny))+";"
                        +str(np.average(bladBezwzgledny))+";"
                        +str((np.max(bladWzgledny))*100.0)+";"
                        +str((np.min(bladWzgledny))*100.0)+";"
                        +str((np.average(bladWzgledny))*100.0)+";",
                )


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


