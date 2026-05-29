# 🏷️ [CS1.E3.US-01] [Phiếu sửa hàng] - Danh sách thành phẩm chờ sửa

**Module:** Xử lý đơn hàng
**Epic:** Quản lý hàng chờ xử lý
**Actor:** Nhân viên xử lý đơn hàng, Quản lý kho/cửa hàng

## 1. USER STORY
- **Là một (As a):** Nhân viên xử lý đơn hàng / Quản lý
- **Tôi muốn (I want):** Xem và quản lý danh sách "Hàng chờ xử lý" bao gồm các thành phẩm đã tiếp nhận đang chờ sửa chữa (hàng hỏi mới, hàng gửi sửa).
- **Để (So that):** Tôi có thể theo dõi chi tiết tình trạng các sản phẩm, thực hiện tìm kiếm và lọc dữ liệu (Phiếu sửa sẽ được tự động tạo từ Kế hoạch sản xuất).

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Xem danh sách Hàng chờ xử lý
- **Given (Biết rằng):** Người dùng có quyền truy cập vào menu "Xử lý đơn hàng" > "Hàng chờ xử lý".
- **When (Khi):** Người dùng truy cập vào màn hình.
- **Then (Thì):** Hệ thống hiển thị danh sách các thành phẩm đang ở trạng thái chờ xử lý.
- **And (Và):** Màn hình cung cấp 3 Tab để phân loại nhanh:
  1. **Tất cả:** Hiển thị toàn bộ danh sách.
  2. **Hàng hỏi mới:** Chỉ hiển thị các sản phẩm phân loại là hàng hỏi mới.
  3. **Hàng gửi sửa:** Chỉ hiển thị các sản phẩm phân loại là hàng gửi sửa.
- **And (Và):** Danh sách được hiển thị dưới dạng bảng (Data table) có hỗ trợ phân trang (ví dụ: 20 dòng/trang).

### AC 2: Tìm kiếm và Lọc dữ liệu
- **Given (Biết rằng):** Người dùng đang ở màn hình Danh sách Hàng chờ xử lý.
- **When (Khi):** Người dùng sử dụng thanh công cụ phía trên danh sách.
- **Then (Thì):** Người dùng có thể thực hiện các thao tác:
  - **Bộ lọc (Filter):** Nhấn vào nút "Bộ lọc" để mở rộng các tiêu chí lọc nâng cao.
  - **Tìm kiếm nhanh:** Nhập từ khóa vào ô "Tìm kiếm mã phiếu nhập, nguồn..." để tìm kiếm tương đối (Search by keyword).
  - **Lọc theo ngày:** Chọn ngày/khoảng ngày tại ô "Ngày tạo" (Mặc định có thể là ngày hiện tại hoặc chọn cụ thể, VD: 13 01 2025).
  - **Lọc theo trạng thái:** Chọn trạng thái từ dropdown "Tất cả trạng thái" (VD: Chờ xử lý, Đang xử lý...).
  - **Nút Refresh:** Bấm vào icon reload để làm mới dữ liệu danh sách.

### AC 3: Tự động tạo phiếu sửa từ Kế hoạch sản xuất
- **Ghi chú:** Tại màn hình này không có chức năng tạo phiếu sửa thủ công.
- Các "Phiếu sửa" sẽ được hệ thống tự động sinh ra dựa trên **Kế hoạch sản xuất** (Production Plan).
- Khi phiếu sửa được tạo, trạng thái của các sản phẩm tương ứng trong danh sách sẽ tự động được cập nhật.
---

## 3. THIẾT KẾ (UX/UI) & HÀNH VI TƯƠNG TÁC
- Giao diện chia làm 3 phần chính:
  1. **Header:** Breadcrumb `Xử lý đơn hàng > Hàng chờ xử lý`, các Tab phân loại (`Tất cả`, `Hàng hỏi mới`, `Hàng gửi sửa`).
  2. **Thanh công cụ (Toolbar):** Bộ lọc, Ô tìm kiếm, Date picker, Trạng thái, Nút `Refresh`, Nút `Export/Cài đặt cột`.
  3. **Bảng dữ liệu (Data Table):** Hiển thị chi tiết thông tin theo cấu trúc cột định nghĩa bên dưới. Có checkbox chọn từng dòng hoặc chọn tất cả (phục vụ export hoặc view).

---

## 4. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| STT | Tên cột (VN) | Ý nghĩa / Ghi chú | Kiểu dữ liệu | Sortable |
|---|---|---|---|---|
| 1 | `[Checkbox]` | Cho phép chọn 1 hoặc nhiều dòng (phục vụ thao tác export hoặc view nếu có) | Boolean | Không |
| 2 | Lô | Mã lô của sản phẩm | Text | Có |
| 3 | Phân loại | Phân loại hàng (Hàng hỏi mới, Hàng gửi sửa) | Badge/Text | Có |
| 4 | Mã hàng | Mã định danh của sản phẩm | Text | Có |
| 5 | Số lượng | Số lượng món hàng | Number | Có |
| 6 | Tuổi | Tuổi vàng quy định (VD: 6100) | Number/Text | Có |
| 7 | Màu | Màu sắc vàng (VD: Y - Yellow, W - White) | Text | Có |
| 8 | TL tổng | Tổng trọng lượng sản phẩm | Decimal (4 số lẻ) | Có |
| 9 | TL đá | Trọng lượng đá | Decimal (4 số lẻ) | Có |
| 10 | TL đá trắng | Trọng lượng đá trắng | Decimal (4 số lẻ) | Có |
| 11 | TL vàng | Trọng lượng vàng nguyên chất (TL tổng - TL đá) | Decimal (4 số lẻ) | Có |
| 12 | Ghi chú lỗi | Mô tả tình trạng lỗi cần sửa (VD: Hư khóa, Hư lacquer, Rớt thêm cast, Thay chấu...) | Text | Không |
| 13 | Khách hàng | Mã/Tên khách hàng hoặc nguồn gửi (VD: PNJ, K.SAO, TOAN...) | Text | Có |
| 14 | Tiền công 1 bọc | Đơn giá tiền công sửa chữa dự kiến cho 1 đơn vị | Currency | Có |
| 15 | Tiền công tổng | Tổng tiền công = (Tiền công 1 bọc * Số lượng) | Currency | Có |
| 16 | Mã bag Sevago | Mã túi chứa hàng (Barcode/QR code) | Text | Có |
| 17 | `[Action]` | Icon Xem chi tiết (kính lúp) để xem thông tin đầy đủ của dòng hàng. | Button/Icon | Không |

---

## 5. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Các sản phẩm trong danh sách này sẽ được hệ thống tự động nhóm và tạo thành Phiếu Sửa dựa trên **Kế hoạch sản xuất**. Khi sản phẩm đã thuộc một phiếu sửa (chuyển sang trạng thái Đang xử lý/Đã tạo phiếu), hệ thống sẽ tự động cập nhật trạng thái và loại bỏ khỏi view "Chờ xử lý".
- **BR-02:** Việc tính toán TL Vàng: `TL Vàng = TL tổng - TL đá - TL đá trắng` (Tuỳ theo công thức quy định cụ thể, có thể hệ thống tự động tính và view lên đây).
- **BR-03:** Tiền công tổng: `Tiền công tổng = Số lượng * Tiền công 1 bọc` (nếu tính theo món) hoặc theo trọng lượng tùy thuộc vào logic tính giá.
