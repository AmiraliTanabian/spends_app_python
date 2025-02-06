from PyQt5 import QtCore, QtGui, QtWidgets
import database


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setStyleSheet('color:white;')
        Dialog.setStyleSheet('background:#13213C')
        Dialog.resize(504, 300)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        
        self.tableWidget.setGeometry(QtCore.QRect(0, 70, 501, 91))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 220, 88, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(197, 220, 101, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/remove2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 25))
        self.pushButton_2.clicked.connect(self.deleteBtn)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 220, 88, 27))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.update_date)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # __________________________ NEW COLOR _____________________________________
        self.tableWidget.setStyleSheet('color:white;')
        self.pushButton.setStyleSheet('color:white;')
        self.pushButton_2.setStyleSheet('color:white;')
        self.pushButton_3.setStyleSheet('color:white;')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ویرایش خرج"))
        Dialog.setWindowIcon(QtGui.QIcon('icon/pencil.png'))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "نام"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "دسته بندی"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "قیمت "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "زمان "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "توضیحات"))
        self.pushButton.setText(_translate("Dialog", "انصراف"))
        self.pushButton_2.setText(_translate("Dialog", "حذف خرج"))
        self.pushButton_3.setText(_translate("Dialog", "تایید "))


    def set_data(self, name, category, price, time, discription):
        self.name = name
        self.category = category

        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(name))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(category))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(price))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(time))
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(discription))

    def update_date(self): 
        new_name = self.tableWidget.item(0,0).text()
        new_cat = self.tableWidget.item(0,1).text()
        new_price = self.tableWidget.item(0,2).text()
        new_time = self.tableWidget.item(0,3).text()
        new_disc = self.tableWidget.item(0,4).text()




        if new_name == '' or new_cat == '' or new_price == '' or new_time == '':
            print(True)
            # On of the fild is empty 
            emptyWaring = QtWidgets.QMessageBox()
            emptyWaring.setText('یکی از فیلد های جدول خالی میباشد!')
            emptyWaring.setWindowTitle('خالی بودن صفحه')
            emptyWaring.setWindowIcon(QtGui.QIcon("icon/alert.png"))
            emptyWaring.defaultButton()
            emptyWaring.exec()
        else : 
            database.update(self.name, self.category, new_name , new_cat , new_price , new_time , new_disc )


            completeUpdatingMsgBox = QtWidgets.QMessageBox()
            completeUpdatingMsgBox.setWindowTitle('آپدیت خرج')
            completeUpdatingMsgBox.setText('خرج با موفقیت آپدیت شد.')
            completeUpdatingMsgBox.setWindowIcon(QtGui.QIcon(r'icon\update.png'))
            completeUpdatingMsgBox.exec()
        
            
    def deleteBtn(self):
        database.delete(self.name, self.category)

        completeDeletingMsgBox = QtWidgets.QMessageBox()
        completeDeletingMsgBox.setWindowTitle('حذف خرج')
        completeDeletingMsgBox.setText('حذف حرج با موفقیت انجام شد.')
        completeDeletingMsgBox.setWindowIcon(QtGui.QIcon('../icon/remove2.png'))
        completeDeletingMsgBox.exec()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    
    sys.exit(app.exec_())
