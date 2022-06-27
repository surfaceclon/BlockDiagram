import sys
import sqlite3
import os
import create_file
import insert_record
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*

class Blocks:
    def __init__(self, place, name):
        global y
        global l
        self.name = QPushButton(place, text=name)
        self.name.setGeometry(500, y, 130, 30)
        self.name.setObjectName(name)
        self.name.setStyleSheet(
            'background-color: white;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.name.show()
        y = y + 50
        
        self.line = QLabel(place)
        self.line.setGeometry(562, l, 3, 30)
        self.line.setObjectName(name)
        self.line.setStyleSheet(
            'background-color: white;\n'
            'border-radius: 7px;\n'
        )
        self.line.show()
        l = l + 50

class OpenLists(QMainWindow):
    def __init__(self, place, name_file, cls):
        super().__init__()
        self.name_file = name_file
        self.place = place
        self.cls = cls

        self.setGeometry(100, 100, 320, 250)
        self.setFixedSize(self.size())
        self.setWindowTitle('DIAGRAM')
        self.setStyleSheet('background-color: lightgray;\n')

        self.lists = QListWidget(self)
        self.lists.setGeometry(15, 15, 200, 220)
        self.lists.setStyleSheet(
            'background: #F0FFFF;\n'
            'border-radius: 10px;\n'
            'font-size: 15px;\n'
            'font-weight: bold;\n'
        )

        self.open_file = QPushButton(self, text='Открыть')
        self.open_file.setGeometry(230, 15, 80, 30)
        self.open_file.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.open_file.clicked.connect(self.op_file)
        self.open_file.setIcon(QIcon(icon_import))

        self.delet_file = QPushButton(self, text='Удалить')
        self.delet_file.setGeometry(230, 55, 80, 30)
        self.delet_file.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.delet_file.clicked.connect(self.del_file)
        self.delet_file.setIcon(QIcon(icon_delete))

        self.show()
        self.update_lists()
        
    def update_lists(self):
        self.list_dir = []
        for i in os.listdir('files'):
            self.list_dir.append(i)
            self.lists.clear()
            self.lists.addItems(self.list_dir)
            self.lists.itemClicked.connect(self.getItem)
    
    def getItem(self, item):
        global itemClick
        itemClick = item.text()

    def del_file(self):
        try:
            os.remove('files\\' + itemClick)
            self.name_file.clear()
            self.cls.clear()
            self.update_lists()
            self.hide()
        except:
            pass

    def op_file(self):
        self.name_file.clear()
        self.name_file.setText(itemClick[:-3])
        self.cls.clear()
        self.hide()

class WinAdded(QMainWindow):
    def __init__(self, place, lists, widgets):
        super().__init__()
        self.place = place
        self.lists = lists
        self.widgets = widgets

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('DIAGRAM')
        self.setFixedSize(self.size())

        self.name_ob = QLineEdit(self)
        self.name_ob.setGeometry(10, 20, 180, 25)
        self.name_ob.setStyleSheet(
            'background-color: white;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.descr_ob = QPlainTextEdit(self)
        self.descr_ob.setGeometry(10, 60, 270, 170)
        self.descr_ob.setStyleSheet(
            'background-color: white;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.ok = QPushButton(self, text='ОК')
        self.ok.setGeometry(10, 250, 80, 30)
        self.ok.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.ok.clicked.connect(self.confirm)
        self.ok.setIcon(QIcon(icon_ok))

        self.cancell = QPushButton(self, text='Отмена')
        self.cancell.setGeometry(100, 250, 80, 30)
        self.cancell.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.cancell.clicked.connect(self.cancelEx)
        self.cancell.setIcon(QIcon(icon_cancel))
        self.show()

    def confirm(self):
        try:
            insert_record.insert(itemClick, self.name_ob.text(), self.descr_ob.toPlainText())
        except:
            pass
        finally:
            self.updae_lists = MainWin.show_record(self)
            self.hide()

    def cancelEx(self):
        self.hide()

class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setGeometry(100,100,1400,900)
        self.setFixedSize(self.size())
        self.setWindowTitle('DIAGRAM')
        self.setWindowIcon(QIcon('image\\app.png'))

        self.name_file = QLineEdit(self)
        self.name_file.setGeometry(10, 10, 180, 25)
        self.name_file.setStyleSheet(
            'background-color: white;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )

        self.add_b = QPushButton(self, text='Добавить')
        self.add_b.setGeometry(100, 85, 80, 30)
        self.add_b.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.add_b.clicked.connect(self.add_record)
        self.add_b.setIcon(QIcon(icon_add))

        self.creatFile = QPushButton(self, text='Создать')
        self.creatFile.setGeometry(5, 45, 80, 30)
        self.creatFile.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.creatFile.clicked.connect(self.creatFil)
        self.creatFile.setIcon(QIcon(icon_create))

        self.opens = QPushButton(self, text='Открыть')
        self.opens.setGeometry(100, 45, 80, 30)
        self.opens.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.opens.clicked.connect(self.openFil)
        self.opens.setIcon(QIcon(icon_open))

        self.shows = QPushButton(self, text='Начать')
        self.shows.setGeometry(5, 85, 80, 30)
        self.shows.setStyleSheet(
            'background-color: #808080;\n'
            'border-radius: 7px;\n'
            'font-weight: bold;\n'
        )
        self.shows.clicked.connect(self.show_record)
        self.shows.setIcon(QIcon(icon_run))

        self.lists = QListWidget(self)
        self.lists.setGeometry(10, 130, 180, 420)
        self.lists.setStyleSheet(
            'background: #F0FFFF;\n'
            'border-radius: 10px;\n'
            'font-size: 15px;\n'
            'font-weight: bold;\n'
        )
        self.lists.itemClicked.connect(self.get_descript)

        self.centralWid()

    def centralWid(self):
        self.widgets = QFrame(self)
        self.widgets.setGeometry(210, 10, 1187, 870)
        self.widgets.setStyleSheet(
            'background-color: lightgray;\n'
            'border-radius: 7px;\n'
        )
        self.widgets.show()

    def creatFil(self):
        self.lists.clear()
        files = self.name_file.text()
        if len(files) < 1:
            pass
        else:
            create_file.createfiles(files)
            self.name_file.clear()

    def add_record(self):
        self.win_added = WinAdded(self, self.lists, self.widgets)
    
    def openFil(self):
        self.opn = OpenLists(self, self.name_file, self.lists)
        self.widgets.hide()
        self.centralWid()

    def show_record(self):
        try:
            global y
            global l
            self.list_block = []
            conn = sqlite3.connect('files\\' + itemClick)
            cur = conn.cursor()
            cur.execute('''
                SELECT * FROM data;
            ''')
            self.list_block.clear()
            y = 10
            l = 35
            for i in (cur.fetchall()):
                self.list_block.append(i[1])
                self.block = Blocks(self.widgets, i[1])
            self.lists.clear()
            self.lists.addItems(self.list_block)
        except:
            pass

    def clearLists(self):
        self.lists.clear()
    
    def get_descript(self, item):
        desc = item.text()
        name = itemClick
        try:
            conn = sqlite3.connect('files\\' + name)
        except:
            pass
        try:
            cur = conn.cursor()
            cur.execute('''
                select content from data where name='{}';
            '''.format(desc))
            description = cur.fetchall()[0][0]
            conn.close()
            self.show_desc(description)
        except:
            pass
    
    def show_desc(self, descript):
        self.box_desc = QTextEdit(self.widgets)
        self.box_desc.setGeometry(5, 5, 250, 150)
        self.box_desc.setText(descript)
        self.box_desc.setStyleSheet(
            'background: lightgray;\n'
            'border-radius: 7px;\n'
            'font-size: 11px;\n'
            'font-weight: bold;\n'
        )
        self.box_desc.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.box_desc.show()

if __name__=='__main__':
    list_bloks = []
    y = 10
    l = 35
    itemClick = ''
    icon_create = 'image\\addFil.png'
    icon_open = 'image\\open-folder.png'
    icon_run = 'image\\run.png'
    icon_add = 'image\\addRec.png'
    icon_import = 'image\\open-files.png'
    icon_delete = 'image\\delete.png'
    icon_ok = 'image\\ok.png'
    icon_cancel = 'image\\cancel.png'
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())