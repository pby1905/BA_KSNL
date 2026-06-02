# 🏷️ [CS1.E3.US-05] [Phiếu sửa hàng] - Phiếu trả thành phẩm chờ sửa

**Module:** Xử lý đơn hàng
**Epic:** Quản lý Phiếu sửa hàng
**Actor:** Nhân viên xử lý đơn hàng, Quản lý kho

## 1. USER STORY
- **Là một (As a):** Nhân viên xử lý đơn hàng / Quản lý kho
- **Tôi muốn (I want):** Tạo Phiếu trả hàng cho các sản phẩm nằm trong "Danh sách thành phẩm chờ sửa" nhưng không thể hoặc không cần thực hiện sửa chữa nữa.
- **Để (So that):** Tôi có thể xuất trả vật lý sản phẩm đó về đúng nguồn (khách hàng hoặc kho), loại bỏ chúng khỏi danh sách chờ sửa và in nhãn/phiếu trả phục vụ luân chuyển hàng hóa.

> **Ngữ cảnh:** Tại màn hình "Danh sách thành phẩm chờ sửa" (CS1.E3.US-01), có những trường hợp sản phẩm bị đánh giá là không thể sửa, lỗi không đáng có, hoặc khách hàng đổi ý hủy yêu cầu sửa. Nhân viên cần một cơ chế để "Trả lại" (Return) những sản phẩm này thay vì nhóm chúng vào Bag sửa chữa (US-02). Sau khi tạo Phiếu trả, nhân viên có thể in tem nhãn trả hàng (liên quan đến CS1.E3.US-03) để dán lên sản phẩm gửi về.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Chọn sản phẩm cần trả từ Danh sách chờ sửa
- **Given (Biết rằng):** Người dùng đang ở màn hình Danh sách "Hàng chờ xử lý" (CS1.E3.US-01).
- **When (Khi):** Người dùng tick chọn một hoặc nhiều dòng sản phẩm có trạng thái "Chờ xử lý".
- **And (Và):** Người dùng bấm nút **"Trả hàng"** (Return) trên thanh công cụ (Toolbar).
- **Then (Thì):** Hệ thống hiển thị Modal/Popup **"Tạo Phiếu trả thành phẩm chờ sửa"**.
- **And (Và):** Modal liệt kê danh sách các sản phẩm đã được chọn (Read-only: Mã hàng, Lô, Số lượng, TL Vàng, Ghi chú lỗi gốc).

### AC 2: Nhập thông tin Phiếu trả
- **Given (Biết rằng):** Modal "Tạo Phiếu trả" đang mở.
- **When (Khi):** Người dùng điền các thông tin bắt buộc cho Phiếu trả:
  - **Lý do trả:** Dropdown (VD: Không thể sửa, Khách hủy yêu cầu, Trả nhầm hàng, Khác...).
  - **Ghi chú trả hàng:** Text area (Cho phép nhập diễn giải chi tiết).
  - **Nơi nhận (Đích đến):** Dropdown (VD: Trả về khách hàng, Trả về kho [Tên kho]).
- **Then (Thì):** Người dùng bấm nút **"Xác nhận tạo phiếu"**.
- **And (Và):** Hệ thống thực hiện:
  1. Tạo một bản ghi **Phiếu trả hàng** (Return Ticket) với mã phiếu tự sinh (VD: RET2405001).
  2. Cập nhật trạng thái các sản phẩm được chọn từ `Chờ xử lý` -> `Đã trả` (hoặc `Chờ xuất trả`).
  3. Các sản phẩm này sẽ được lọc/ẩn khỏi view mặc định của Danh sách thành phẩm chờ sửa.
  4. Hiển thị thông báo Toast thành công.

### AC 3: In tem nhãn / Phiếu giao nhận trả hàng (Liên kết US-03)
- **Given (Biết rằng):** Người dùng đã tạo thành công Phiếu trả hàng. Hệ thống hiển thị Dialog thông báo thành công kèm theo các action phụ.
- **When (Khi):** Người dùng bấm chọn **"In nhãn trả hàng"** (hoặc truy cập vào màn hình chi tiết Phiếu trả và chọn "In nhãn").
- **Then (Thì):** Hệ thống kế thừa logic In nhãn của (CS1.E3.US-03) để hiển thị Print Preview.
- **And (Và):** Tem nhãn trả hàng có layout tương tự US-03 nhưng thay đổi Header thành **"PHIẾU TRẢ HÀNG"**, nội dung tem bao gồm:
  - Mã Barcode/QR Code của Phiếu trả.
  - Mã hàng, Lô.
  - Lý do trả (ngắn gọn).
  - Đích đến (Routing: Trả về [Tên khách] / [Tên Kho]).

