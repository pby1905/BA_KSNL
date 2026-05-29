# 🏷️ [CS1.E1.US-34] Mua NL - Chi tiết ASN (Kế hoạch nhận hàng)

**Epic:** Nhận nguyên liệu (CS1.E1)
**Actor:** Nhân viên Kho (Warehouse Staff)

## 1. USER STORY
- **Là một (As a):** Nhân viên Kho hoặc Quản lý Kho.
- **Tôi muốn (I want):** Xem thông tin chi tiết của một Kế hoạch nhận hàng (ASN) cụ thể, bao gồm thông tin chung (Header) của đơn đặt hàng và danh sách toàn bộ các vật tư (Line Items) thuộc PO đó.
- **Để (So that):** Nắm bắt toàn bộ bối cảnh của chuyến hàng từ nhà cung cấp, chuẩn bị vị trí lưu kho, đối chiếu tổng thể với chứng từ giao nhận (Delivery Note / Packing List) của nhà cung cấp và có thể thao tác nhận hàng hàng loạt (Receive All) một cách tiện lợi.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Hiển thị Thông tin chung (Header Information)
- **Given:** Người dùng click vào một "Mã PO" bất kỳ trên màn hình "Danh sách PO chờ nhận" (US-32).
- **When:** Hệ thống điều hướng sang màn hình "Chi tiết ASN".
- **Then:** Phần trên cùng (Header Panel) hiển thị thông tin tổng quan của PO, bao gồm:
    - Mã PO (PO Number).
    - Tên và Mã Nhà cung cấp (Vendor Info).
    - Ngày đặt hàng (PO Date) và Ngày dự kiến giao tổng thể (Expected Date).
    - Người phụ trách mua hàng (Buyer).
    - Trạng thái nhận hàng hiện tại (Chờ nhận / Nhận một phần / Hoàn tất).

### AC 2: Tab "Vật tư chờ nhận" (Pending Items Grid)
- **Then:** Bên dưới phần Header là khu vực Tab. Tab mặc định là **"Vật tư chờ nhận"**.
- **And:** Hiển thị danh sách các vật tư (Lines) thuộc PO này. Cột hiển thị gồm:
    - STT, Mã Item, Tên Item, ĐVT.
    - **SL Đặt (Ordered):** Số lượng gốc trên PO.
    - **Đã nhận (Received):** Số lượng đã tiếp nhận thành công.
    - **Còn lại (Open/Pending):** Mức chênh lệch.
    - **Ngày dự kiến giao (Line Date):** Nếu PO có chia nhiều đợt giao cho các mặt hàng khác nhau.
- **And:** Chỉ hiển thị các dòng có **SL Còn lại > 0** hoặc có tuỳ chọn (toggle) để xem tất cả bao gồm cả dòng đã nhận xong.

### AC 3: Tương tác "Tiếp nhận" (Receive Actions)
- **When:** Người dùng cần khởi tạo phiếu nhập kho từ màn hình Chi tiết ASN.
- **Then:** Cung cấp 2 lựa chọn thao tác:
    - **Nhận hàng loạt (Receive All):** Nút nằm ở góc phải Header. Nhấn vào sẽ đẩy toàn bộ các dòng Item có "Còn lại > 0" sang màn hình Tạo Phiếu Nhập Kho.
    - **Nhận hàng từng phần (Partial Select):** Checkbox ở đầu mỗi dòng Item. Nhấn nút "Tiếp nhận các mục đã chọn" để đẩy riêng các mặt hàng thực tế được giao vào Phiếu Nhập Kho.

