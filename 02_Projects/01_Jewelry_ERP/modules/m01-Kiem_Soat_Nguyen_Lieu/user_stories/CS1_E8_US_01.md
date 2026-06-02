# 🏷️ [CS1.E8.US-01] Kho NL Khách - Quản lý Tồn Kho Khách Hàng (Customer Material Inventory)

**Epic:** Tồn kho (CS1.E8)
**Actor:** Trưởng bộ phận Material Control, Kế toán, Thủ kho

## 1. USER STORY
- **Là một:** Nhân viên MC / Thủ kho / Kế toán.
- **Tôi muốn:** Xem và quản lý danh sách tồn kho của các nguyên liệu, dẻ, hàng hồi được nhận từ khách hàng.
- **Để:** Kiểm soát chặt chẽ số lượng, trọng lượng tài sản ký gửi của khách hàng đang nằm trong xưởng chưa qua xử lý chốt công nợ.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Bộ lọc tìm kiếm (Filter)
- **Given:** Người dùng đang ở màn hình Tồn Kho NL Khách.
- **When:** Người dùng nhập các tiêu chí lọc:
    - **Tìm kiếm thông minh (Smart Search):** Mã Lot, Mã Khách hàng, Mã phiếu nhập.
    - **Phân loại tồn kho:**
        - Chờ nhập (Nguyên liệu, Thành phẩm chờ sửa)
        - Chờ trả (Nguyên liệu, Thành phẩm chờ sửa)
        - Đang kiểm định (Đang đo quang phổ, tính đá)
    - **Khoảng thời gian:** Từ ngày ... Đến ngày (ngày nhập kho).
- **Then:** Hệ thống hiển thị danh sách các Lot/Item thỏa mãn điều kiện.

### AC2: Danh sách tồn kho (Inventory Grid)
- **Then:** Dữ liệu hiển thị bao gồm các cột:
    1. **Mã Lô/Mã Item (Lot ID):** (VD: LOT-CUS-2510001).
    2. **Khách hàng:** Tên và Mã khách hàng.
    3. **Phân loại:** (Nguyên liệu, TP chờ sửa, Dẻ).
    4. **Trạng thái:** (Chờ nhập, Đang kiểm định, Chờ trả).
    5. **Trọng lượng tổng (Gross Weight):** Trọng lượng bao gồm bao bì.
    6. **Trọng lượng tịnh (Net Weight):** Trọng lượng kim loại thực tế (sau khi bóc tách).
    7. **Hành động:** Nút "Chi tiết", "Lịch sử giao dịch" (Stock Card).

### AC3: Ngăn chặn xuất âm (Negative Inventory Prevention)
- **Given:** Người dùng cố gắng thực hiện lệnh xuất trả khách hoặc chuyển quyền sở hữu.
- **When:** Trọng lượng xuất lớn hơn trọng lượng Tồn khả dụng (Available).
- **Then:** Hệ thống **chặn thao tác**, hiển thị thông báo lỗi: "Không thể xuất kho. Trọng lượng xuất vượt quá tồn khả dụng hiện tại." (Không cho phép tồn kho âm).

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

**Trạng thái View:**
- Màn hình sử dụng Component Table với phân trang (Pagination).
- Nút Action "Lịch sử giao dịch" mở ra dạng Drawer (Thẻ kho) ghi nhận tất cả các In/Out của Lot này.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Hàng trong Kho NL Khách mang tính chất ký gửi, Seva chưa có quyền sở hữu. Không được phép xuất đúc (Casting) trực tiếp từ kho này.
- **BR-02:** Chuyển đổi trạng thái kho (ví dụ từ "Chờ nhập" sang "Chờ trả" hoặc "Đã chốt công nợ") sẽ tự động giảm tồn ở khu vực tương ứng và ghi nhận vào lịch sử thẻ kho.
- **BR-03:** Tuyệt đối không cho phép tồn kho âm. Mọi giao dịch xuất phải có số dư tồn kho >= số lượng xuất.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Mã Lot | Lot ID | Text | Unique ID của lô hàng |
| Mã KH | Customer Code | Text | |
| Trạng thái | Status | Enum | Chờ nhập / Chờ trả / Đang kiểm định |
| Tồn khả dụng | Available Qty | Decimal(10,4) | Trọng lượng có thể thao tác |

