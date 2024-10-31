# 定义各类对话框界面，例如登录、注册、订票确认等。
# dialog.py  
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox  
from PyQt5.QtCore import pyqtSignal  

class LoginDialog(QDialog):  
    login_successful = pyqtSignal()  

    def __init__(self):  
        super().__init__()  
        self.init_ui()  

    def init_ui(self):  
        self.setWindowTitle('登录')  
        self.resize(300, 150)  

        self.username_label = QLabel('用户名:')  
        self.username_edit = QLineEdit()  
        self.password_label = QLabel('密码:')  
        self.password_edit = QLineEdit()  
        self.password_edit.setEchoMode(QLineEdit.Password)  

        self.login_button = QPushButton('登录')  
        self.cancel_button = QPushButton('取消')  

        layout = QGridLayout()  
        layout.addWidget(self.username_label, 0, 0)  
        layout.addWidget(self.username_edit, 0, 1)  
        layout.addWidget(self.password_label, 1, 0)  
        layout.addWidget(self.password_edit, 1, 1)  
        layout.addWidget(self.login_button, 2, 0)  
        layout.addWidget(self.cancel_button, 2, 1)  

        self.setLayout(layout)  

        self.login_button.clicked.connect(self.handle_login)  
        self.cancel_button.clicked.connect(self.reject)  

    def handle_login(self):  
        username = self.username_edit.text().strip()  
        password = self.password_edit.text().strip()  
        # TODO: 在此添加实际的用户验证逻辑  
        if username == 'admin' and password == '123456':  
            QMessageBox.information(self, '成功', '登录成功！')  
            self.accept()  
            self.login_successful.emit()  
        else:  
            QMessageBox.warning(self, '失败', '用户名或密码错误！')