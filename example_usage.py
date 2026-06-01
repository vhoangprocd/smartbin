"""
Ví dụ cách sử dụng module waste_classifier trong dự án của bạn
"""

from waste_classifier import load_model, predict_waste_binary
from pathlib import Path


def example_single_image():
    """Ví dụ 1: Phân loại một ảnh đơn"""
    print("=" * 60)
    print("VÍ DỤ 1: Phân loại một ảnh")
    print("=" * 60)
    
    # Tải mô hình một lần
    processor, model = load_model()
    
    # Phân loại ảnh
    image_path = "img.png"
    result = predict_waste_binary(image_path, processor, model)
    
    if result:
        print(f"\n✅ Kết quả: {result['final_category']}")
        print(f"   Độ tự tin: {result['confidence_score']:.2%}")


def example_batch_processing():
    """Ví dụ 2: Xử lý nhiều ảnh"""
    print("\n" + "=" * 60)
    print("VÍ DỤ 2: Xử lý nhiều ảnh")
    print("=" * 60)
    
    # Tải mô hình một lần cho tất cả ảnh (hiệu quả hơn)
    processor, model = load_model()
    
    # Danh sách ảnh cần xử lý
    image_folder = Path("./images")
    
    if not image_folder.exists():
        print(f"⚠️ Thư mục {image_folder} không tồn tại")
        print("📝 Hãy tạo thư mục 'images' và đặt các ảnh vào đó")
        return
    
    image_files = list(image_folder.glob("*.jpg")) + list(image_folder.glob("*.png"))
    
    print(f"📁 Tìm thấy {len(image_files)} ảnh")
    
    results = {}
    for img_path in image_files:
        print(f"\n🔍 Xử lý: {img_path.name}")
        result = predict_waste_binary(str(img_path), processor, model)
        if result:
            results[img_path.name] = result
    
    # Thống kê kết quả
    print("\n" + "=" * 60)
    print("📊 THỐNG KÊ KẾT QUẢ")
    print("=" * 60)
    for filename, result in results.items():
        print(f"{filename:30} | {result['final_category']}")


def example_get_classification_details():
    """Ví dụ 3: Lấy chi tiết phân loại"""
    print("\n" + "=" * 60)
    print("VÍ DỤ 3: Chi tiết phân loại")
    print("=" * 60)
    
    processor, model = load_model()
    image_path = "img.png"
    
    result = predict_waste_binary(image_path, processor, model)
    
    if result:
        print("\n📋 Chi tiết đầy đủ:")
        print(f"  - Phân loại cuối: {result['final_category']}")
        print(f"  - Nhãn chi tiết: {result['original_label']}")
        print(f"  - Độ tự tin: {result['confidence_score']:.2%}")
        print(f"  - Số loại rác được phát hiện: {len(result['all_labels'])}")


# Chạy ví dụ
if __name__ == "__main__":
    try:
        example_single_image()
        # example_batch_processing()
        # example_get_classification_details()
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
