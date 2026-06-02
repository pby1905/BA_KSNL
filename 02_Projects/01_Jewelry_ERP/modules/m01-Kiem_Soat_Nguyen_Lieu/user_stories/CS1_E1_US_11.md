# 🏷️ [CS1.E1.US-11] Nhận NL khách - Xử lý: Kiểm mã hàng (Item Verification)

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** Nhân viên Tiếp nhận Nguyên liệu

## 1. USER STORY
- **Là một (As a):** Nhân viên Tiếp nhận Nguyên liệu
- **Tôi muốn (I want):** Thực hiện đối soát mã sản phẩm thực tế của khách hàng so với danh mục hàng hóa (Item) của công ty.
- **Để (So that):** Xác định chính xác thông tin hàng hóa, đảm bảo tính nguyên bản của sản phẩm và ghi nhận các sai lệch về thông tin mã hàng nếu có.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Kiểm mã hàng
- **Given (Biết rằng):** Nhân viên mở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhận ở bước trước.
- **And (Và):** Nhân viên chọn các dòng nguyên liệu có:
  - Loại = "Hàng hồi mới" hoặc "Hàng gửi sửa".
  - Tình trạng = "Đơn hàng".
- **And (Và):** Nhấn vào nút "Kiểm mã hàng".
- **When (Khi):** Hệ thống hiển thị Modal "Kiểm mã hàng" (như hình ảnh thiết kế).
- **Then (Thì):** Nhân viên có thể nhập thông tin mã hàng tương ứng cho từng dòng được chọn.

### AC 2: Kiểm lại & hủy xác nhận chênh lệch
- **Given (Biết rằng):** Nhân viên chọn các dòng nguyên liệu có:
  - Loại = "Hàng hồi mới" hoặc "Hàng gửi sửa".
  - Tình trạng = "Đơn hàng".
  - Trạng thái = "Đang xử lý".
- **And (Và):** Dòng nguyên liệu này có xử lý chênh lệch.
- **When (Khi):** Nhân viên nhấn vào nút "Kiểm mã hàng".
- **Then (Thì):** Hiển thị popup xác nhận:
  - **VN:** Phiếu Xử lý Chênh lệch tại các dòng {line 1, line 2...} sẽ chuyển sang trạng thái "Hủy". Bạn có chắc chắn muốn tiếp tục? "Có / Không"
  - **EN:** The Variance Processing Ticket for lines {line 1, line 2...} will be changed to 'Cancelled' status. Are you sure you want to proceed? 'Yes / No'
- **Hành động tiếp:**
  - Nhập **Có**: → Mở Modal "Kiểm mã hàng" và cho phép edit → Khi Submit kết quả Modal "Kiểm mã hàng" → Chuyển trạng thái phiếu "Xử lý chênh lệch" sang trạng thái → "Hủy".

---

## 3. THIẾT KẾ (UX/UI)
- (Tham chiếu thiết kế)

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Chỉ những dòng nguyên liệu thỏa mãn điều kiện sau có thể thực hiện Kiểm mã hàng, kiểm tra theo thứ tự sau:
  - Phân loại = "Hàng hồi mới / Hàng gửi sửa" → Vi phạm, cảnh báo: "Chỉ nguyên liệu 'Hàng hồi mới / Hàng gửi sửa' có thể thực hiện Kiểm mã hàng" (Only "Hàng hồi mới / Hàng gửi sửa" materials can perform Item Verification).
  - Tình trạng = "Đơn hàng" → Vi phạm, cảnh báo: "Chỉ tình trạng 'Đang đơn hàng' có thể thực hiện Kiểm mã hàng" (Item Verification can only be performed when the origin is "Order").
  - Trạng thái = "Đang xử lý" → Vi phạm, cảnh báo: "Chỉ trạng thái 'Đang xử lý' có thể thực hiện Đo phổ" (Item Verification can only be performed when the status is "In Progress").
- **BR-02:** Kết quả sau khi "Hoàn tất" sẽ được lưu log lịch sử (Audit Trail) để truy vết nếu có khiếu nại từ khách hàng về sau.

---

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)

### 5.1 Workflow validation
- Logic check phụ thuộc vào dòng đầu tiên (nhân bản validation tuổi).

### 5.2 Field Definition Table (Modal Kiểm mã hàng)

#### Bảng: Thông tin mã hàng

| Tên trường (VN) | EN Field Name | Type | Required | Rules |
|---|---|---|---|---|
| Hàng sai tem | Tag discrepancy detected | Checkbox | Không | Default = uncheck |
| Mã hàng | Item code | Search select | Default: Có | Không required nếu "Hàng sai tem" = checked. Cho phép search like các mã thành phẩm; Status = Active/Inactive. Chọn 1 từ gợi ý. |
| Số bag | Bag number | Search select | Không | Cho phép search like các mã bag (Sales Order / Repair Order / G Order / Sample Order / Proto Order); Tất cả Status. Chọn 1 từ gợi ý. |
| PO khách | Cust PO | Text | Không | Max 20 ký tự |
| Số lượng | Qty | Integer | Có | `value > 0` |
| Tuổi | Purity | Decimal (4,2) | Có | `0 < value < 100`. Validate: tuổi từ dòng thứ 2 tự động update theo dòng thứ 1 (Tất cả các dòng mã hàng trong 1 dòng nguyên liệu phải cùng tuổi). |
| Màu | Color | Dropdown | Có | Chọn từ Master Data màu |
| TL tổng | Total Weight | Decimal (10,4) | Có | `value > 0` |
| TL đá / bao | Stone Weight / bag | Decimal (10,4) | Có | `value > 0` |
| TL đá tổng | Total Stone Weight | Decimal (10,4) | Read-only | `= "Số lượng" * "TL đá / bao"` |
| TL | Metal Weight | Decimal (10,4) | Read-only | `= "TL tổng" - "TL đá tổng"` |
| Giá công / bao | Labour Cost / bag | Currency | Có | `value > 0` |
| Giá công tổng | Total Labour Cost | Currency | Read-only | `= "Số lượng" * "Giá công / bao"` |
| Ghi chú lỗi | Defect Reason | Dropdown | Không | Chọn từ Master Data ghi chú lỗi |

#### Bảng: Kiểm mã hàng (Tổng hợp)

| Tên trường (VN) | EN Field Name | Type | Required | Rules |
|---|---|---|---|---|
| Tuổi - Seva | Purity (Seva) | Decimal (4,2) | Read-only | = "Tuổi" ở dòng đầu tiên của bảng thông tin mã hàng |
| TL - Seva | Metal Weight (Seva) | Decimal (10,4) | Read-only | = Sum của cột "TL" bảng Thông tin mã hàng |
| Quy 99.99 - Seva | 99.99 Equiv. (Seva) | Decimal (10,4) | Read-only | = `"Tuổi - Seva" * "TL - Seva" / 99.99` |
| Giá công - Seva | Labour Cost (Seva) | Currency | Read-only | = Sum của cột "Giá công tổng" bảng Thông tin mã hàng |

---

## 6. GHI CHÚ CHO QC
- Cần validation pop-ups nếu trạng thái hoặc phân loại không match.
