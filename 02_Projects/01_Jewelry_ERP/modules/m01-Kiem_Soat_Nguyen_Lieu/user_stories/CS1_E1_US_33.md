# 🏷️ [CS1.E1.US-33] Mua NL - Tự động Tạo phiếu ASN (Kế hoạch nhận hàng) từ PO

**Epic:** Nhận nguyên liệu (CS1.E1)
**Actor:** Hệ thống (System Integration) / Trưởng bộ phận Mua hàng (Purchasing Manager)

## 1. USER STORY
- **Là một (As a):** Hệ thống ERP (System) hoặc Quản lý Mua hàng.
- **Tôi muốn (I want):** Hệ thống tự động khởi tạo Kế hoạch nhận hàng (Advanced Shipping Notice - ASN) tại phân hệ Kho ngay khi một Đơn đặt hàng (Purchase Order - PO) được phê duyệt (Approved).
- **Để (So that):** Đảm bảo luồng thông tin xuyên suốt từ lúc đặt hàng đến lúc nhận hàng, loại bỏ thao tác gửi email/thông báo thủ công, và cung cấp dữ liệu tức thời (real-time) cho bộ phận Kho để chuẩn bị tiếp nhận.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Kích hoạt tự động (Trigger Rule)
- **Given:** Một PO mua nguyên vật liệu vừa được duyệt (Status chuyển sang "Approved").
- **When:** Quá trình duyệt hoàn tất.
- **Then:** Hệ thống tự động sinh ra một bản ghi (Record) Kế hoạch nhận hàng (ASN) tương ứng tại phân hệ Kho (nơi được truy xuất bởi US-32 và US-32.1).
- **And:** Người dùng ở bộ phận Kho không cần thực hiện thêm bất kỳ thao tác nào để thấy được PO này trong danh sách chờ nhận.

### AC 2: Dữ liệu khởi tạo mặc định (Initial State)
- **Given:** ASN được tạo ra từ PO.
- **Then:** Trạng thái mặc định của ASN là **"Chờ nhận hàng" (Pending Receipt)**.
- **And:** Số lượng "Còn lại" (Open Qty) của mỗi mặt hàng (Item) trong ASN bằng chính xác "Số lượng đặt" (Ordered Qty) trên PO. Số lượng "Đã nhận" (Received Qty) khởi tạo bằng 0.

### AC 3: Xử lý khi Hủy (Cancel) PO từ Mua hàng
- **Given:** PO đã được duyệt và ASN đã sinh ra ở Kho.
- **And:** Kho **chưa** thực hiện bất kỳ phiếu nhập nào cho PO này (Received Qty = 0).
- **When:** Bộ phận Mua hàng quyết định Hủy (Cancel) PO đó.
- **Then:** Hệ thống tự động đổi trạng thái ASN bên Kho thành **"Đã hủy" (Cancelled)** hoặc ẩn khỏi danh sách "Chờ nhận hàng" để kho không tiếp nhận nhầm.

### AC 4: Khóa cập nhật khi đã bắt đầu nhận hàng
- **Given:** Kho đã tiếp nhận một phần (Partial Receipt) hàng hóa của PO (Received Qty > 0).
- **When:** Mua hàng cố gắng Sửa (Revise) hoặc Hủy (Cancel) PO.
- **Then:** Hệ thống báo lỗi và chặn hành động của Mua hàng: *"PO này đã bắt đầu được nhận hàng tại Kho. Không thể hủy hoặc sửa trực tiếp. Vui lòng liên hệ bộ phận Kho hoặc sử dụng quy trình xử lý ngoại lệ."*

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- **UX/UI:** Đây là một User Story dạng Hệ thống/Tích hợp (System Integration / Backend US). Do đó không có màn hình UI trực tiếp để "Tạo ASN". Giao diện là màn hình kết quả tại US-32 (Danh sách PO) và US-32.1 (Danh sách Item).
- **Kiến trúc Dữ liệu:** 
    - Có thể sử dụng chung Table `Purchase Orders` và filter bằng `Status` thay vì tạo Table vật lý riêng cho ASN (Tùy thuộc kiến trúc database ERP). Nếu tách table, cần đảm bảo Sync Data realtime.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)

- **BR-01:** Rule Mapping Tỉ lệ 1:1. Một PO chỉ sinh ra duy nhất một ASN Header.
- **BR-02:** Thay đổi ngày dự kiến giao (Expected Delivery Date): Nếu Purchasing có cập nhật ngày dự kiến giao (mà hệ thống cho phép sửa đổi khi chưa nhận hàng), thay đổi này phải lập tức được phản ánh (sync) sang ASN của Kho.
- **BR-03:** Phân luồng loại PO: Chỉ các PO thuộc loại "Mua nguyên liệu" hoặc "Gia công ngoài" (Subcontracting) có liên quan đến nhập kho vật tư mới được trigger tạo ASN vào phân hệ Quản lý Kho NL. Các PO dịch vụ (VD: thuê ngoài dọn dẹp, mua phần mềm) không sinh ASN tại đây.

---

## 5. BẢNG MAPPING TRƯỜNG DỮ LIỆU (DATA MAPPING: PO -> ASN)

Hệ thống sẽ thực hiện map tự động các trường sau:

| Trường trên Purchase Order (PO) | Trường trên Kế hoạch nhận hàng (ASN) | Ghi chú |
|---|---|---|
| PO Number (Mã PO) | Ref PO Number | Tham chiếu gốc |
| Vendor (Nhà cung cấp) | Vendor | |
| Expected Delivery Date | Expected Date | |
| Ordered Quantity (Line Item) | Ordered Qty | |
| *Không có* | Received Qty | Khởi tạo = 0 |
| *Không có* | Open Qty | Khởi tạo = Ordered Qty |
| Item Code / Name | Item Code / Name | |
| UoM (ĐVT) | UoM | |

---

## 6. GHI CHÚ CHO QC

- **Test Case Tích hợp:**
    1. Tạo 1 PO mới -> trạng thái Draft -> Kiểm tra màn hình ASN bên kho -> **Chưa thấy (Pass)**.
    2. Duyệt PO -> trạng thái Approved -> Kiểm tra lại màn hình ASN -> **Thấy PO và toàn bộ Item xuất hiện, trạng thái "Chờ nhận hàng" (Pass)**.
    3. Trả PO về nháp (hoặc Hủy PO) khi chưa nhận -> Kiểm tra màn hình ASN -> **PO biến mất khỏi lưới "Chờ nhận" (Pass)**.
    4. Cố tình nhập kho 1 phần cho PO đó, sau đó quay lại tab Mua hàng cố gắng Hủy PO -> **Hệ thống phải chặn (Block) và văng cảnh báo (Pass)**.