### AC 4: Tab "Lịch sử nhận hàng" (Receipt History)
- **Given:** Kế hoạch nhận hàng (PO) này có thể giao làm nhiều đợt (Partial deliveries).
- **When:** Người dùng chuyển sang tab **"Lịch sử nhận hàng"**.
- **Then:** Hệ thống liệt kê tất cả các Phiếu Nhập Kho (Goods Receipt) đã được tạo và liên kết thành công với mã PO này.
- **And:** Hiển thị các thông tin: Mã Phiếu nhập, Ngày tạo phiếu, Người nhận hàng, Trạng thái phiếu nhập (Đang xử lý / Hoàn thành), và có link bấm vào để xem chi tiết từng Phiếu Nhập Kho.

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- **Layout:** Sử dụng cấu trúc Master-Detail. Header hiển thị dạng Card (Read-only). Bên dưới là Tabs (Pending Items & Receipt History).
- **Phân biệt trực quan:** Sử dụng Progress Bar (Thanh tiến trình) tại Header để thể hiện trực quan "% Hoàn thành nhận hàng" của toàn bộ PO (tính theo tổng số lượng hoặc tổng dòng).
- **Sticky Header:** Phần Header Info nên được ghim (sticky) khi cuộn chuột qua danh sách Item dài để người dùng không bị mất ngữ cảnh của Nhà cung cấp.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)

- **BR-01: Quyền truy cập (Read-only)**: Tại màn hình này, nhân viên kho chỉ có quyền **Xem** thông tin PO. Không được phép chỉnh sửa Nhà cung cấp, Item, hoặc Số lượng đặt. Mọi thay đổi phải được thực hiện tại phân hệ Mua hàng (Purchasing) bởi người có thẩm quyền.
- **BR-02: Đóng ASN (Auto-Close)**: Nếu tổng số lượng "Còn lại" (Open Qty) của tất cả các dòng Item bằng `0`, trạng thái ASN tự động chuyển thành **"Hoàn tất" (Fully Received)**. Các nút hành động "Tiếp nhận" sẽ tự động bị ẩn hoặc disable.
- **BR-03: Xử lý Hủy (Cancel)**: Nếu PO bị hủy bên Mua hàng (theo AC3 của US-33), màn hình chi tiết ASN này sẽ hiển thị cảnh báo Banner màu đỏ: *"PO này đã bị hủy. Vui lòng không thực hiện tiếp nhận hàng hóa."* và disable các nút Tiếp nhận.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

*(Phần Header)*
| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Note |
|---|---|---|---|
| Mã PO | PO Number | Text | |
| Nhà cung cấp | Vendor | Text | Tên & Mã đối tác |
| Ngày đặt | PO Date | Date | |
| Ngày dự kiến giao | Expected Date | Date | Ngày giao hàng tổng thể của PO |
| Người phụ trách mua | Buyer | Text | Tên nhân viên Mua hàng để liên hệ khi có sự cố |
| Tiến độ | Progress | % | Tự động tính |

*(Phần Receipt History Tab)*
| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Note |
|---|---|---|---|
| Mã phiếu nhập | Receipt Code | Link | Link tới US-30 / US-16 |
| Ngày nhập | Receipt Date | Date/Time | |
| Người nhận | Received By | Text | User Kho |
| Trạng thái phiếu | Status | Label | |

---

## 6. GHI CHÚ CHO QC

- **Kiểm tra Tab Lịch sử:**
    - Tạo PO -> Mở Chi tiết ASN -> Tab Lịch sử phải rỗng.
    - Thực hiện "Tiếp nhận" 1 phần -> Lưu phiếu Nhập Kho -> Quay lại màn hình này, kiểm tra Tab lịch sử xem mã Phiếu Nhập Kho đã xuất hiện đúng chưa.
- **Kiểm tra Nút Nhận hàng loạt (Receive All):** Bấm "Receive All", kiểm tra màn hình Tạo phiếu nhập kho có tự động load đủ tất cả các line item có Open Qty > 0 hay không.
- **Kiểm tra Auto-Close:** Nhận hàng đủ 100% số lượng, quay lại xem ASN có đổi sang "Hoàn tất" và mất nút "Tiếp nhận" hay không.
