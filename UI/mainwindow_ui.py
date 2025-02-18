# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(901, 629)
        self.actionSetup = QAction(MainWindow)
        self.actionSetup.setObjectName(u"actionSetup")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 881, 561))
        self.tab_rawdata = QWidget()
        self.tab_rawdata.setObjectName(u"tab_rawdata")
        self.groupBox_statistics = QGroupBox(self.tab_rawdata)
        self.groupBox_statistics.setObjectName(u"groupBox_statistics")
        self.groupBox_statistics.setGeometry(QRect(10, 10, 851, 511))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupBox_statistics.setFont(font)
        self.verticalLayoutWidget = QWidget(self.groupBox_statistics)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 621, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_1 = QLabel(self.verticalLayoutWidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(16777180, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_1.setFont(font1)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_1)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.checkBox_reads = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_reads.setObjectName(u"checkBox_reads")
        self.checkBox_reads.setFont(font1)

        self.horizontalLayout_2.addWidget(self.checkBox_reads)

        self.checkBox_bases = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_bases.setObjectName(u"checkBox_bases")
        self.checkBox_bases.setFont(font1)

        self.horizontalLayout_2.addWidget(self.checkBox_bases)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayoutWidget = QWidget(self.groupBox_statistics)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 80, 831, 371))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 734, 317))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 2, 1, 1, 1)

        self.progressBar_rawdata_analysis = QProgressBar(self.gridLayoutWidget)
        self.progressBar_rawdata_analysis.setObjectName(u"progressBar_rawdata_analysis")
        self.progressBar_rawdata_analysis.setValue(24)

        self.gridLayout_2.addWidget(self.progressBar_rawdata_analysis, 1, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.button_analysis_start = QPushButton(self.gridLayoutWidget)
        self.button_analysis_start.setObjectName(u"button_analysis_start")
        self.button_analysis_start.setEnabled(True)
        self.button_analysis_start.setFont(font1)

        self.gridLayout_2.addWidget(self.button_analysis_start, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_rawdata, "")
        self.tab_fastqcreport = QWidget()
        self.tab_fastqcreport.setObjectName(u"tab_fastqcreport")
        self.verticalLayoutWidget_2 = QWidget(self.tab_fastqcreport)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 231, 521))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_fastQC_Report = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_fastQC_Report.setObjectName(u"pushButton_fastQC_Report")
        self.pushButton_fastQC_Report.setEnabled(True)

        self.verticalLayout_3.addWidget(self.pushButton_fastQC_Report)

        self.progressBar_fastqc = QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_fastqc.setObjectName(u"progressBar_fastqc")
        self.progressBar_fastqc.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar_fastqc)

        self.radioButton_base_seq_quality = QRadioButton(self.verticalLayoutWidget_2)
        self.fastqcRadioButtonGroup = QButtonGroup(MainWindow)
        self.fastqcRadioButtonGroup.setObjectName(u"fastqcRadioButtonGroup")
        self.fastqcRadioButtonGroup.addButton(self.radioButton_base_seq_quality)
        self.radioButton_base_seq_quality.setObjectName(u"radioButton_base_seq_quality")
        self.radioButton_base_seq_quality.setEnabled(False)
        font2 = QFont()
        font2.setPointSize(12)
        self.radioButton_base_seq_quality.setFont(font2)

        self.verticalLayout_3.addWidget(self.radioButton_base_seq_quality)

        self.radioButton_base_seq_content = QRadioButton(self.verticalLayoutWidget_2)
        self.fastqcRadioButtonGroup.addButton(self.radioButton_base_seq_content)
        self.radioButton_base_seq_content.setObjectName(u"radioButton_base_seq_content")
        self.radioButton_base_seq_content.setEnabled(False)
        self.radioButton_base_seq_content.setFont(font2)

        self.verticalLayout_3.addWidget(self.radioButton_base_seq_content)

        self.listWidget_fastqcreport = QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_fastqcreport.setObjectName(u"listWidget_fastqcreport")

        self.verticalLayout_3.addWidget(self.listWidget_fastqcreport)

        self.verticalLayoutWidget_3 = QWidget(self.tab_fastqcreport)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(250, 10, 621, 521))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_image = QLabel(self.verticalLayoutWidget_3)
        self.label_image.setObjectName(u"label_image")

        self.verticalLayout_4.addWidget(self.label_image)

        self.tabWidget.addTab(self.tab_fastqcreport, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 901, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionSetup)
        self.menu.addAction(self.actionClear)
        self.menu.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metagenome Analysis Tool", None))
        self.actionSetup.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.groupBox_statistics.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u91cf\u7edf\u8ba1", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u539f\u59cb\u6570\u636e\uff1a", None))
        self.checkBox_reads.setText(QCoreApplication.translate("MainWindow", u"Total Reads", None))
        self.checkBox_bases.setText(QCoreApplication.translate("MainWindow", u"Total Bases", None))
        self.button_analysis_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5206\u6790", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rawdata), QCoreApplication.translate("MainWindow", u"\u6d4b\u5e8f\u6570\u636e", None))
        self.pushButton_fastQC_Report.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210FastQC Report", None))
        self.radioButton_base_seq_quality.setText(QCoreApplication.translate("MainWindow", u"Read \u78b1\u57fa\u8d28\u91cf\u5206\u5e03\u56fe", None))
        self.radioButton_base_seq_content.setText(QCoreApplication.translate("MainWindow", u"Read \u78b1\u57fa\u7ec4\u6210\u5206\u5e03\u56fe", None))
        self.label_image.setText(QCoreApplication.translate("MainWindow", u"Image  will appear here", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fastqcreport), QCoreApplication.translate("MainWindow", u"FastQC Report", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Trim\u8d28\u63a7", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
    # retranslateUi

