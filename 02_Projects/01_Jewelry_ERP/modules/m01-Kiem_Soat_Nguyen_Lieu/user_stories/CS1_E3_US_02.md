# 🏷️ [CS1.E3.US-02] [Phiếu sửa hàng] - Danh sách Phiếu sửa

**Module:** Xử lý đơn hàng
**Epic:** Quản lý Phiếu sửa hàng
**Actor:** Nhân viên xử lý đơn hàng, Quản lý kho/cửa hàng

## 1. USER STORY
- **Là một (As a):** Nhân viên xử lý đơn hàng / Quản lý
- **Tôi muốn (I want):** Xem và quản lý danh sách các "Phiếu sửa hàng (Bag)" tương ứng với các sản phẩm/lô hàng cần sửa (được hệ thống tự động sinh ra từ Kế hoạch sản xuất).
- **Để (So that):** Tôi có thể theo dõi tiến độ sửa chữa, nắm bắt các công đoạn (Work Center - WC) và kiểm soát trạng thái xử lý của từng món/lô hàng sửa.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Xem danh sách Phiếu sửa hàng
- **Given (Biết rằng):** Người dùng có quyền truy cập vào menu "Xử lý đơn hàng" > "Phiếu sửa hàng".
- **When (Khi):** Người dùng truy cập vào màn hình.
- **Then (Thì):** Hệ thống hiển thị danh sách các Phiếu sửa hàng (Bags) đã được tự động tạo.
- **And (Và):** Màn hình cung cấp 3 Tab để phân loại nhanh:
  1. **Tất cả:** Hiển thị toàn bộ danh sách phiếu.
  2. **Hàng hỏi mới:** Chỉ hiển thị các phiếu thuộc phân loại hàng hỏi mới.
  3. **Hàng gửi sửa:** Chỉ hiển thị các phiếu thuộc phân loại hàng gửi sửa.
- **And (Và):** Danh sách được hiển thị dưới dạng bảng (Data table) có hỗ trợ phân trang (ví dụ: 20 dòng/trang).

### AC 2: Tìm kiếm và Lọc dữ liệu
- **Given (Biết rằng):** Người dùng đang ở màn hình Danh sách Phiếu sửa.
- **When (Khi):** Người dùng tương tác với thanh công cụ tìm kiếm và lọc.
- **Then (Thì):** Người dùng có thể thực hiện:
  - **Bộ lọc (Filter):** Nhấn vào nút "Bộ lọc" để mở rộng tiêu chí lọc.
  - **Tìm kiếm nhanh:** Theo từ khóa vào ô "Tìm kiếm mã phiếu nhập, nguồn...".
  - **Lọc theo ngày tạo:** Chọn ngày qua Date picker (VD: 13 01 2025).
  - **Lọc theo trạng thái:** Chọn từ dropdown "Tất cả trạng thái" (Chờ xuất, Đang xử lý, Hoàn Thành...).
  - **Làm mới dữ liệu:** Click icon Refresh.
  - **Cài đặt cột (Settings):** Bấm icon Settings để tùy chỉnh ẩn/hiện cột.

### AC 3: Các thao tác trên danh sách
- **Given (Biết rằng):** Người dùng đang xem bảng dữ liệu phiếu sửa hàng.
- **When (Khi):** Click vào Icon Action ở cột cuối.
- **Then (Thì):** Hệ thống cho phép hiển thị các tùy chọn hành động liên quan tới phiếu này, ví dụ: "Xem chi tiết", "In phiếu bag", "Lịch sử chuyển công đoạn" (tuỳ vào thiết kế UI chi tiết).

---

