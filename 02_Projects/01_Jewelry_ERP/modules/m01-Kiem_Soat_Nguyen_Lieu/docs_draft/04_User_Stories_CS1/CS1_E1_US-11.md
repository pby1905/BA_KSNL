✅CS1.E1.US-11: [Nhận NL khách] - Xử lý: Kiểm mã hàng (Item Verification)✅CS1.E1.US-11: [Nhận NL khách] - Xử lý: Kiểm mã hàng (Item Verification)1. USER STORYLà một:Nhân viên Tiếp nhận Nguyên liệu
Tôi muốn:Thực hiện đối soát mã sản phẩm thực tế của khách hàng so với danh mục hàng hóa (Item) của công ty.
Để:Xác định chính xác thông tin hàng hóa, đảm bảo tính nguyên bản của sản phẩm và ghi nhận các sai lệch về thông tin mã hàng nếu có.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Kiểm mã hàng
Given:Nhân viên đo phổ mở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhận ở bước trước.
And:Nhân viên chọn các dòng nguyên liệu có:Loại = "Hàng hồi mới" hoặc "Hàng gửi sửa".và, tình trạng = "Đơn hàng"And:Nhấn vào nút "Kiểm mã hàng".When:Hệ thống hiển thị Modal "Kiểm mã hàng" (như hình ảnh thiết kế).
Then:Nhân viên có thể nhập thông tin mã hàng tương ứng cho từng dòng được chọn.
AC 2: Kiểm lại & hủy xác nhận chênh lệch
Given:Nhân viên chọn các dòng nguyên liệu có:Loại = "Hàng hồi mới" hoặc "Hàng gửi sửa".và, tình trạng = "Đơn hàng"và, trạng thái = "Đang xử lý"And:Dòng nguyên liệu này có xử lý chênh lệchWhen:Nhân viên nhấn vào nút "Kiểm mã hàng"Then:Hiển thị popup xác nhậnVN: Phiếu Xử lý Chênh lệch tại các dòng {line 1, line 2...} sẽ chuyển sang trạng thái "Hủy". Bạn có chắc chắn muốn tiếp tục? "Có / Không"EN: The Variance Processing Ticket for lines {line 1, line 2...} will be changed to 'Cancelled' status. Are you sure you want to proceed? 'Yes / No'Có:→ Mở Modal "Kiểm mã hàng" và cho phép edit→ Khi Submit kết quả Modal "Kiểm mã hàng" → Chuyển trạng thái phiếu "Xử lý chênh lệch" sang trạng thái → "Hủy"
3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Chỉ những dòng nguyên liệu thõa mãn điều kiện sau có thể thực hiện Kiểm mã hàng, kiểm tra theo thứ tự sau:
Phân loại = "Hàng hồi mới / Hàng gửi sửa" → Vi phạm, cảnh báo:Chỉ nguyên liệu "Hàng hồi mới / Hàng gửi sửa" có thể thực hiện Kiểm mã hàngOnly "Hàng hồi mới / Hàng gửi sửa" materials can perform Item Verificationvà, tình trạng = "Đơn hàng"  → Vi phạm, cảnh báo:Chỉ tình trạng "Đơn hàng" có thể thực hiện Kiểm mã hàngItem Verification can only be performed when the origin is "Order"và, trạng thái = "Đang xử lý" → Vi phạm, cảnh báo:Chỉ trạng thái "Đang xử lý" có thể thực hiện Đo phổItem Verification can only be performed when the status is "In Progress"BR-02:Kết quả sau khi "Hoàn tất" sẽ được lưu log lịch sử (Audit Trail) để truy vết nếu có khiếu nại từ khách hàng về sau.
5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Workflow validation5.2 Field Definition Table (Modal đo phổ)
Tên trường (VN) | EN Field Name | Type | Required | Rules | 
Thông tin mã hàng | 
Hàng sai tem | Tag discrepancy detected | Checkbox | Không | Default = uncheck | 
Mã hàng | Item code | Search select | Default: Có
Không required nếu "Hàng sai tem" = checked | Cho phép search like các mã thành phẩm; Status = Active/InactiveChọn 1 từ gợi ý | 
Số bag | Bag number | Search select | Không | Cho phép search like các mã bag (Sales Order / Repair Prrder / G Order / Sample Order / Proto Order); Tất cả StatusChọn 1 từ gợi ý | 
PO khách | Cust PO | Text | Không | Max 20 ký tự | 
Số lượng | Qty | Interger | Có | {value} > 0 | 
Tuổi | Purity | Decimal (4,2) | Có | 0 < {value} < 100
Validate, tuổi từ dòng thứ 2 tự động update theo dòng thứ 1 (Tất cả các dòng mã hàng trong 1 dòng nguyên liệu phải cùng tuổi)
 | 
Màu | Color | Dropdown | Có | Chọn từ Master Data màu
 | 
TL tổng | Total Weight | Decimal (10,4) | Có | {value} > 0 | 
TL đá / bao | Stone Weight / bag | Decimal (10,4) | Có | {value} > 0
 | 
TL đá tổng | Total Stone Weight | Decimal (10,4) | Read-only | = "Số lượng" x "TL đá / bao" | 
TL | Metal Weight | Decimal (10,4) | Read-only | = "TL tổng" - "TL đá tổng" | 
Giá công / bao | Labour Cost / bag | Currency | Có | {value} > 0 | 
Giá công tổng | Total Labour Cost | Currency | Read-only | = "Số lượng" x "Giá công / bao" | 
Ghi chú lỗi | Remarks | Dropdown | Không | Chọn từ Master Data ghi chú lỗi | 
Kiểm mã hàng | 
Tuổi - Seva | Purity (Seva) | Decimal (4,2) | Read-only | = "Tuổi" ở dòng đầu tiên của bảng thông tin mã hàng | 
TL - Seva | Metal Weight (Seva) | Decimal (10,4) | Read-only | = Sum của cột "TL tổng" bảng Thông tin mã hàng | 
Quy 99.99 - Seva | 99.99 Equiv. (Seva) | Decimal (10,4) | Read-only | = "Tuổi - Seva" x "TL - Seva" / 99.99 | 
Giá công - Seva | Labour Cost (Seva) | Currency | Read-only | = Sum của cột "Giá công tổng" bảng Thông tin mã hàng | 
6. GHI CHÚ CHO QC