# 🏷️ [CS1.E1.US-31] Nhận NL khách - Danh mục Vật tư Nhập Kho (Goods Receipt Item List)

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** NV tiếp nhận NL đầu vào

## 1. USER STORY
- **Là một:** Nhân viên Kho hoặc QC.
- **Tôi muốn:** Có một màn hình hiển thị danh sách chi tiết tất cả các dòng vật tư (Item/Lô) đã được nhập kho thành công.
- **Để:** Dễ dàng tra cứu thông tin kỹ thuật của từng lô hàng (trọng lượng, tuổi vàng, vị trí) mà không cần phải mở từng Phiếu nhập kho riêng lẻ.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Bộ lọc tìm kiếm chi tiết (Advanced Filter)
- **Given:** Người dùng đang ở màn hình Danh mục Vật tư Nhập Kho.
- **When:** Người dùng lọc theo các thuộc tính vật tư:
    - **Số Lô (LOT):** Search chính xác hoặc gần đúng mã Lô.
    - **Mã Item (SKU):** Lọc theo loại vật tư nguyên liệu.
    - **Nguồn:** L/G/P/S/R/C/H.
    - **Kho/Khu vực/Vị trí:** Dropdown phân cấp (Hierarchy).
    - **Tuổi vàng:** Khoảng giá trị (VD: Tuổi từ 74.5 đến 75.1).
- **Then:** Hệ thống hiển thị danh sách các Record vật tư con.

### AC2: Lưới dữ liệu vật tư (Item/Lot Grid)
- **Then:** Bảng dữ liệu hiển thị (Thừa hưởng cấu trúc từ **Bảng Tồn Kho** trong US-16):
    1. **Mã Phiếu (PNK):** (Click vào sẽ điều hướng về chi tiết phiếu US-30).
    2. **Lô (LOT):** Mã lô duy nhất của dòng hàng.
    3. **Item:** Mã nguyên liệu.
    4. **Kho/Khu vực/Vị trí:** Nơi lưu trữ hiện tại.
    5. **Tuổi:** Tuổi Seva.
    6. **Số lượng (Qty):** Chỉ hiện nếu TrackMode có `Q`.
    7. **Trọng lượng tổng (Total Weight):** Decimal(10,4).
    8. **TL Đá (Stone Weight):** Decimal(10,4).
    9. **TL Kim loại (Metal Weight):** Decimal(10,4).
    10. **Quy 99.99:** Giá trị vàng tinh khiết tương ứng.
    11. **Ngày Nhập:** Ngày phiếu PNK được tạo.

---

## 3. THIẾT KẾ (UX/UI)
- Sử dụng Data Grid hỗ trợ:
    - **Export Excel:** Cho phép tải xuống danh sách vật tư chi tiết để làm báo cáo kiểm kê.
    - **Sorting:** Cho phép sắp xếp theo Trọng lượng hoặc Mã Lô.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Dữ liệu tại đây phải khớp 100% với dữ liệu tại bảng `Goods Receipt Detail`.
- **BR-02:** Chế độ hiển thị: **Read-only**. Không hỗ trợ bất kỳ hành động Edit/Delete nào trên các record này.

---

## 5. BẢNG ĐÌNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

*(Các trường dữ liệu tương tự như Phụ lục B - Từ điển trường dữ liệu)*

| Tên trường (VN) | Tên trường (EN) | Data Type | Note |
|---|---|---|---|
| Mã phiếu | Receipt Code | Link | Link to US-30 |
| Lô | Lot | Text | Unique ID |
| Tuổi | Purity | Decimal(4,2) | Tuổi Seva |
| TL tổng | Total Weight | Decimal(10,4) | |
| TL đá | Stone Weight | Decimal(10,4) | |
| TL | Metal Weight | Decimal(10,4) | |
| Quy 99.99 | 99.99 Equiv. | Decimal(10,4) | |

---

## 6. GHI CHÚ CHO QC
- Kiểm tra tính đồng nhất của số liệu giữa màn hình Header (US-30) và tổng Record Detail (US-31).
- Verify việc ẩn hoàn toàn các cột Công nợ để đảm bảo bảo mật thông tin phí/giá.
- Kiểm tra link điều hướng từ Mã phiếu về Header.
