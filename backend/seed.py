from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

VIOLATIONS = [
    # Giao thông đường bộ
    {
        "title": "Điều khiển xe ô tô vượt tốc độ từ 10 km/h đến dưới 20 km/h",
        "description": "Người điều khiển xe ô tô chạy quá tốc độ quy định từ 10 km/h đến dưới 20 km/h",
        "category": "giao_thong",
        "min_fine": 3000000,
        "max_fine": 5000000,
        "legal_basis": "Nghị định 100/2019/NĐ-CP, Điều 5",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển xe ô tô vượt tốc độ từ 20 km/h đến dưới 35 km/h",
        "description": "Người điều khiển xe ô tô chạy quá tốc độ quy định từ 20 km/h đến dưới 35 km/h",
        "category": "giao_thong",
        "min_fine": 5000000,
        "max_fine": 8000000,
        "legal_basis": "Nghị định 100/2019/NĐ-CP, Điều 5",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển xe ô tô vượt tốc độ trên 35 km/h",
        "description": "Người điều khiển xe ô tô chạy quá tốc độ quy định trên 35 km/h",
        "category": "giao_thong",
        "min_fine": 10000000,
        "max_fine": 12000000,
        "legal_basis": "Nghị định 100/2019/NĐ-CP, Điều 5",
        "additional_penalty": "Tước giấy phép lái xe từ 2 đến 4 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển xe mô tô vượt tốc độ từ 10 km/h đến dưới 20 km/h",
        "description": "Người điều khiển xe mô tô, xe gắn máy chạy quá tốc độ quy định từ 10 km/h đến dưới 20 km/h",
        "category": "giao_thong",
        "min_fine": 800000,
        "max_fine": 1000000,
        "legal_basis": "Nghị định 100/2019/NĐ-CP, Điều 6",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    {
        "title": "Không đội mũ bảo hiểm khi đi mô tô, xe máy",
        "description": "Người điều khiển, người ngồi trên xe mô tô, xe gắn máy không đội mũ bảo hiểm hoặc đội mũ bảo hiểm không cài quai đúng quy cách khi tham gia giao thông",
        "category": "giao_thong",
        "min_fine": 400000,
        "max_fine": 600000,
        "legal_basis": "Nghị định 100/2019/NĐ-CP, Điều 6",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển phương tiện khi có nồng độ cồn vượt mức 0,25 mg/l đến 0,4 mg/l khí thở",
        "description": "Người điều khiển xe ô tô và các loại xe tương tự xe ô tô vi phạm quy định về nồng độ cồn ở mức từ trên 0,25 mg/l đến 0,4 mg/l khí thở",
        "category": "giao_thong",
        "min_fine": 16000000,
        "max_fine": 18000000,
        "legal_basis": "Nghị định 100/2019/NĐ-CP, Điều 5",
        "additional_penalty": "Tước giấy phép lái xe từ 16 đến 18 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển phương tiện khi có nồng độ cồn vượt mức 0,4 mg/l khí thở",
        "description": "Người điều khiển xe ô tô vi phạm quy định về nồng độ cồn ở mức trên 0,4 mg/l khí thở",
        "category": "giao_thong",
        "min_fine": 30000000,
        "max_fine": 40000000,
        "legal_basis": "Nghị định 100/2019/NĐ-CP, Điều 5",
        "additional_penalty": "Tước giấy phép lái xe từ 22 đến 24 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Sử dụng điện thoại di động khi đang lái xe ô tô",
        "description": "Người điều khiển xe ô tô dùng tay sử dụng điện thoại di động khi đang điều khiển xe chạy trên đường",
        "category": "giao_thong",
        "min_fine": 1000000,
        "max_fine": 2000000,
        "legal_basis": "Nghị định 100/2019/NĐ-CP, Điều 5",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    {
        "title": "Vượt đèn đỏ, đèn vàng (xe ô tô)",
        "description": "Người điều khiển xe ô tô không chấp hành hiệu lệnh của đèn tín hiệu giao thông",
        "category": "giao_thong",
        "min_fine": 4000000,
        "max_fine": 6000000,
        "legal_basis": "Nghị định 100/2019/NĐ-CP, Điều 5",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Không thắt dây an toàn khi ngồi trong xe ô tô",
        "description": "Người điều khiển xe ô tô hoặc người ngồi trên xe ô tô không thắt dây an toàn khi xe đang chạy",
        "category": "giao_thong",
        "min_fine": 800000,
        "max_fine": 1000000,
        "legal_basis": "Nghị định 100/2019/NĐ-CP, Điều 5",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    # Môi trường
    {
        "title": "Xả nước thải chưa qua xử lý ra môi trường (dưới 5 m³/ngày đêm)",
        "description": "Xả nước thải không qua xử lý hoặc xử lý không đạt quy chuẩn kỹ thuật ra môi trường với lưu lượng dưới 5 m³/ngày đêm",
        "category": "moi_truong",
        "min_fine": 1000000,
        "max_fine": 5000000,
        "legal_basis": "Nghị định 45/2022/NĐ-CP, Điều 13",
        "additional_penalty": None,
        "remedial_measure": "Buộc thực hiện biện pháp khắc phục tình trạng ô nhiễm môi trường",
    },
    {
        "title": "Đốt rơm, rạ, phụ phẩm nông nghiệp trên đồng ruộng",
        "description": "Đốt rơm rạ và phụ phẩm nông nghiệp tại khu vực đồng ruộng gây ô nhiễm không khí",
        "category": "moi_truong",
        "min_fine": 2500000,
        "max_fine": 3000000,
        "legal_basis": "Nghị định 45/2022/NĐ-CP, Điều 9",
        "additional_penalty": None,
        "remedial_measure": "Buộc thực hiện biện pháp giảm thiểu ô nhiễm không khí",
    },
    {
        "title": "Vứt, thải chất thải sinh hoạt không đúng nơi quy định",
        "description": "Vứt, thải, bỏ chất thải sinh hoạt, chất thải rắn thông thường không đúng nơi quy định tại khu chung cư, thương mại, dịch vụ hoặc nơi công cộng",
        "category": "moi_truong",
        "min_fine": 1000000,
        "max_fine": 2000000,
        "legal_basis": "Nghị định 45/2022/NĐ-CP, Điều 26",
        "additional_penalty": None,
        "remedial_measure": "Buộc khắc phục tình trạng ô nhiễm môi trường",
    },
    # Lao động
    {
        "title": "Không ký hợp đồng lao động bằng văn bản",
        "description": "Không giao kết hợp đồng lao động bằng văn bản với người lao động làm việc có thời hạn từ 1 tháng trở lên",
        "category": "lao_dong",
        "min_fine": 2000000,
        "max_fine": 5000000,
        "legal_basis": "Nghị định 12/2022/NĐ-CP, Điều 9",
        "additional_penalty": None,
        "remedial_measure": "Buộc giao kết hợp đồng lao động bằng văn bản",
    },
    {
        "title": "Trả lương thấp hơn mức lương tối thiểu vùng",
        "description": "Trả lương cho người lao động thấp hơn mức lương tối thiểu vùng do Chính phủ quy định",
        "category": "lao_dong",
        "min_fine": 20000000,
        "max_fine": 75000000,
        "legal_basis": "Nghị định 12/2022/NĐ-CP, Điều 17",
        "additional_penalty": None,
        "remedial_measure": "Buộc trả đủ tiền lương cộng với khoản tiền lãi chậm trả",
    },
    {
        "title": "Không đóng bảo hiểm xã hội bắt buộc cho người lao động",
        "description": "Chậm đóng bảo hiểm xã hội bắt buộc, bảo hiểm thất nghiệp cho người lao động",
        "category": "lao_dong",
        "min_fine": 12000000,
        "max_fine": 20000000,
        "legal_basis": "Nghị định 12/2022/NĐ-CP, Điều 38",
        "additional_penalty": None,
        "remedial_measure": "Buộc đóng đủ số tiền bảo hiểm xã hội, bảo hiểm thất nghiệp và tiền lãi",
    },
    {
        "title": "Làm thêm giờ vượt quá số giờ quy định",
        "description": "Sử dụng người lao động làm thêm giờ vượt quá số giờ quy định theo tháng hoặc năm",
        "category": "lao_dong",
        "min_fine": 25000000,
        "max_fine": 50000000,
        "legal_basis": "Nghị định 12/2022/NĐ-CP, Điều 18",
        "additional_penalty": None,
        "remedial_measure": "Buộc trả thêm cho người lao động một khoản tiền ít nhất bằng mức tiền lương làm thêm giờ",
    },
    # Y tế
    {
        "title": "Hành nghề khám chữa bệnh mà không có giấy phép hành nghề",
        "description": "Người hành nghề khám bệnh, chữa bệnh mà không có giấy phép hành nghề hoặc đang trong thời gian bị đình chỉ hành nghề",
        "category": "y_te",
        "min_fine": 40000000,
        "max_fine": 50000000,
        "legal_basis": "Nghị định 117/2020/NĐ-CP, Điều 39",
        "additional_penalty": "Đình chỉ hoạt động từ 12 đến 24 tháng",
        "remedial_measure": "Buộc nộp lại số lợi bất hợp pháp có được",
    },
    {
        "title": "Kinh doanh thuốc không rõ nguồn gốc, xuất xứ",
        "description": "Kinh doanh thuốc, nguyên liệu làm thuốc không có nguồn gốc, xuất xứ rõ ràng",
        "category": "y_te",
        "min_fine": 30000000,
        "max_fine": 50000000,
        "legal_basis": "Nghị định 117/2020/NĐ-CP, Điều 60",
        "additional_penalty": "Tước quyền sử dụng giấy phép kinh doanh từ 1 đến 3 tháng",
        "remedial_measure": "Buộc tiêu hủy thuốc vi phạm",
    },
    # Xây dựng
    {
        "title": "Xây dựng công trình không có giấy phép xây dựng",
        "description": "Xây dựng nhà ở, công trình thuộc đối tượng phải có giấy phép xây dựng mà không có giấy phép",
        "category": "xay_dung",
        "min_fine": 60000000,
        "max_fine": 80000000,
        "legal_basis": "Nghị định 16/2022/NĐ-CP, Điều 16",
        "additional_penalty": "Đình chỉ thi công xây dựng công trình",
        "remedial_measure": "Buộc phá dỡ công trình vi phạm",
    },
    {
        "title": "Xây dựng công trình sai phép (sai vị trí, diện tích, số tầng)",
        "description": "Xây dựng công trình sai với giấy phép xây dựng được cấp về vị trí, diện tích xây dựng, số tầng, chiều cao",
        "category": "xay_dung",
        "min_fine": 30000000,
        "max_fine": 50000000,
        "legal_basis": "Nghị định 16/2022/NĐ-CP, Điều 16",
        "additional_penalty": "Đình chỉ thi công xây dựng công trình",
        "remedial_measure": "Buộc phá dỡ phần công trình vi phạm",
    },
    # Thương mại
    {
        "title": "Kinh doanh hàng hóa nhập lậu (giá trị từ 3 đến dưới 5 triệu đồng)",
        "description": "Buôn bán hàng hóa nhập lậu có giá trị từ 3.000.000 đồng đến dưới 5.000.000 đồng",
        "category": "thuong_mai",
        "min_fine": 500000,
        "max_fine": 1000000,
        "legal_basis": "Nghị định 98/2020/NĐ-CP, Điều 8",
        "additional_penalty": "Tịch thu tang vật vi phạm",
        "remedial_measure": "Buộc tiêu hủy hàng hóa nhập lậu không đảm bảo chất lượng",
    },
    {
        "title": "Kinh doanh hàng giả mạo nhãn mác, bao bì",
        "description": "Buôn bán hàng giả mạo nhãn hàng hóa, bao bì hàng hóa có giá trị hàng hóa thật tương đương từ 5.000.000 đồng đến dưới 10.000.000 đồng",
        "category": "thuong_mai",
        "min_fine": 3000000,
        "max_fine": 7000000,
        "legal_basis": "Nghị định 98/2020/NĐ-CP, Điều 11",
        "additional_penalty": "Tịch thu tang vật, tước quyền sử dụng giấy phép kinh doanh từ 1 đến 3 tháng",
        "remedial_measure": "Buộc tiêu hủy hàng giả",
    },
    # Phòng cháy chữa cháy
    {
        "title": "Không trang bị phương tiện phòng cháy chữa cháy theo quy định",
        "description": "Cơ sở không trang bị đầy đủ phương tiện phòng cháy và chữa cháy theo quy định",
        "category": "phong_chay",
        "min_fine": 15000000,
        "max_fine": 25000000,
        "legal_basis": "Nghị định 144/2021/NĐ-CP, Điều 36",
        "additional_penalty": "Đình chỉ hoạt động từ 3 đến 5 tháng nếu vi phạm nghiêm trọng",
        "remedial_measure": "Buộc trang bị đầy đủ phương tiện phòng cháy chữa cháy",
    },
]


def seed():
    db = SessionLocal()
    try:
        existing = db.query(models.Violation).count()
        if existing > 0:
            print(f"Database already has {existing} violations. Skipping seed.")
            return
        for v in VIOLATIONS:
            db.add(models.Violation(**v))
        db.commit()
        print(f"Seeded {len(VIOLATIONS)} violations successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
