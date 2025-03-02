import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from apps.search_app import SearchApp

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("デスクトップアプリランチャー")
        self.setGeometry(100, 100, 600, 400)
        
        # メインレイアウト
        layout = QVBoxLayout()
        
        # アプリ起動ボタン
        self.search_button = QPushButton("検索アプリを起動")
        self.search_button.clicked.connect(self.open_search_app)
        layout.addWidget(self.search_button)
        
        # 中央ウィジェットの設定
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def open_search_app(self):
        self.search_app = SearchApp()
        self.search_app.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
