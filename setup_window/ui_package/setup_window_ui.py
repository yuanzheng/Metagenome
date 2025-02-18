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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_SetupForm(object):
    def setupUi(self, SetupForm):
        if not SetupForm.objectName():
            SetupForm.setObjectName(u"SetupForm")
        SetupForm.resize(666, 187)
        font = QFont()
        font.setPointSize(12)
        SetupForm.setFont(font)
        self.gridLayout = QGridLayout(SetupForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_cancel = QPushButton(SetupForm)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.gridLayout.addWidget(self.pushButton_cancel, 1, 1, 1, 1)

        self.pushButton_save = QPushButton(SetupForm)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.gridLayout.addWidget(self.pushButton_save, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.groupBox = QGroupBox(SetupForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_fastQParser = QLineEdit(self.groupBox)
        self.lineEdit_fastQParser.setObjectName(u"lineEdit_fastQParser")
        font1 = QFont()
        font1.setPointSize(11)
        self.lineEdit_fastQParser.setFont(font1)

        self.gridLayout_4.addWidget(self.lineEdit_fastQParser, 4, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_4.addWidget(self.label_2, 4, 0, 1, 1)

        self.lineEdit_fastQCReportDirectory = QLineEdit(self.groupBox)
        self.lineEdit_fastQCReportDirectory.setObjectName(u"lineEdit_fastQCReportDirectory")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_fastQCReportDirectory.sizePolicy().hasHeightForWidth())
        self.lineEdit_fastQCReportDirectory.setSizePolicy(sizePolicy)
        self.lineEdit_fastQCReportDirectory.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.lineEdit_fastQCReportDirectory.setFont(font2)
        self.lineEdit_fastQCReportDirectory.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_4.addWidget(self.lineEdit_fastQCReportDirectory, 9, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_4.addWidget(self.label_3, 9, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_fastQParser = QPushButton(self.groupBox)
        self.pushButton_fastQParser.setObjectName(u"pushButton_fastQParser")
        self.pushButton_fastQParser.setFont(font1)

        self.gridLayout_4.addWidget(self.pushButton_fastQParser, 4, 2, 1, 1)

        self.lineEdit_fastQDataDirectory = QLineEdit(self.groupBox)
        self.lineEdit_fastQDataDirectory.setObjectName(u"lineEdit_fastQDataDirectory")
        self.lineEdit_fastQDataDirectory.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_fastQDataDirectory.setFont(font1)

        self.gridLayout_4.addWidget(self.lineEdit_fastQDataDirectory, 0, 1, 1, 1)

        self.pushButton_searchFastQDataDirectory = QPushButton(self.groupBox)
        self.pushButton_searchFastQDataDirectory.setObjectName(u"pushButton_searchFastQDataDirectory")
        self.pushButton_searchFastQDataDirectory.setFont(font1)

        self.gridLayout_4.addWidget(self.pushButton_searchFastQDataDirectory, 0, 2, 1, 1)

        self.pushButton_fastQCDirectory = QPushButton(self.groupBox)
        self.pushButton_fastQCDirectory.setObjectName(u"pushButton_fastQCDirectory")
        self.pushButton_fastQCDirectory.setFont(font1)

        self.gridLayout_4.addWidget(self.pushButton_fastQCDirectory, 9, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)


        self.retranslateUi(SetupForm)

        QMetaObject.connectSlotsByName(SetupForm)
    # setupUi

    def retranslateUi(self, SetupForm):
        SetupForm.setWindowTitle(QCoreApplication.translate("SetupForm", u"\u914d\u7f6e\u53c2\u6570", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("SetupForm", u"\u53d6\u6d88", None))
        self.pushButton_save.setText(QCoreApplication.translate("SetupForm", u"\u4fdd\u5b58", None))
        self.groupBox.setTitle(QCoreApplication.translate("SetupForm", u"\u8bf7\u7ed9\u51fa\u4e00\u4e0b\u53c2\u6570", None))
        self.label_2.setText(QCoreApplication.translate("SetupForm", u"FastQ \u89e3\u6790\u5668", None))
        self.label_3.setText(QCoreApplication.translate("SetupForm", u"FastQC Report \u8f93\u51fa\u76ee\u5f55", None))
        self.label.setText(QCoreApplication.translate("SetupForm", u"\u539f\u59cb\u6570\u636e\u76ee\u5f55", None))
        self.pushButton_fastQParser.setText(QCoreApplication.translate("SetupForm", u"\u67e5\u627e...", None))
        self.pushButton_searchFastQDataDirectory.setText(QCoreApplication.translate("SetupForm", u"\u67e5\u627e...", None))
        self.pushButton_fastQCDirectory.setText(QCoreApplication.translate("SetupForm", u"\u67e5\u627e...", None))
    # retranslateUi

