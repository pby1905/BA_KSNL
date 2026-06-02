# 🏷️ [CS1.E3.US-03] [Phiếu sửa hàng] - In nhãn phiếu sửa hàng

**Module:** Xử lý đơn hàng
**Epic:** Quản lý Phiếu sửa hàng
**Actor:** Nhân viên xử lý đơn hàng, Quản lý kho/cửa hàng

## 1. USER STORY
- **Là một (As a):** Nhân viên xử lý đơn hàng / Quản lý kho
- **Tôi muốn (I want):** In tem nhãn (Label/Tag) cho các Phiếu sửa hàng (Bag).
- **Để (So that):** Tôi có thể đính kèm tem nhãn này vào túi zip hoặc hộp đựng sản phẩm vật lý, giúp thợ sửa chữa dễ dàng nhận diện thông tin lỗi và để nhân viên có thể quét mã vạch (Barcode/QR Code) tracking trạng thái qua các công đoạn (Work Center).

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Kích hoạt chức năng in nhãn
- **Given (Biết rằng):** Người dùng đang ở màn hình "Danh sách Phiếu sửa hàng" hoặc màn hình "Chi tiết Phiếu sửa hàng".
- **When (Khi):** Người dùng bấm vào nút/icon **"In nhãn"** (Print Label) tại cột Action của một dòng Phiếu (hoặc chọn nhiều dòng rồi bấm "In nhãn hàng loạt").
- **Then (Thì):** Hệ thống hiển thị cửa sổ Print Preview (Xem trước bản in) với layout tem nhãn đã được thiết kế sẵn.
- **And (Và):** Người dùng có thể chọn máy in (Label printer) và số lượng bản in cho mỗi nhãn.

### AC 2: Nội dung hiển thị trên tem nhãn
- **Given (Biết rằng):** Cửa sổ Print Preview được mở.
- **Then (Thì):** Nhãn in phải bao gồm các thông tin tối thiểu sau:
  - **Mã vạch (Barcode) hoặc QR Code:** Mã hóa giá trị của `Mã phiếu (bag)` để phục vụ quét máy scan.
  - **Mã phiếu (Bag ID):** Hiển thị rõ dạng text bên dưới mã vạch.
  - **Mã hàng / Lô:** Định danh món hàng.
  - **Ghi chú lỗi:** Thông tin mô tả lỗi cần sửa (rất quan trọng cho thợ).
  - **Trọng lượng & Tuổi vàng:** TL Vàng, Tuổi vàng (nhằm kiểm soát hao hụt khi giao nhận thợ).
  - **Công đoạn định tuyến:** Ghi chú công đoạn / xưởng sẽ nhận.

### AC 3: Tương thích thiết bị in
- **Given (Biết rằng):** Hệ thống có kết nối với máy in tem nhãn (Thermal Label Printer - VD: Xprinter, Godex, Zebra...).
- **When (Khi):** Người dùng thực hiện lệnh in.
- **Then (Thì):** Nhãn được in ra đúng kích thước tiêu chuẩn đã cấu hình (ví dụ: tem trang sức 50x30mm, 72x22mm hoặc tem dán túi zip 70x50mm).
- **And (Và):** Mã vạch/QR Code in ra sắc nét, thiết bị quét mã vạch tiêu chuẩn của xưởng phải đọc được (Scannable).

---

## 3. THIẾT KẾ (UX/UI) & BỐ CỤC TEM NHÃN

**Gợi ý Bố cục tem nhãn (Label Layout):**
```text
+-----------------------------------------+
| SEVAGO JEWELRY - PHIẾU SỬA (BAG)        |
|                                         |
|  [     BARCODE / QR CODE IMAGE      ]   |
|  Bag ID: HS28010001                     |
|                                         |
| Mã Hàng: N36075 52    Lô: KH280101001   |
| TL Vàng: 1.2986       Tuổi: 6100 (Y)    |
| Lỗi: Hư khóa                            |
| Tuyến: Sản xuất -> Repair               |
+-----------------------------------------+
```
*(Lưu ý: Thiết kế UI sẽ căn chỉnh CSS hoặc File Report (.rpt / .jrxml) để vừa vặn với kích thước giấy in tem thực tế của dự án).*

---

## 4. BẢNG MAPPING TRƯỜNG DỮ LIỆU IN

| STT | Thông tin trên tem | Trường dữ liệu (Database/API) | Ghi chú / Format |
|---|---|---|---|
| 1 | Mã QR / Barcode | `bag_id` (Mã phiếu bag) | Generate dạng Code 128 (Barcode) hoặc QR Code |
| 2 | Bag ID (Text) | `bag_id` | Text |
| 3 | Mã hàng | `item_code` | Text |
| 4 | Mã Lô | `lot_id` | Text |
| 5 | TL Vàng & Tuổi | `gold_weight` & `gold_age` & `color` | Gom chung dòng cho tiết kiệm diện tích (VD: 1.29 - 6100 Y) |
| 6 | Ghi chú lỗi | `error_note` | Có thể cho phép tự động ngắt dòng nếu text quá dài |
| 7 | Routing / Công đoạn | `routing_path` hoặc `next_workcenter` | Nơi bag này sẽ được chuyển đến tiếp theo |

---

## 5. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01 (Tần suất in):** Một Phiếu sửa hàng (Bag) có thể được in lại tem nhãn nhiều lần (Reprint) trong trường hợp tem cũ bị rách, mờ hoặc mất trong quá trình luân chuyển. Không giới hạn số lần in.
- **BR-02 (Ràng buộc dữ liệu):** Chỉ có thể in nhãn khi Phiếu sửa hàng đã được tạo thành công trong hệ thống (đã có mã Bag ID).
- **BR-03 (Bảo mật thông tin):** Trên tem nhãn sửa chữa (giao cho xưởng/thợ) thường **không** hiển thị Tên Khách hàng trực tiếp để bảo mật thông tin nội bộ, thay vào đó dùng Mã Lô hoặc Mã Phiếu để tracking hệ thống. (Ngoại trừ trường hợp quy định riêng của team).
