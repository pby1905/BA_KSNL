# 🏷️ [CS1.E8.US-04] Tồn kho - Xem chi tiết Thẻ Kho (Stock Card View)

**Epic:** Tồn kho (CS1.E8)
**Actor:** Nhân viên MC (Material Control)

## 1. USER STORY
- **Là một:** Nhân viên MC.
- **Tôi muốn:** Xem chi tiết Thẻ kho (Stock Card) của một mã hàng/lô để theo dõi toàn bộ lịch sử các lần giao dịch tăng, giảm (Nhập/Xuất).
- **Để:** Kiểm soát được biến động tồn kho, đối chiếu chứng từ và nắm rõ số dư lũy kế (Running Balance) tại bất kỳ thời điểm nào trong quá khứ cho đến hiện tại.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Quản lý danh sách Thẻ kho đang mở (Sidebar)
- **Given:** Người dùng truy cập tính năng "Thẻ kho".
- **When:** Hệ thống hiển thị danh sách các Thẻ kho đang được mở (Left Sidebar).
- **Then:** 
    - Hiển thị tóm tắt: Mã hàng (VD: HJ-26520), Thuộc tính (RG-18K-01 Au 75.00 Y), và Tồn hiện tại.
    - Có chức năng "Ghim" (Pin - icon Ngôi sao) để đưa các thẻ kho ưu tiên lên đầu danh sách.
    - Khi click vào một thẻ kho bên trái, chi tiết thẻ kho sẽ load ở màn hình chính bên phải.

### AC2: Xem lịch sử giao dịch và số dư lũy kế
- **Given:** Người dùng đang xem chi tiết một Thẻ kho.
- **When:** Hệ thống render bảng danh sách giao dịch theo trình tự thời gian (từ cũ đến mới hoặc ngược lại tùy filter).
- **Then:**
    - Header hiển thị: Thông tin mã hàng, Số dư ban đầu (Opening Balance) và Tồn kho hiện tại (Current Balance).
    - Cột **Giao dịch**: Hiển thị loại (Nhập kho, Xuất kho).
    - Cột **Nguồn**: Nơi xuất phát hoặc đích đến (VD: Kho 102, Đồng bộ Finding, Loại reject).
    - Cột **SL (PC)**, **Chiều dài (M)**, **TL**: Hiển thị giá trị biến động của giao dịch đó (VD: +12, -1) và kèm theo **Số dư lũy kế** tại thời điểm đó nằm trong ngoặc đơn (VD: (12), (11)). Tất cả các ô này đều ở trạng thái Read-only.

### AC3: Chỉ cho phép xem (View-only)
- **Given:** Người dùng đang ở màn hình Thẻ kho.
- **When:** Người dùng cố gắng click hoặc chỉnh sửa các con số.
- **Then:** Các trường dữ liệu hoàn toàn bị khóa (Read-only), không cho phép chỉnh sửa trực tiếp. Không có nút "Cập nhật giao dịch" hay tính năng tự động cân bằng lại.

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- **Bố cục (Layout):** 
  - Giao diện chia 2 cột: Sidebar trái (khoảng 30%) cho danh sách Items, Khu vực phải (70%) cho chi tiết Thẻ kho.
- **Nút bấm:** "Đóng" (thoát khỏi màn hình). 

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01 (Chỉ đọc):** Màn hình Thẻ kho chỉ dùng để truy vấn lịch sử. Mọi nhu cầu điều chỉnh sai sót phải được thực hiện thông qua quy trình tạo Phiếu điều chỉnh (Inventory Adjustment) riêng biệt (Epic 9), hệ thống tuyệt đối không cho sửa trực tiếp trên thẻ kho để bảo vệ Audit Trail.
- **BR-02 (Tồn lũy kế):** Số dư lũy kế (Running Balance) phải được tính toán chính xác và khớp tuyệt đối với chênh lệch Tổng Nhập - Tổng Xuất tại mốc thời gian đó.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Mã Hàng | Item Code | Text | Read-only |
| Giao dịch | Transaction Type | Enum | Nhập / Xuất |
| Nguồn | Source / Destination | Text | Read-only |
| Số lượng (biến động) | Trans Qty | Integer | Read-only |
| Chiều dài (biến động) | Trans Length | Decimal(10,4) | Read-only |
| Trọng lượng (biến động) | Trans Weight | Decimal(10,4) | Read-only |
| Số dư lũy kế SL | Running Qty | Integer | Auto-calculate |
| Số dư lũy kế TL | Running Weight | Decimal(10,4) | Auto-calculate |
