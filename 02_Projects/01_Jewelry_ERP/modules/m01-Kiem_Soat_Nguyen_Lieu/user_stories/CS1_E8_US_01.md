# 🏷️ [CS1.E8.US-01] Quản lý Tồn Kho Tổng Hợp (Master Inventory View)

**Epic:** Tồn kho (CS1.E8)
**Actor:** Trưởng bộ phận Material Control, Kế toán, Thủ kho

## 1. USER STORY
- **Là một:** Nhân viên MC / Thủ kho / Kế toán.
- **Tôi muốn:** Xem và quản lý danh sách tồn kho trên một màn hình tổng hợp duy nhất, cho phép chuyển đổi giữa các pháp nhân/loại kho (Khách, Seva, Hội) và xem dưới nhiều góc độ khác nhau (Mã hàng, Lô, Vị trí).
- **Để:** Dễ dàng tra cứu, kiểm soát vật tư, điều phối sản xuất và tránh thất thoát mà không phải điều hướng qua nhiều màn hình rời rạc.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Bộ chuyển đổi Loại Kho (Warehouse Switcher)
- **Given:** Người dùng truy cập màn hình "Quản lý Tồn kho".
- **When:** Người dùng click vào bộ chuyển đổi "Loại kho".
- **Then:** Hệ thống cho phép chọn 1 trong 3 khu vực:
    1. **Kho NL Khách (Customer Inventory):** Tài sản ký gửi chờ xử lý hoặc chờ trả.
    2. **Kho NL Seva (Company Inventory):** Tài sản công ty dùng để đúc, phân kim.
    3. **Kho Hội (Alloy Inventory):** Phụ gia, kim loại màu.

### AC2: Hệ thống 3 Tabs View (Góc nhìn dữ liệu)
- **Given:** Người dùng đã chọn 1 Loại kho.
- **When:** Màn hình hiển thị dữ liệu tồn kho.
- **Then:** Người dùng có thể chuyển đổi giữa 3 Tabs sau:
    - **Tab 1: Tồn kho theo Mã Hàng (By Item):** Gom nhóm tổng trọng lượng/số lượng theo từng Mã Item (không phân biệt lô, không phân biệt vị trí).
    - **Tab 2: Tồn kho theo Lô (By Lot):** Chi tiết tồn kho tách bạch theo từng Lot ID cụ thể để phục vụ truy vết.
    - **Tab 3: Tồn kho theo Vị trí (By Location):** Gom nhóm số lượng theo khu vực vật lý (Zone/Bin), ví dụ: Tủ 1, Ngăn 2.

### AC3: Bộ lọc dùng chung (Unified Filters)
- **Given:** Người dùng đang ở bất kỳ Tab nào.
- **When:** Người dùng sử dụng khu vực Filter.
- **Then:** Có thể tìm kiếm bằng các tiêu chí:
    - **Thanh tìm kiếm:** Mã hàng, Tên hàng, Mã Lot.
    - **Pháp nhân (Legal Entity):** Lọc theo các công ty thuộc tập đoàn (VD: Sevago).
    - **Nhóm hàng (Item Group):** Vàng nguyên liệu, Bạc, Master Alloy, Dẻ...
    - **Loại tồn kho (Sub-Inventory):** Chờ nhập, WIP, Fine Gold, Hội lưu trữ, Hội hàng ngày...
    - **Tình trạng (Status):** Khả dụng, Đang bị hold, Cần bổ sung...

### AC4: Lưới dữ liệu tiêu chuẩn (Unified Data Grid)
- **Then:** Các cột hiển thị trên Grid bao gồm:
    1. Pháp nhân (Legal Entity)
    2. Nhóm hàng (Item Group)
    3. Hình ảnh (Image Thumbnail)
    4. Mã hàng (Item Code)
    5. Tên hàng (Item Name)
    6. Loại tồn kho (Inventory Type)
    7. Tình trạng (Status)
    8. Tổng trọng lượng (Gross Weight)
    9. Trọng lượng đá (Stone Weight)
    10. Trọng lượng kim loại (Net Metal Weight)
    11. Số lượng (Quantity)
    12. Chiều dài (Length) - *Note: Sẽ hiển thị trống (null) đối với vàng khối/dẻ.*

### AC5: Cảnh báo Tồn tối thiểu (Dành riêng cho Kho Hội)
- **Given:** Người dùng đang xem "Kho Hội".
- **When:** Có bất kỳ Item nào (đặc biệt trong Kho Hàng Ngày) có trọng lượng/số lượng rơi xuống dưới mức Min-level đã cấu hình.
- **Then:** Hệ thống highlight đỏ/cam dòng đó trên Grid và cột "Tình trạng" đổi thành "Cần bổ sung".

### AC6: Ngăn chặn xuất âm (Chung)
- **Given:** Người dùng tạo một giao dịch xuất/chuyển kho (từ màn hình thao tác khác hoặc popup).
- **When:** Trọng lượng xuất lớn hơn Tồn kho khả dụng của Lô/Item đó.
- **Then:** Hệ thống chặn giao dịch và báo lỗi: "Không thể xuất kho. Vượt quá tồn khả dụng hiện tại."

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- **Layout tổng thể:**
  - Header: Warehouse Switcher (Khách/Seva/Hội) to và rõ ràng.
  - Sub-Header: 3 Tabs (Theo Mã Hàng | Theo Lô | Theo Vị trí).
  - Left Sidebar / Top Bar: Vùng Filters mở rộng.
  - Main Body: Component Table tích hợp Horizontal Scroll (Do nhiều cột).
- Có nút Action "Lịch sử giao dịch" (Stock Card) ở mỗi dòng để xem log In/Out.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Tuyệt đối không cho phép tồn kho âm đối với bất kỳ khu vực nào.
- **BR-02:** Hàng thuộc "Kho NL Khách" mang tính chất ký gửi, không được phép xuất thẳng vào các Lệnh Đúc (Casting Order) cho đến khi hoàn thành chốt công nợ (chuyển sang Kho Seva).
- **BR-03:** "Kho Hội" được phân chia cấp bậc (Lưu trữ và Hàng ngày) để đảm bảo an ninh bảo mật. Các giao dịch xuất hao hụt thường nhật chỉ được lấy từ Kho Hàng ngày.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Pháp nhân | Legal Entity | Text | Tên Công ty thuộc tập đoàn (VD: Sevago) |
| Trọng lượng kim loại | Net Metal Weight | Decimal(10,4) | Gross Weight - Stone Weight - Bao bì |
| Chiều dài | Length | Decimal | Dành cho dây chuyền. Bỏ trống nếu là Dẻ/Thỏi |
| Loại tồn kho | Sub-Inventory | Enum | |
