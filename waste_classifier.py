import os
import sys
import torch
from PIL import Image
from pathlib import Path
from transformers import AutoImageProcessor, AutoModelForImageClassification


def map_to_organic_inorganic(fine_grained_label):
    """
    Hàm mapping chuyển đổi từ 6 nhãn gốc của mô hình sang 2 nhóm chính.
    Bản chất tập dữ liệu gốc của mô hình này (TrashNet) chủ yếu gồm rác vô cơ tái chế,
    nhãn 'trash' thường chứa rác thải sinh hoạt còn lại hoặc một số rác hữu cơ/vô cơ không tái chế.
    """
    # Định nghĩa quy luật phân nhóm:
    if fine_grained_label in ['cardboard', 'paper']:
        return "VÔ CƠ (Rác tái chế - Giấy / Bìa cứng)"
    elif fine_grained_label in ['glass', 'metal', 'plastic']:
        return "VÔ CƠ (Rác tái chế - Chai lọ / Kim loại / Nhựa)"
    elif fine_grained_label == 'trash':
        return "VÔ CƠ (Rác thải sinh hoạt còn lại / Không tái chế)"
    else:
        return "HỮU CƠ (Rác dễ phân hủy sinh học)"


def load_model(model_name="watersplash/waste-classification"):
    """Tải mô hình và processor từ Hugging Face"""
    print("⏳ Đang tải mô hình từ Hugging Face...")
    processor = AutoImageProcessor.from_pretrained(model_name)
    model = AutoModelForImageClassification.from_pretrained(model_name)
    print("✅ Mô hình đã tải thành công!")
    return processor, model


def process_image(image_path):
    """Xử lý và kiểm tra file ảnh"""
    image_path = Path(image_path)
    
    if not image_path.exists():
        print(f"❌ Lỗi: Không tìm thấy file '{image_path}'")
        return None
    
    try:
        raw_image = Image.open(image_path)
        if raw_image.mode != "RGB":
            raw_image = raw_image.convert("RGB")
        print(f"✅ Đã tải ảnh: {image_path}")
        return raw_image
    except Exception as e:
        print(f"❌ Lỗi khi đọc file ảnh: {e}")
        return None


def predict_waste_binary(image_path, processor, model):
    """
    Dự đoán loại rác từ ảnh
    
    Args:
        image_path: Đường dẫn đến file ảnh
        processor: Image processor từ Hugging Face
        model: Mô hình phân loại rác
    """
    # Xử lý ảnh
    raw_image = process_image(image_path)
    if raw_image is None:
        return None
    
    # Tiền xử lý dữ liệu ảnh đầu vào
    inputs = processor(images=raw_image, return_tensors="pt")
    
    # AI chạy dự đoán
    print("🔍 Đang phân tích ảnh...")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    
    # Tính toán xác suất (%)
    probabilities = torch.nn.functional.softmax(logits, dim=-1)[0]
    predicted_class_idx = logits.argmax(-1).item()
    
    # Lấy nhãn gốc tiếng Anh của mô hình
    labels = model.config.id2label
    original_label = labels[predicted_class_idx]
    confidence_score = probabilities[predicted_class_idx].item()
    
    # BƯỚC MAPPING PHÂN LOẠI HỮU CƠ / VÔ CƠ
    final_category = map_to_organic_inorganic(original_label)
    
    # In kết quả phân loại cuối cùng đã chuyển đổi
    print("\n" + "="*60)
    print(f"🏆 PHÂN LOẠI CUỐI CÙNG: {final_category.upper()}")
    print(f"🔍 Nhãn chi tiết phát hiện: {original_label.upper()}")
    print(f"📊 Độ tự tin: {confidence_score:.2%}")
    print("="*60)
    
    # Hiển thị thêm bảng thống kê xác suất các thành phần rác phát hiện được
    print("\n📋 Xác suất chi tiết các thành phần trong ảnh:")
    for idx, score in enumerate(probabilities):
        percentage = score.item() * 100
        bar_length = int(percentage / 5)
        bar = "█" * bar_length + "░" * (20 - bar_length)
        print(f"  {labels[idx]:12} | {bar} | {percentage:6.2f}%")
    
    return {
        "final_category": final_category,
        "original_label": original_label,
        "confidence_score": confidence_score,
        "probabilities": probabilities.cpu().numpy().tolist(),
        "all_labels": labels
    }


def main():
    """Hàm chính"""
    # Kiểm tra đầu vào
    if len(sys.argv) < 2:
        print("⚠️ Cách sử dụng: python waste_classifier.py <đường_dẫn_ảnh>")
        print("\nVí dụ: python waste_classifier.py img.png")
        print("       python waste_classifier.py /path/to/image.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    # Tải mô hình
    processor, model = load_model()
    
    # Phân loại ảnh
    print(f"\n🖼️ Đang xử lý: {image_path}")
    result = predict_waste_binary(image_path, processor, model)
    
    if result:
        print("\n✅ Phân loại hoàn tất!")
    else:
        print("\n❌ Phân loại không thành công!")


if __name__ == "__main__":
    main()
