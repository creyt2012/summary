# Hướng Dẫn Cài Đặt và Sử Dụng Ứng Dụng Tóm Tắt Văn Bản Python

## Giới Thiệu

Ứng dụng tóm tắt văn bản Python cho phép người dùng tóm tắt nội dung của file DOCX và xuất ra file TXT. 
Ứng dụng này hỗ trợ cả tiếng Việt và các ngôn ngữ khác, giúp tiết kiệm thời gian cho người dùng trong 
việc tìm kiếm thông tin quan trọng.

## Yêu Cầu Hệ Thống

- Hệ điều hành: Windows, macOS, hoặc Linux
- Phiên bản Python: 3.6 trở lên

## Cài Đặt Môi Trường

1. **Cài Đặt Python**: Bạn có thể tải về Python từ [trang chủ Python](https://www.python.org/downloads/).
2. **Tạo Môi Trường Ảo** (tùy chọn):

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # trên macOS/Linux
   myenv\\Scripts\\activate  # trên Windows
#Cài Đặt Thư Viện Cần Thiết
 ```bash
pip install python-docx transformers torch
python summary.py

