"""
File cấu hình cho hệ thống phân loại rác SmartBin
"""

# ====== CONFIGURATION ======

# 1. MÔ HÌ HU
MODEL_NAME = "watersplash/waste-classification"

# 2. CÀI ĐẶT ÁNH
IMAGE_FORMAT = "RGB"  # RGB hoặc RGBA
MAX_IMAGE_SIZE = 2048  # Pixels

# 3. CÀI ĐẶT PHÂN LOẠI
# Mapping từ nhãn chi tiết sang nhóm chính
WASTE_CATEGORIES = {
    "cardboard": {
        "group": "VÔ CƠ",
        "type": "Rác tái chế - Giấy / Bìa cứng",
        "recyclable": True,
        "instructions": "Tập hợp, bóp dẹp, đặt vào thùng tái chế"
    },
    "paper": {
        "group": "VÔ CƠ",
        "type": "Rác tái chế - Giấy",
        "recyclable": True,
        "instructions": "Gọn gàng, chập nhỏ, đặt vào thùng giấy"
    },
    "glass": {
        "group": "VÔ CƠ",
        "type": "Rác tái chế - Chai lọ",
        "recyclable": True,
        "instructions": "Tránh bể vỡ, rửa sạch, để chung thùng kính"
    },
    "metal": {
        "group": "VÔ CƠ",
        "type": "Rác tái chế - Kim loại",
        "recyclable": True,
        "instructions": "Rửa sạch, bóp dẹp nếu cần, để thùng kim loại"
    },
    "plastic": {
        "group": "VÔ CƠ",
        "type": "Rác tái chế - Nhựa",
        "recyclable": True,
        "instructions": "Rửa sạch, bóp dẹp, để thùng nhựa"
    },
    "trash": {
        "group": "VÔ CƠ",
        "type": "Rác thải sinh hoạt còn lại",
        "recyclable": False,
        "instructions": "Gói kín, để thùng rác thường"
    }
}

# 4. CÀI ĐẶT XỪIỆP (DEVICE)
USE_GPU = True  # True để sử dụng GPU nếu có, False để dùng CPU

# 5. NGÔN NGỮ
LANGUAGE = "vi"  # "vi" cho Tiếng Việt, "en" cho English

# 6. CÀI ĐẶT LOGGING
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
SAVE_PREDICTIONS = True  # Lưu kết quả dự đoán vào file
PREDICTIONS_LOG_FILE = "predictions.log"

# ====== MESSAGES ======

MESSAGES = {
    "vi": {
        "loading_model": "⏳ Đang tải mô hình từ Hugging Face...",
        "model_loaded": "✅ Mô hình đã tải thành công!",
        "processing": "🔍 Đang phân tích ảnh...",
        "error_file_not_found": "❌ Lỗi: Không tìm thấy file '{0}'",
        "error_reading_image": "❌ Lỗi khi đọc file ảnh: {0}",
        "result_header": "PHÂN LOẠI CUỐI CÙNG",
        "confidence": "Độ tự tin",
        "detailed_label": "Nhãn chi tiết phát hiện",
        "probability_details": "Xác suất chi tiết các thành phần trong ảnh",
    },
    "en": {
        "loading_model": "⏳ Loading model from Hugging Face...",
        "model_loaded": "✅ Model loaded successfully!",
        "processing": "🔍 Processing image...",
        "error_file_not_found": "❌ Error: File '{0}' not found",
        "error_reading_image": "❌ Error reading image file: {0}",
        "result_header": "FINAL CLASSIFICATION",
        "confidence": "Confidence",
        "detailed_label": "Detailed label detected",
        "probability_details": "Detailed probability of waste components",
    }
}
