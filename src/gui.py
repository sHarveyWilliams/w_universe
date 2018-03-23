#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os.path
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget,
                             QWidget, QHBoxLayout, QVBoxLayout, QGridLayout,
                             QLabel, QSlider, QPushButton, QMessageBox, QComboBox,
                             QTabWidget, QTableWidgetItem, QFrame, QSplitter,
                             QTableView, QStackedLayout, QLineEdit, QTextEdit)
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel)
from PyQt5.QtGui import (QFont)
from PyQt5.QtCore import (Qt)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("White universe")
        self.resize(1366, 768)
        self.statusBar().showMessage('alpha 0.3')
        self.setStyleSheet("MainWindow {background-color: rgb(200, 200, 200)}")

        self.db = DB(self)

        self.fast = FastSearchTab(self)
        self.detailed = DetailedSearchTab(self)
        self.dbws = DBWorkspaceTab(self)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.fast, "Fast search")
        self.tabs.addTab(self.detailed, "Detailed search")
        self.tabs.addTab(self.dbws, "Database workspace")

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.tabs)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.vbox)
        self.setCentralWidget(self.main_widget)

        self.show()


class FastSearchTab(QWidget):

    def __init__(self, parent=None):
        super(FastSearchTab, self).__init__(parent)

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


class DetailedSearchTab(QWidget):

    def __init__(self, parent=None):
        super(DetailedSearchTab, self).__init__(parent)

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
        self.search_btn.clicked.connect(QApplication.instance().quit)

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

        self.params_box = QGridLayout()
        self.params_box.addWidget(self.cost, 0, 0)
        self.params_box.addWidget(self.prod_match, 0, 1)
        self.params_box.addWidget(self.delivery_spd, 0, 2)
        self.params_box.addWidget(self.quality, 1, 0)
        self.params_box.addWidget(self.reliability, 1, 1)
        self.params_box.addWidget(self.search_btn, 1, 2)

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


class DBWorkspaceTab(QWidget):

    def __init__(self, parent=None):
        super(DBWorkspaceTab, self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.editor = DBEditor(self)

        self.terminal = DBTerminal(self)

        self.spliterV = QSplitter(Qt.Vertical, self)
        self.spliterV.addWidget(self.editor)
        self.spliterV.addWidget(self.terminal)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.spliterV)

        self.setLayout(self.hbox)


class Table(QWidget):
    def __init__(self, table_name='', table_cols=[], parent=None):
        super(Table, self).__init__(parent)

        self.cols = len(table_cols)

        self.model = QSqlTableModel(self)
        self.model.setTable(table_name)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()

        for self.col_name, self.id in zip(table_cols, range(len(table_cols))):
            self.model.setHeaderData(self.id, Qt.Horizontal, self.col_name)

        self.rows = self.model.rowCount()

        self.initUI()

    def initUI(self):
        self.view = QTableView()
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()
        self.view.verticalHeader().hide()
        self.view.setFixedWidth(sum([self.view.columnWidth(self.col_num) for self.col_num in range(self.cols)]) + 5)

        if (self.view.rowHeight(0) * self.rows + self.view.horizontalHeader().height() * 1.1) > 320:
            self.view.setFixedHeight(320)
        else:
            self.view.setFixedHeight(self.view.rowHeight(0) * self.rows + self.view.horizontalHeader().height() * 1.1)

        self.add_row_btn = QPushButton("Add row")
        self.add_row_btn.pressed.connect(self.addRow)

        self.del_row_btn = QPushButton("Remove row")
        self.del_row_btn.pressed.connect(self.delRow)

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.pressed.connect(self.submit)

        self.btns_box = QVBoxLayout()
        self.btns_box.addWidget(self.add_row_btn)
        self.btns_box.addWidget(self.del_row_btn)
        self.btns_box.addWidget(self.submit_btn)
        self.btns_box.addStretch(1)

        self.view_lay = QVBoxLayout()
        self.view_lay.addWidget(self.view)
        self.view_lay.addStretch(1)

        # self.grid = QGridLayout()
        # self.grid.addLayout(self.view_lay, 0, 0)
        # self.grid.addLayout(self.btns_box, 0, 1)

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.view_lay)
        self.hbox.addStretch(1024)
        self.hbox.addLayout(self.btns_box)
        # self.hbox.addLayout(self.grid)
        self.hbox.addStretch(1)

        self.setLayout(self.hbox)

    def addRow(self):
        self.model.insertRow(self.rows)
        self.rows = self.model.rowCount()
        if (self.view.rowHeight(0) * self.rows + self.view.horizontalHeader().height() * 1.1) > 320:
            self.view.setFixedHeight(320)
        else:
            self.view.setFixedHeight(self.view.rowHeight(0) * self.rows + self.view.horizontalHeader().height() * 1.1)

    def delRow(self):
        if self.rows > 0:
            self.rows -= 1
            self.model.removeRow(self.rows)

            if (self.view.rowHeight(0) * self.rows + self.view.horizontalHeader().height() * 1.1) > 320:
                self.view.setFixedHeight(320)
            else:
                self.view.setFixedHeight(self.view.rowHeight(0) * self.rows + self.view.horizontalHeader().height() * 1.1)
        else:
            QMessageBox.warning(self, "ERROR", "Selected table does not have rows")

    def submit(self):
        self.model.database().transaction()
        if self.model.submitAll():
            self.model.database().commit()
        else:
            self.model.database().rollback()
            QMessageBox.warning(self, "ERROR", "The database reported an error: %s" % self.model.lastError().text())


