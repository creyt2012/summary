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
   myenv\\Scripts\\activate  # trên Windows```

## Cài Đặt Thư Viện Cần Thiết

 ```bash
pip install python-docx transformers torch
python summary.py
```
## Đảm bảo rằng bạn cũng đã cài đặt torch, vì nhiều mô hình trong transformers yêu cầu thư viện này. Bạn có thể cài đặt torch như sau (tùy thuộc vào hệ điều hành và CUDA mà bạn đang sử dụng):
 ```bash
  pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
 ```

## các mô hình ngôn ngữ thay thế
1. BART
Hugging Face BART
2. BART cho tiếng Việt
bartpho
3. T5
Hugging Face T5
mT5
4. LED (Longformer Encoder-Decoder)
Hugging Face LED
5. PEGASUS
Hugging Face PEGASUS
6. VietAI/vit5-base
VietAI vit5-base
7. UniLM
Hugging Face UniLM
8. DistilBART
Hugging Face DistilBART
9. mBART
Hugging Face mBART

### Hệ thống sẽ hoạt động tốt với tài nguyên 16 core - 128gb ram
