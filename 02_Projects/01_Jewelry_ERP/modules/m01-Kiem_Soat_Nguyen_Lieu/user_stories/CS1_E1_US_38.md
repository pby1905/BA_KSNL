# 🏷️ [CS1.E1.US-38] Nhận NL khách - Danh mục Vật tư Xuất Kho (Goods Issue Item List)

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** NV Kho, QC, Kế toán

## 1. USER STORY
- **Là một:** Nhân viên Kho, QC hoặc Kế toán.
- **Tôi muốn:** Có một màn hình hiển thị danh sách chi tiết tất cả các dòng vật tư (Item/Lô) đã được xuất khỏi kho.
- **Để:** Dễ dàng tra cứu thông tin kỹ thuật của từng lô hàng đã xuất (trọng lượng, tuổi vàng, loại xuất) mà không cần phải mở từng Phiếu xuất kho riêng lẻ, phục vụ đắc lực cho việc đối soát và làm báo cáo.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Bộ lọc tìm kiếm chi tiết (Advanced Filter)
- **Given:** Người dùng đang ở màn hình Danh mục Vật tư Xuất Kho.
- **When:** Người dùng lọc theo các thuộc tính vật tư:
    - **Số Lô (LOT):** Search chính xác hoặc gần đúng mã Lô.
    - **Mã Item (SKU):** Lọc theo loại vật tư nguyên liệu.
    - **Loại xuất:** Dropdown đa chọn (Xuất trả, Xuất xử, Xuất phân kim, Xuất chuyển chế, Xuất cấp NL).
    - **Kho xuất / Khu vực / Vị trí:** Dropdown phân cấp (Hierarchy).
    - **Tuổi vàng:** Khoảng giá trị (VD: Tuổi từ 74.5 đến 75.1).
    - **Khoảng thời gian:** Lọc theo ngày xuất.
- **Then:** Hệ thống hiển thị danh sách các Record vật tư con đã xuất kho.

### AC2: Lưới dữ liệu vật tư (Item/Lot Grid)
- **Then:** Bảng dữ liệu hiển thị các cột thông tin chi tiết:
    1. **Mã Phiếu Xuất (PXK):** (Có gắn link, Click vào sẽ điều hướng về chi tiết phiếu xuất ở US-37).
    2. **Lô (LOT):** Mã lô của vật tư/nguyên liệu được xuất.
    3. **Item:** Mã nguyên liệu.
    4. **Kho xuất:** Kho/Khu vực/Vị trí lưu trữ ngay trước khi xuất.
    5. **Loại xuất:** Nhãn (Label) mục đích xuất (Theo 5 loại).
    6. **Tuổi:** Tuổi Seva.
    7. **Số lượng (Qty):** (Chỉ hiện nếu TrackMode có quản lý Qty).
    8. **Trọng lượng tổng (Total Weight):** Decimal(10,4).
    9. **TL Đá (Stone Weight):** Decimal(10,4).
    10. **TL Kim loại (Metal Weight):** Decimal(10,4).
    11. **Quy 99.99:** Giá trị vàng tinh khiết tương ứng.
    12. **Ngày Xuất:** Ngày ghi nhận phiếu PXK.

---

## 3. THIẾT KẾ (UX/UI)
- Sử dụng Data Grid hỗ trợ:
    - **Export Excel:** Cho phép tải xuống danh sách vật tư chi tiết phục vụ báo cáo xuất kho.
    - **Sorting:** Cho phép sắp xếp theo Ngày xuất, Trọng lượng hoặc Mã Lô.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Dữ liệu tại đây phải đồng bộ và khớp 100% với dữ liệu tại bảng `Goods Issue Detail`.
- **BR-02:** Chế độ hiển thị: **Read-only**. Không hỗ trợ bất kỳ hành động Edit/Delete nào trên các record này vì vật tư đã xuất khỏi hệ thống tồn kho.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

*(Các trường dữ liệu được thừa hưởng và map từ cấu trúc Goods Issue Detail)*

| Tên trường (VN) | Tên trường (EN) | Data Type | Note |
|---|---|---|---|
| Mã phiếu xuất | Issue Code | Link | Hyperlink to US-37 |
| Lô | Lot | Text | Unique ID của dòng vật tư |
| Item | Item Code | Text | Mã hàng hóa |
| Loại xuất | Issue Type | Label | Kế thừa từ Header |
| Tuổi | Purity | Decimal(4,2) | Tuổi Seva |
| Kho xuất | Storage Location | Text | Kho - Zone - Location |
| TL tổng | Total Weight | Decimal(10,4) | Trọng lượng xuất |
| TL đá | Stone Weight | Decimal(10,4) | Trọng lượng xuất |
| TL kim loại | Metal Weight | Decimal(10,4) | Trọng lượng xuất |
| Quy 99.99 | 99.99 Equiv. | Decimal(10,4) | |

---

## 6. GHI CHÚ CHO QC
- Kiểm tra tính đồng nhất của số liệu xuất giữa màn hình Header (US-37) và màn hình Detail (US-38).
- Kiểm tra dữ liệu khi Export Excel xem có đẩy ra đầy đủ các cột và đúng định dạng số thập phân hay không.
- Verify tính năng link điều hướng (Hyperlink) từ cột Mã phiếu xuất có click được và mở đúng trang chi tiết hay không.
