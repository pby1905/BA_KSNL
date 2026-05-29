# 🏷️ [CS1.E1.US-35] Mua NL - Tạo phiếu tiếp nhận NL mua

**Epic:** Nhận nguyên liệu (CS1.E1)
**Actor:** Nhân viên Kho (Warehouse Staff)

## 1. USER STORY
- **Là một (As a):** Nhân viên Kho.
- **Tôi muốn (I want):** Tạo Phiếu tiếp nhận nguyên liệu mua từ nhà cung cấp, dựa trên dữ liệu kế thừa từ Đơn đặt hàng (PO / ASN).
- **Để (So that):** Ghi nhận chính xác số lượng thực tế nhận được, tự động đối trừ vào số lượng chờ nhận của PO, sinh mã lô (Lot) quản lý và đưa vật tư vào khu vực chờ kiểm tra chất lượng (QC) trước khi nhập kho chính thức.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Khởi tạo phiếu tiếp nhận & Auto-fill
- **Given:** Người dùng thao tác "Tiếp nhận" từ màn hình Chi tiết ASN (US-34) hoặc danh sách Item (US-32.1).
- **When:** Màn hình "Tạo phiếu tiếp nhận nguyên liệu mua" được hiển thị.
- **Then:** Hệ thống tự động điền (Auto-fill) các thông tin Header:
    - Nhà cung cấp.
    - Mã PO tham chiếu (Có link xem lại PO).
    - Ngày nhận (Mặc định là ngày hiện tại).
- **And:** Lưới chi tiết hàng hóa (Grid) tự động load các mặt hàng tương ứng đã chọn. Cột **"SL Nhận thực tế"** (Actual Qty) được gợi ý mặc định bằng với **"SL Còn lại"** (Open Qty) của PO để giảm thao tác gõ phím.

### AC 2: Ghi nhận thông tin giao hàng & Số lượng thực tế
- **When:** Người dùng kiểm đếm thực tế và cập nhật lại số liệu.
- **Then:** Người dùng có thể:
    - Nhập **Số chứng từ giao hàng** (Delivery Note / Packing List / Hóa đơn) của NCC cung cấp.
    - Chỉnh sửa lại **SL Nhận thực tế** tại từng dòng hàng cho khớp với kiểm đếm thực tế. (Có thể nhận ít hơn hoặc nhận đúng số lượng).
    - Nếu mặt hàng nào không giao đợt này, có thể xóa dòng đó khỏi lưới (Xóa khỏi phiếu nhận, PO không bị ảnh hưởng).

### AC 3: Giới hạn dung sai (Over-receipt Tolerance)
- **Given:** Người dùng nhập "SL Nhận thực tế" lớn hơn "SL Còn lại" trên PO (Nhận dư).
- **When:** Hệ thống kiểm tra rule nhận dư.
- **Then:**
    - Nếu tổng SL nhận (bao gồm các đợt trước) nằm trong giới hạn dung sai cho phép (VD: +5% cho vàng/bạc do sai số cân đo): Cho phép nhập và hiện cảnh báo màu cam.
    - Nếu vượt quá giới hạn dung sai: Hệ thống báo lỗi đỏ và chặn lưu phiếu. (Cần thông báo Purchasing sửa PO hoặc trả lại hàng).

### AC 4: Lưu nháp (Draft)
- **When:** Người dùng đang kiểm đếm dang dở, chưa chốt số cuối cùng và nhấn "Lưu nháp".
- **Then:** Phiếu được lưu ở trạng thái "Nháp" (Draft).
- **And:** "SL Còn lại" trên bảng gốc PO **chưa** bị trừ đi. Phiếu nháp có thể mở lên sửa tiếp sau.

