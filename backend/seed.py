from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

# Cập nhật theo các nghị định đang có hiệu lực tính đến 2025:
# - Nghị định 168/2024/NĐ-CP (giao thông, hiệu lực 01/01/2025, thay thế NĐ 100/2019 và NĐ 123/2021)
# - Nghị định 45/2022/NĐ-CP (môi trường)
# - Nghị định 12/2022/NĐ-CP (lao động)
# - Nghị định 117/2020/NĐ-CP sửa đổi bởi NĐ 124/2021/NĐ-CP (y tế)
# - Nghị định 16/2022/NĐ-CP (xây dựng)
# - Nghị định 98/2020/NĐ-CP sửa đổi bởi NĐ 17/2022/NĐ-CP (thương mại)
# - Nghị định 144/2021/NĐ-CP (phòng cháy chữa cháy)

VIOLATIONS = [
    # ===== GIAO THÔNG ĐƯỜNG BỘ =====
    # Căn cứ: Nghị định 168/2024/NĐ-CP (hiệu lực 01/01/2025)
    {
        "title": "Điều khiển xe ô tô vượt tốc độ từ 10 km/h đến dưới 20 km/h",
        "description": "Người điều khiển xe ô tô chạy quá tốc độ quy định từ 10 km/h đến dưới 20 km/h",
        "category": "giao_thong",
        "min_fine": 4000000,
        "max_fine": 6000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển xe ô tô vượt tốc độ từ 20 km/h đến dưới 35 km/h",
        "description": "Người điều khiển xe ô tô chạy quá tốc độ quy định từ 20 km/h đến dưới 35 km/h",
        "category": "giao_thong",
        "min_fine": 6000000,
        "max_fine": 8000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 2 đến 4 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển xe ô tô vượt tốc độ trên 35 km/h",
        "description": "Người điều khiển xe ô tô chạy quá tốc độ quy định trên 35 km/h",
        "category": "giao_thong",
        "min_fine": 10000000,
        "max_fine": 14000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 2 đến 4 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển xe mô tô vượt tốc độ từ 10 km/h đến dưới 20 km/h",
        "description": "Người điều khiển xe mô tô, xe gắn máy chạy quá tốc độ quy định từ 10 km/h đến dưới 20 km/h",
        "category": "giao_thong",
        "min_fine": 1000000,
        "max_fine": 2000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 6 (hiệu lực 01/01/2025)",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển xe mô tô vượt tốc độ từ 20 km/h đến dưới 35 km/h",
        "description": "Người điều khiển xe mô tô, xe gắn máy chạy quá tốc độ quy định từ 20 km/h đến dưới 35 km/h",
        "category": "giao_thong",
        "min_fine": 2000000,
        "max_fine": 3000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 6 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Không đội mũ bảo hiểm khi đi mô tô, xe máy",
        "description": "Người điều khiển, người ngồi trên xe mô tô, xe gắn máy không đội mũ bảo hiểm hoặc đội mũ bảo hiểm không cài quai đúng quy cách khi tham gia giao thông",
        "category": "giao_thong",
        "min_fine": 600000,
        "max_fine": 1000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 6 (hiệu lực 01/01/2025)",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển ô tô khi có nồng độ cồn từ trên 0 đến 0,25 mg/l khí thở",
        "description": "Người điều khiển xe ô tô vi phạm quy định về nồng độ cồn ở mức từ trên 0 mg/l đến 0,25 mg/l khí thở",
        "category": "giao_thong",
        "min_fine": 10000000,
        "max_fine": 12000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 10 đến 12 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển ô tô khi có nồng độ cồn từ 0,25 mg/l đến 0,4 mg/l khí thở",
        "description": "Người điều khiển xe ô tô vi phạm quy định về nồng độ cồn ở mức từ trên 0,25 mg/l đến 0,4 mg/l khí thở",
        "category": "giao_thong",
        "min_fine": 18000000,
        "max_fine": 20000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 16 đến 18 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển ô tô khi có nồng độ cồn vượt trên 0,4 mg/l khí thở",
        "description": "Người điều khiển xe ô tô vi phạm quy định về nồng độ cồn ở mức trên 0,4 mg/l khí thở",
        "category": "giao_thong",
        "min_fine": 30000000,
        "max_fine": 40000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 22 đến 24 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển mô tô khi có nồng độ cồn từ 0,25 mg/l đến 0,4 mg/l khí thở",
        "description": "Người điều khiển xe mô tô, xe gắn máy vi phạm nồng độ cồn mức từ trên 0,25 mg/l đến 0,4 mg/l khí thở",
        "category": "giao_thong",
        "min_fine": 6000000,
        "max_fine": 8000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 6 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 16 đến 18 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Điều khiển mô tô khi có nồng độ cồn vượt trên 0,4 mg/l khí thở",
        "description": "Người điều khiển xe mô tô, xe gắn máy vi phạm nồng độ cồn mức trên 0,4 mg/l khí thở",
        "category": "giao_thong",
        "min_fine": 8000000,
        "max_fine": 10000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 6 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 22 đến 24 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Sử dụng điện thoại di động khi đang lái xe ô tô",
        "description": "Người điều khiển xe ô tô dùng tay sử dụng điện thoại di động khi đang điều khiển xe chạy trên đường",
        "category": "giao_thong",
        "min_fine": 2000000,
        "max_fine": 3000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    {
        "title": "Vượt đèn đỏ, đèn vàng (xe ô tô)",
        "description": "Người điều khiển xe ô tô không chấp hành hiệu lệnh của đèn tín hiệu giao thông",
        "category": "giao_thong",
        "min_fine": 4000000,
        "max_fine": 6000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Vượt đèn đỏ, đèn vàng (xe mô tô, xe máy)",
        "description": "Người điều khiển xe mô tô, xe gắn máy không chấp hành hiệu lệnh của đèn tín hiệu giao thông",
        "category": "giao_thong",
        "min_fine": 1000000,
        "max_fine": 2000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 6 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Không thắt dây an toàn khi ngồi trong xe ô tô",
        "description": "Người điều khiển xe ô tô hoặc người ngồi trên xe ô tô không thắt dây an toàn khi xe đang chạy",
        "category": "giao_thong",
        "min_fine": 800000,
        "max_fine": 1000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    {
        "title": "Đi ngược chiều đường một chiều (xe ô tô)",
        "description": "Người điều khiển xe ô tô đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển cấm đi ngược chiều",
        "category": "giao_thong",
        "min_fine": 10000000,
        "max_fine": 12000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 2 đến 4 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Đi ngược chiều đường một chiều (xe mô tô)",
        "description": "Người điều khiển xe mô tô, xe gắn máy đi ngược chiều của đường một chiều, đi ngược chiều trên đường có biển cấm đi ngược chiều",
        "category": "giao_thong",
        "min_fine": 2000000,
        "max_fine": 3000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 6 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Xe ô tô chở quá số người quy định từ 02 người trở lên",
        "description": "Điều khiển xe ô tô chở người quá số người quy định từ 02 người trở lên (trừ xe buýt, xe khách)",
        "category": "giao_thong",
        "min_fine": 4000000,
        "max_fine": 6000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": None,
    },
    {
        "title": "Xe ô tô chở hàng hóa quá tải trọng cho phép trên 50%",
        "description": "Điều khiển xe ô tô chở hàng hóa vượt quá trọng tải cho phép trên 50%",
        "category": "giao_thong",
        "min_fine": 7000000,
        "max_fine": 8000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 24 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": "Buộc hạ tải hàng hóa xuống đúng quy định",
    },
    {
        "title": "Điều khiển xe ô tô khi không có giấy phép lái xe",
        "description": "Người điều khiển xe ô tô không có giấy phép lái xe hoặc sử dụng giấy phép lái xe không do cơ quan có thẩm quyền cấp",
        "category": "giao_thong",
        "min_fine": 10000000,
        "max_fine": 12000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 21 (hiệu lực 01/01/2025)",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    {
        "title": "Dừng, đỗ xe ô tô trên phần đường xe chạy gây cản trở giao thông",
        "description": "Dừng xe, đỗ xe ô tô trên phần đường xe chạy ở đoạn đường ngoài đô thị nơi có lề đường gây cản trở giao thông",
        "category": "giao_thong",
        "min_fine": 800000,
        "max_fine": 1000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    {
        "title": "Không chấp hành hiệu lệnh của cảnh sát giao thông (xe ô tô)",
        "description": "Người điều khiển xe ô tô không chấp hành hiệu lệnh, yêu cầu kiểm tra, kiểm soát của người thi hành công vụ",
        "category": "giao_thong",
        "min_fine": 6000000,
        "max_fine": 8000000,
        "legal_basis": "Nghị định 168/2024/NĐ-CP, Điều 5 (hiệu lực 01/01/2025)",
        "additional_penalty": "Tước giấy phép lái xe từ 1 đến 3 tháng",
        "remedial_measure": None,
    },
    # ===== MÔI TRƯỜNG =====
    # Căn cứ: Nghị định 45/2022/NĐ-CP (còn hiệu lực)
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
        "title": "Xả nước thải chưa qua xử lý ra môi trường (từ 5 m³ đến dưới 50 m³/ngày đêm)",
        "description": "Xả nước thải không qua xử lý hoặc xử lý không đạt quy chuẩn kỹ thuật ra môi trường với lưu lượng từ 5 m³ đến dưới 50 m³/ngày đêm",
        "category": "moi_truong",
        "min_fine": 30000000,
        "max_fine": 60000000,
        "legal_basis": "Nghị định 45/2022/NĐ-CP, Điều 13",
        "additional_penalty": "Đình chỉ hoạt động từ 3 đến 6 tháng",
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
        "title": "Vứt, thải chất thải sinh hoạt không đúng nơi quy định tại nơi công cộng",
        "description": "Vứt, thải, bỏ chất thải sinh hoạt không đúng nơi quy định tại khu chung cư, thương mại, dịch vụ hoặc nơi công cộng",
        "category": "moi_truong",
        "min_fine": 1000000,
        "max_fine": 2000000,
        "legal_basis": "Nghị định 45/2022/NĐ-CP, Điều 26",
        "additional_penalty": None,
        "remedial_measure": "Buộc khắc phục tình trạng ô nhiễm môi trường",
    },
    {
        "title": "Gây tiếng ồn vượt quy chuẩn kỹ thuật trong khu dân cư",
        "description": "Gây tiếng ồn vượt quy chuẩn kỹ thuật về tiếng ồn trong khu dân cư, khu vực có yêu cầu sự yên tĩnh",
        "category": "moi_truong",
        "min_fine": 1000000,
        "max_fine": 5000000,
        "legal_basis": "Nghị định 45/2022/NĐ-CP, Điều 22",
        "additional_penalty": None,
        "remedial_measure": "Buộc thực hiện biện pháp giảm thiểu tiếng ồn",
    },
    {
        "title": "Không lập báo cáo đánh giá tác động môi trường",
        "description": "Thực hiện dự án đầu tư thuộc đối tượng phải lập báo cáo đánh giá tác động môi trường mà không lập hoặc không được phê duyệt",
        "category": "moi_truong",
        "min_fine": 100000000,
        "max_fine": 200000000,
        "legal_basis": "Nghị định 45/2022/NĐ-CP, Điều 9",
        "additional_penalty": "Đình chỉ hoạt động từ 6 đến 12 tháng",
        "remedial_measure": "Buộc lập và trình phê duyệt báo cáo đánh giá tác động môi trường",
    },
    # ===== LAO ĐỘNG =====
    # Căn cứ: Nghị định 12/2022/NĐ-CP (còn hiệu lực)
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
        "remedial_measure": "Buộc trả thêm cho người lao động khoản tiền ít nhất bằng mức tiền lương làm thêm giờ",
    },
    {
        "title": "Phân biệt đối xử về giới tính trong tuyển dụng lao động",
        "description": "Phân biệt đối xử về giới tính, dân tộc, màu da, thành phần xã hội trong tuyển dụng, sử dụng, đào tạo lao động",
        "category": "lao_dong",
        "min_fine": 5000000,
        "max_fine": 10000000,
        "legal_basis": "Nghị định 12/2022/NĐ-CP, Điều 8",
        "additional_penalty": None,
        "remedial_measure": "Buộc nhận người lao động trở lại làm việc",
    },
    {
        "title": "Không trả lương đúng hạn cho người lao động",
        "description": "Trả lương không đúng hạn theo quy định của pháp luật mà không có lý do chính đáng",
        "category": "lao_dong",
        "min_fine": 5000000,
        "max_fine": 10000000,
        "legal_basis": "Nghị định 12/2022/NĐ-CP, Điều 17",
        "additional_penalty": None,
        "remedial_measure": "Buộc trả đủ tiền lương cộng với khoản tiền lãi chậm trả",
    },
    {
        "title": "Không có biện pháp bảo đảm an toàn lao động tại nơi làm việc",
        "description": "Không có biện pháp bảo đảm an toàn lao động đối với những nơi có nguy cơ tai nạn lao động cao",
        "category": "lao_dong",
        "min_fine": 8000000,
        "max_fine": 12000000,
        "legal_basis": "Nghị định 12/2022/NĐ-CP, Điều 22",
        "additional_penalty": "Đình chỉ hoạt động cho đến khi khắc phục xong",
        "remedial_measure": "Buộc thực hiện đầy đủ biện pháp bảo đảm an toàn lao động",
    },
    # ===== Y TẾ =====
    # Căn cứ: Nghị định 117/2020/NĐ-CP sửa đổi bởi Nghị định 124/2021/NĐ-CP
    {
        "title": "Hành nghề khám chữa bệnh mà không có giấy phép hành nghề",
        "description": "Người hành nghề khám bệnh, chữa bệnh mà không có giấy phép hành nghề hoặc đang trong thời gian bị đình chỉ hành nghề",
        "category": "y_te",
        "min_fine": 40000000,
        "max_fine": 50000000,
        "legal_basis": "Nghị định 117/2020/NĐ-CP sửa đổi bởi Nghị định 124/2021/NĐ-CP, Điều 39",
        "additional_penalty": "Đình chỉ hoạt động từ 12 đến 24 tháng",
        "remedial_measure": "Buộc nộp lại số lợi bất hợp pháp có được",
    },
    {
        "title": "Kinh doanh thuốc không rõ nguồn gốc, xuất xứ",
        "description": "Kinh doanh thuốc, nguyên liệu làm thuốc không có nguồn gốc, xuất xứ rõ ràng",
        "category": "y_te",
        "min_fine": 30000000,
        "max_fine": 50000000,
        "legal_basis": "Nghị định 117/2020/NĐ-CP sửa đổi bởi Nghị định 124/2021/NĐ-CP, Điều 60",
        "additional_penalty": "Tước quyền sử dụng giấy phép kinh doanh từ 1 đến 3 tháng",
        "remedial_measure": "Buộc tiêu hủy thuốc vi phạm",
    },
    {
        "title": "Kinh doanh thực phẩm không đảm bảo an toàn vệ sinh",
        "description": "Sản xuất, kinh doanh thực phẩm không bảo đảm an toàn thực phẩm gây ảnh hưởng đến sức khỏe người tiêu dùng",
        "category": "y_te",
        "min_fine": 20000000,
        "max_fine": 40000000,
        "legal_basis": "Nghị định 115/2018/NĐ-CP sửa đổi bởi Nghị định 124/2021/NĐ-CP, Điều 5",
        "additional_penalty": "Đình chỉ hoạt động từ 1 đến 3 tháng",
        "remedial_measure": "Buộc tiêu hủy thực phẩm vi phạm",
    },
    {
        "title": "Quảng cáo thuốc không có giấy phép quảng cáo",
        "description": "Quảng cáo thuốc khi chưa được cơ quan nhà nước có thẩm quyền xác nhận nội dung quảng cáo",
        "category": "y_te",
        "min_fine": 20000000,
        "max_fine": 30000000,
        "legal_basis": "Nghị định 117/2020/NĐ-CP sửa đổi bởi Nghị định 124/2021/NĐ-CP, Điều 69",
        "additional_penalty": None,
        "remedial_measure": "Buộc tháo gỡ, xóa quảng cáo vi phạm",
    },
    # ===== XÂY DỰNG =====
    # Căn cứ: Nghị định 16/2022/NĐ-CP (còn hiệu lực)
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
    {
        "title": "Không nghiệm thu công trình trước khi đưa vào sử dụng",
        "description": "Đưa công trình xây dựng vào khai thác, sử dụng khi chưa được nghiệm thu theo quy định",
        "category": "xay_dung",
        "min_fine": 30000000,
        "max_fine": 50000000,
        "legal_basis": "Nghị định 16/2022/NĐ-CP, Điều 34",
        "additional_penalty": "Đình chỉ việc đưa công trình vào khai thác sử dụng",
        "remedial_measure": "Buộc thực hiện nghiệm thu theo quy định",
    },
    # ===== THƯƠNG MẠI =====
    # Căn cứ: Nghị định 98/2020/NĐ-CP sửa đổi bởi Nghị định 17/2022/NĐ-CP
    {
        "title": "Kinh doanh hàng hóa nhập lậu (giá trị từ 3 đến dưới 5 triệu đồng)",
        "description": "Buôn bán hàng hóa nhập lậu có giá trị từ 3.000.000 đồng đến dưới 5.000.000 đồng",
        "category": "thuong_mai",
        "min_fine": 500000,
        "max_fine": 1000000,
        "legal_basis": "Nghị định 98/2020/NĐ-CP sửa đổi bởi Nghị định 17/2022/NĐ-CP, Điều 8",
        "additional_penalty": "Tịch thu tang vật vi phạm",
        "remedial_measure": "Buộc tiêu hủy hàng hóa nhập lậu không đảm bảo chất lượng",
    },
    {
        "title": "Kinh doanh hàng giả mạo nhãn mác, bao bì",
        "description": "Buôn bán hàng giả mạo nhãn hàng hóa, bao bì hàng hóa có giá trị hàng hóa thật tương đương từ 5.000.000 đồng đến dưới 10.000.000 đồng",
        "category": "thuong_mai",
        "min_fine": 3000000,
        "max_fine": 7000000,
        "legal_basis": "Nghị định 98/2020/NĐ-CP sửa đổi bởi Nghị định 17/2022/NĐ-CP, Điều 11",
        "additional_penalty": "Tịch thu tang vật, tước quyền sử dụng giấy phép kinh doanh từ 1 đến 3 tháng",
        "remedial_measure": "Buộc tiêu hủy hàng giả",
    },
    {
        "title": "Không niêm yết giá hàng hóa, dịch vụ",
        "description": "Không niêm yết giá hoặc niêm yết giá không rõ ràng gây nhầm lẫn cho khách hàng",
        "category": "thuong_mai",
        "min_fine": 500000,
        "max_fine": 1000000,
        "legal_basis": "Nghị định 98/2020/NĐ-CP sửa đổi bởi Nghị định 17/2022/NĐ-CP, Điều 17",
        "additional_penalty": None,
        "remedial_measure": "Buộc niêm yết giá đúng quy định",
    },
    {
        "title": "Bán hàng hóa, dịch vụ cao hơn giá niêm yết",
        "description": "Bán hàng hóa, dịch vụ với giá cao hơn giá đã niêm yết",
        "category": "thuong_mai",
        "min_fine": 1000000,
        "max_fine": 3000000,
        "legal_basis": "Nghị định 98/2020/NĐ-CP sửa đổi bởi Nghị định 17/2022/NĐ-CP, Điều 17",
        "additional_penalty": None,
        "remedial_measure": "Buộc trả lại số tiền đã thu cao hơn giá niêm yết cho khách hàng",
    },
    # ===== PHÒNG CHÁY CHỮA CHÁY =====
    # Căn cứ: Nghị định 144/2021/NĐ-CP (còn hiệu lực)
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
    {
        "title": "Sử dụng nguồn lửa, nguồn nhiệt không đúng quy định tại nơi có nguy hiểm cháy nổ",
        "description": "Dùng lửa trần, hút thuốc, sử dụng nguồn lửa, nguồn nhiệt không đúng quy định tại những nơi có nguy hiểm về cháy, nổ",
        "category": "phong_chay",
        "min_fine": 5000000,
        "max_fine": 10000000,
        "legal_basis": "Nghị định 144/2021/NĐ-CP, Điều 30",
        "additional_penalty": None,
        "remedial_measure": None,
    },
    {
        "title": "Cản trở, không chấp hành lệnh huy động của lực lượng chữa cháy",
        "description": "Cản trở hoặc không chấp hành lệnh huy động tham gia chữa cháy của người có thẩm quyền",
        "category": "phong_chay",
        "min_fine": 5000000,
        "max_fine": 10000000,
        "legal_basis": "Nghị định 144/2021/NĐ-CP, Điều 42",
        "additional_penalty": None,
        "remedial_measure": None,
    },
]


def seed():
    db = SessionLocal()
    try:
        existing_titles = {v.title for v in db.query(models.Violation.title).all()}
        new_violations = [v for v in VIOLATIONS if v["title"] not in existing_titles]

        if not new_violations:
            print(f"No new violations to seed. Database already has {len(existing_titles)} violations.")
            return

        for v in new_violations:
            db.add(models.Violation(**v))
        db.commit()
        print(f"Seeded {len(new_violations)} new violations. Total: {len(existing_titles) + len(new_violations)}.")
    finally:
        db.close()


def reseed():
    """Xóa toàn bộ dữ liệu cũ và seed lại từ đầu với dữ liệu mới nhất."""
    db = SessionLocal()
    try:
        deleted = db.query(models.Violation).delete()
        db.commit()
        print(f"Deleted {deleted} old violations.")

        for v in VIOLATIONS:
            db.add(models.Violation(**v))
        db.commit()
        print(f"Reseeded {len(VIOLATIONS)} violations successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--reseed":
        reseed()
    else:
        seed()
