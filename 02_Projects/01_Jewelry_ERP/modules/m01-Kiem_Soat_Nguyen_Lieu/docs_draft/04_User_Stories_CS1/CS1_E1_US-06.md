✅CS1.E1.US-06: [Nhận NL khách] - Kiểm tra TL chi tiết✅CS1.E1.US-06: [Nhận NL khách] - Kiểm tra TL chi tiết1. USER STORYLà một (As a):Nhân viên Tiếp nhận Nguyên liệu
Tôi muốn (I want):Nhập liệu chi tiết phân loại nguyên liệu, trọng lượng khách báo, trọng lượng Seva cân thực tế và tuổi vàng cho từng dòng hàng
Để (So that):Hệ thống ghi nhận dữ liệu bóc tách chi tiết làm cơ sở tính toán quy đổi vàng ròng (Quy 9999) và đối chiếu sai lệch trước khi xử lý tiếp.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Hiển thị thông tin tiến trình và thông tin chungGiven (Biết rằng):Nhân viên đã xác nhận bao bì thành công ở bước 1.
When (Khi):Truy cập vào chi tiết phiếu
Then (Thì):
Hệ thống hiển thịSteppergồm 3 bước: 1. Xác nhận bao bì (đã hoàn thành), 2. Kiểm tra trọng lượng chi tiết (đang thực hiện), 3. Xử lý từng loại.
Hiển thịThông tin chung(Khách hàng, Lô, Ngày tiếp nhận...) vàLịch sử hoạt độngcủa phiếu.
AC 2: Tự động tính toán trên từng dòng (Row Calculation)Given (Biết rằng):Nhân viên nhập dữ liệu vào các cột tương ứng.
When (Khi):Dữ liệu thay đổi.
Then (Thì):Hệ thống tự động tính toán theo công thức:
TL - khách= [TL tổng - khách] - [TL đá - khách].
Quy 99.99 - khách= ([TL - khách] * [Tuổi - khách]) / 99.99.
AC 3: Tổng hợp dữ liệu cuối bảng (Footer Summary)Given (Biết rằng):Bảng có nhiều dòng dữ liệu.
Then (Thì):DòngTổngở cuối bảng phải tự động cập nhật tổng cộng của các cột: TL tổng - khách, TL đá - khách, TL - khách, Quy 9999 - khách, TL tổng - Seva, và Tiền công - khách.
AC 4: Ghi tồn Tiếp nhận NL kháchGiven (Biết rằng):Nhân đã hoàn thành nhập dữ liệu Kiểm tra TL chi tiết
When (Khi):Nhân viên chọn "Tiếp tục"
Then (Thì):
Hệ thống ghi nhận tồn kho theo thông tin trên vào kho đã được cấu hình là kho Tiếp nhận NL khách
Ghi nhận vào Khu vực "Chờ nhập"
Ghi nhận vào Vị tríNếu, tình trạng = NL khách → Vị trí: Nguyên liệuNếu, tính trạng = Đơn hàng → Vị trí: Đơn hàngGhi nhận vào Item = phân loại (Dẻ, hàng hồi nấu, hàng hồi mới,..)
Nguyên liệu | 
 | Tồn cần ghi | 
Tình trạng | Loại | → | Kho | Khu vực | Vị trí | Item
(= "loại")
 | Lô
 | Tuổi
 | Màu
 | Tổng TL
 | TL đá
 | TL
 | Quy 99.99
 | 
