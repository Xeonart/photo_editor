import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QAction,
    QFileDialog, QDesktopWidget, QMessageBox, QSizePolicy, QToolBar, QStatusBar,
    QDockWidget, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

class PhotoEditor(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setFixedSize(650, 650)
        self.setWindowTitle('5.2 - Photo Editor GUI')
        self.centerMainWindow()
        self.createToolsDockWidget()
        self.createMenu()
        self.createToolBar()
        self.photoEditorWidgets()

        self.show()

    def createMenu(self):
        
        self.open_action = QAction(QIcon("D:\\Programming\\Py3_WS\\photo_editor\\Icons\\open_fle.png"), "Open", parent=self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.setStatusTip("Open a new image")
        self.open_action.triggered.connect(self.saveImage)

        self.save_action = QAction(QIcon('D:\\Programming\\Py3_WS\\photo_editor\\Icons\\save_file.png'),"Save", self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setStatusTip('Save image')
        self.save_action.triggered.connect(self.saveImage)

        self.print_action = QAction(QIcon('D:\\Programming\\Py3_WS\\photo_editor\\Icons\\print.png'), "Print", self)
        self.print_action.setShortcut('Ctrl+P')
        self.print_action.setStatusTip('Print image')
        self.print_action.triggered.connect(self.printImage)
        self.print_action.setEnabled(False)

        self.exit_action = QAction(QIcon('D:\\Programming\\Py3_WS\\photo_editor\\Icons\\exit.png'), 'Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Quit program')
        self.exit_action.triggered.connect(self.close)

        self.rotate90_action = QAction("Rotate 90º", self)
        self.rotate90_action.setStatusTip('Rotate image 90º clockwise')
        self.rotate90_action.triggered.connect(self.rotateImage90)

        self.rotate180_action = QAction("Rotate 180º", self)
        self.rotate180_action.setStatusTip('Rotate image 180º clockwise')
        self.rotate180_action.triggered.connect(self.rotateImage180)

        self.flip_hor_action = QAction("Flip Horizontal", self)
        self.flip_hor_action.setStatusTip('Flip image across horizontal axis')
        self.flip_hor_action.triggered.connect(self.flipImageHorizontal)

        self.flip_ver_action = QAction("Flip Vertical", self)
        self.flip_ver_action.setStatusTip('Flip image across vertical axis')
        self.flip_ver_action.triggered.connect(self.flipImageVertical)

        self.resize_action = QAction("Resize Half", self)
        self.resize_action.setStatusTip('Resize image to half the original size')
        self.resize_action.triggered.connect(self.resizeImageHalf)

        self.clear_action = QAction(QIcon('images/clear.png'), "Clear Image", self)
        self.clear_action.setShortcut("Ctrl+D")
        self.clear_action.setStatusTip('Clear the current image')
        self.clear_action.triggered.connect(self.clearImage)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.print_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(self.rotate90_action)
        edit_menu.addAction(self.rotate180_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flip_hor_action)
        edit_menu.addAction(self.flip_ver_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_action)

        view_menu = menu_bar.addMenu('View')
        view_menu.addAction(self.toggle_dock_tools_act)

        self.setStatusBar(QStatusBar(self))
