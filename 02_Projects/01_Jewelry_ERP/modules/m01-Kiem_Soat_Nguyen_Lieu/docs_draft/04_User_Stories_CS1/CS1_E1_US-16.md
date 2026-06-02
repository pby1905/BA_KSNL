✅CS1.E1.US-16: [Nhận NL khách] - Xử lý: Nhập kho (Stock Inbound) (tạo Lô & in nhãn)✅CS1.E1.US-16: [Nhận NL khách] - Xử lý: Nhập kho (Stock Inbound) (tạo Lô & in nhãn)1. USER STORYLà một:Nhân viên tiếp nhận nguyên liệu.
Tôi muốn:Thực hiện nhập kho các dòng nguyên liệu đã hoàn tất đối soát, hệ thống tự động sinh mã Lô (Lot Number) và in nhãn định danh.
Để:Chính thức ghi tăng tồn kho, sẵn sàng cho công đoạn cấp phát sản xuất và đảm bảo tính truy xuất nguồn gốc của vàng.
2. TIÊU CHÍ CHẤP NHẬN (AC)AC1: Nhập khoGiven:Các dòng nguyên liệu đang ở trạng thái"Đang xử lý"(đã qua đo phổ/kiểm mã).
When:Nhân viên chọn các dòng có
Trạng thái = "Đang xử lý"và, "Quy 99.99 - Seva" không rỗng (> 0)And:Nhân viên chọn hành động"Nhập kho" (Stock Inbound)từ menu thao tác.
Then:Hệ thống hiển thị Modal "Nhập kho"
When:Nhân viên hoàn thành Form là nhấn "Xác nhận"Then:Hệ thống cập nhậtTrạng thái dòng nguyên liệu: từ "Đang xử lý" → "Đã nhập kho"Xóa tồn kho NL kháchXóa tồn các dòng tương ứng tại [kho tiếp nhận NL khách]Tạo phiếu nhập NL (Goods Receipt, bao gồm header và dtl) (ghi nhận trước, sẽ có màn hình show dữ liệu bảng này. Note ngoài action này, còn nhiều action khác/nguồn khác ghi nhận vào bảng này)
Goods Receipt - Header | 
 | 
 | 
Code | Type | Ref Code | Received by | Received at | 
Mã | Loại | Mã tham chiếu | Người nhận | Ngày nhận | 
Mã phiếu nhập
→Phụ lục A - Mã hóa | 
Tình trạng | → | Loại | 
NL khách | → | L: Công nợ | 
Hàng chờ sửa | → | G: Hàng khách gửi | 
 | Mã phiếu tiếp nhận NL | User thao tác | Datetime | 
 | Loại bao gồm:
Mã: tên VN (Tên EN)L: Công nợ (Liability Receipt)
G: Hàng khách gửi (Guest)P: Công ty tự mua (Purchased)
S: Vụn từ xưởng (Scrap)
R: Từ thu hồi (Recovery)C: Từ đúc CastH: Từ đúc HTJ | 
 | 
 | 
 | 
#Ghi chú: Mỗi loại là 1 GR khác nhau, tách mỗi loại 1 GR khi nhập 1 lần nhiều loại
Goods Receipt - Detail | 
 | 
 | 
 | 
 | 
SubWarehouse | Zone | Location | Item | LOT | Qty | Lenght | Purity | Color | Total Weight | Stone Weight | Metal Weight | 99.99 Equiv. | Liability Impact | 99.99 Equiv. Liability Adjustment | Net 99.99 Equiv. Liability Receipt | Labour Cost | 
Kho | Khu vực | Vị trí | Item | Lô | SL | Chiều dài | Tuổi | Màu | Tổng TL | TL đá | TL | Quy 99.99 | Tính công nợ | Quy 99.99 - Công nợ điều chỉnh | Quy 99.99 - Công nợ | Giá công | 
 | 
 | 
 | 
 | 
 | 
 | Decimal (10,4) | 
 | 
 | 
 | 
 | 
 | 
 | 
 | 
 | 
 | 
 | 
Notes: Value ghi tương tự bảng ghi tồn bên dưới | 
 | 
 | 
 | 
 | 
Ghi tồn kho NL theo GR detail (ghi nhận trước, sẽ có màn hình show dữ liệu bảng này. Note ngoài action này, còn nhiều action khác/nguồn khác ghi nhận/cập nhật vào bảng này)
Nguyên liệu | 
 | Tồn cần ghi | 
Tình trạng | Loại | → | Kho | Khu vực | Vị trí | Item | Lô | Tuổi | Màu | SL | Chiều dài | Tổng TL | TL đá | TL | Quy 99.99 | Phương thức quản lý tồn | 
Condition | Classification | 
 | SubWarehouse | Zone | Location | Item | LOT | Purity | Color | Qty | Lenght | Total Weight | Stone Weight | Metal Weight | 99.99 Equiv. | Track Mode | 
