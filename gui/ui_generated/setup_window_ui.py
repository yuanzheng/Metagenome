# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SetupForm(object):
    def setupUi(self, SetupForm):
        if not SetupForm.objectName():
            SetupForm.setObjectName(u"SetupForm")
        SetupForm.resize(618, 311)
        font = QFont()
        font.setPointSize(12)
        SetupForm.setFont(font)
        self.gridLayout = QGridLayout(SetupForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.groupBox = QGroupBox(SetupForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_fastQDataDirectory = QLineEdit(self.groupBox)
        self.lineEdit_fastQDataDirectory.setObjectName(u"lineEdit_fastQDataDirectory")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_fastQDataDirectory.sizePolicy().hasHeightForWidth())
        self.lineEdit_fastQDataDirectory.setSizePolicy(sizePolicy)
        self.lineEdit_fastQDataDirectory.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_fastQDataDirectory.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit_fastQDataDirectory)

        self.pushButton_searchFastQDataDirectory = QPushButton(self.groupBox)
        self.pushButton_searchFastQDataDirectory.setObjectName(u"pushButton_searchFastQDataDirectory")
        self.pushButton_searchFastQDataDirectory.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_searchFastQDataDirectory)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_fastQParser = QLineEdit(self.groupBox)
        self.lineEdit_fastQParser.setObjectName(u"lineEdit_fastQParser")
        self.lineEdit_fastQParser.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lineEdit_fastQParser)

        self.pushButton_fastQParser = QPushButton(self.groupBox)
        self.pushButton_fastQParser.setObjectName(u"pushButton_fastQParser")
        self.pushButton_fastQParser.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_fastQParser)

        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_fastQCReportDirectory = QLineEdit(self.groupBox)
        self.lineEdit_fastQCReportDirectory.setObjectName(u"lineEdit_fastQCReportDirectory")
        sizePolicy.setHeightForWidth(self.lineEdit_fastQCReportDirectory.sizePolicy().hasHeightForWidth())
        self.lineEdit_fastQCReportDirectory.setSizePolicy(sizePolicy)
        self.lineEdit_fastQCReportDirectory.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.lineEdit_fastQCReportDirectory.setFont(font2)
        self.lineEdit_fastQCReportDirectory.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_4.addWidget(self.lineEdit_fastQCReportDirectory)

        self.pushButton_fastQCDirectory = QPushButton(self.groupBox)
        self.pushButton_fastQCDirectory.setObjectName(u"pushButton_fastQCDirectory")
        self.pushButton_fastQCDirectory.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton_fastQCDirectory)

        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_fastqQualityStats = QLineEdit(self.groupBox)
        self.lineEdit_fastqQualityStats.setObjectName(u"lineEdit_fastqQualityStats")
        self.lineEdit_fastqQualityStats.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lineEdit_fastqQualityStats)

        self.pushButton_fastqQualityStats = QPushButton(self.groupBox)
        self.pushButton_fastqQualityStats.setObjectName(u"pushButton_fastqQualityStats")
        self.pushButton_fastqQualityStats.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pushButton_fastqQualityStats)

        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEdit_trimmed_fastq_directory = QLineEdit(self.groupBox)
        self.lineEdit_trimmed_fastq_directory.setObjectName(u"lineEdit_trimmed_fastq_directory")
        sizePolicy.setHeightForWidth(self.lineEdit_trimmed_fastq_directory.sizePolicy().hasHeightForWidth())
        self.lineEdit_trimmed_fastq_directory.setSizePolicy(sizePolicy)
        self.lineEdit_trimmed_fastq_directory.setSizeIncrement(QSize(0, 0))
        self.lineEdit_trimmed_fastq_directory.setFont(font2)
        self.lineEdit_trimmed_fastq_directory.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_6.addWidget(self.lineEdit_trimmed_fastq_directory)

        self.pushButton_search_trimmed_files = QPushButton(self.groupBox)
        self.pushButton_search_trimmed_files.setObjectName(u"pushButton_search_trimmed_files")
        self.pushButton_search_trimmed_files.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pushButton_search_trimmed_files)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)

        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)

        self.pushButton_save = QPushButton(SetupForm)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.gridLayout.addWidget(self.pushButton_save, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.pushButton_cancel = QPushButton(SetupForm)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.gridLayout.addWidget(self.pushButton_cancel, 2, 1, 1, 1)


        self.retranslateUi(SetupForm)

        QMetaObject.connectSlotsByName(SetupForm)
    # setupUi

    def retranslateUi(self, SetupForm):
        SetupForm.setWindowTitle(QCoreApplication.translate("SetupForm", u"\u914d\u7f6e\u53c2\u6570", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("SetupForm", u"\u539f\u59cb\u6570\u636e\u76ee\u5f55", None))
        self.pushButton_searchFastQDataDirectory.setText(QCoreApplication.translate("SetupForm", u"\u67e5\u627e...", None))
        self.label_2.setText(QCoreApplication.translate("SetupForm", u"FastQ \u78b1\u57fa\u89e3\u6790\u5668", None))
        self.pushButton_fastQParser.setText(QCoreApplication.translate("SetupForm", u"\u67e5\u627e...", None))
        self.label_3.setText(QCoreApplication.translate("SetupForm", u"FastQC Report \u8f93\u51fa\u76ee\u5f55", None))
        self.pushButton_fastQCDirectory.setText(QCoreApplication.translate("SetupForm", u"\u67e5\u627e...", None))
        self.label_4.setText(QCoreApplication.translate("SetupForm", u"FastQ \u8d28\u63a7(Trim)", None))
        self.pushButton_fastqQualityStats.setText(QCoreApplication.translate("SetupForm", u"\u67e5\u627e...", None))
        self.label_5.setText(QCoreApplication.translate("SetupForm", u"Trimmed FASTQ \u8f93\u51fa\u76ee\u5f55", None))
        self.pushButton_search_trimmed_files.setText(QCoreApplication.translate("SetupForm", u"\u67e5\u627e...", None))
        self.pushButton_save.setText(QCoreApplication.translate("SetupForm", u"\u4fdd\u5b58", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("SetupForm", u"\u53d6\u6d88", None))
    # retranslateUi

