# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SideBar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 543)
        icon = QIcon()
        icon.addFile(u":/icons/Ir_logo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_widget = QWidget(self.centralwidget)
        self.icon_widget.setObjectName(u"icon_widget")
        self.verticalLayout_3 = QVBoxLayout(self.icon_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/icons/Ir_logo.jpg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_button = QPushButton(self.icon_widget)
        self.home_button.setObjectName(u"home_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/SideBar_Qt/icon/home-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setIconSize(QSize(20, 20))
        self.home_button.setCheckable(True)
        self.home_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_button)

        self.Tokenize_button = QPushButton(self.icon_widget)
        self.Tokenize_button.setObjectName(u"Tokenize_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/SideBar_Qt/icon/activity-feed-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.Tokenize_button.setIcon(icon2)
        self.Tokenize_button.setIconSize(QSize(20, 20))
        self.Tokenize_button.setCheckable(True)
        self.Tokenize_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Tokenize_button)

        self.stem_button = QPushButton(self.icon_widget)
        self.stem_button.setObjectName(u"stem_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/SideBar_Qt/icon/product-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.stem_button.setIcon(icon3)
        self.stem_button.setIconSize(QSize(20, 20))
        self.stem_button.setCheckable(True)
        self.stem_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.stem_button)

        self.normalize_button = QPushButton(self.icon_widget)
        self.normalize_button.setObjectName(u"normalize_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/SideBar_Qt/icon/dashboard-5-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.normalize_button.setIcon(icon4)
        self.normalize_button.setIconSize(QSize(20, 20))
        self.normalize_button.setCheckable(True)
        self.normalize_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.normalize_button)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 317, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exit_button = QPushButton(self.icon_widget)
        self.exit_button.setObjectName(u"exit_button")
        icon5 = QIcon()
        icon5.addFile(u":/icons/SideBar_Qt/icon/close-window-64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon5)
        self.exit_button.setIconSize(QSize(20, 20))
        self.exit_button.setCheckable(True)
        self.exit_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.exit_button)


        self.gridLayout.addWidget(self.icon_widget, 0, 0, 1, 1)

        self.fullMenu_widgt = QWidget(self.centralwidget)
        self.fullMenu_widgt.setObjectName(u"fullMenu_widgt")
        self.verticalLayout_4 = QVBoxLayout(self.fullMenu_widgt)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.fullMenu_widgt)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/Ir_logo.jpg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.fullMenu_widgt)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_button_2 = QPushButton(self.fullMenu_widgt)
        self.home_button_2.setObjectName(u"home_button_2")
        self.home_button_2.setIcon(icon1)
        self.home_button_2.setIconSize(QSize(14, 14))
        self.home_button_2.setCheckable(True)
        self.home_button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_button_2)

        self.Tokenize_button_2 = QPushButton(self.fullMenu_widgt)
        self.Tokenize_button_2.setObjectName(u"Tokenize_button_2")
        self.Tokenize_button_2.setIcon(icon2)
        self.Tokenize_button_2.setIconSize(QSize(14, 14))
        self.Tokenize_button_2.setCheckable(True)
        self.Tokenize_button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Tokenize_button_2)

        self.stem_button_2 = QPushButton(self.fullMenu_widgt)
        self.stem_button_2.setObjectName(u"stem_button_2")
        self.stem_button_2.setIcon(icon3)
        self.stem_button_2.setIconSize(QSize(14, 14))
        self.stem_button_2.setCheckable(True)
        self.stem_button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.stem_button_2)

        self.normalize_button_2 = QPushButton(self.fullMenu_widgt)
        self.normalize_button_2.setObjectName(u"normalize_button_2")
        self.normalize_button_2.setIcon(icon4)
        self.normalize_button_2.setIconSize(QSize(14, 14))
        self.normalize_button_2.setCheckable(True)
        self.normalize_button_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.normalize_button_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 351, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exit_button_2 = QPushButton(self.fullMenu_widgt)
        self.exit_button_2.setObjectName(u"exit_button_2")
        self.exit_button_2.setIcon(icon5)
        self.exit_button_2.setIconSize(QSize(14, 14))
        self.exit_button_2.setCheckable(True)
        self.exit_button_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.exit_button_2)


        self.gridLayout.addWidget(self.fullMenu_widgt, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.burger_button = QPushButton(self.widget)
        self.burger_button.setObjectName(u"burger_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/SideBar_Qt/icon/menu-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.burger_button.setIcon(icon6)
        self.burger_button.setIconSize(QSize(14, 14))
        self.burger_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.burger_button)

        self.horizontalSpacer_2 = QSpacerItem(102, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.search_lineEdit = QLineEdit(self.widget)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        font = QFont()
        font.setFamilies([u"8514oem"])
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.search_lineEdit)

        self.search_button = QPushButton(self.widget)
        self.search_button.setObjectName(u"search_button")
        icon7 = QIcon()
        icon7.addFile(u":/icons/SideBar_Qt/icon/search-13-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon7)
        self.search_button.setIconSize(QSize(10, 10))

        self.horizontalLayout.addWidget(self.search_button)

        self.horizontalSpacer = QSpacerItem(102, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.result_page = QWidget()
        self.result_page.setObjectName(u"result_page")
        self.horizontalLayout_4 = QHBoxLayout(self.result_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.result_page)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_4)

        self.result_listWidget = QListWidget(self.result_page)
        self.result_listWidget.setObjectName(u"result_listWidget")

        self.verticalLayout_6.addWidget(self.result_listWidget)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.result_page)
        self.tokenize_page = QWidget()
        self.tokenize_page.setObjectName(u"tokenize_page")
        self.verticalLayout_11 = QVBoxLayout(self.tokenize_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tokenize_Button = QPushButton(self.tokenize_page)
        self.tokenize_Button.setObjectName(u"tokenize_Button")

        self.verticalLayout_7.addWidget(self.tokenize_Button)

        self.label_5 = QLabel(self.tokenize_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_5)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.tokenize_listWidget = QListWidget(self.tokenize_page)
        self.tokenize_listWidget.setObjectName(u"tokenize_listWidget")

        self.verticalLayout_10.addWidget(self.tokenize_listWidget)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.stackedWidget.addWidget(self.tokenize_page)
        self.swords_page = QWidget()
        self.swords_page.setObjectName(u"swords_page")
        self.verticalLayout_12 = QVBoxLayout(self.swords_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stemer_Button = QPushButton(self.swords_page)
        self.stemer_Button.setObjectName(u"stemer_Button")

        self.verticalLayout_8.addWidget(self.stemer_Button)

        self.label_6 = QLabel(self.swords_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_6)

        self.swords_listWidget = QListWidget(self.swords_page)
        self.swords_listWidget.setObjectName(u"swords_listWidget")

        self.verticalLayout_8.addWidget(self.swords_listWidget)


        self.verticalLayout_12.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.swords_page)
        self.normalize_page = QWidget()
        self.normalize_page.setObjectName(u"normalize_page")
        self.verticalLayout_13 = QVBoxLayout(self.normalize_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Normalize_Button = QPushButton(self.normalize_page)
        self.Normalize_Button.setObjectName(u"Normalize_Button")

        self.verticalLayout_9.addWidget(self.Normalize_Button)

        self.label_7 = QLabel(self.normalize_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_7)

        self.normalized_listWidget = QListWidget(self.normalize_page)
        self.normalized_listWidget.setObjectName(u"normalized_listWidget")

        self.verticalLayout_9.addWidget(self.normalized_listWidget)


        self.verticalLayout_13.addLayout(self.verticalLayout_9)

        self.stackedWidget.addWidget(self.normalize_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.burger_button.toggled.connect(self.icon_widget.setVisible)
        self.burger_button.toggled.connect(self.fullMenu_widgt.setHidden)
        self.home_button.toggled.connect(self.home_button_2.setChecked)
        self.Tokenize_button.toggled.connect(self.Tokenize_button_2.setChecked)
        self.stem_button.toggled.connect(self.stem_button_2.setChecked)
        self.normalize_button.toggled.connect(self.normalize_button_2.setChecked)
        self.home_button_2.toggled.connect(self.home_button.setChecked)
        self.Tokenize_button_2.toggled.connect(self.Tokenize_button.setChecked)
        self.stem_button_2.toggled.connect(self.stem_button.setChecked)
        self.normalize_button_2.toggled.connect(self.normalize_button.setChecked)
        self.exit_button_2.clicked.connect(MainWindow.close)
        self.exit_button.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.home_button.setText("")
        self.Tokenize_button.setText("")
        self.stem_button.setText("")
        self.normalize_button.setText("")
        self.exit_button.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SideBar", None))
        self.home_button_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Tokenize_button_2.setText(QCoreApplication.translate("MainWindow", u"Tokenize", None))
        self.stem_button_2.setText(QCoreApplication.translate("MainWindow", u"Stemmer", None))
        self.normalize_button_2.setText(QCoreApplication.translate("MainWindow", u"Normalize", None))
        self.exit_button_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.burger_button.setText("")
        self.search_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"The results from the web search are:", None))
        self.tokenize_Button.setText(QCoreApplication.translate("MainWindow", u"Tokenize", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"The tokenized form of the sentence is:", None))
        self.stemer_Button.setText(QCoreApplication.translate("MainWindow", u"Stem", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"The stemmed words are:", None))
        self.Normalize_Button.setText(QCoreApplication.translate("MainWindow", u"Normalize", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"The normalized form of the sentence is:", None))
    # retranslateUi

