#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QTableWidget, QHBoxLayout, QVBoxLayout,
                             QLabel, QSlider, QPushButton, QScrollArea,
                             QTabWidget, QTableWidgetItem, QFrame)
from PyQt5.QtGui import (QFont)
from PyQt5.QtCore import (Qt)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("White universe")
        self.resize(1366, 768)
        self.statusBar().showMessage('pre-alpha 0.1')

        self.fast = FastSearchTab()
        self.detailed = DetailedSearchTab()

        self.tabs = QTabWidget()
        self.tabs.addTab(self.fast, "Fast search")
        self.tabs.addTab(self.detailed, "Detailed search")

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.tabs)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.vbox)
        self.setCentralWidget(self.main_widget)

        self.show()


class DetailedSearchTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.main_lbl = QLabel("Search parameters", self)
        self.main_lbl.setFont(QFont("Arial",24))
        self.main_lbl.setStyleSheet("font-weight: bold")

        self.scnd_lbl = QLabel("Search results", self)
        self.scnd_lbl.setFont(QFont("Arial",24))
        self.scnd_lbl.setStyleSheet("font-weight: bold")

        self.cost = SearchParameterSlider("Cost", 10, "cheaper", "expensive")
        self.quality = SearchParameterSlider("Quality", 5, "worst", "best")
        self.prod_match = SearchParameterSlider("Production match", 3, "less", "more")
        self.reliability = SearchParameterSlider("Reliability", 6, "0", "5")
        self.delivery_spd = SearchParameterSlider("Delivery speed", 4, "slow", "fast")

        self.search_btn = QPushButton("Search")

        # testing search result widget
        #
        self.goods_list = ["rvdddd", "trshg", "aer", "aerg",
                           "aer", "aerg", "trshg", "trshg"]

        self.search_result1 = SearchResult("oessedgson", "5678", "@tiloh",
                                          "llooll", self.goods_list)

        self.search_result2 = SearchResult("oessedgson", "5678", "@tiloh",
                                          "llooll", self.goods_list)

        self.search_result3 = SearchResult("oessedgson", "5678", "@tiloh",
                                          "llooll", self.goods_list)

        self.v1params = QVBoxLayout()
        self.v1params.addStretch(1)
        self.v1params.addWidget(self.cost)
        self.v1params.addStretch(1)
        self.v1params.addWidget(self.quality)
        self.v1params.addStretch(1)

        self.v2params = QVBoxLayout()
        self.v2params.addStretch(1)
        self.v2params.addWidget(self.prod_match)
        self.v2params.addStretch(1)
        self.v2params.addWidget(self.reliability)
        self.v2params.addStretch(1)

        self.v3params = QVBoxLayout()
        self.v3params.addWidget(self.delivery_spd)
        self.v3params.addStretch(3)
        self.v3params.addWidget(self.search_btn)
        self.v3params.addStretch(1)

        self.params_box = QHBoxLayout()
        self.params_box.addStretch(1)
        self.params_box.addLayout(self.v1params)
        self.params_box.addStretch(1)
        self.params_box.addLayout(self.v2params)
        self.params_box.addStretch(1)
        self.params_box.addLayout(self.v3params)
        self.params_box.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.main_lbl)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.params_box)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.scnd_lbl)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.search_result1)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.search_result2)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.search_result3)
        self.vbox.addStretch(7)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch(5)

        self.setLayout(self.hbox)


class FastSearchTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.main_lbl = QLabel("Best result", self)
        self.main_lbl.setFont(QFont("Arial",24))
        self.main_lbl.setStyleSheet("font-weight: bold")

        self.scnd_lbl = QLabel("Another results", self)
        self.scnd_lbl.setFont(QFont("Arial",24))
        self.scnd_lbl.setStyleSheet("font-weight: bold")

        # testing search result widget
        #
        self.goods_list = ["rvdddd", "trshg", "aer", "aerg",
                           "aer", "aerg", "trshg", "trshg"]

        self.search_result = SearchResult("oessedgson", "5678", "@tiloh",
                                          "llooll", self.goods_list)

        self.search_result1 = SearchResult("oessedgson", "5678", "@tiloh",
                                          "llooll", self.goods_list)

        self.search_result2 = SearchResult("oessedgson", "5678", "@tiloh",
                                          "llooll", self.goods_list)

        self.search_result3 = SearchResult("oessedgson", "5678", "@tiloh",
                                          "llooll", self.goods_list)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.main_lbl)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.search_result)
        self.vbox.addStretch(2)
        self.vbox.addWidget(self.scnd_lbl)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.search_result1)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.search_result2)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.search_result3)
        self.vbox.addStretch(13)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch(5)

        self.setLayout(self.hbox)


