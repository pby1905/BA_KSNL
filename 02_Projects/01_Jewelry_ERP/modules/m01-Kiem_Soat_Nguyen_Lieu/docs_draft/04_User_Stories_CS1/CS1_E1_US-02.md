✅CS1.E1.US-02: [Nhận NL khách] - Thiết lập/chỉnh sửa người duyệt và mức chênh lệch✅CS1.E1.US-02: [Nhận NL khách] - Thiết lập/chỉnh sửa người duyệt và mức chênh lệch1. USER STORYLà một (As a):Trưởng bộ phận Material Control (TBP MC)
Tôi muốn (I want):Cấu hình danh sách người phê duyệt và thiết lập các ngưỡng chênh lệch cho phép đối:
TL bao bì;TL và tuổi dẻ;TL đá hàng hồi;TL, tuổi, giá công hàng hồi mới/hàng gửi sửaĐể (So that):Hệ thống có thể tự động kiểm soát dữ liệu đầu vào, ngăn chặn các sai sót vượt mức và đảm bảo quy trình phê duyệt diễn ra đúng thẩm quyền khi có biến động bất thường.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Cấu hình danh sách người phê duyệt (Approval Workflow)Given:TBP MC đang ở màn hình "Cấu hình phê duyệt chênh lệch".
When:Chọn loại nghiệp vụ (Kiểm bao bì/Kiểm dẻ/Kiểm hàng hồi/Kiểm hàng sửa) và chọn danh sách người dùng từ danh mục nhân viên để phân quyền phê duyệt.
Then:Hệ thống lưu lại danh sách
AC 2: Cấu hình ngưỡng chênh lệch Trọng lượng (TL) bao bìGiven:Đang thực hiện cấu hình cho mục Kiểm bao bì.
When:Nhập trị số chênh lệch tối đa cho phép giữa trọng lượng khách báo và trọng lượng thực tế và nhấn "Lưu".
Then:Hệ thống lưu lại cấu hình.
AC 3: Cấu hình chênh lệch Dẻ (TL & Tuổi dẻ)Given:Đang cấu hình thông số cho Kiểm dẻ.
When:Thiết lập ngưỡng sai số cho Trọng lượng và sai số Tuổi dẻ và nhấn "Lưu".
Then:Hệ thống lưu lại cấu hình.
AC 4: Cấu hình chênh lệch Hàng hồiGiven:Đang cấu hình cho Kiểm hàng hồi.
When:Nhập ngưỡng cho phép cho 2 chỉ số: TL đá và nhấn "Lưu".
Then:Hệ thống lưu lại cấu hình.
AC 4: Cấu hình chênh lệch Hàng hồi & Hàng gửi sửaGiven:Đang cấu hình cho Kiểm hàng sửa.
When:Nhập ngưỡng cho phép cho 3 chỉ số: Trọng lượng (TL), Tuổi vàng, Giá công và nhấn "Lưu".
Then:Hệ thống lưu lại cấu hình.3. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Một loại cấu hình chỉ được phép có01 phiên bản Hiệu lựctại một thời điểm.
BR-02:Mỗi loại chênh lệch cần có ít nhất 1 người duyệt4. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)
Tên trường | Kiểu dữ liệu | Required | Quy tắc Validation | 
Loại nghiệp vụ | Dropdown | Có | Kiểm bao bìKiểm dẻKiểm hàng hồiKiểm hàng sửa | 
Người phê duyệt | List (User) | Có | Chọn từ danh sách User | 
TL bao bì | Decimal (4,4) | Có | Cho phép nhập số dương. Đơn vị: lượng. | 
TL NL | Decimal (4,4) | Có | Cho phép nhập số dương. Đơn vị: lượng. | 
Tuổi | Decimal (2,2) | Có | Cho phép nhập số dương ( > 0, <= 99.99) | 
Trọng lượng đá | Decimal (4,4) | Có | Cho phép nhập số dương. Đơn vị: lượng. | 
Giá công | Amount | Có | Số tiền chênh lệch tối đa cho phép. | 
5. GHI CHÚ CHO QC