from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QListWidget

class SearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("検索アプリ")
        self.setGeometry(150, 150, 500, 400)
        
        # メインレイアウト
        layout = QVBoxLayout()
        
        # 検索フィールド
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("検索条件を入力")
        layout.addWidget(self.search_input)
        
        # 検索ボタン
        self.search_button = QPushButton("検索")
        self.search_button.clicked.connect(self.perform_search)
        layout.addWidget(self.search_button)
        
        # 検索結果表示用リスト
        self.result_list = QListWidget()
        layout.addWidget(self.result_list)
        
        # 中央ウィジェットの設定
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def perform_search(self):
        # 検索ボタンが押された時の処理
        query = self.search_input.text()
        self.result_list.clear()
        if query:
            # ダミーデータの検索結果（後でAPIと連携）
            results = [f"{query}の結果1", f"{query}の結果2", f"{query}の結果3"]
            self.result_list.addItems(results)