NL khách | Dẻ | → | [kho nhập NL đã kiểm] | NL Chờ xử | Dẻ KH | Mã Item NL khách
→Phụ lục A - Mã hóa | Mã Lô nhập NL đã kiểm
→Phụ lục A - Mã hóa | = "Tuổi - Seva" | N/A | N/A | N/A | = "Tổng TL - Seva" | = "TL đá - Seva" | = "TL - Seva" | = "Quy 99.99 - Seva" | W | 
NL khách | Hàng hồi nấu | → | [kho nhập NL đã kiểm] | NL Chờ xử | Hàng hồi | Mã Item NL khách
→Phụ lục A - Mã hóa | Mã Lô nhập NL đã kiểm
→Phụ lục A - Mã hóa | = "Tuổi - Seva" | N/A | N/A | N/A | = "Tổng TL - Seva" | = "TL đá - Seva" | = "TL - Seva" | = "Quy 99.99 - Seva" | W | 
NL khách | hàng hồi mới | → | [kho nhập NL đã kiểm] | NL Chờ xử | Hàng hồi | Mã Item NL khách
→Phụ lục A - Mã hóa | Mã Lô nhập NL đã kiểm
→Phụ lục A - Mã hóa | = "Tuổi - Seva" | N/A | N/A | N/A | = "Tổng TL - Seva" | = "TL đá - Seva" | = "TL - Seva" | = "Quy 99.99 - Seva" | W | 
Đơn hàng | Hàng hồi mới | → | [kho nhập NL đã kiểm] | TP Chờ sửa | Hàng hồi mới | Mã Item NL khách
→Phụ lục A - Mã hóa | Mã Lô nhập NL đã kiểm
→Phụ lục A - Mã hóa | = "Tuổi - Seva" | N/A | = SL Item | N/A | = "Tổng TL - Seva" | = "TL đá - Seva" | = "TL - Seva" | = "Quy 99.99 - Seva" | Q+W | 
Đơn hàng | Hàng gửi sửa | → | [kho nhập NL đã kiểm] | TP Chờ sửa | Hàng gửi sửa | Mã Item NL khách
→Phụ lục A - Mã hóa | Mã Lô nhập NL đã kiểm
→Phụ lục A - Mã hóa | = "Tuổi - Seva" | N/A | = SL Item | N/A | = "Tổng TL - Seva" | = "TL đá - Seva" | = "TL - Seva" | = "Quy 99.99 - Seva" | Q+W | 
#Ghi chú:TrackMode bao gồmW: chỉ quản lý trọng lượngQ+W: quản lý bằng số lượng và trọng lượngQ+W+H: quản lý bằng số lượng, trọng lượng và chiều dàiTrackMode ghi nhận nhằm phục vụ công tác nhập/xuất tồn, nhằm xác định key và dữ liệu cần đối chiếu khi ghi nhận hoặc trừ tồnVí dụ:Với record có TrackMode = W → Khi xuất kho, cần xác định trọng lượng xuất, trừ trọng lượng tương ứng khi xuấtVới record có TrackMode = Q+W → Khi xuất kho, cần xác định cả số lượng và trọng lượng, trừ số lượng và trọng lượng tương ứng khi xuất...Với thành phần nào không có ở TrackMode, khi ghi tồn → thành phần đó ghinullVD: Nếu record có TrackMode = W → Khi ghi tồn, trường Qty và Lenght =N/AIf:Phiếu NL không còn dòng nguyên liệu ở trạng thái: "Đang xử lý" / "Chờ xác nhận"Then:Hệ thống cập nhật trạng thái Phiếu tiếp nhận NL từ: "Đang thực hiện" sang → "Hoàn thành"3. THIẾT KẾ (UX/UI) *Link Figma:(Theo link mẫu của dự án)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES) *BR-01:Một GR chỉ bao gồm 1 loại nhập kho (công nợ/công ty mua/,...)
5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES) *5.1 Workflow validation5.2 Field Definition Table
Field Name (VN) | Field Name (EN) | Type | Required | Rules | 
Tính công nợ | Liability Impact | Checkbox | Read-only | 
Phân loại | Tình trạng | → | Tính công nợ | 
Dẻ | NL từ khách | → | Checked | 
Hàng hồi nấu | NL từ khách | → | Checked | 
Hàng hồi mới | NL từ khách | → | Checked | 
Hàng hồi mới | Đơn hàng | → | Unchecked | 
Hàng gửi sửa | Đơn hàng | → | Unchecked | 
 | 
Quy 99.99 - Công nợ điều chỉnh | 99.99 Equiv. Liability Adjustment | Decimal(10,4) | N | Chỉ show khi Tính công nợ = checked
Default = 0, enable cho phép editNếu, dòng NL là dẻ và có Phiếu xử lý chênh lệch→ = "Có tạp"."Quy 99.99 - Tổng khách bù"Notes: "Quy 99.99 - Tổng khách bù" ghi nhận giá trị "âm" | 
Quy 99.99 - Công nợ | Net 99.99 Equiv. Liability Receipt | Decimal(10,4) | Read-only | Chỉ show khi Tính công nợ = checked
= "Quy 99.99 - Seva" + "Quy 99.99 - Công nợ điều chỉnh"
Notes: "Quy 99.99 - Công nợ điều chỉnh" có thể mang giá trị âm/dương → Khi đó cộng đúng giá trị âm/dương của "Quy 99.99 - Công nợ điều chỉnh"
VD: 100.0000 + (-50.0000) = 50.0000Validate: {value} > = 0 | 
Giá công - Seva | Labour Cost (Seva) | Currency | N | Chỉ show khi: field "tình trạng" = đơn hàng | 
Khu vực nhập kho | Storage Zone | Dropdown | Y | Value = List danh sách khu vực thuộc [kho nhập NL đã kiểm]
Default:
Tình trạng | → | Kho | Khu vực | 
NL từ khách | → | [kho nhập NL đã kiểm] | NL chờ xử | 
Đơn hàng | → | [kho nhập NL đã kiểm] | TP chờ sửa | 
 | 
Ghi chú | Remarks | Text | N | Max 100 ký tự | 
6. GHI CHÚ CHO QCKiểm tra phiếu GR được tạo, kiểm tra TH 2 loại có tạo thành 2 phiếu riêngKiểm tra thông tin công nợKiểm tra bảng tồnKiểm tra các field SL, chiều dài, TL ở tồnLuật thép: Trọng lượng không được sai