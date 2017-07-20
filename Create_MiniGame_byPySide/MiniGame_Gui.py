
from PySide import QtGui,QtCore
import sys
import tictactoe_Fuction as ttt
reload(ttt)
class mainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setWindowTitle('HELLO BUBBLE')
        self.tabMenu()
        center = Main()
        self.setCentralWidget(center)
        
    def tabMenu(self):
        restartAction = QtGui.QAction('restart', self)
        exitAction = QtGui.QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        restartAction.triggered.connect(self.show)


        menu = QtGui.QMenu("Manage")
        menu.addAction(restartAction)
        menu.addAction(exitAction)


        menubar = QtGui.QMenuBar()
        menubar.addMenu(menu)

        self.setMenuBar(menubar)

class Main(QtGui.QDialog):
    def __init__(self):
        super(Main,self).__init__()
        self.setFixedSize(QtCore.QSize(800,500))
        self.widget()
        self.Layout()
        self.connect()

    def widget(self):

        self.titlelabel = QtGui.QLabel("Title Name")
        self.hpHero = QtGui.QLabel("HP")
        self.hpMonster = QtGui.QLabel("HP")
        self.turn = QtGui.QLabel("00")
        self.heroName = QtGui.QLabel("HERO")
        self.monsterName = QtGui.QLabel("MONSTER")
        QtGui.QLabel("Title Name")
        self.processBar1 = QtGui.QProgressBar()
        self.processBar1.setValue(50)
        self.processBar1.setTextVisible(False)
        self.processBar2 = QtGui.QProgressBar()
        self.processBar2.setValue(70)
        self.processBar2.setInvertedAppearance(True)
        self.processBar2.setTextVisible(False)

        self.heroPicture = QtGui.QLabel()
        self.heroPicture.setPixmap(QtGui.QPixmap("charHero.png"))
        self.heroChoose = QtGui.QLabel()
        self.heroChoose.setPixmap(QtGui.QPixmap("blank.png"))
        self.vsTest = QtGui.QLabel("VS")
        self.monsterPicture = QtGui.QLabel()
        self.monsterChoose = QtGui.QLabel()
        self.monsterPicture.setPixmap(QtGui.QPixmap("charMons.png"))
        self.monsterChoose.setPixmap(QtGui.QPixmap("blank.png"))
        self.card1_btn = QtGui.QPushButton()

        self.card1_btn.setIcon(QtGui.QIcon("rock.png"))
        self.card1_btn.setFixedSize(QtCore.QSize(150,150))
        self.card1_btn.setIconSize(QtCore.QSize(150,150))
        self.card2_btn = QtGui.QPushButton()
        self.card2_btn.setIcon(QtGui.QIcon("scissors.png"))
        self.card2_btn.setFixedSize(QtCore.QSize(150,150))
        self.card2_btn.setIconSize(QtCore.QSize(150,150))
        self.card3_btn = QtGui.QPushButton()
        self.card3_btn.setIcon(QtGui.QIcon("paper.png"))
        self.card3_btn.setFixedSize(QtCore.QSize(150,150))
        self.card3_btn.setIconSize(QtCore.QSize(150,150))


    def Layout(self):
        self.main_layout = QtGui.QVBoxLayout()
        self.worksapace_layout = QtGui.QVBoxLayout()
        self.row_layout = QtGui.QHBoxLayout()
        self.rowPic_layout = QtGui.QHBoxLayout()
        self.hero_layout = QtGui.QVBoxLayout()
        self.hero_pic_layout = QtGui.QHBoxLayout()
        self.monster_layout = QtGui.QVBoxLayout()
        self.monster_pic_layout = QtGui.QHBoxLayout()
        self.card_layout = QtGui.QHBoxLayout()

        self.setWindowTitle("Hello Bubble")

        self.worksapace_layout.addWidget(self.titlelabel)
        self.worksapace_layout.setAlignment(QtCore.Qt.AlignTop)
        self.worksapace_layout.setAlignment(self.titlelabel,QtCore.Qt.AlignCenter)


        self.card_layout.addWidget(self.card1_btn)
        self.card_layout.addWidget(self.card2_btn)
        self.card_layout.addWidget(self.card3_btn)

        self.row_layout.addWidget(self.hpHero)
        self.row_layout.addWidget(self.processBar1)
        self.row_layout.addWidget(self.turn)
        self.row_layout.addWidget(self.processBar2)
        self.row_layout.addWidget(self.hpMonster)
        self.rowPic_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.hero_layout.addLayout(self.hero_pic_layout)
        self.monster_layout.addLayout(self.monster_pic_layout)
        self.hero_pic_layout.addWidget(self.heroPicture)
        self.hero_pic_layout.addWidget(self.heroChoose)
        self.monster_pic_layout.addWidget(self.monsterChoose)
        self.monster_pic_layout.addWidget(self.monsterPicture)
        self.hero_layout.addWidget(self.heroName)
        self.monster_layout.addWidget(self.monsterName)
        self.hero_layout.setAlignment(self.heroName,QtCore.Qt.AlignCenter)
        self.monster_layout.setAlignment(self.monsterName,QtCore.Qt.AlignCenter)


        self.main_layout.addLayout(self.worksapace_layout )
        self.worksapace_layout.addLayout(self.row_layout)
        self.worksapace_layout.addLayout(self.rowPic_layout)
        self.rowPic_layout.addLayout(self.hero_layout)
        self.rowPic_layout.addWidget(self.vsTest)
        self.rowPic_layout.addLayout(self.monster_layout)
        self.worksapace_layout.addLayout(self.card_layout)
        self.setLayout(self.main_layout)
        
    def connect(self):
        self.card1_btn.clicked.connect(self.card1)
        self.card2_btn.clicked.connect(self.card2)
        self.card3_btn.clicked.connect(self.card3)

    def card1(self):
        print 1
    def card2(self):
        print 2
    def card3(self):
        print 3
    def pressClose(self):
        window.close()

app = QtGui.QApplication(sys.argv)
window = mainWindow()
window.show()
app.exec_()