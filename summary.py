import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from docx import Document
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

class TextSummarizerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        self.summarizer = pipeline("summarization", model="facebook/bart-large-multilingual")

    def initUI(self):
        self.setWindowTitle("Tóm Tắt Văn Bản - PyQt5")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #f0f0f5;")
        layout = QtWidgets.QVBoxLayout()
        title = QtWidgets.QLabel("✨ Ứng dụng Tóm Tắt Văn Bản ✨")
        title.setFont(QtGui.QFont("Helvetica", 16, QtGui.QFont.Bold))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        self.docxButton = QtWidgets.QPushButton("Chọn tệp DOCX")
        self.docxButton.clicked.connect(self.select_docx)
        layout.addWidget(self.docxButton)

        self.docxPath = QtWidgets.QLineEdit()
        layout.addWidget(self.docxPath)
        self.txtButton = QtWidgets.QPushButton("Chọn nơi lưu tệp TXT")
        self.txtButton.clicked.connect(self.select_txt)
        layout.addWidget(self.txtButton)

        self.txtPath = QtWidgets.QLineEdit()
        layout.addWidget(self.txtPath)
        self.summarizeButton = QtWidgets.QPushButton("Tóm Tắt")
        self.summarizeButton.clicked.connect(self.summarize_and_save)
        layout.addWidget(self.summarizeButton)
        self.logText = QtWidgets.QTextEdit()
        self.logText.setReadOnly(True)
        layout.addWidget(self.logText)

        self.setLayout(layout)

    def select_docx(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Chọn tệp DOCX", "", "Word Documents (*.docx);;All Files (*)", options=options)
        if file_path:
            self.docxPath.setText(file_path)

    def select_txt(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Chọn nơi lưu tệp TXT", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            self.txtPath.setText(file_path)

    def read_docx(self, file_path):
        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            if para.text.strip():
                full_text.append(para.text)
        return "\n".join(full_text)

    def summarize_text(self, text, max_length=150):
        summary = self.summarizer(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]['summary_text']

    def summarize_and_save(self):
        self.log("Bắt đầu quá trình tóm tắt...")
        docx_file = self.docxPath.text()
        output_file = self.txtPath.text()

        if not docx_file or not output_file:
            QtWidgets.QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng chọn tệp DOCX và nơi lưu tệp TXT.")
            return

        try:
            text = self.read_docx(docx_file)
            self.log("Đọc tệp DOCX thành công.")
            summary = self.summarize_text(text)
            self.log("Tóm tắt hoàn thành.")

            with open(output_file, "w", encoding="utf-8") as file:
                file.write(summary)
            self.log("Tóm tắt đã lưu vào tệp TXT.")
            QtWidgets.QMessageBox.information(self, "Thành công", "Tóm tắt đã được lưu vào tệp TXT.")
        except Exception as e:
            self.log(f"Lỗi: {e}")
            QtWidgets.QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {e}")

    def log(self, message):
        self.logText.append(message)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TextSummarizerApp()
    window.show()
    sys.exit(app.exec_())
