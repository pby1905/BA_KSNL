# 🏷️ [CS1.E9.US-02] Kiểm kê kho - Nhập kết quả kiểm đếm thực tế (Enter Physical Count)

**Epic:** Kiểm kê kho & Điều chỉnh (CS1.E9)
**Actor:** Nhân viên MC, Thủ kho

## 1. USER STORY
- **Là một:** Nhân viên MC hoặc Thủ kho.
- **Tôi muốn:** Nhập số lượng/trọng lượng đếm thực tế vào phiếu kiểm kê thông qua màn hình máy tính hoặc quét mã vạch (Barcode/QR code).
- **Để:** Hệ thống ghi nhận số liệu thực tế tại kho.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Nhập liệu thủ công (Manual Entry)
- **Given:** Người dùng mở một Phiếu kiểm kê đang ở trạng thái `In Progress`.
- **When:** Hệ thống hiển thị danh sách các Lot/Item cần đếm.
- **Then:** Người dùng có thể nhập số liệu vào cột "Tồn thực tế" (Physical Qty) cho từng dòng. Hệ thống tự động lưu nháp dữ liệu.

### AC2: Nhập liệu bằng Barcode (Barcode Scanning)
- **Given:** Người dùng đang ở màn hình kiểm đếm.
- **When:** Người dùng dùng súng bắn mã vạch quét Barcode của một Lot/Bag.
- **Then:** Hệ thống tự động tìm đúng dòng Lot đó trong danh sách và highlight lên. Nếu là hàng đếm số lượng (Finding/Phụ kiện), mỗi lần quét cộng dồn +1, nếu là vàng (cân trọng lượng), focus vào ô nhập trọng lượng.

### AC3: Hoàn thành đếm
- **Given:** Người dùng đã nhập xong dữ liệu thực tế.
- **When:** Người dùng bấm "Xác nhận hoàn thành đếm".
- **Then:** Phiếu chuyển sang trạng thái `Reviewing`. Các giao dịch kho được mở khóa (unfreeze) nếu có cấu hình cho phép mở ngay sau khi đếm xong.

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- Giao diện dạng Data Grid (Bảng) tối ưu cho việc nhập liệu nhanh. Cột "Tồn thực tế" có thể Edit trực tiếp (Inline Edit).
- Tích hợp ô Input "Scan Barcode" luôn nổi ở trên cùng để thao tác quét nhanh.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Người nhập kết quả kiểm kê không được xem cột "Tồn sổ sách" (Blind count) nếu hệ thống cấu hình kiểm kê mù để đảm bảo tính khách quan (Tùy chọn cấu hình).
- **BR-02:** Có thể có nhiều nhân viên kho cùng truy cập 1 phiếu kiểm kê để nhập liệu đồng thời (Real-time sync).

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Mã Lot/Item | Lot/Item ID | Text | |
| Tồn thực tế | Physical Qty | Decimal(10,4) | > 0, cho phép nhập số lẻ với vàng |
| Ghi chú đếm | Count Note | Text | Lý do bất thường nếu thấy rõ bằng mắt |
