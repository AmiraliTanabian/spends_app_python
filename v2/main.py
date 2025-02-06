import Pages.editRowPage as ed
import datetime
import database
import database as db
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as graph

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # This var use for detect app is startuo or no (function: showByFilter)
        self.index = 0
        
        MainWindow.setWindowTitle('مدیریت مخارج')
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMaximumSize(816, 639)
        MainWindow.setMinimumSize(816, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ______________________ SET TAB WIDGET _________________________
        self.TabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(270, 0, 600, 621))
        self.TabWidget.setObjectName('TabWidget')
        # First Tab
        self.FirstTab = QtWidgets.QWidget()
        self.FirstTab.setObjectName("First Tab")
        self.TabWidget.addTab(self.FirstTab, "جدول")
        # Second Tab
        self.SecondTab = QtWidgets.QWidget()
        self.SecondTab.setObjectName("Second Tab")
        self.TabWidget.addTab(self.SecondTab, "تحلیل مخارج")
        



        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(40, 290, 75, 23))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(10)
        self.add_btn.setFont(font)
        self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_btn.setObjectName("add_btn")
        self.discription_input = QtWidgets.QLineEdit(self.centralwidget)
        self.discription_input.setGeometry(QtCore.QRect(10, 200, 113, 20))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(10)
        self.discription_input.setFont(font)
        self.discription_input.setObjectName("discription_input")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(10, 170, 113, 20))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(10)
        self.name_input.setFont(font)
        self.name_input.setObjectName("name_input")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 0, 10, 641))
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.group_input = QtWidgets.QLineEdit(self.centralwidget)
        self.group_input.setGeometry(QtCore.QRect(10, 230, 113, 20))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(10)
        self.group_input.setFont(font)
        self.group_input.setObjectName("group_input")
        self.pay_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pay_input.setGeometry(QtCore.QRect(10, 260, 113, 20))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(10)
        self.pay_input.setFont(font)
        self.pay_input.setObjectName("pay_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(186, 170, 21, 20))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 200, 100, 20))
        
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 230, 71, 20))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Set success ful msg
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(-50, 340, 291, 101))
        font_lalezar = QtGui.QFont()
        font_lalezar.setFamily("Lalezar")
        font_lalezar.setPointSize(13)
        self.label_6.setFont(font_lalezar)
        self.label_6.setStyleSheet("color:green;\n""")
        self.label_6.setText( "خرج شما با موفقیت به فهرست اضافه شد.")
        self.label_6.hide()

        # ____________ icons of add spend part ______________
        self.name_icon = QtWidgets.QLabel(self.centralwidget)
        self.name_icon.setGeometry(QtCore.QRect(230, 170, 20, 19))
        self.name_icon.setText("")
        self.name_icon.setPixmap(QtGui.QPixmap("icon/name_icon.png"))
        self.name_icon.setObjectName("name_icon")

        self.info_icon = QtWidgets.QLabel(self.centralwidget)
        self.info_icon.setGeometry(QtCore.QRect(230, 200, 30, 19))
        self.info_icon.setText("")
        self.info_icon.setPixmap(QtGui.QPixmap("icon/category_icon.png"))
        self.info_icon.setObjectName("info_icon")

        self.category_icon = QtWidgets.QLabel(self.centralwidget)
        self.category_icon.setGeometry(QtCore.QRect(230, 230, 30, 19))
        self.category_icon.setText("")
        self.category_icon.setPixmap(QtGui.QPixmap("icon/group_icon.png"))
        self.category_icon.setObjectName("category_icon")

        self.price_icon = QtWidgets.QLabel(self.centralwidget)
        self.price_icon.setGeometry(QtCore.QRect(231, 259, 20, 20))
        self.price_icon.setText("")
        self.price_icon.setPixmap(QtGui.QPixmap("icon/price_icon.png.png"))
        self.price_icon.setObjectName("price_icon")


        self.add_icon_lbl = QtWidgets.QLabel(self.centralwidget)
        self.add_icon_lbl.setGeometry(QtCore.QRect(200, 100, 61, 61))
        self.add_icon_lbl.setText("")
        self.add_icon_lbl.setPixmap(QtGui.QPixmap("icon/add_icon.png"))
        self.add_icon_lbl.setObjectName("add_icon_lbl")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 260, 41, 20))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(40, 320, 75, 23))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(10)
        self.exit_btn.setFont(font)
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_btn.setObjectName("exit_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-10, 100, 191, 61))

        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(self.FirstTab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 551, 561))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # _______________________________FILTER PART___________________________________
        self.label_7 = QtWidgets.QLabel(parent=self.FirstTab)
        self.label_7.setGeometry(QtCore.QRect(490, 370, 61, 71))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("icon/find.png"))
        self.label_7.setObjectName("label_7")
        self.search_lbl = QtWidgets.QLabel(parent=self.FirstTab)
        self.search_lbl.setGeometry(QtCore.QRect(370, 360, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.search_lbl.setFont(font)
        self.search_lbl.setObjectName("search_lbl")
        self.date_filter = QtWidgets.QLabel(parent=self.FirstTab)
        self.date_filter.setGeometry(QtCore.QRect(460, 490, 71, 41))
        self.date_filter.setObjectName("date_filter")
        self.Filter_name_lebel = QtWidgets.QLabel(parent=self.FirstTab)
        self.Filter_name_lebel.setGeometry(QtCore.QRect(510, 440, 21, 20))
        self.Filter_name_lebel.setObjectName("Filter_name_lebel")
        self.categoryFilter = QtWidgets.QLabel(parent=self.FirstTab)
        self.categoryFilter.setGeometry(QtCore.QRect(470, 470, 66, 20))
        self.categoryFilter.setObjectName("categoryFilter")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.FirstTab)
        self.lineEdit.setGeometry(QtCore.QRect(380, 440, 121, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.showByFilter)
        self.comboBox = QtWidgets.QComboBox(parent=self.FirstTab)
        self.comboBox.setGeometry(QtCore.QRect(380, 470, 81, 27))
        self.comboBox.setCurrentIndex(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem(' - ')
        self.comboBox.currentTextChanged.connect(self.showByFilter)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.FirstTab)
        self.dateEdit.setDisplayFormat('yy/M/d')
        self.dateEdit.setGeometry(QtCore.QRect(380, 500, 110, 28))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.dateChanged.connect(self.showByFilter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.resetButton = QtWidgets.QPushButton(parent=self.FirstTab)
        self.resetButton.setGeometry(QtCore.QRect(360, 536, 61, 21))
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.FilterResetButton)
        self.resetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ##################################################################################

        # Set the delete all table button
        self.delete_all_btn = QtWidgets.QPushButton(self.FirstTab)
        self.delete_all_btn.setGeometry(QtCore.QRect(0, 380, 151, 27))
        self.delete_all_btn.setObjectName("delete_all_btn")
        self.delete_all_btn.setIcon(QtGui.QIcon('icon/remove2.png'))
        self.delete_all_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_all_btn.clicked.connect(self.delete_all_items)


        self.retranslateUi(MainWindow)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # set table readonly
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Set validator for the pay fild
        validator = QtGui.QIntValidator()
        self.pay_input.setValidator(validator)
        self.show_dates_for_first()

        # Create timer
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)

        self.add_btn.clicked.connect(self.show_dates)
        self.exit_btn.clicked.connect(self.exit)

        # self.tableWidget.cellClicked['int', 'int'].connect(self.test)
        self.tableWidget.cellClicked['int', 'int'].connect(self.cellClicked)

        self.update_category_filter()

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.total_lbl2 = QtWidgets.QLabel(self.SecondTab)
        self.total_lbl2.setGeometry(QtCore.QRect(355, 50, 171, 51))
        self.total_lbl2.setObjectName("total_lbl2")
        self.total_lbl2.setText('نمایش مجموع خرج ها')
        self.total_combo = QtWidgets.QComboBox(self.SecondTab)
        self.total_combo.setGeometry(QtCore.QRect(270, 60, 86, 27))
        self.total_combo.setObjectName("total_combo")
        self.total_combo.addItem(' - ')
        self.total_combo.addItem("ماهانه")
        self.total_combo.addItem("روزانه")
        self.total_combo.addItem("سالانه")
        self.total_combo.addItem("هفتگی")
        self.total_combo.setCurrentIndex(0)
        self.total_combo.currentIndexChanged.connect(self.total_handler)
        self.total_lbl3 = QtWidgets.QLabel(self.SecondTab)
        self.total_lbl3.setText('برای نمایش مجموع خرج ها آیتم بالا را انتخاب کنید ')
        self.total_lbl3.setGeometry(QtCore.QRect(90, 100, 311, 20))
        self.total_lbl3.setObjectName("total_lbl3")
        self.line_3 = QtWidgets.QFrame(self.SecondTab)
        self.line_3.setGeometry(QtCore.QRect(0, 150, 561, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.total_lbl = QtWidgets.QLabel(self.SecondTab)
        self.total_lbl.setText('مجموع خرج ها')
        self.total_lbl.setGeometry(QtCore.QRect(170, 10, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.total_lbl.setFont(font)
        self.total_lbl.setObjectName("total_lbl")
        self.label_11 = QtWidgets.QLabel(self.SecondTab)
        self.label_11.setGeometry(QtCore.QRect(490, 0, 61, 60))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("icon/tota.png"))
        self.label_11.setObjectName("label_11")
        self.TabWidget.addTab(self.SecondTab, "تحلیل مخارج")


        # ____________________CHART PART_____________________________
        self.chart_lbl1 = QtWidgets.QLabel(self.SecondTab)
        self.chart_lbl1.setGeometry(QtCore.QRect(160, 170, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.chart_lbl1.setFont(font)
        self.chart_lbl1.setObjectName("chart_lbl1")
        self.chart_lbl1.setText('نمایش نمودار')
        self.chart_lbl2 = QtWidgets.QLabel(self.SecondTab)
        self.chart_lbl2.setGeometry(QtCore.QRect(360, 210, 171, 51))
        self.chart_lbl2.setObjectName("chart_lbl2")
        self.chart_lbl2.setText('نمایش نمودار بر اساس خرج ')
        self.chart_combo = QtWidgets.QComboBox(self.SecondTab)
        self.chart_combo.setGeometry(QtCore.QRect(270, 220, 86, 27))
        self.chart_combo.setObjectName("chart_combo")
        self.chart_combo.addItem(" - ")
        self.chart_combo.addItem("ماهانه")
        self.chart_combo.addItem("سالانه")
        self.chart_combo.addItem("هفتگی")
        self.chart_combo.setCurrentIndex(0)
        self.label_12 = QtWidgets.QLabel(self.SecondTab)
        self.label_12.setGeometry(QtCore.QRect(490, 160, 61, 60))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("icon/chart_icon.png"))
        self.label_12.setObjectName("label_12")
        self.warning_chart = QtWidgets.QLabel(self.SecondTab)
        self.warning_chart.setGeometry(QtCore.QRect(70, 250, 411, 51))
        self.warning_chart.setStyleSheet("color:red;")
        self.warning_chart.setObjectName("chart_lbl2_2")
        self.warning_chart.setText("ابتدا مشخص کنید نمودار بر اساس خرج چه مدتی نمایش داده شود ! ")
        
        # ________________________________________ GRAPH _______________________________________________
        self.graph = graph.PlotWidget(self.SecondTab)
        self.graph.setGeometry(QtCore.QRect(10, 300, 521, 241))
        self.graph_pen = graph.mkPen(color=(255, 0,0))
        self.graph.hide()
        self.chart_combo.currentTextChanged.connect(self.graph_handler)

        # __________________________________________ NEW COLOR ___________________________________________
        self.TabWidget.setStyleSheet("color:white; background:#293b5c")
        self.add_btn.setStyleSheet("background:white")
        self.pay_input.setStyleSheet("color:white; background:#293b5c;")
        self.name_input.setStyleSheet("color:white;  background:#293b5c")
        self.discription_input.setStyleSheet("color:white;background:#293b5c")
        self.group_input.setStyleSheet("color:white;background:#293b5c")
        # MainWindow.setStyleSheet('background-color:#13213C')
        MainWindow.setStyleSheet('background-color:#6f85ad')

        self.label.setStyleSheet('color:white;')
        self.label_2.setStyleSheet('color:white;')
        self.label_3.setStyleSheet('color:white;')
        self.label_4.setStyleSheet('color:white;')
        self.label_6.setStyleSheet('color:white;')
        self.label_5.setStyleSheet('color:white;')
        self.total_lbl.setStyleSheet('color:white;')
        self.total_lbl2.setStyleSheet('color:white;')
        self.total_lbl3.setStyleSheet('color:white;')
        self.chart_lbl1.setStyleSheet('color:white;')
        self.chart_lbl2.setStyleSheet('color:white;')
        self.warning_chart.setStyleSheet('color:white;')
        self.lineEdit.setStyleSheet('color:white;')
        self.comboBox.setStyleSheet('color:white;')
        self.dateEdit.setStyleSheet('color:white;')
        self.tableWidget.setStyleSheet('''color:white;''')
        self.FirstTab.setStyleSheet('color:white')
        self.add_btn.setStyleSheet('''
                                   QPushButton:hover{
                                   background:#243657;
                                   }''')
        
        


    def graph_handler(self):
        # item[3] = data
        # item[2] = pay (price)
        if self.chart_combo.currentText() == ' - ':
            self.warning_chart.show()
            self.graph.hide()
        
        elif self.chart_combo.currentText() == 'هفتگی' : 
            self.graph.clear()
            self.graph.show()
            self.graph.setTitle('مخارج هفته جاری')
            self.warning_chart.hide()


            result = dict.fromkeys(['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 0)
            for item in database.show() : 
                date = item[3].split('|')[0].strip().split('/') # [year, month, day]
                date_year = int(date[0]) + 2000
                data_month = int(date[1])
                data_day = int(date[2])
                date_object = datetime.date(date_year, data_month, data_day)
                date_week = datetime.datetime.isocalendar(date_object).week
                current_week = datetime.datetime.isocalendar(datetime.datetime.now()).week
                current_year = datetime.datetime.now().year

                if current_week == date_week and current_year == date_year : 
                    day_name = date_object.strftime('%A').capitalize()
                    result[day_name] += float(item[2])
                
            self.graph.plot(list(range(1,8)), list(result.values()),
                            symbol='+', symbolSize=20, symbolBrush='#50E6FF', pen=self.graph_pen)

        elif self.chart_combo.currentText() == 'ماهانه':
            self.graph.clear()
            self.graph.setTitle('مخارج ماه جاری')
            self.warning_chart.hide()
            self.graph.show()

            current_month = int(datetime.datetime.now().month)
            current_year = int(datetime.datetime.now().year)

            result = dict.fromkeys(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], 0)
            for item in database.show():
                date = item[3].split('|')[0].strip().split('/')
                year = int(date[0]) + 2000 
                month = int(date[1]) 
                day = int(date[2])
                date_object = datetime.date(year, month, day)
                
                if year == current_year:
                    month_name = date_object.strftime('%B')
                    result[month_name] += float(item[2])

            self.graph.plot(list(range(1,13)), list(result.values()),
                    symbol='+', symbolSize=20, symbolBrush='#50E6FF', pen=self.graph_pen )

        else :
            self.graph.setTitle('مخارج سال جاری')
            self.warning_chart.hide()
            self.graph.clear()
            self.graph.show()

            years_list = set()
            for item in database.show():
                date_year = int(item[3].split('|')[0].strip().split('/')[0]) + 2000
                years_list.add(date_year)

            years_list = list(years_list)
            years_list.sort()

            result = dict.fromkeys(years_list, 0)
            current_year = datetime.datetime.now().year
            for item in database.show() :
                date = item[3].split('|')[0].strip().split('/')
                date_year = int(date[0]) + 2000

                
                result[date_year] += float(item[2])

            print(list(result.values()))
            self.graph.plot(years_list, list(result.values()),
                            symbol='+', symbolSize=20, symbolBrush='#50E6FF', pen=self.graph_pen)
                
            

    def total_handler(self):
        self.current_year = datetime.datetime.now().year


        if self.total_combo.currentText() == ' - ':
            # User dont select item
            self.total_lbl3.setText('برای نمایش مجموع خرج ها آیتم بالا را انتخاب کنید ')
        elif self.total_combo.currentText() == 'ماهانه' : 
            now = datetime.datetime.now()
            now_year = now.year - 2000
            now_month = now.month
            finally_now = f'{now_year}/{now_month}'

            currents_pay = []
            for item in database.show():
                # remove day from date 
                date = item[3].split('|')[0].strip()
                date = date.split('/')[:2]
                date = '/'.join(date)

                if date == finally_now:
                    # item[2] : pay
                    currents_pay.append(float(item[2]))

            total_year_price = sum(currents_pay)

            # show result 
            self.total_lbl3.setText(f'شما در این  ماه {str(total_year_price)} هزینه کردید ')


        elif self.total_combo.currentText() == 'سالانه' :

            currents_pay = []
            for item in database.show():
                date = item[3].split('|')[0].strip()
                if str(self.current_year)[2:] in date:
                    pay = item[2]
                    currents_pay.append(float(pay))

            total_year_price = sum(currents_pay)

            # Show result 
            self.total_lbl3.setText(f'شما در این  سال {str(total_year_price)} هزینه کردید ')

        elif self.total_combo.currentText() == 'روزانه':

            # get current date with the database saving format
            now = datetime.datetime.now()
            now_year = now.year - 2000
            now_month = now.month
            now_day = now.day
            finally_now = f'{now_year}/{now_month}/{now_day}'

            currents_pay = []
            for item in database.show():
                # get the spend date from database and remove the time E.X : 25/6/29 | 23:34 --> 25/6/29 
                date = item[3].split('|')[0].strip()
                if date == finally_now:
                    # item[2] : pay
                    currents_pay.append(float(item[2]))

            total_year_price = sum(currents_pay)

            # show result 
            self.total_lbl3.setText(f'شما در این  روز {str(total_year_price)} هزینه کردید ')


        # هفتگی
        else:

            # get current week
            now = datetime.datetime.now()
            current_week = datetime.datetime.isocalendar(now).week

            currents_pay = []
            # get the databases item week
            for item in database.show():
                date = item[3].split('|')[0].strip()
                date_year = int(date.split('/')[0])
                date_month = int(date.split('/')[1])
                date_day = int(date.split('/')[2])

                week = datetime.datetime.isocalendar(datetime.date(date_year, date_month, date_day)).week

                if week == current_week : 
                    # item[2] = pay
                    currents_pay.append(float(item[2]))

            total_year_price = sum(currents_pay)

            # show result 
            self.total_lbl3.setText(f'شما در این  هفته {str(total_year_price)} هزینه کردید ')
            

    def cellClicked(self, row, col):
        self.clicked_row = row

        Dialog = QtWidgets.QDialog()
        ui = ed.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()

        # Insert current row on the pop up 
        name = self.tableWidget.item(row, 0).text()
        cat = self.tableWidget.item(row, 1).text()
        price = self.tableWidget.item(row, 2).text()
        time = self.tableWidget.item(row, 3).text()
        disc = self.tableWidget.item(row, 4).text()


        ui.set_data(name, cat, price, time, disc)        

        Dialog.exec_()

        self.show_dates_for_first()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.add_btn.setText(_translate("MainWindow", "افزودن"))
        self.discription_input.setPlaceholderText(_translate("MainWindow", "Discription "))
        self.name_input.setPlaceholderText(_translate("MainWindow", "Name "))
        self.group_input.setPlaceholderText(_translate("MainWindow", "Group"))
        self.pay_input.setPlaceholderText(_translate("MainWindow", "Pay"))
        self.label.setText(_translate("MainWindow", "نام "))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>توضیحات<span style=\" font-size:7pt;\">(اختیاری) </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "دسته بندی"))
        self.label_4.setText(_translate("MainWindow", "قیمت "))
        self.exit_btn.setText(_translate("MainWindow", "خروج"))
        self.exit_btn.setStyleSheet('background-color:red;')
        self.label_5.setText(_translate("MainWindow", "افزودن خرج"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "نام "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "دسته بندی "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "قیمت "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "زمان "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "توضیحات "))
        self.delete_all_btn.setText(_translate("MainWindow", "پاک کردن کل جدول"))
        self.search_lbl.setText(_translate("MainWindow", "فیلتر"))
        self.Filter_name_lebel.setText(_translate("MainWindow", "نام"))
        self.categoryFilter.setText(_translate("MainWindow", "دسته بندی "))
        self.date_filter.setText(_translate("MainWindow", "تاریخ"))
        self.resetButton.setText(_translate("MainWindow", "ریست"))

        



    def delete_all_items(self):

        msgBoxRemoveAll = QtWidgets.QMessageBox()
        msgBoxRemoveAll.setText('آیا از حذف کامل جدول اطمیمان دارید؟ \n بعد از این امکان بازیابی جدول وجود ندارد.')
        msgBoxRemoveAll.setIcon(QtWidgets.QMessageBox.Warning)
        msgBoxRemoveAll.setStyleSheet('color:#13213C')
        msgBoxRemoveAll.setWindowTitle('هشدار برای حذف کامل جدول')
        msgBoxRemoveAll.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msgBoxRemoveAll.buttonClicked.connect(self.delete_all_handeler)
        msgBoxRemoveAll.exec()






    def delete_all_handeler(self, btn):
        # User need to remove all of the item at table
        if btn.text() == '&OK' :
            print(True)
            import os
            os.remove('database.db')
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)

            database.createTable()
            database.init()

            removeResult = QtWidgets.QMessageBox()
            removeResult.setWindowTitle('حذف کل جدول')
            removeResult.setText('تمام خرج ها حذف شدند!')
            removeResult.exec()



    def show_dates(self):
        name = self.name_input.text().strip()
        description = self.discription_input.text().strip()
        category = self.group_input.text().strip()
        pay = self.pay_input.text().strip()

        if name == '' or category == '' or pay == '' :
            emptyError = QtWidgets.QMessageBox()
            emptyError.setText('لطفا همه مقادیر را به درستی وارد نمایید')
            emptyError.setWindowTitle('خالی بودن فیلد ورودی')
            emptyError.setIcon(QtWidgets.QMessageBox.Information)
            emptyError.setStyleSheet('color:#13213C;')
            emptyError.exec()

        else:    
            db.app_spend(name, category, pay, description)
            db.init()


            result = db.show()
            rowCount = len(result)
            self.tableWidget.setRowCount(rowCount)

            self.displayItems(result)

            def hide():
                self.label_6.hide()

            # Show msg
            self.label_6.show()
            self.timer.timeout.connect(hide)
            self.timer.start(3000)

            # clear all the filds 
            self.name_input.clear()
            self.discription_input.clear()
            self.pay_input.clear()
            self.group_input.clear()

            # update combo box
            self.update_category_filter()


    def show_dates_for_first(self):
        db.init()

        result = db.show()
        rowCount = len(result)
        self.tableWidget.setRowCount(rowCount)

        j = 0
        for item in result:
            for (i, __item__) in enumerate(item):
                self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(__item__))
            j += 1

    def showByFilter(self):
        # if index == 0 -- > App is startup and filter part don't do anythig
        if self.index != 0 :
            FName = self.lineEdit.text().strip() # defualt = ""
            FCategory = self.comboBox.itemText(self.comboBox.currentIndex()) # defualt = " - "
            FDate = self.dateEdit.text() # Default = 00/1/1
            print(FCategory)
            # The filteres are empty

            if FName == '' and FDate == '00/1/1' and FCategory == ' - ' :
                self.show_dates_for_first()


            # Just the name get value
            elif FName != '' and FCategory == ' - ' and FDate == '00/1/1' :
                allTableItem = database.show()

                def FilterFunc(item):
                    if FName in item[0]:
                       return True

                result = list(filter(FilterFunc, allTableItem))

                rowCount = len(result)
                self.tableWidget.setRowCount(rowCount)

                self.displayItems(result)


            elif FName != '' and FCategory != ' - ' and FDate == '00/1/1':
                allTableItem = database.show()
                
                def FilterFunc(item):
                    if FName in item[0] and FCategory == item[1] :
                        return True

                    
                result = list(filter(FilterFunc,allTableItem))
                rowCount = len(result)
                self.tableWidget.setRowCount(rowCount)

                self.displayItems(result)

            # all of the filter filds get value
            elif FName != '' and FCategory != ' - ' and FDate != '00/1/1' :
                allTableItem = database.show()

                def FilterFunc(item):
                    if FName in item[0] and FCategory == item[1] and FDate == item[3].split('|')[0].strip():
                        return True


                result = list(filter(FilterFunc, allTableItem))

                self.displayItems(result)

            elif FName != '' and FCategory == ' - ' and FDate != '00/1/1':
                allTableItem = database.show()

                def FilterFunc(item):
                    if FName in item[0] and FDate == item[3].split('|')[0].strip():
                        return True


                result = list(filter(FilterFunc, allTableItem))
                print("Result:", result)
                self.displayItems(result)


            elif FName == '' and FCategory != ' - ' and FDate != '00/1/1' :
                allTableItem = database.show()
                def FilterFunc(item):
                    if FCategory in item[1] and FDate in item[3].split('|')[0].strip():
                        return True


                result = list(filter(FilterFunc, allTableItem))
                self.displayItems(result)


            elif FName == '' and FCategory != '' and FDate == '00/1/1' :
                allTableItem = database.show()
                def FilterFunc(item):
                    if FCategory == item[1]:
                        return True



                result = list(filter(FilterFunc, allTableItem))
                self.displayItems(result)


            # when just give  new date
            elif FDate != '00/1/1' and FName == '' and FCategory == ' - ':
                allTableItem = database.show()
                def FilterFunc(item):
                    if FDate == item[3].split('|')[0].strip() :
                        return True
                result = list(filter(FilterFunc, allTableItem))
                self.displayItems(result)



        self.index += 1


    def FilterResetButton(self):
        self.lineEdit.clear()
        # 00/1/1
        self.dateEdit.setDisplayFormat('yy/M/d')
        self.dateEdit.setDate(QtCore.QDate(2000, 1, 1))
        self.comboBox.setCurrentIndex(0)
        self.show_dates_for_first()
        

    def displayItems(self, result):
        self.tableWidget.clearContents()
        j = 0
        for item in result:
            for (i, __item__) in enumerate(item):
                self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(__item__))
            j += 1

    def update_category_filter(self):
        all_on_db = db.show()

        allComboItems = []
        count = self.comboBox.count()
        for i in range(1, count + 1):
            allComboItems.append(self.comboBox.itemText(i))
        allComboItems = set(allComboItems)


        categories = set(map(lambda item:item[1], all_on_db))

        addItems = []
        for element in categories :
            if element not in allComboItems :
                addItems.append(element)

        self.comboBox.addItems(addItems)


    def exit(self):
        raise SystemExit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