### AC 4: Validation khi lập Phiếu trả
- **Given (Biết rằng):** Người dùng thao tác trên Modal Tạo Phiếu trả.
- **Then (Thì):** 
  - Không cho phép tạo phiếu (nút Xác nhận bị disable) nếu chưa chọn `Lý do trả` hoặc `Nơi nhận`.
  - Nếu danh sách Item chọn bao gồm các sản phẩm của **nhiều Khách hàng khác nhau** nhưng lại chọn `Nơi nhận = Trả về khách hàng`, hệ thống sẽ cảnh báo: *"Danh sách hàng thuộc nhiều khách hàng khác nhau. Vui lòng tách riêng phiếu trả cho từng khách hàng."* (Block action).

---

## 3. THIẾT KẾ (UX/UI) & HÀNH VI TƯƠNG TÁC
- **Trên màn hình US-01:** Bổ sung thêm nút **[Trả hàng]** (Màu cảnh báo như Cam hoặc Đỏ outline) trên thanh Toolbar. Nút này chỉ Active khi có ít nhất 1 checkbox được tick.
- **Modal "Tạo Phiếu trả":**
  - **Layout chia 2 phần:**
    - Phần trên: Form nhập liệu thông tin chung của Phiếu trả (Lý do, Nơi nhận, Ghi chú).
    - Phần dưới: Bảng Data table thu gọn, liệt kê lại các Items đã chọn để user kiểm tra chéo lần cuối.
  - **Nút Action:** **[Hủy]** (Đóng modal) và **[Xác nhận tạo phiếu]** (Primary Button).
- **Tem nhãn trả hàng:** Tái sử dụng component Print Preview của màn in nhãn (US-03), chỉ thay đổi logic truyền data binding cho phù hợp với ngữ cảnh Trả hàng.

---

## 4. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION) - PHIẾU TRẢ

| STT | Tên trường (VN) | Ý nghĩa / Ghi chú | Kiểu dữ liệu | Required |
|---|---|---|---|---|
| 1 | Mã phiếu trả | Sinh tự động theo quy tắc hệ thống (VD: RET-YYMM-XXXX) | Text | Yes (Auto) |
| 2 | Ngày tạo phiếu | Thời gian hệ thống lúc tạo phiếu | DateTime | Yes (Auto) |
| 3 | Người tạo | Tên/Account User đang thao tác lập phiếu | Text | Yes (Auto) |
| 4 | Lý do trả | Chọn từ danh mục Master Data được cấu hình sẵn | Dropdown | Yes |
| 5 | Ghi chú trả hàng | Diễn giải thêm tình trạng/lý do trả (Max 500 ký tự) | Textarea | No |
| 6 | Nơi nhận (Đích đến) | Xác định nơi hàng sẽ đi về (Kho nội bộ hoặc Trả Khách hàng) | Dropdown | Yes |
| 7 | Danh sách Item | Danh sách chi tiết các sản phẩm trả (ID, Mã, Lô, TL) | Array/List | Yes |

---

## 5. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01 (Điều kiện khả dụng):** Chỉ các sản phẩm đang ở trạng thái `Chờ xử lý` (tức là chưa được đưa vào bất kỳ Bag sửa hàng nào ở US-02) mới được phép đưa vào Phiếu trả.
- **BR-02 (Tích hợp Tồn kho):** 
  - Nếu `Nơi nhận` là một Kho nội bộ, việc hoàn tất Phiếu trả có thể tạo lệnh chờ nhập kho (Stock Inbound) tại kho đích để ghi nhận lại tồn kho. 
  - Nếu `Nơi nhận` là Khách hàng, hệ thống tiến hành ghi nhận xuất kho và trừ tồn hoàn toàn khỏi phân hệ lưu trữ hàng sửa.
- **BR-03 (Liên kết in nhãn):** Việc in nhãn phiếu trả dùng chung hạ tầng với chức năng in mã vạch của Phiếu sửa hàng (US-03), đảm bảo mã vạch Phiếu trả có thể dùng máy quét tại cổng bảo vệ hoặc quầy giao nhận để kiểm tra (tracking) trạng thái xuất hàng.
