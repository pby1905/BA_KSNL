# 🏷️ [CS1.E9.US-03] Kiểm kê kho - Báo cáo chênh lệch kiểm kê (Variance Report)

**Epic:** Kiểm kê kho & Điều chỉnh (CS1.E9)
**Actor:** Trưởng bộ phận MC (TBP MC), Kế toán

## 1. USER STORY
- **Là một:** TBP MC hoặc Kế toán.
- **Tôi muốn:** Xem báo cáo đối chiếu giữa Tồn sổ sách và Tồn thực tế sau khi nhân viên đã hoàn thành đếm.
- **Để:** Phát hiện các khoản chênh lệch (thừa/thiếu) và quyết định yêu cầu đếm lại (Recount) hoặc tiến hành điều chỉnh tồn kho.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Tính toán chênh lệch tự động
- **Given:** Phiếu kiểm kê ở trạng thái `Reviewing`.
- **When:** Người dùng mở chi tiết phiếu.
- **Then:** Hệ thống hiển thị bảng so sánh gồm:
    - Tồn sổ sách (Snapshot Qty)
    - Tồn thực tế (Physical Qty)
    - Số lượng chênh lệch (Variance Qty = Physical - Snapshot)
    - Tỷ lệ chênh lệch (%)

### AC2: Lọc dữ liệu chênh lệch
- **Given:** Người dùng ở màn hình Báo cáo chênh lệch.
- **When:** Người dùng chọn bộ lọc "Chỉ hiển thị có chênh lệch".
- **Then:** Hệ thống ẩn các dòng khớp số liệu (Variance = 0) và highlight màu Đỏ cho các dòng Thiếu (Variance < 0), Xanh cho dòng Thừa (Variance > 0).

### AC3: Yêu cầu đếm lại (Recount)
- **Given:** Phát hiện chênh lệch lớn ở một vài Lot.
- **When:** Người dùng chọn các Lot đó và bấm "Yêu cầu đếm lại".
- **Then:** Trạng thái Lot trở về "Cần đếm lại" và thông báo cho Nhân viên kho đi kiểm tra lại.

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- Giao diện Báo cáo (Report View) tập trung vào phân tích dữ liệu, có tính năng Export ra Excel/PDF để ký tá.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Chỉ những Lot/Item có chênh lệch sau khi chốt đếm lại mới được phép đẩy sang quy trình tạo Phiếu điều chỉnh.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Tồn sổ sách | Snapshot Qty | Decimal | |
| Tồn thực tế | Physical Qty | Decimal | |
| Chênh lệch | Variance Qty | Decimal | Công thức: Physical - Snapshot |
| Tỷ lệ chênh lệch | Variance Pct | Decimal | Công thức: (Variance / Snapshot) * 100 |