NL khách | Dẻ | → | [kho tiếp nhận NL khách] | Chờ nhập | Nguyên liệu | Dẻ | = "Lô phiếu tiếp nhận NL" | = "Tuổi - khách" | null | = "Tổng TL - khách" | = "TL đá - khách" | = "TL khách" | = "Quy 99.99 - khách | 
NL khách | Hàng hồi nấu | → | [kho tiếp nhận NL khách] | Chờ nhập | Nguyên liệu | Hàng hồi nấu | = "Lô phiếu tiếp nhận NL" | = "Tuổi - khách" | null | = "Tổng TL - khách" | = "TL đá - khách" | = "TL khách" | = "Quy 99.99 - khách | 
NL khách | hàng hồi mới | → | [kho tiếp nhận NL khách] | Chờ nhập | Nguyên liệu | Hàng hồi mới | = "Lô phiếu tiếp nhận NL" | = "Tuổi - khách" | null | = "Tổng TL - khách" | = "TL đá - khách" | = "TL khách" | = "Quy 99.99 - khách | 
Đơn hàng | Hàng hồi mới | → | [kho tiếp nhận NL khách] | Chờ nhập | TP chờ sửa | Hàng hồi mới | = "Lô phiếu tiếp nhận NL" | = "Tuổi - khách" | null | = "Tổng TL - khách" | = "TL đá - khách" | = "TL khách" | = "Quy 99.99 - khách | 
Đơn hàng | Hàng gửi sửa | → | [kho tiếp nhận NL khách] | Chờ nhập | TP chờ sửa | Hàng gửi sửa | = "Lô phiếu tiếp nhận NL" | = "Tuổi - khách" | null | = "Tổng TL - khách" | = "TL đá - khách" | = "TL khách" | = "Quy 99.99 - khách | 
Notes: Cần thiết lập trước Khu vực và Vị trí cho Kho tiếp nhận NL, bao gồm:
Kho: tiếp nhận NL kháchKhu vực: Chờ nhậpVị trí: Nguyên liệuVị trí: TP chờ sửaKhu vực: Chờ trảVị trí: Nguyên liệuVị trí: TP chờ sửa3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Tất cả các ô nhập trọng lượng phải cho phép nhập tối đa 4 chữ số thập phân (ví dụ: 10.4740).
BR-02:Cột "Tiền công - khách" chỉ bắt buộc nhập nếu tình trạng = "Đơn hàng"
BR-03:Nếu "TL tổng - Seva" chưa được nhập đủ cho tất cả các dòng, nút "Tiếp tục" sẽ bị disabled.
5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1. Validation Logic5.2. Field Definition Table (Bảng định nghĩa trường dữ liệu)
Tên trường (VN) | EN Field Name | Loại dữ liệu | Bắt buộc | Quy tắc / Ghi chú (Rules) | 
Phân loại | Classification | Dropdown | Có | Chọn từ danh sách: Dẻ (Scrap), Hàng hồi nấu (Recycle-Melt), Hàng hồi mới (Recycle-New), Hàng gửi sửa (Repair). | 
Tình trạng | Origin | Dropdown | Có | Xác định nguồn gốc: NL từ khách (Customer Material), Đơn hàng (Sales Order). | 
Tuổi - khách | Purity (Cust) | Decimal(4,2) | Có | 0 < {Value} < 100
 | 
TL tổng - khách | Total Weight (Cust) | Decimal(10,4) | Có | 0 < {Value} | 
TL đá - khách | Stone Weight (Cust) | Decimal(10,4) | Có | Default = 0
0 <= {Value}
 | 
TL - khách | Metal Weight (Cust) | Decimal(10,4) | Read-only | = [Total Weight (Cust)] - [Stone Weight (Cust)] | 
Quy 99.99 - khách | 99.99 Equiv. (Cust) | Decimal(10,4) | Read-only | = ([Metal Weight (Cust)] * [Purity (Cust)]) / 99.99 | 
TL tổng - Seva | Total Weight (Seva) | Decimal(10,4) | Có | 0 < {Value} | 
Tiền công - khách | Labour Cost (Cust) | Currency | Điều kiện | Bắt buộc nếu tình trạng = "Đơn hàng" | 
Ghi chú | Remarks | Text Area | Không | Max 100 ký tự | 
6. GHI CHÚ CHO DEV & QCQC:Kiểm tra việc thêm/xóa dòng có làm sai lệch số tổng ở dòng cuối cùng hay không.