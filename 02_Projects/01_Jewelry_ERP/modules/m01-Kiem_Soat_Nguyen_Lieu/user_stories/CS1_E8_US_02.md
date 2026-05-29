# 🏷️ [CS1.E8.US-02] Kho NL (Seva) - Quản lý Tồn Kho Công ty (Company Raw Material Inventory)

**Epic:** Tồn kho (CS1.E8)
**Actor:** Trưởng bộ phận Material Control, Kế toán, Thủ kho

## 1. USER STORY
- **Là một:** Nhân viên MC / Thủ kho / Kế toán.
- **Tôi muốn:** Xem và quản lý danh sách tồn kho của các nguyên liệu, dẻ, hàng hồi thuộc sở hữu của Seva.
- **Để:** Điều phối nguyên liệu cho sản xuất, theo dõi tồn kho thực tế, tồn khả dụng và kiểm soát thất thoát vàng.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Bộ lọc tìm kiếm (Filter)
- **Given:** Người dùng đang ở màn hình Tồn Kho NL (Seva).
- **When:** Người dùng nhập các tiêu chí lọc:
    - **Tìm kiếm thông minh (Smart Search):** Mã Lot, Mã Phiếu nhập.
    - **Phân loại tồn kho (Sub-inventory):**
        - NL chờ xử (Dẻ KH đã chốt công nợ, Hàng hồi từ SX)
        - NL chờ phân kim
        - NL Au 0-59 / NL Au 60-99
        - Fine Gold (Au 99.99)
        - NL Đúc (Cast, HTJ)
        - TP chờ sửa (Hàng hồi mới, Hàng hồi nấu, Hàng mẫu)
    - **Khoảng thời gian:** Từ ngày ... Đến ngày (ngày nhập kho).
- **Then:** Hệ thống hiển thị danh sách các Lot/Item thỏa mãn điều kiện.

### AC2: Danh sách tồn kho (Inventory Grid)
- **Then:** Dữ liệu hiển thị bao gồm các cột:
    1. **Mã Lô/Mã Item (Lot ID):** (VD: LOT-SEVA-2510001).
    2. **Phân loại:** (Fine Gold, NL chờ xử, Hàng hồi...).
    3. **Tuổi vàng (Karat/Purity):** (VD: 99.99%, 75%, 58.5%).
    4. **Trọng lượng thực tế (On-hand Weight):** Tổng trọng lượng đang có vật lý trong kho.
    5. **Trọng lượng chờ xuất (Allocated Weight):** Trọng lượng đã được giữ (reserve) cho các lệnh cấp NL nhưng chưa xuất kho thực tế.
    6. **Tồn khả dụng (Available Qty):** `On-hand Weight - Allocated Weight`.
    7. **Hành động:** Nút "Chi tiết", "Lịch sử thẻ kho" (Stock Card).

### AC3: Ngăn chặn xuất âm (Negative Inventory Prevention)
- **Given:** Người dùng cố gắng thực hiện lệnh xuất cấp NL, xuất xử hoặc phân kim.
- **When:** Trọng lượng xuất yêu cầu lớn hơn trọng lượng **Tồn khả dụng** (Available Qty).
- **Then:** Hệ thống **chặn thao tác**, hiển thị thông báo lỗi: "Không thể xuất kho. Trọng lượng xuất vượt quá tồn khả dụng hiện tại." (Không cho phép tồn kho âm).

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

**Trạng thái View:**
- Màn hình sử dụng Component Table với phân trang (Pagination).
- Khu vực hiển thị tổng quan (Dashboard) bên trên: Hiển thị tổng tồn Fine Gold, tổng tồn quy đổi 9999 của toàn kho.
- Nút Action "Lịch sử thẻ kho" dạng Drawer ghi nhận In/Out.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Hàng trong Kho NL (Seva) là tài sản công ty. Được phép sử dụng để cấp cho sản xuất (Casting, HTJ) thông qua lệnh cấp NL.
- **BR-02:** Việc tính toán Tồn khả dụng rất quan trọng để tránh Double-booking (một lô vàng được cấp cho 2 lệnh sản xuất khác nhau).
- **BR-03:** Tuyệt đối không cho phép tồn kho âm đối với bất kỳ phân khu nào trong Kho NL (Seva).

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Mã Lot | Lot ID | Text | Unique ID của lô hàng Seva |
| Phân loại | Sub-Inventory | Enum | Khu vực chứa hàng |
| Tuổi vàng | Purity | Decimal(5,2) | Tỷ lệ vàng tinh khiết (%) |
| Tồn khả dụng | Available Qty | Decimal(10,4) | Trọng lượng có thể xuất kho |
| Tồn chờ xuất | Allocated Qty | Decimal(10,4) | Trọng lượng đang bị block bởi lệnh SX |