class SearchParameterSlider(QWidget):

    def __init__(self, label="", count=2, min="", max=""):
        self.cnt = count
        self.lbl = label
        self.max = max
        self.min = min

        super().__init__()

        self.initUI()

    def initUI(self):
        self.slider_lbl = QLabel(self.lbl, self)
        self.slider_lbl.setFont(QFont("Arial", 16))

        self.max_lbl = QLabel(self.max, self)
        self.max_lbl.setFont(QFont("Arial", 10))

        self.min_lbl = QLabel(self.min, self)
        self.min_lbl.setFont(QFont("Arial", 10))

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setMaximum(self.cnt - 1)
        self.slider.setMinimumWidth(200)
        self.slider.setMaximumWidth(200)

        self.max_min_box = QHBoxLayout()
        self.max_min_box.addWidget(self.min_lbl)
        self.max_min_box.addStretch(2)
        self.max_min_box.addWidget(self.max_lbl)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.slider_lbl)
        self.vbox.addStretch(2)
        self.vbox.addWidget(self.slider)
        self.vbox.addLayout(self.max_min_box)
        self.vbox.addStretch(4)

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox)

        self.setLayout(self.hbox)


class SearchResult(QWidget):

    def __init__(self, name="", tel="", eml="", address="", goods=[]):
        self.name = name
        self.phone = "Phone: " + tel
        self.email = "Email: " + eml
        self.address = "Address: " + address
        self.goods = goods

        super().__init__()

        self.initUI()

    def initUI(self):
        self.name_lbl = QLabel(self.name, self)
        self.name_lbl .setFont(QFont("Arial", 24))

        self.phone_lbl = QLabel(self.phone, self)
        self.phone_lbl.setFont(QFont("Arial", 10))

        self.email_lbl = QLabel(self.email, self)
        self.email_lbl.setFont(QFont("Arial", 10))

        self.address_lbl = QLabel(self.address, self)
        self.address_lbl.setFont(QFont("Arial", 10))

        self.list_table = QTableWidget(len(self.goods), 1, self)
        self.list_table.setHorizontalHeaderItem(0, QTableWidgetItem("Goods to purchase"))
        for i in range(len(self.goods)):
            self.list_table.setItem(i-1, 1, QTableWidgetItem(self.goods[i]))

        self.list_table.resizeColumnsToContents()
        self.list_table.resizeRowsToContents()
        self.list_table.setMaximumWidth(self.list_table.columnWidth(0) + 28)
        self.list_table.setMinimumWidth(self.list_table.columnWidth(0) + 28)
        self.list_table.setMaximumHeight(self.list_table.rowHeight(0) * 3.8)
        self.list_table.setMinimumHeight(self.list_table.rowHeight(0) * 3.8)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.name_lbl)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.phone_lbl)
        self.vbox.addWidget(self.email_lbl)
        self.vbox.addWidget(self.address_lbl)

        self.rect = QFrame()
        self.rect.setFixedWidth(self.list_table.width() / 4)
        self.rect.setFixedHeight(self.list_table.height())
        self.rect.setStyleSheet("QWidget { background-color: %s }" % self.palette().color(self.backgroundRole()))

        self.separator = QFrame()
        self.separator.setFixedWidth(2)
        self.separator.setFixedHeight(self.list_table.height())
        self.separator.setStyleSheet("QWidget { background-color:grey }")

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox)
        self.hbox.addWidget(self.rect)
        self.hbox.addWidget(self.rect)
        self.hbox.addWidget(self.rect)
        self.hbox.addWidget(self.separator)
        self.hbox.addWidget(self.rect)
        self.hbox.addWidget(self.list_table)

        self.setLayout(self.hbox)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())