class TableViewer(QWidget):

    def __init__(self, parent=None):
        super(TableViewer, self).__init__(parent)

        self.tables = {}
        self.tables_count = 0

        self.initUI()

    def initUI(self):
        self.lays = QStackedLayout()

        for self.table_name in self.parent().parent().parent().db.tables():
            self.tables[self.table_name] = self.lays.addWidget(Table(self.table_name, self.parent().parent().parent().db.cols(self.table_name)))
        self.tables_count = len(self.tables)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.lays)
        self.vbox.addStretch(1)

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch(1)

        self.setLayout(self.hbox)

    def updateTables(self):
        for self.iter in range(self.tables_count):
            self.lays.removeWidget(self.lays.widget(0))
        for self.table_name in self.parent().parent().parent().parent().parent().parent().parent().db.tables():
            self.tables[self.table_name] = self.lays.addWidget(Table(self.table_name, self.parent().parent().parent().parent().parent().parent().parent().db.cols(self.table_name)))

    def changeTable(self, table_name):
        self.lays.setCurrentIndex(self.tables[table_name])


class DBEditor(QWidget):

    def __init__(self, parent=None):
        super(DBEditor, self).__init__(parent)

        self.tables_count = 0

        self.initUI()

    def initUI(self):
        self.viewer = TableViewer(self)

        self.table_chooser = QComboBox(self)
        self.table_chooser.addItems(self.parent().parent().db.tables())
        self.table_chooser.setMaximumWidth(160)
        self.table_chooser.activated[str].connect(self.changeTable)
        self.tables_count = self.table_chooser.count()
        self.cur_table = self.table_chooser.currentText()

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.table_chooser)
        self.vbox.addWidget(self.viewer)
        self.vbox.addStretch(3)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch(7)

        self.setLayout(self.hbox)

    def updateTables(self):
        self.cur_table = self.table_chooser.currentText()
        self.viewer.updateTables()
        for self.iter in range(self.tables_count):
            self.table_chooser.removeItem(0)
        self.table_chooser.addItems(self.parent().parent().parent().parent().parent().parent().db.tables())
        self.tables_count = self.table_chooser.count()

        if self.cur_table in self.parent().parent().parent().parent().parent().parent().db.tables():
            self.table_chooser.setCurrentText(self.cur_table)
        self.changeTable(self.table_chooser.currentText())

    def changeTable(self, table_name):
        self.viewer.changeTable(table_name)


