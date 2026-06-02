✅CS1.E1.US-15: [Nhận NL khách] - Thiết lập/chỉnh sửa kho nhận NL khách mặc định✅CS1.E1.US-15: [Nhận NL khách] - Thiết lập/chỉnh sửa kho nhận NL khách mặc định1. USER STORYLà một (As a):Trưởng bộ phận Material Control (TBP MC)
Tôi muốn (I want):Cấu hình nhà kho mặc định khi tiếp nhận NL khách và khi nhập kho
Để (So that):Hệ thống có thể tự động ghi nhận tồn kho tương ứng khi người dùng thao tác
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Cấu hình kho nhận NLWhen:TBP MC mở màn hình "Cấu hình nhà kho tiếp nhận NL khách"Then:Hệ thống hiển thị Form chọn nhà kho choKho tiếp nhận NL kháchKho nhập NL đã kiểmAnd:Chọn nhà kho tương ứng và nhấn "Xác nhận"Then:Hệ thống khi nhận nhà kho được chọn3. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Một loại cấu hình chỉ được phép có01 phiên bản Hiệu lựctại một thời điểm.
BR-02:Mỗi loại chênh lệch cần có ít nhất 1 người duyệt4. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)
Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Required | Quy tắc Validation | 
Nhà kho | Sub Warehouse | Dropdown | Có | Chọn từ Master Data Sub Warehoude; Chỉ show Sub Warehouse có loại = Kho nguyên liệu / WIP | 
5. GHI CHÚ CHO QC