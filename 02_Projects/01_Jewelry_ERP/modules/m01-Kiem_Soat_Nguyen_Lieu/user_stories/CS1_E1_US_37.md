# 🏷️ [CS1.E1.US-37] Nhận NL khách - Danh sách Phiếu Xuất Kho (Goods Issue List)

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** Trưởng bộ phận Material Control, Kế toán, Thủ kho

## 1. USER STORY
- **Là một:** Trưởng bộ phận, Kế toán viên hoặc Thủ kho.
- **Tôi muốn:** Xem danh sách tổng hợp các Phiếu xuất kho (PXK) từ tất cả các nguồn khác nhau.
- **Để:** Quản lý lịch sử xuất kho theo từng đợt, đối soát số lượng phiếu và truy xuất nhanh các chứng từ liên quan.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Bộ lọc tìm kiếm (Filter)
- **Given:** Người dùng đang ở màn hình Danh sách Phiếu Xuất Kho.
- **When:** Người dùng nhập các tiêu chí lọc:
    - **Tìm kiếm thông minh (Smart Search):** Ô tìm kiếm duy nhất cho phép nhập:
        - Mã phiếu đầy đủ (VD: `PXK-25100001`).
        - Chỉ phần số của phiếu (VD: `25100001`).
        - Mã tham chiếu gốc (VD: Ref Code, Mã lệnh/Phiếu yêu cầu...).
        - Logic: Search `Like %keyword%` trên cả 2 cột `Mã phiếu` và `Mã tham chiếu`.
    - **Loại phiếu xuất (Nguồn):** Dropdown đa chọn:
        - Xuất trả
        - Xuất xử
        - Xuất phân kim
        - Xuất chuyển chế
        - Xuất cấp NL
    - **Người xuất:** Search select theo nhân viên.
    - **Kho xuất:** Danh sách nhà kho hệ thống.
    - **Khoảng thời gian:** Từ ngày ... Đến ngày (theo thời điểm xuất kho).
- **Then:** Hệ thống hiển thị danh sách các phiếu xuất thỏa mãn điều kiện.

### AC2: Danh sách phiếu (Header Grid)
- **Then:** Dữ liệu hiển thị bao gồm các cột:
    1. **Mã phiếu xuất:** (VD: PXK-25100001).
    2. **Mã tham chiếu:** (Mã chứng từ/lệnh liên quan).
    3. **Loại phiếu:** Nhãn hiển thị mục đích xuất (VD: Xuất cấp NL).
    4. **Người xuất:** User thực hiện xuất kho.
    5. **Ngày xuất:** Định dạng DD/MM/YYYY HH:mm.
    6. **Tổng số dòng:** Số lượng Lot/Item hàng bên trong phiếu xuất.
    7. **Hành động:** Nút "Chi tiết".

### AC3: Xem chi tiết phiếu (Navigation)
- **When:** Người dùng nhấn nút **"Chi tiết"** trên một dòng phiếu.
- **Then:** Hệ thống điều hướng (hoặc mở Drawer) hiển thị thông tin đầy đủ của Phiếu xuất đó:
    - Khu vực thông tin Header (Thông tin chung của phiếu).
    - Bảng danh sách các Item/Lot bên trong.
    - **Lưu ý:** Chế độ xem là Read-only (Chỉ xem), không cho phép sửa/xóa vì phiếu đã ghi nhận trừ tồn hệ thống thành công.

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

**Trạng thái View:**
- Màn hình này sử dụng Component Table với phân trang (Pagination).
- Màu sắc nhãn **Loại phiếu xuất** nên phân biệt để dễ nhận diện khi nhìn lướt qua:
    - **Xuất trả:** Đỏ hoặc Cam nhạt (Mang ý nghĩa loại bỏ/trả về).
    - **Xuất xử:** Tím.
    - **Xuất phân kim:** Vàng đậm/Cam.
    - **Xuất chuyển chế:** Xanh dương.
    - **Xuất cấp NL:** Xanh lá (Luồng xuất sản xuất thường xuyên).

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Chỉ hiển thị các phiếu PXK đã ở trạng thái Hoàn thành (Đã Commit trừ tồn kho thành công).
- **BR-02:** Chế độ hiển thị danh sách là Read-only, không cung cấp tính năng sửa dữ liệu Header sau khi xuất. Mọi sự thay đổi (nếu có) phải tạo phiếu hoàn/nhập lại chứ không sửa trực tiếp.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Mã phiếu xuất | Issue Code | Text | Theo chuẩn mã hóa (PXK-...) |
| Loại xuất | Issue Type | Label | Mapping (Xuất trả, xử, phân kim, chuyển chế, cấp NL) |
| Người xuất | Issued By | Text | Tên User thao tác xuất |
| Ngày xuất | Issued At | Datetime | Thời điểm hoàn tất xuất kho |
| Tổng số dòng | Total Lines | Integer | Số lượng dòng Item trong phiếu |
| Tổng trọng lượng | Total Weight Sum | Decimal(10,4) | Tổng Metal Weight của các item bên trong |

---

## 6. GHI CHÚ CHO QC
- Kiểm tra tính chính xác của bộ lọc theo Thời gian và Loại phiếu xuất.
- Kiểm tra link "Chi tiết" dẫn đúng đến đúng dữ liệu của Header ID đó.
- Verify mã PXK được format chuẩn theo Phụ lục A (nếu có).