### AC 5: Hoàn thành Phiếu (Complete Receipt)
- **When:** Người dùng nhấn "Hoàn thành".
- **Then:** Hệ thống chốt Phiếu tiếp nhận và sinh mã phiếu duy nhất (VD: PNNL-251001).
- **And:** Hệ thống tự động cập nhật lại bảng PO: Tăng "SL Đã nhận" (Received Qty) và Giảm "SL Còn lại" (Open Qty).
- **And:** Tự động sinh ra **Mã Lô (Lot/Batch ID)** cho từng dòng hàng vừa nhận thành công để theo dõi xuyên suốt trong hệ thống. (Tham chiếu cấu trúc mã Lô NL tại Phụ lục).

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- **Layout:** Kế thừa giao diện màn hình tạo Phiếu Tiếp Nhận Khách Hàng (US-01) nhưng có sự khác biệt về Header (thêm Supplier, PO Ref) và không có phần "Xác nhận bao bì khách báo" (Vì nhà cung cấp luôn giao kèm Delivery Note rõ ràng).
- **Cảnh báo trực quan:** Nếu "SL Nhận thực tế" < "SL Còn lại" (Nhận thiếu), dòng đó có icon/cảnh báo nhẹ (Information) để nhắc nhở người dùng rằng đợt này nhận thiếu so với dự kiến.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)

- **BR-01: Auto-Link**: Phiếu tiếp nhận nguồn "Mua hàng" bắt buộc phải có PO tham chiếu, không cho phép nhận hàng mua mà không có PO trên hệ thống.
- **BR-02: Trạng thái Tồn kho**: Hàng hóa sau khi hoàn thành phiếu tiếp nhận (Receiving) chưa được coi là Tồn kho khả dụng (Available Inventory). Nó sẽ nằm ở trạng thái **"Chờ kiểm định (In-QC)"** hoặc **"Khu vực nhận hàng (Receiving Dock)"**. Cần có bước Đo phổ / Kiểm tra tuổi / QC trước khi chính thức nhập kho (Sẽ mô tả ở US tiếp theo).
- **BR-03: Không cho phép sửa sau khi hoàn thành**: Sau khi Phiếu tiếp nhận chuyển sang trạng thái "Hoàn thành" và đã cập nhật số PO, nhân viên kho không được sửa hay xóa phiếu này. Mọi sai sót cần quy trình hủy phiếu (Cancel/Reverse Receipt) để hệ thống tự động hoàn lại (Rollback) số lượng cho PO gốc.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Required | Note |
|---|---|---|---|---|
| Mã phiếu | Receipt Code | Text | N/A | Tự động sinh sau khi Lưu/Hoàn thành. |
| Nhà cung cấp | Vendor | Link | Có | Kế thừa từ PO (Read-only). |
| PO Tham chiếu | PO Reference | Link | Có | Kế thừa từ hành động click. |
| Số CT giao hàng | Delivery Note No | Text | Không | User nhập từ chứng từ giấy NCC giao. |
| Ngày nhận | Receipt Date | Date/Time | Có | Mặc định Now. Cho phép lùi ngày (không được ở tương lai). |
| Ghi chú | Remarks | Text | Không | Các lưu ý thêm. |
| **BẢNG CHI TIẾT** | **LINE ITEMS** | | | |
| Mã Item / Tên | Item Code/Name | Label | Có | Từ PO sang. |
| ĐVT | UoM | Label | Có | Từ PO sang. |
| SL Còn lại (PO)| Open Qty | Decimal(10,4) | N/A | Read-only. Số lượng chờ nhận hiện tại. |
| SL Nhận thực tế | Actual Received Qty | Decimal(10,4) | Có | User nhập (Mặc định = Open Qty). |
| Lô sinh ra | Lot Number | Text | N/A | Tự sinh khi Hoàn thành. |

---

## 6. GHI CHÚ CHO QC

- **Test luồng Auto-fill:** Xác nhận việc click "Nhận toàn bộ" bên US-34 sẽ fill đủ số lượng dòng và số lượng thực tế bằng đúng với số lượng Còn lại.
- **Test Tolerance (Dung sai):** 
    - Nhận lớn hơn mức cho phép -> Verify hệ thống chặn (Error message).
    - Nhận bằng hoặc ít hơn -> Verify hệ thống cho lưu (Pass).
- **Test Cập nhật PO (Rollup):** Hoàn thành phiếu -> Mở lại màn hình chi tiết ASN (US-34) để kiểm tra cột "Đã nhận" và "Còn lại" có cộng/trừ đúng số học hay không.
- **Test Trạng thái:** Phiếu Nháp không ảnh hưởng số lượng PO. Phiếu Hoàn thành ảnh hưởng PO.
