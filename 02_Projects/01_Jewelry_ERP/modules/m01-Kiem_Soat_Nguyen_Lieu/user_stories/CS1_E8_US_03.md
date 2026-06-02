# 🏷️ [CS1.E8.US-03] Kho Hội - Quản lý Tồn Kho Hội (Alloy Inventory)

**Epic:** Tồn kho (CS1.E8)
**Actor:** Trưởng bộ phận Material Control, Kế toán, Thủ kho

## 1. USER STORY
- **Là một:** Nhân viên MC / Thủ kho Hội / Kế toán.
- **Tôi muốn:** Xem và quản lý danh sách tồn kho của các kim loại màu, phụ gia (Hội) dùng để pha trộn tuổi vàng.
- **Để:** Đảm bảo luôn có đủ vật tư phụ cho quá trình đúc, phân kim và kiểm soát hao hụt hội theo từng khu vực (Lưu trữ và Hàng ngày).

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Bộ lọc tìm kiếm (Filter)
- **Given:** Người dùng đang ở màn hình Tồn Kho Hội.
- **When:** Người dùng nhập các tiêu chí lọc:
    - **Tìm kiếm thông minh (Smart Search):** Mã Item, Tên hội (VD: Bạc, Đồng, Master Alloy 18K).
    - **Phân loại kho (Sub-inventory):**
        - Hội Lưu trữ (Kho tổng bảo mật)
            - AG/CU/STEEL/INOX
            - Phụ gia
        - Hội Hàng ngày (Kho tạm xuất dùng hàng ngày)
            - AG/CU/STEEL/INOX
            - Phụ gia
        - Hội chờ nhập / Hội chờ trả
- **Then:** Hệ thống hiển thị danh sách tồn kho hội thỏa mãn điều kiện.

### AC2: Danh sách tồn kho (Inventory Grid)
- **Then:** Dữ liệu hiển thị bao gồm các cột:
    1. **Mã Item:** (VD: ALLOY-AG-01).
    2. **Tên Hội:** (Bạc tinh khiết 999).
    3. **Khu vực kho:** (Lưu trữ / Hàng ngày).
    4. **Trọng lượng thực tế (On-hand Weight):** Gram/Kg.
    5. **Mức tồn tối thiểu (Min-Level):** Ngưỡng cảnh báo hết hàng.
    6. **Trạng thái cảnh báo:** (Đủ hàng, Cần bổ sung).
    7. **Hành động:** Nút "Lịch sử giao dịch" (Stock Card).

### AC3: Cảnh báo mức tồn tối thiểu (Min-Level Alert)
- **Given:** Hệ thống kiểm tra tồn kho hội định kỳ hoặc khi có giao dịch xuất.
- **When:** Trọng lượng thực tế của một Item trong **Kho Hàng ngày** giảm xuống dưới `Mức tồn tối thiểu`.
- **Then:** Hệ thống tự động highlight dòng item đó màu đỏ/cam và có thể gửi Notification cho Thủ kho báo cần làm lệnh **Điều chuyển nội bộ** từ Kho Lưu trữ sang Kho Hàng ngày.

### AC4: Ngăn chặn xuất âm (Negative Inventory Prevention)
- **Given:** Người dùng cố gắng thực hiện lệnh xuất kho hội hoặc cấp bù hội.
- **When:** Trọng lượng xuất yêu cầu lớn hơn trọng lượng **Tồn kho hiện tại**.
- **Then:** Hệ thống **chặn thao tác**, hiển thị thông báo lỗi: "Không thể xuất kho. Trọng lượng xuất vượt quá tồn kho hội hiện tại."

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

**Trạng thái View:**
- Component Table.
- Tính năng Group By (Gộp nhóm) theo loại Hội để xem tổng tồn ở cả 2 khu vực Lưu trữ và Hàng ngày.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Kho Hội được chia làm 2 cấp (Lưu trữ và Hàng ngày) nhằm hạn chế rủi ro an ninh do hội cũng là tài sản có giá trị (như Bạc). Lệnh cấp phát hàng ngày chỉ được lấy từ **Kho Hàng ngày**.
- **BR-02:** Tuyệt đối không cho phép tồn kho âm đối với Hội.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Mã Item | Item ID | Text | |
| Khu vực kho | Sub-Inventory | Enum | Lưu trữ / Hàng ngày |
| Tồn thực tế | On-hand Qty | Decimal(10,4) | |
| Mức tối thiểu | Min Level | Decimal(10,4) | Ngưỡng cảnh báo |
