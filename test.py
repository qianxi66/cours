import sys  
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QMenuBar, QAction, QVBoxLayout, QWidget  
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):  
    def __init__(self):  
        super().__init__()  

        self.setWindowTitle("PyQt5 Web-like Interface")  
        self.setGeometry(100, 100, 800, 600)  

        # Create a central widget  
        central_widget = QTextEdit("Main Content Area")  
        self.setCentralWidget(central_widget)  

        # Create a menu bar  
        menu_bar = self.menuBar()  
        file_menu = menu_bar.addMenu("File")  
        edit_menu = menu_bar.addMenu("Edit")  

        # Add actions to the menu  
        new_action = QAction("New", self)  
        file_menu.addAction(new_action)  

        # Create a dock widget for the sidebar  
        dock_widget = QDockWidget("Sidebar", self)  
        dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)   # type: ignore

        # Add a simple widget to the dock  
        dock_content = QTextEdit("Sidebar Content")  
        dock_widget.setWidget(dock_content)  

        # Add the dock widget to the main window  
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)  

if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec_())