## 3. THIẾT KẾ (UX/UI) & HÀNH VI TƯƠNG TÁC
- **Header:** Breadcrumb `Xử lý đơn hàng > Phiếu sửa hàng`, các Tab phân loại (`Tất cả`, `Hàng hỏi mới`, `Hàng gửi sửa`).
- **Thanh công cụ (Toolbar):** Nút `Bộ lọc`, Ô tìm kiếm, `Ngày tạo` (Date picker), Dropdown `Tất cả trạng thái`, Nút `Settings` (cài đặt hiển thị cột), Nút `Refresh`. (Không có nút "Tạo phiếu" vì tự sinh).
- **Data Table:** 
  - Giao diện dạng list view chi tiết.
  - Cột trạng thái thể hiện rõ ràng qua định dạng Badge:
    - **Chờ xuất:** Chữ màu xanh dương, viền xanh dương.
    - **Đang xử lý:** Chữ màu vàng cam, viền vàng cam.
    - **Hoàn Thành:** Chữ màu xanh lá, viền xanh lá.

---

## 4. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| STT | Tên cột (VN) | Ý nghĩa / Ghi chú | Kiểu dữ liệu | Sortable |
|---|---|---|---|---|
| 1 | Mã phiếu (bag) | Mã định danh duy nhất của Phiếu sửa (Bag ID). Auto-generated từ KH SX. | Text | Có |
| 2 | Lô | Mã lô của sản phẩm | Text | Có |
| 3 | Phân loại | Phân loại hàng (Hàng hỏi mới, Hàng gửi sửa) | Text | Có |
| 4 | Mã hàng | Mã định danh của sản phẩm/món hàng | Text | Có |
| 5 | Số lượng | Số lượng món hàng trong bag | Number | Có |
| 6 | Tuổi | Tuổi vàng quy định (VD: 6100) | Number/Text | Có |
| 7 | Màu | Màu sắc vàng (VD: Y - Yellow, W - White) | Text | Có |
| 8 | TL tổng | Tổng trọng lượng sản phẩm | Decimal (4 số lẻ) | Có |
| 9 | TL đá | Trọng lượng đá | Decimal (4 số lẻ) | Có |
| 10 | TL đá trắng | Trọng lượng đá trắng | Decimal (4 số lẻ) | Có |
| 11 | TL vàng | Trọng lượng vàng nguyên chất (TL tổng - TL đá) | Decimal (4 số lẻ) | Có |
| 12 | Ghi chú lỗi | Mô tả tình trạng lỗi cần sửa (Hư khóa, Rớt chấu...) | Text | Không |
| 13 | Công đoạn (WC) | Hiển thị quá trình công đoạn hiện tại (VD: Sản xuất -> Repair...) | Text | Không |
| 14 | Trạng thái | Tình trạng hiện tại của Phiếu sửa (Chờ xuất, Đang xử lý, Hoàn Thành) | Badge | Có |
| 15 | `[Action]` | Icon tùy chọn các hành động trên dòng. | Button/Icon | Không |

---

## 5. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01 (Nguồn tạo phiếu):** Người dùng **không** được tạo thủ công Phiếu sửa hàng (Bag) từ màn hình này. Các Phiếu sửa (Bags) sẽ do hệ thống gen tự động ra từ **Kế hoạch sản xuất (Production Plan)**. Mỗi món/lô hàng cần sửa sẽ được đóng gói logic thành một Bag tương ứng với 1 Mã Phiếu.
- **BR-02 (Luồng công đoạn):** Trường `Công đoạn (WC)` sẽ hiển thị chuỗi định tuyến xử lý sửa chữa (Routing) mà Kế hoạch sản xuất đã chỉ định.
- **BR-03 (Cập nhật trạng thái):** 
  - **Chờ xuất:** Mặc định khi phiếu vừa gen ra, chờ Kho giao cho Thợ/Xưởng.
  - **Đang xử lý:** Khi đã xuất giao dịch đưa qua công đoạn Repair.
  - **Hoàn Thành:** Khi thợ sửa xong, trả lại và Nhập kho kiểm định đạt. (Các điều kiện cụ thể phụ thuộc luồng Routing xuất/nhập kho).