class DBTerminal(QWidget):

    def __init__(self, parent=None):
        super(DBTerminal, self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.setMaximumHeight(200)

        self.history = []
        self.last_command = ''
        self.ok = False
        self.hist_iter = -1

        self.terminal = QLineEdit()
        self.terminal.setDragEnabled(True)

        self.hist_view = QTextEdit()
        self.hist_view.setReadOnly(True)
        self.hist_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.hist_view)
        self.vbox.addWidget(self.terminal)

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox)

        self.setLayout(self.hbox)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            if self.terminal.text() != '':
                self.history.insert(0, self.terminal.text())
                self.ok = self.makeSQLQuery(self.terminal.text())
            if self.ok:
                self.hist_view.append(">>> " + '<font color="green">' + self.terminal.text() + "</font>")
            else:
                self.hist_view.append(">>> " + "<font color='red'>" + self.terminal.text() + "</font>")
            self.hist_view.verticalScrollBar().setValue(self.hist_view.verticalScrollBar().maximum())

            self.terminal.clear()
            self.hist_iter = -1
        elif QKeyEvent.key() == Qt.Key_Up:
            if self.hist_iter == -1:
                self.last_command = self.terminal.text()
            if self.hist_iter+1 < len(self.history):
                self.hist_iter += 1
                self.terminal.setText(self.history[self.hist_iter])
        elif QKeyEvent.key() == Qt.Key_Down:
            if self.hist_iter >= 0:
                self.hist_iter -= 1
            if self.hist_iter >= 0:
                self.terminal.setText(self.history[self.hist_iter])
            else:
                self.terminal.setText(self.last_command)

    def makeSQLQuery(self, command):
        return self.parent().parent().parent().parent().parent().parent().db.exec(command)


class DB:

    def __init__(self, parent=None):
        super(DB, self).__init__()

        self.parent = parent

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('../data/wudb')
        if not self.db.open():
            QMessageBox.critical(None, "Cannot open database",
                                 "Unable to establish a database connection.\n"
                                 "This example needs SQLite support. Please read the Qt SQL "
                                 "driver documentation for information how to build it.\n\n"
                                 "Click Cancel to exit.",
                                 QMessageBox.Cancel)

        self.query = QSqlQuery()

        self.tables_list = {}

        self.initDB()

    def initDB(self):
        if not os.path.exists("../data/wudb"):
            with open("../data/wu.db", 'r', encoding="utf-8") as self.lines:
                for self.string in self.lines:
                    if self.string != '\n':
                        self.query.exec_(self.string)

        for self.table in self.db.tables():
            if self.table != "sqlite_sequence":
                self.tables_list[self.table] = [self.db.record(self.table).fieldName(x) for x in range(self.db.record(self.table).count())]

    def exec(self, command):
        self.query_res = self.query.exec_(command)
        if self.query_res:
            for self.table in self.db.tables():
                if self.table != "sqlite_sequence":
                    self.tables_list[self.table] = [self.db.record(self.table).fieldName(x) for x in range(self.db.record(self.table).count())]
            for self.table in self.tables():
                if self.table not in self.db.tables():
                    self.tables_list.pop(self.table)

            self.parent.dbws.editor.updateTables()
        return self.query_res


    def tables(self):
        return list(self.tables_list.keys())

    def cols_count(self, table_name):
        return len(self.tables_list[table_name])

    def cols(self, table_name):
        return self.tables_list[table_name]


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
        self.list_table.setFixedWidth(self.list_table.columnWidth(0) + self.list_table.verticalHeader().width())
        self.list_table.setFixedHeight(self.list_table.rowHeight(0) * 3.8)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.name_lbl)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.phone_lbl)
        self.vbox.addWidget(self.email_lbl)
        self.vbox.addWidget(self.address_lbl)

        self.rect = QFrame()
        self.rect.setFixedWidth(self.list_table.width() / 4)
        self.rect.setFixedHeight(self.list_table.height())
        # self.rect.setStyleSheet("QWidget { background-color: %s }" % self.palette().color(self.backgroundRole()))

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