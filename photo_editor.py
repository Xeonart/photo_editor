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

        self.save_action = QAction(QIcon('D:\\Programming\\Py3_WS\\photo_editor\\Icons\\save_file.png'),"Save", parent=self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setStatusTip('Save image')
        self.save_action.triggered.connect(self.saveImage)

        self.print_action = QAction(QIcon('D:\\Programming\\Py3_WS\\photo_editor\\Icons\\print.png'), "Print", parent=self)
        self.print_action.setShortcut('Ctrl+P')
        self.print_action.setStatusTip('Print image')
        self.print_action.triggered.connect(self.printImage)
        self.print_action.setEnabled(False)

        self.exit_action = QAction(QIcon('D:\\Programming\\Py3_WS\\photo_editor\\Icons\\exit.png'), 'Exit', parent=self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Quit program')
        self.exit_action.triggered.connect(self.close)

        self.rotate90_action = QAction("Rotate 90º", parent=self)
        self.rotate90_action.setStatusTip('Rotate image 90º clockwise')
        self.rotate90_action.triggered.connect(self.rotateImage90)

        self.rotate180_action = QAction("Rotate 180º", parent=self)
        self.rotate180_action.setStatusTip('Rotate image 180º clockwise')
        self.rotate180_action.triggered.connect(self.rotateImage180)

        self.flip_hor_action = QAction("Flip Horizontal", parent=self)
        self.flip_hor_action.setStatusTip('Flip image across horizontal axis')
        self.flip_hor_action.triggered.connect(self.flipImageHorizontal)

        self.flip_ver_action = QAction("Flip Vertical", parent=self)
        self.flip_ver_action.setStatusTip('Flip image across vertical axis')
        self.flip_ver_action.triggered.connect(self.flipImageVertical)

        self.resize_action = QAction("Resize Half", parent=self)
        self.resize_action.setStatusTip('Resize image to half the original size')
        self.resize_action.triggered.connect(self.resizeImageHalf)

        self.clear_action = QAction(QIcon('images/clear.png'), "Clear Image", parent=self)
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


    def createToolBar(self):
        tool_bar = QToolBar("Photo Editor Toolbar")
        tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(tool_bar)

        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.print_act)
        tool_bar.addAction(self.clear_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.exit_act)

    def createToolsDockWidget(self):
        self.dock_tools_view = QDockWidget()
        self.dock_tools_view.setWindowTitle("Edit Image Tools")
        self.dock_tools_view.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | 
        Qt.DockWidgetArea.RightDockWidgetArea)

        self.tools_contents = QWidget()

        self.rotate90 = QPushButton("Rotate 90º")
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.setStatusTip('Rotate image 90º clockwise')
        self.rotate90.clicked.connect(self.rotateImage90)

        self.rotate180 = QPushButton("Rotate 180º")
        self.rotate180.setMinimumSize(QSize(130, 40))
        self.rotate180.setStatusTip('Rotate image 180º clockwise')
        self.rotate180.clicked.connect(self.rotateImage180)

        self.flip_horizontal = QPushButton("Flip Horizontal")
        self.flip_horizontal.setMinimumSize(QSize(130, 40))
        self.flip_horizontal.setStatusTip('Flip image across horizontal axis')
        self.flip_horizontal.clicked.connect(self.flipImageHorizontal)

        self.flip_vertical = QPushButton("Flip Vertical")
        self.flip_vertical.setMinimumSize(QSize(130, 40))
        self.flip_vertical.setStatusTip('Flip image across vertical axis')
        self.flip_vertical.clicked.connect(self.flipImageVertical)

        self.resize_half = QPushButton("Resize Half")
        self.resize_half.setMinimumSize(QSize(130, 40))
        self.resize_half.setStatusTip('Resize image to half the original size')
        self.resize_half.clicked.connect(self.resizeImageHalf)

        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        dock_v_box.addWidget(self.rotate180)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.flip_horizontal)
        dock_v_box.addWidget(self.flip_vertical)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize_half)
        dock_v_box.addStretch(6)

        self.tools_contents.setLayout(dock_v_box)
        self.dock_tools_view.setWidget(self.tools_contents)
        
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock_tools_view)
        self.toggle_dock_tools_act = self.dock_tools_view.toggleViewAction()

    def photoEditorWidgets(self):
        """
        Set up instances of widgets for photo editor GUI
        """
        self.image = QPixmap()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        # Use setSizePolicy to specify how the widget can be 
        # resized, horizontally and vertically. Here, the image 
        # will stretch horizontally, but not vertically.
        self.image_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        self.setCentralWidget(self.image_label)

    def openImage(self):
        image_file, _ = QFileDialog.getOpenFileName(self,
        "Open Image",
        "", 
        "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;Bitmap Files (*.bmp);;GIF Files (*.gif)")
        if image_file:
            self.image = QPixmap(image_file)
            self.image_label.setPixmap(self.image.scaled(self.image_label.size()),
            Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        else:
            QMessageBox.information(self, "Error", "unable to open image", QMessageBox.standardButton.Ok)

    def printImage(self):
        """
        Print image.
        """
        # create printer object and print output defined by the platform
        # the program is being run on. 
        # QPrinter.NativeFormat is the default
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.NativeFormat) 

        # Create printer dialog to configure printer
        print_dialog = QPrintDialog(printer)

         # if the dialog is accepted by the user, begin printing
        if (print_dialog.exec_() == QPrintDialog.Accepted):
            # use QPainter to output a PDF file 
            painter = QPainter()
            # begin painting device
            painter.begin(printer)
            # Set QRect to hold painter's current viewport, which 
            # is the image_label 
            rect = QRect(painter.viewport())
            # get the size of image_label and use it to set the size 
            # of the viewport
            size = QSize(self.image_label.pixmap().size())
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image_label.pixmap().rect())
            # scale the image_label to fit the rect source (0, 0) 
            painter.drawPixmap(0, 0, self.image_label.pixmap())
            # end painting
            painter.end()

    def clearImage(self):
        self.image_label.clear()
        self.image = QPixmap() # reset pixmap so that isNull() = True

    def rotateImage90(self):
        if not self.image.isNull():
            transform90 = QTransform.rotate(90)
            pixmap = QPixmap(self.image)
            

    