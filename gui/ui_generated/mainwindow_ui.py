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
    QComboBox, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(902, 806)
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
        font.setPointSize(12)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget_fastq_analysis.sizePolicy().hasHeightForWidth())
        self.listWidget_fastq_analysis.setSizePolicy(sizePolicy2)
        self.listWidget_fastq_analysis.setFont(font)
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
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.checkBox_total_bases.setFont(font2)
        self.checkBox_total_bases.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_total_bases)

        self.checkBox_total_reads = QCheckBox(self.groupBox_fastq_analysis)
        self.checkBox_total_reads.setObjectName(u"checkBox_total_reads")
        self.checkBox_total_reads.setFont(font2)
        self.checkBox_total_reads.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_total_reads)

        self.checkBox_Q20 = QCheckBox(self.groupBox_fastq_analysis)
        self.checkBox_Q20.setObjectName(u"checkBox_Q20")
        self.checkBox_Q20.setFont(font)
        self.checkBox_Q20.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_Q20)

        self.checkBox_Q30 = QCheckBox(self.groupBox_fastq_analysis)
        self.checkBox_Q30.setObjectName(u"checkBox_Q30")
        self.checkBox_Q30.setFont(font)
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
        self.tableWidget_fastq_analysis.setFont(font)
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
        self.pushButton_fastQC_Report.setFont(font)
        self.pushButton_fastQC_Report.setStyleSheet(u"background-color: rgb(5, 155, 72);")

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
        self.radioButton_base_seq_quality.setFont(font)

        self.verticalLayout_3.addWidget(self.radioButton_base_seq_quality)

        self.radioButton_base_seq_content = QRadioButton(self.verticalLayoutWidget_2)
        self.fastqcRadioButtonGroup.addButton(self.radioButton_base_seq_content)
        self.radioButton_base_seq_content.setObjectName(u"radioButton_base_seq_content")
        self.radioButton_base_seq_content.setEnabled(False)
        self.radioButton_base_seq_content.setFont(font)

        self.verticalLayout_3.addWidget(self.radioButton_base_seq_content)

        self.listWidget_fastqcreport = QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_fastqcreport.setObjectName(u"listWidget_fastqcreport")
        self.listWidget_fastqcreport.setFont(font)

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
        self.tab_trimFastQ = QWidget()
        self.tab_trimFastQ.setObjectName(u"tab_trimFastQ")
        self.verticalLayoutWidget = QWidget(self.tab_trimFastQ)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 814, 681))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setMaximumSize(QSize(90, 30))

        self.verticalLayout_13.addWidget(self.label_7)

        self.listWidget_trim_rawdata = QListWidget(self.verticalLayoutWidget)
        self.listWidget_trim_rawdata.setObjectName(u"listWidget_trim_rawdata")
        sizePolicy1.setHeightForWidth(self.listWidget_trim_rawdata.sizePolicy().hasHeightForWidth())
        self.listWidget_trim_rawdata.setSizePolicy(sizePolicy1)
        self.listWidget_trim_rawdata.setMinimumSize(QSize(0, 200))
        self.listWidget_trim_rawdata.setMaximumSize(QSize(150, 300))
        self.listWidget_trim_rawdata.setFont(font)
        self.listWidget_trim_rawdata.setAlternatingRowColors(False)
        self.listWidget_trim_rawdata.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.listWidget_trim_rawdata.setSelectionRectVisible(False)

        self.verticalLayout_13.addWidget(self.listWidget_trim_rawdata)

        self.verticalLayout_13.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_13)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(130, 30))
        self.label.setFont(font)

        self.horizontalLayout_5.addWidget(self.label)

        self.comboBox_trim_paired_end = QComboBox(self.verticalLayoutWidget)
        self.comboBox_trim_paired_end.setObjectName(u"comboBox_trim_paired_end")
        sizePolicy1.setHeightForWidth(self.comboBox_trim_paired_end.sizePolicy().hasHeightForWidth())
        self.comboBox_trim_paired_end.setSizePolicy(sizePolicy1)
        self.comboBox_trim_paired_end.setMinimumSize(QSize(50, 20))
        self.comboBox_trim_paired_end.setMaximumSize(QSize(50, 20))
        self.comboBox_trim_paired_end.setFont(font)

        self.horizontalLayout_5.addWidget(self.comboBox_trim_paired_end)

        self.horizontalSpacer_3 = QSpacerItem(54, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(270, 230))
        self.groupBox.setMaximumSize(QSize(270, 250))
        self.verticalLayoutWidget_6 = QWidget(self.groupBox)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 30, 251, 185))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(71, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.verticalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.comboBox_trim_adapter = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_trim_adapter.setObjectName(u"comboBox_trim_adapter")
        self.comboBox_trim_adapter.setFont(font)

        self.horizontalLayout_6.addWidget(self.comboBox_trim_adapter)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(53, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.verticalLayoutWidget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.spinBox_trim_seed_mismatches = QSpinBox(self.verticalLayoutWidget_6)
        self.spinBox_trim_seed_mismatches.setObjectName(u"spinBox_trim_seed_mismatches")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_seed_mismatches.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_seed_mismatches.setSizePolicy(sizePolicy1)
        self.spinBox_trim_seed_mismatches.setFont(font)
        self.spinBox_trim_seed_mismatches.setValue(2)

        self.horizontalLayout_7.addWidget(self.spinBox_trim_seed_mismatches)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_7 = QSpacerItem(4, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.label_4 = QLabel(self.verticalLayoutWidget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.spinBox_trim_palindrome = QSpinBox(self.verticalLayoutWidget_6)
        self.spinBox_trim_palindrome.setObjectName(u"spinBox_trim_palindrome")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_palindrome.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_palindrome.setSizePolicy(sizePolicy1)
        self.spinBox_trim_palindrome.setFont(font)
        self.spinBox_trim_palindrome.setValue(30)
        self.spinBox_trim_palindrome.setDisplayIntegerBase(10)

        self.horizontalLayout_8.addWidget(self.spinBox_trim_palindrome)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_10 = QSpacerItem(29, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.label_5 = QLabel(self.verticalLayoutWidget_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.spinBox_trim_simple = QSpinBox(self.verticalLayoutWidget_6)
        self.spinBox_trim_simple.setObjectName(u"spinBox_trim_simple")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_simple.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_simple.setSizePolicy(sizePolicy1)
        self.spinBox_trim_simple.setFont(font)
        self.spinBox_trim_simple.setValue(10)

        self.horizontalLayout_9.addWidget(self.spinBox_trim_simple)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_12 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.label_6 = QLabel(self.verticalLayoutWidget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.comboBox_trim_keepbothreads = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_trim_keepbothreads.setObjectName(u"comboBox_trim_keepbothreads")
        self.comboBox_trim_keepbothreads.setFont(font)

        self.horizontalLayout_10.addWidget(self.comboBox_trim_keepbothreads)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 4)
        self.verticalLayout_5.setStretch(2, 2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.trim_paramLayout = QVBoxLayout()
        self.trim_paramLayout.setObjectName(u"trim_paramLayout")
        self.groupBox_trim_slidingwindow = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_trim_slidingwindow.setObjectName(u"groupBox_trim_slidingwindow")
        sizePolicy1.setHeightForWidth(self.groupBox_trim_slidingwindow.sizePolicy().hasHeightForWidth())
        self.groupBox_trim_slidingwindow.setSizePolicy(sizePolicy1)
        self.groupBox_trim_slidingwindow.setMinimumSize(QSize(170, 100))
        self.groupBox_trim_slidingwindow.setMaximumSize(QSize(180, 100))
        self.groupBox_trim_slidingwindow.setFont(font)
        self.verticalLayoutWidget_9 = QWidget(self.groupBox_trim_slidingwindow)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 30, 151, 56))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.verticalLayoutWidget_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(100, 20))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_9)

        self.spinBox_trim_window_size = QSpinBox(self.verticalLayoutWidget_9)
        self.spinBox_trim_window_size.setObjectName(u"spinBox_trim_window_size")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_window_size.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_window_size.setSizePolicy(sizePolicy1)
        self.spinBox_trim_window_size.setMinimumSize(QSize(50, 20))
        self.spinBox_trim_window_size.setMaximumSize(QSize(50, 20))
        self.spinBox_trim_window_size.setValue(1)

        self.horizontalLayout_11.addWidget(self.spinBox_trim_window_size)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.verticalLayoutWidget_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(100, 20))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_10)

        self.spinBox_trim_window_quality = QSpinBox(self.verticalLayoutWidget_9)
        self.spinBox_trim_window_quality.setObjectName(u"spinBox_trim_window_quality")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_window_quality.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_window_quality.setSizePolicy(sizePolicy1)
        self.spinBox_trim_window_quality.setMinimumSize(QSize(50, 20))
        self.spinBox_trim_window_quality.setMaximumSize(QSize(50, 20))
        self.spinBox_trim_window_quality.setValue(10)

        self.horizontalLayout_12.addWidget(self.spinBox_trim_window_quality)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)


        self.trim_paramLayout.addWidget(self.groupBox_trim_slidingwindow)

        self.leading_widget = QHBoxLayout()
        self.leading_widget.setObjectName(u"leading_widget")
        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(80, 0))
        self.label_8.setMaximumSize(QSize(80, 20))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.leading_widget.addWidget(self.label_8)

        self.spinBox_trim_leading = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_trim_leading.setObjectName(u"spinBox_trim_leading")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_leading.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_leading.setSizePolicy(sizePolicy1)
        self.spinBox_trim_leading.setMinimumSize(QSize(50, 20))
        self.spinBox_trim_leading.setMaximumSize(QSize(50, 20))

        self.leading_widget.addWidget(self.spinBox_trim_leading)

        self.leading_widget.setStretch(0, 1)

        self.trim_paramLayout.addLayout(self.leading_widget)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(80, 0))
        self.label_11.setMaximumSize(QSize(80, 20))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_11)

        self.spinBox_trim_trailing = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_trim_trailing.setObjectName(u"spinBox_trim_trailing")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_trailing.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_trailing.setSizePolicy(sizePolicy1)
        self.spinBox_trim_trailing.setMinimumSize(QSize(50, 20))
        self.spinBox_trim_trailing.setMaximumSize(QSize(50, 20))

        self.horizontalLayout_13.addWidget(self.spinBox_trim_trailing)

        self.horizontalLayout_13.setStretch(0, 1)

        self.trim_paramLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setMinimumSize(QSize(80, 0))
        self.label_12.setMaximumSize(QSize(80, 20))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_12)

        self.spinBox_trim_maxnn = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_trim_maxnn.setObjectName(u"spinBox_trim_maxnn")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_maxnn.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_maxnn.setSizePolicy(sizePolicy1)
        self.spinBox_trim_maxnn.setMinimumSize(QSize(50, 20))
        self.spinBox_trim_maxnn.setMaximumSize(QSize(50, 20))

        self.horizontalLayout_14.addWidget(self.spinBox_trim_maxnn)

        self.horizontalLayout_14.setStretch(0, 1)

        self.trim_paramLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(80, 0))
        self.label_13.setMaximumSize(QSize(80, 20))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_13)

        self.spinBox_trim_minlen = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_trim_minlen.setObjectName(u"spinBox_trim_minlen")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_minlen.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_minlen.setSizePolicy(sizePolicy1)
        self.spinBox_trim_minlen.setMinimumSize(QSize(50, 20))
        self.spinBox_trim_minlen.setMaximumSize(QSize(50, 20))

        self.horizontalLayout_15.addWidget(self.spinBox_trim_minlen)

        self.horizontalLayout_15.setStretch(0, 1)

        self.trim_paramLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(80, 0))
        self.label_14.setMaximumSize(QSize(80, 20))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_14)

        self.spinBox_trim_crop = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_trim_crop.setObjectName(u"spinBox_trim_crop")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_crop.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_crop.setSizePolicy(sizePolicy1)
        self.spinBox_trim_crop.setMinimumSize(QSize(50, 20))
        self.spinBox_trim_crop.setMaximumSize(QSize(50, 20))

        self.horizontalLayout_16.addWidget(self.spinBox_trim_crop)

        self.horizontalLayout_16.setStretch(0, 1)

        self.trim_paramLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setMinimumSize(QSize(80, 0))
        self.label_15.setMaximumSize(QSize(80, 20))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_15)

        self.spinBox_trim_headcrop = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_trim_headcrop.setObjectName(u"spinBox_trim_headcrop")
        sizePolicy1.setHeightForWidth(self.spinBox_trim_headcrop.sizePolicy().hasHeightForWidth())
        self.spinBox_trim_headcrop.setSizePolicy(sizePolicy1)
        self.spinBox_trim_headcrop.setMinimumSize(QSize(50, 20))
        self.spinBox_trim_headcrop.setMaximumSize(QSize(50, 20))

        self.horizontalLayout_17.addWidget(self.spinBox_trim_headcrop)

        self.horizontalLayout_17.setStretch(0, 1)

        self.trim_paramLayout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_16 = QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(100, 20))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_16)

        self.comboBox_trim_phred_code = QComboBox(self.verticalLayoutWidget)
        self.comboBox_trim_phred_code.setObjectName(u"comboBox_trim_phred_code")
        sizePolicy1.setHeightForWidth(self.comboBox_trim_phred_code.sizePolicy().hasHeightForWidth())
        self.comboBox_trim_phred_code.setSizePolicy(sizePolicy1)
        self.comboBox_trim_phred_code.setMinimumSize(QSize(100, 20))
        self.comboBox_trim_phred_code.setMaximumSize(QSize(100, 20))

        self.horizontalLayout_18.addWidget(self.comboBox_trim_phred_code)

        self.horizontalLayout_18.setStretch(0, 1)

        self.trim_paramLayout.addLayout(self.horizontalLayout_18)

        self.trim_paramLayout.setStretch(0, 3)
        self.trim_paramLayout.setStretch(1, 1)
        self.trim_paramLayout.setStretch(2, 1)
        self.trim_paramLayout.setStretch(3, 1)
        self.trim_paramLayout.setStretch(4, 1)
        self.trim_paramLayout.setStretch(5, 1)
        self.trim_paramLayout.setStretch(6, 1)
        self.trim_paramLayout.setStretch(7, 1)

        self.horizontalLayout_4.addLayout(self.trim_paramLayout)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_trim_params = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_trim_params.setObjectName(u"groupBox_trim_params")
        self.groupBox_trim_params.setMinimumSize(QSize(150, 300))
        self.groupBox_trim_params.setMaximumSize(QSize(150, 300))
        self.listWidget_trim_params_orders = QListWidget(self.groupBox_trim_params)
        self.listWidget_trim_params_orders.setObjectName(u"listWidget_trim_params_orders")
        self.listWidget_trim_params_orders.setGeometry(QRect(10, 30, 131, 261))
        sizePolicy1.setHeightForWidth(self.listWidget_trim_params_orders.sizePolicy().hasHeightForWidth())
        self.listWidget_trim_params_orders.setSizePolicy(sizePolicy1)
        self.listWidget_trim_params_orders.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)

        self.verticalLayout_11.addWidget(self.groupBox_trim_params)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(3, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_10 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_10.setSpacing(-1)
#endif
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_start_trim = QPushButton(self.verticalLayoutWidget)
        self.pushButton_start_trim.setObjectName(u"pushButton_start_trim")
        sizePolicy1.setHeightForWidth(self.pushButton_start_trim.sizePolicy().hasHeightForWidth())
        self.pushButton_start_trim.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u".AppleSystemUIFont"])
        font3.setPointSize(12)
        self.pushButton_start_trim.setFont(font3)
        self.pushButton_start_trim.setStyleSheet(u"background-color: rgb(5, 155, 72);")

        self.verticalLayout_10.addWidget(self.pushButton_start_trim)

        self.pushButton_start_analysis = QPushButton(self.verticalLayoutWidget)
        self.pushButton_start_analysis.setObjectName(u"pushButton_start_analysis")
        self.pushButton_start_analysis.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pushButton_start_analysis.sizePolicy().hasHeightForWidth())
        self.pushButton_start_analysis.setSizePolicy(sizePolicy1)
        self.pushButton_start_analysis.setFont(font3)
        self.pushButton_start_analysis.setStyleSheet(u"background-color: rgb(59, 104, 244)")

        self.verticalLayout_10.addWidget(self.pushButton_start_analysis)


        self.gridLayout.addLayout(self.verticalLayout_10, 0, 1, 1, 1)

        self.groupBox_trim_cmd_preview = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_trim_cmd_preview.setObjectName(u"groupBox_trim_cmd_preview")
        sizePolicy.setHeightForWidth(self.groupBox_trim_cmd_preview.sizePolicy().hasHeightForWidth())
        self.groupBox_trim_cmd_preview.setSizePolicy(sizePolicy)
        self.groupBox_trim_cmd_preview.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.textEdit_trim_cmd_preview = QTextEdit(self.groupBox_trim_cmd_preview)
        self.textEdit_trim_cmd_preview.setObjectName(u"textEdit_trim_cmd_preview")
        self.textEdit_trim_cmd_preview.setGeometry(QRect(10, 30, 701, 31))

        self.gridLayout.addWidget(self.groupBox_trim_cmd_preview, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.progressBar_trim_tab = QProgressBar(self.verticalLayoutWidget)
        self.progressBar_trim_tab.setObjectName(u"progressBar_trim_tab")
        self.progressBar_trim_tab.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar_trim_tab)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_17 = QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)

        self.verticalLayout_14.addWidget(self.label_17)

        self.listWidget_fastq_analysis_trimmed = QListWidget(self.verticalLayoutWidget)
        self.listWidget_fastq_analysis_trimmed.setObjectName(u"listWidget_fastq_analysis_trimmed")
        sizePolicy2.setHeightForWidth(self.listWidget_fastq_analysis_trimmed.sizePolicy().hasHeightForWidth())
        self.listWidget_fastq_analysis_trimmed.setSizePolicy(sizePolicy2)
        self.listWidget_fastq_analysis_trimmed.setMinimumSize(QSize(0, 200))
        self.listWidget_fastq_analysis_trimmed.setMaximumSize(QSize(16777215, 200))
        self.listWidget_fastq_analysis_trimmed.setFont(font)
        self.listWidget_fastq_analysis_trimmed.setAlternatingRowColors(False)
        self.listWidget_fastq_analysis_trimmed.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.listWidget_fastq_analysis_trimmed.setSelectionRectVisible(False)

        self.verticalLayout_14.addWidget(self.listWidget_fastq_analysis_trimmed)

        self.verticalLayout_14.setStretch(1, 1)

        self.horizontalLayout_19.addLayout(self.verticalLayout_14)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.tableWidget_fastq_analysis_trimmed = QTableWidget(self.groupBox_2)
        self.tableWidget_fastq_analysis_trimmed.setObjectName(u"tableWidget_fastq_analysis_trimmed")
        self.tableWidget_fastq_analysis_trimmed.setGeometry(QRect(10, 30, 641, 201))
        self.tableWidget_fastq_analysis_trimmed.setFont(font)
        self.tableWidget_fastq_analysis_trimmed.setAlternatingRowColors(True)

        self.horizontalLayout_19.addWidget(self.groupBox_2)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_19)

        self.verticalLayout_2.setStretch(3, 1)
        self.tabWidget.addTab(self.tab_trimFastQ, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 902, 22))
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

        self.tabWidget.setCurrentIndex(2)


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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u539f\u59cb\u6570\u636e\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Paired-End/Single-End: ", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"ILLUMINACLIP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Adapter: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u9519\u914d\u6570\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Palindrome\u526a\u5207\u9600\u503c\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Simple\u526a\u5207\u9600\u503c\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u7559\u53cc\u7aef\u4fe1\u606f\uff1a", None))
        self.groupBox_trim_slidingwindow.setTitle(QCoreApplication.translate("MainWindow", u"SLIDINGWINDOW", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u5927\u5c0f:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u8d28\u91cf\u9608\u503c: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"LEADING: ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TRAILING: ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"MAXNN: ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"MINLEN: ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CROP: ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"HEADCROP: ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Phred \u5206\u6570\u7f16\u7801\uff1a", None))
        self.comboBox_trim_phred_code.setCurrentText("")
        self.groupBox_trim_params.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u987a\u5e8f\u63a7\u5236", None))
        self.pushButton_start_trim.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8d28\u63a7", None))
        self.pushButton_start_analysis.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5206\u6790", None))
        self.groupBox_trim_cmd_preview.setTitle(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u9884\u89c8\u533a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u8d28\u63a7\u540e\u6570\u636e\uff1a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8d28\u63a7\u540e\u6570\u636e\u91cf\u7edf\u8ba1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_trimFastQ), QCoreApplication.translate("MainWindow", u"Trim\u8d28\u63a7", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
    # retranslateUi

