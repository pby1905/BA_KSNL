# 🏷️ [CS1.E1.US-32] Mua NL - Xem danh sách PO chờ nhận (ASN)

**Epic:** Nhận nguyên liệu (CS1.E1)
**Actor:** Nhân viên Kho (Warehouse Staff), Trưởng bộ phận Material Control

## 1. USER STORY
- **Là một (As a):** Nhân viên Kho hoặc Quản lý kho.
- **Tôi muốn (I want):** Xem danh sách các Đơn đặt hàng mua nguyên liệu (Purchase Order - PO) đã được duyệt và đang trong trạng thái chờ nhận hàng (Kế hoạch nhận hàng - ASN).
- **Để (So that):** Nắm bắt được kế hoạch vật tư/nguyên liệu sắp về kho, chuẩn bị không gian/nguồn lực tiếp nhận, và có thể nhanh chóng tạo Phiếu tiếp nhận dựa trên thông tin PO khi nhà cung cấp giao hàng.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Bộ lọc tìm kiếm kế hoạch nhận hàng (Filter)
- **Given:** Người dùng truy cập vào màn hình "Kế hoạch nhận hàng (ASN)".
- **When:** Người dùng nhập các tiêu chí lọc:
    - **Tìm kiếm thông minh (Smart Search):** Tìm theo Mã PO (VD: `PO-2510001`), Mã hoặc Tên Nhà Cung Cấp (Vendor).
    - **Nhà cung cấp (Vendor):** Search select theo danh sách nhà cung cấp hệ thống.
    - **Trạng thái nhận hàng:** Mặc định chọn "Chờ nhận hàng" (Pending) và "Nhận một phần" (Partial Receipt). Có thể chọn thêm "Hoàn tất" (Fully Received) để xem lịch sử nếu cần.
    - **Khoảng thời gian:** Lọc theo "Ngày dự kiến giao" (Expected Delivery Date) - Từ ngày... Đến ngày...
- **Then:** Hệ thống hiển thị danh sách các PO thỏa mãn điều kiện tìm kiếm.

### AC 2: Hiển thị danh sách PO chờ nhận (ASN Grid)
- **Then:** Dữ liệu trong bảng danh sách hiển thị các cột:
    1. **Mã PO:** Link click để xem chi tiết PO (Read-only).
    2. **Nhà cung cấp:** Tên/Mã Vendor.
    3. **Ngày đặt hàng:** Ngày bộ phận Mua hàng (Purchasing) tạo PO.
    4. **Ngày dự kiến giao:** Thời gian theo kế hoạch giao hàng.
    5. **Tổng trọng lượng/Số lượng đặt:** Trọng lượng hoặc số lượng tổng cộng trên PO.
    6. **Tiến độ nhận:** Trạng thái (Ví dụ: Chưa nhận / Đã nhận 50%).
    7. **Hành động:** Nút **"Tiếp nhận"** (Receive).

### AC 3: Khởi tạo phiếu tiếp nhận từ PO
- **Given:** Người dùng tìm thấy PO cần nhận hàng trong danh sách.
- **When:** Người dùng nhấn nút **"Tiếp nhận"** trên dòng tương ứng.
- **Then:** Hệ thống điều hướng người dùng sang màn hình "Tạo phiếu tiếp nhận NL" (hoặc Tạo Phiếu Nhập Kho).
- **And:** Hệ thống **tự động điền (auto-fill)** các thông tin từ PO sang phiếu tiếp nhận mới (bao gồm: Nhà cung cấp, danh sách các vật tư/Item cần nhận, số lượng dự kiến) để giảm thiểu thao tác nhập liệu thủ công.

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- **Trạng thái View:** 
    - Giao diện Table Data Grid có hỗ trợ Pagination.
    - Nổi bật các dòng PO quá hạn giao hàng (Expected Date < Current Date) bằng màu cảnh báo (Ví dụ: Chữ đỏ hoặc highlight nền vàng nhạt) để kho chủ động đôn đốc.
- **Tương tác:** Nút "Tiếp nhận" là Call-to-Action (CTA) chính yếu trên mỗi dòng.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)

- **BR-01:** Chỉ hiển thị các PO đã ở trạng thái **Đã duyệt (Approved)** từ phân hệ Mua hàng (Purchasing). Các PO nháp hoặc đang chờ duyệt sẽ không xuất hiện tại đây.
- **BR-02:** Quyền dữ liệu: Nhân viên kho chỉ có quyền **Xem (Read-only)** thông tin nội dung của PO, không được phép chỉnh sửa giá cả, số lượng đặt hay thông tin nhà cung cấp trên PO.
- **BR-03:** Các PO có trạng thái "Đã nhận đủ" (Fully Received) hoặc "Đã hủy" (Cancelled) sẽ không hiển thị mặc định, trừ khi người dùng chủ động đổi bộ lọc trạng thái.
- **BR-04:** Chặn hiển thị thông tin nhạy cảm: Có thể cấu hình ẩn các cột liên quan đến "Đơn giá mua" (Unit Price) hoặc "Tổng tiền" (Total Amount) đối với user là Nhân viên kho nếu có yêu cầu bảo mật từ hệ thống.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation / Ghi chú |
|---|---|---|---|
| Mã PO | PO Number | Link | Link tham chiếu xem chi tiết PO. |
| Nhà cung cấp | Vendor | Text | Lấy từ danh mục Supplier. |
| Ngày đặt hàng | PO Date | Date | |
| Ngày dự kiến giao | Expected Date | Date | Thời gian dự kiến NCC giao hàng tới kho. |
| Tổng số lượng đặt | Total Ordered Qty| Decimal(10,4)| Tổng trọng lượng (Weight) hoặc số lượng (Pieces). |
| Tiến độ nhận | Receiving Status | Label | Trạng thái: Pending, Partial, Fully Received. |
| Quá hạn | Overdue Flag | Boolean | Hệ thống tự tính: `True` nếu Expected Date < Today. |

---

## 6. GHI CHÚ CHO QC

- Kiểm tra luồng tích hợp (Integration Test): Tạo 1 PO từ bộ phận Mua hàng, duyệt PO đó và xác nhận PO xuất hiện chính xác bên màn hình ASN của Kho.
- Kiểm tra tính năng "Tự động điền": Bấm "Tiếp nhận", kiểm tra xem dữ liệu trên form tạo phiếu nhập kho mới có map đúng 1-1 với dữ liệu của PO hay không.
- Verify bộ lọc trạng thái mặc định chỉ hiện PO chưa hoàn tất nhận hàng.
