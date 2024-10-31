#主窗口界面，包含主要的GUI逻辑，实现机票显示、查询、订票等功能。
# mainwindow.py  
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QMessageBox  
from PyQt5.QtGui import QIcon  
from gui.dialog import LoginDialog  

class MainWindow(QMainWindow):  
    def __init__(self):  
        super().__init__()  
        self.init_ui()  

    def init_ui(self):  
        self.setWindowTitle('飞机票订购平台')  
        self.resize(1024, 768)  

        # 创建菜单栏  
        menubar = self.menuBar()  
        file_menu = menubar.addMenu('文件')  
        help_menu = menubar.addMenu('帮助')  

        # 创建工具栏  
        toolbar = self.addToolBar('工具栏')  

        # 创建状态栏  
        self.statusBar().showMessage('欢迎使用飞机票订购平台')  

        # 创建动作  
        login_action = QAction(QIcon('resources/icons/login.png'), '登录', self)  
        logout_action = QAction(QIcon('resources/icons/logout.png'), '注销', self)  
        exit_action = QAction(QIcon('resources/icons/exit.png'), '退出', self)  
        about_action = QAction('关于', self)  

        # 将动作添加到菜单栏  
        file_menu.addAction(login_action)  
        file_menu.addAction(logout_action)  
        file_menu.addSeparator()  
        file_menu.addAction(exit_action)  
        help_menu.addAction(about_action)  

        # 将动作添加到工具栏  
        toolbar.addAction(login_action)  
        toolbar.addAction(logout_action)  

        # 连接信号和槽  
        login_action.triggered.connect(self.show_login_dialog)  
        logout_action.triggered.connect(self.logout)  
        exit_action.triggered.connect(self.close)  
        about_action.triggered.connect(self.show_about)  

        # 初始化主功能界面  
        # TODO: 在此添加主界面的组件，如航班列表、查询区域等  

    def show_login_dialog(self):  
        login_dialog = LoginDialog()  
        if login_dialog.exec_() == QDialog.Accepted:  
            self.statusBar().showMessage('登录成功')  
            # TODO: 在此处理登录成功后的逻辑  

    def logout(self):  
        reply = QMessageBox.question(self, '提示', '确认要注销吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  
        if reply == QMessageBox.Yes:  
            self.statusBar().showMessage('已注销')  
            # TODO: 在此处理注销后的逻辑  

    def show_about(self):  
        QMessageBox.about(self, '关于', '飞机票订购平台\n版本：1.0\n作者：你的名字')  

if __name__ == '__main__':  
    import sys  
    app = QApplication(sys.argv)  
    main_window = MainWindow()  
    main_window.show()  
    sys.exit(app.exec_())