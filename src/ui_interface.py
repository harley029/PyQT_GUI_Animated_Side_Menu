# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceRCTtgc.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PyQt6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from Custom_Widgets.Widgets import QCustomSlideMenu
import icons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 305)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "* {\n"
            "border:none ;\n"
            "background-color: transparent;\n"
            "color:#fdfdfd\n"
            "}\n"
            "#centralwidget{\n"
            "background-color: #040f13;\n"
            "}\n"
            "#side_menu{\n"
            "background-color: #071e26;\n"
            "border-radius: 20px;\n"
            "}\n"
            "QPushButton{\n"
            "padding: 10px;\n"
            "background-color: #040f13;\n"
            "border-radius: 5px;\n"
            "}\n"
            "#main_body{\n"
            "background-color: #071e26;\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName("header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.menuBtn = QPushButton(self.frame_2)
        self.menuBtn.setObjectName("menuBtn")
        self.menuBtn.setMinimumSize(QSize(0, 30))
        self.menuBtn.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(True)
        self.menuBtn.setFont(font)
        icon = QIcon()
        icon.addFile(":/icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.menuBtn)

        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName("label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.side_menu = QCustomSlideMenu(self.frame)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName("pushButton_2")
        icon1 = QIcon()
        icon1.addFile(
            ":/icons/aperture.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName("pushButton_3")
        icon2 = QIcon()
        icon2.addFile(
            ":/icons/command.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.pushButton_3.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName("pushButton_4")
        icon3 = QIcon()
        icon3.addFile(
            ":/icons/codesandbox.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.pushButton_4.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName("pushButton_5")
        icon4 = QIcon()
        icon4.addFile(
            ":/icons/database.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.pushButton_5.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.side_menu)

        self.main_body = QFrame(self.frame)
        self.main_body.setObjectName("main_body")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.main_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_body)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QLabel(self.main_body)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout.addWidget(self.main_body)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", "MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "MY APP", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "Item 1", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", "Item 2", None)
        )
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", "Item 3", None)
        )
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", "Item 4", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "MAIN BODY", None)
        )

    # retranslateUi
