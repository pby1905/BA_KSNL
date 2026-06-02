# 🏷️ [CS1.E1.US-30] Nhận NL khách - Danh sách Phiếu Nhập Kho (Goods Receipt List)

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** Trưởng bộ phận Material Control, Kế toán

## 1. USER STORY
- **Là một:** Trưởng bộ phận hoặc Kế toán viên.
- **Tôi muốn:** Xem danh sách tổng hợp các Phiếu nhập kho (PNK) từ tất cả các nguồn khác nhau đổ về hệ thống.
- **Để:** Quản lý lịch sử nhập kho theo từng đợt, đối soát số lượng phiếu và truy xuất nhanh các chứng từ liên quan.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Bộ lọc tìm kiếm (Filter)
- **Given:** Người dùng đang ở màn hình Danh sách Phiếu Nhập Kho.
- **When:** Người dùng nhập các tiêu chí lọc:
    - **Tìm kiếm thông minh (Smart Search):** Ô tìm kiếm duy nhất cho phép nhập:
        - Mã phiếu đầy đủ (VD: `PNK-25100001`).
        - Chỉ phần số của phiếu (VD: `25100001`).
        - Mã tham chiếu gốc (VD: Phiếu NNL-..., Ref Code).
        - Logic: Search `Like %keyword%` trên cả 2 cột `Mã phiếu` và `Mã tham chiếu`.
    - **Người nhận:** Search select theo nhân viên.
    - **Kho nhập:** Danh sách nhà kho chính thức.
    - **Khoảng thời gian:** Từ ngày ... Đến ngày (theo thời điểm nhập kho).
- **Then:** Hệ thống hiển thị danh sách các phiếu thỏa mãn điều kiện.

### AC2: Danh sách phiếu (Header Grid)
- **Then:** Dữ liệu hiển thị bao gồm các cột:
    1. **Mã phiếu nhập:** (VD: PNK-25100001).
    2. **Mã tham chiếu:** (Phiếu NNL hoặc các mã Ref khác).
    3. **Loại phiếu (Nguồn):** Hiển thị nhãn rõ ràng (VD: L -> Vàng Công Nợ).
    4. **Người nhận:** User thực hiện nhập kho.
    5. **Ngày nhận:** Định dạng DD/MM/YYYY HH:mm.
    6. **Tổng số dòng:** Số lượng Lot hàng bên trong phiếu.
    7. **Hành động:** Nút "Chi tiết".

### AC3: Xem chi tiết phiếu (Navigation)
- **When:** Người dùng nhấn nút **"Chi tiết"** trên một dòng phiếu.
- **Then:** Hệ thống điều hướng (hoặc mở Drawer) hiển thị thông tin đầy đủ của Phiếu đó:
    - Khu vực thông tin Header (Thông tin chung).
    - Bảng danh sách các Item/Lot bên trong (Thừa hưởng cấu trúc Grid từ US-16).
    - **Lưu ý:** Chế độ xem là Read-only (Chỉ xem), không cho phép sửa/xóa.

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

**Trạng thái View:**
- Màn hình này sử dụng Component Table với phân trang (Pagination).
- Màu sắc nhãn Loại phiếu (Source) nên phân biệt để dễ nhận diện:
    - `L` (Công nợ): Màu Cam.
    - `P` (Tự mua): Màu Xanh lá.
    - `S/R` (Nội bộ): Màu Xanh dương.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Chỉ hiển thị các phiếu PNK đã ở trạng thái Hoàn thành (Đã Commit vào kho).
- **BR-02:** Không hiển thị các cột liên quan đến tính toán Chênh lệch hay Công nợ tại màn hình danh sách tổng (Overview). Các thông tin đó chỉ nằm trong màn hình Detail của phiếu.

---

## 5. BẢNG ĐÌNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Mã phiếu nhập | Receipt Code | Text | Theo Phụ lục A (PNK-...) |
| Nguồn gốc | Source Type | Label | Mapping từ Type (L, G, P, S, R, C, H) |
| Người nhận | Received By | Text | Tên User thực hiện |
| Ngày nhận | Received At | Datetime | Thời điểm hoàn tất nhập kho |
| Tổng trọng lượng | Total Weight Sum | Decimal(10,4) | Tổng Metal Weight của các item bên trong |

---

## 6. GHI CHÚ CHO QC
- Kiểm tra tính chính xác của bộ lọc theo Thời gian.
- Kiểm tra link "Chi tiết" dẫn đúng đến đúng dữ liệu của Header ID đó.
- Verify mã PNK khớp với chuẩn Phụ lục A.
