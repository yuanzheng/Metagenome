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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QCheckBox,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(899, 628)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionSetup = QAction(MainWindow)
        self.actionSetup.setObjectName(u"actionSetup")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(13)
        self.tabWidget.setFont(font)
        self.tab_rawdata = QWidget()
        self.tab_rawdata.setObjectName(u"tab_rawdata")
        self.horizontalLayoutWidget = QWidget(self.tab_rawdata)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 861, 531))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_1 = QLabel(self.horizontalLayoutWidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(16777180, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_1.setFont(font1)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_1)

        self.listWidget_fastq_analysis = QListWidget(self.horizontalLayoutWidget)
        self.listWidget_fastq_analysis.setObjectName(u"listWidget_fastq_analysis")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget_fastq_analysis.sizePolicy().hasHeightForWidth())
        self.listWidget_fastq_analysis.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.listWidget_fastq_analysis.setFont(font2)
        self.listWidget_fastq_analysis.setAlternatingRowColors(False)
        self.listWidget_fastq_analysis.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.listWidget_fastq_analysis.setSelectionRectVisible(False)

        self.verticalLayout_6.addWidget(self.listWidget_fastq_analysis)

        self.verticalLayout_6.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_fastq_analysis = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_fastq_analysis.setObjectName(u"groupBox_fastq_analysis")
        sizePolicy.setHeightForWidth(self.groupBox_fastq_analysis.sizePolicy().hasHeightForWidth())
        self.groupBox_fastq_analysis.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_fastq_analysis)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_total_bases = QCheckBox(self.groupBox_fastq_analysis)
        self.checkBox_total_bases.setObjectName(u"checkBox_total_bases")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.checkBox_total_bases.setFont(font3)
        self.checkBox_total_bases.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_total_bases)

        self.checkBox_total_reads = QCheckBox(self.groupBox_fastq_analysis)
        self.checkBox_total_reads.setObjectName(u"checkBox_total_reads")
        self.checkBox_total_reads.setFont(font3)
        self.checkBox_total_reads.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_total_reads)

        self.checkBox_Q20 = QCheckBox(self.groupBox_fastq_analysis)
        self.checkBox_Q20.setObjectName(u"checkBox_Q20")
        self.checkBox_Q20.setFont(font2)
        self.checkBox_Q20.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_Q20)

        self.checkBox_Q30 = QCheckBox(self.groupBox_fastq_analysis)
        self.checkBox_Q30.setObjectName(u"checkBox_Q30")
        self.checkBox_Q30.setFont(font2)
        self.checkBox_Q30.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_Q30)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_3.setStretch(4, 1)

        self.verticalLayout_7.addWidget(self.groupBox_fastq_analysis)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_analysis_start = QPushButton(self.horizontalLayoutWidget)
        self.button_analysis_start.setObjectName(u"button_analysis_start")
        self.button_analysis_start.setEnabled(True)
        self.button_analysis_start.setFont(font1)
        self.button_analysis_start.setStyleSheet(u"background-color: rgb(5, 155, 72);")

        self.horizontalLayout_2.addWidget(self.button_analysis_start)

        self.progressBar_fastq_analysis = QProgressBar(self.horizontalLayoutWidget)
        self.progressBar_fastq_analysis.setObjectName(u"progressBar_fastq_analysis")
        self.progressBar_fastq_analysis.setValue(0)

        self.horizontalLayout_2.addWidget(self.progressBar_fastq_analysis)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.tableWidget_fastq_analysis = QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget_fastq_analysis.setObjectName(u"tableWidget_fastq_analysis")
        self.tableWidget_fastq_analysis.setFont(font2)
        self.tableWidget_fastq_analysis.setAlternatingRowColors(True)

        self.verticalLayout_7.addWidget(self.tableWidget_fastq_analysis)

        self.verticalLayout_7.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
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
        self.progressBar_fastqc.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar_fastqc)

        self.radioButton_base_seq_quality = QRadioButton(self.verticalLayoutWidget_2)
        self.fastqcRadioButtonGroup = QButtonGroup(MainWindow)
        self.fastqcRadioButtonGroup.setObjectName(u"fastqcRadioButtonGroup")
        self.fastqcRadioButtonGroup.addButton(self.radioButton_base_seq_quality)
        self.radioButton_base_seq_quality.setObjectName(u"radioButton_base_seq_quality")
        self.radioButton_base_seq_quality.setEnabled(False)
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
        self.listWidget_fastqcreport.setFont(font2)

        self.verticalLayout_3.addWidget(self.listWidget_fastqcreport)

        self.verticalLayoutWidget_3 = QWidget(self.tab_fastqcreport)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(250, 10, 621, 521))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_image = QLabel(self.verticalLayoutWidget_3)
        self.label_image.setObjectName(u"label_image")
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.label_image)

        self.tabWidget.addTab(self.tab_fastqcreport, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 899, 24))
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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metagenome Analysis Tool", None))
        self.actionSetup.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u539f\u59cb\u6570\u636e\uff1a", None))
        self.groupBox_fastq_analysis.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7edf\u8ba1\u9879", None))
        self.checkBox_total_bases.setText(QCoreApplication.translate("MainWindow", u"Total Bases", None))
        self.checkBox_total_reads.setText(QCoreApplication.translate("MainWindow", u"Total Reads", None))
        self.checkBox_Q20.setText(QCoreApplication.translate("MainWindow", u"Q 20", None))
        self.checkBox_Q30.setText(QCoreApplication.translate("MainWindow", u"Q 30", None))
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

