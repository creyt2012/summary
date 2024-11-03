import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from docx import Document
from transformers import pipeline

class TextSummarizerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # Sử dụng mô hình BART cho tiếng Việt
        self.summarizer = pipeline("summarization", model="vinai/bartpho-summarization")

    def initUI(self):
        self.setWindowTitle("Text Summarizer")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #f0f4f8;")

        layout = QtWidgets.QVBoxLayout()

        title = QtWidgets.QLabel("✨ Document Summarization App ✨")
        title.setFont(QtGui.QFont("Segoe UI", 24, QtGui.QFont.Bold))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)

        self.docxButton = QtWidgets.QPushButton("📂 Select DOCX File")
        self.docxButton.setStyleSheet(self.buttonStyle())
        self.docxButton.clicked.connect(self.select_docx)
        layout.addWidget(self.docxButton)

        self.docxPath = QtWidgets.QLineEdit()
        self.docxPath.setPlaceholderText("Path to DOCX file...")
        layout.addWidget(self.docxPath)

        self.txtButton = QtWidgets.QPushButton("💾 Select Save Location")
        self.txtButton.setStyleSheet(self.buttonStyle())
        self.txtButton.clicked.connect(self.select_txt)
        layout.addWidget(self.txtButton)

        self.txtPath = QtWidgets.QLineEdit()
        self.txtPath.setPlaceholderText("Path to save TXT file...")
        layout.addWidget(self.txtPath)

        self.summarizeButton = QtWidgets.QPushButton("📝 Summarize")
        self.summarizeButton.setStyleSheet(self.buttonStyle())
        self.summarizeButton.clicked.connect(self.summarize_and_save)
        layout.addWidget(self.summarizeButton)

        self.logText = QtWidgets.QTextEdit()
        self.logText.setReadOnly(True)
        self.logText.setStyleSheet("background-color: #ffffff; border: 1px solid #ccc; padding: 5px;")
        layout.addWidget(self.logText)

        self.setLayout(layout)

    def buttonStyle(self):
        return """
            QPushButton {
                background-color: #007BFF; 
                color: white; 
                padding: 12px; 
                border-radius: 8px;
                font-size: 18px;
                border: none;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """

    def select_docx(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select DOCX File", "", "Word Documents (*.docx);;All Files (*)", options=options)
        if file_path:
            self.docxPath.setText(file_path)

    def select_txt(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Select Save Location", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            self.txtPath.setText(file_path)

    def read_docx(self, file_path):
        doc = Document(file_path)
        full_text = [para.text for para in doc.paragraphs if para.text.strip()]
        return "\n".join(full_text)

    def summarize_text(self, text, max_length=150):
        summary = self.summarizer(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]['summary_text']

    def summarize_and_save(self):
        self.log("Starting summarization...")
        docx_file = self.docxPath.text()
        output_file = self.txtPath.text()

        if not docx_file or not output_file:
            QtWidgets.QMessageBox.warning(self, "Missing Information", "Please select a DOCX file and a TXT save location.")
            return

        try:
            text = self.read_docx(docx_file)
            self.log("Successfully read DOCX file.")
            summary = self.summarize_text(text)
            self.log("Summarization completed.")

            with open(output_file, "w", encoding="utf-8") as file:
                file.write(summary)
            self.log("Summary saved to TXT file.")
            QtWidgets.QMessageBox.information(self, "Success", "Summary has been saved to the TXT file.")
        except Exception as e:
            self.log(f"Error: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def log(self, message):
        self.logText.append(message)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TextSummarizerApp()
    window.show()
    sys.exit(app.exec_())
