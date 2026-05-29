# ✅CS1.E1.US-24: [Phiếu trả NL] - In biên bản trả NL - lệch bao bì

--------------------------------------------------------------------------------

✅CS1.E1.US-24: [Phiếu trả NL] - In biên bản trả NL - lệch bao bì

## 1. USER STORY
**Là một (As a):** Nhân viên tiếp nhận nguyên liệu (MC).
**Tôi muốn (I want):** Hệ thống hỗ trợ in "Biên bản trả nguyên liệu khách hàng" cho trường hợp bị từ chối nhận do lệch trọng lượng bao bì.
**Để (So that):** Tôi có chứng từ vật lý hợp lệ (in 2 liên: 1 liên giao cho khách, 1 liên lưu tại kho) có đầy đủ chữ ký xác nhận của hai bên, làm cơ sở pháp lý chứng minh việc hoàn trả lại nguyên liệu.

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Điều kiện kích hoạt nút In biên bản
**Given (Biết rằng):** Nhân viên đang ở màn hình chi tiết của một Phiếu tiếp nhận NL.
**And (Và):** Phiếu này có phát sinh chênh lệch trọng lượng bao bì vượt ngưỡng và đã được người có thẩm quyền phê duyệt với hành động **"Yêu cầu trả NL"** (Trạng thái phiếu chuyển thành *Trả hàng*).
**When (Khi):** Nhân viên mở menu hành động (Actions).
**Then (Thì):** Nút **"In biên bản trả hàng"** (Print Return Record) được hiển thị và có thể bấm được (Enabled). Nếu phiếu không ở trạng thái trả hàng, nút này sẽ bị ẩn hoặc vô hiệu hóa.

### AC 2: Thiết lập cấu hình in (Print Settings)
**Given (Biết rằng):** Nhân viên bấm nút "In biên bản trả hàng".
**When (Khi):** Hệ thống mở cửa sổ Print Preview của trình duyệt.
**Then (Thì):** Hệ thống tự động thiết lập sẵn các tham số in ấn mặc định:
- **Thiết kế biểu mẫu (Layout):** File gốc được thiết kế theo khổ giấy A5, bố cục dọc (Portrait).
- **Số liên & Thiết lập in:** Hệ thống tự động sinh ra 2 trang (page) nội dung giống nhau đại diện cho 2 liên. Khi in, cấu hình máy in chọn khổ A5 và in 2 page trên 1 mặt giấy (2 pages per sheet).
- Không in Header/Footer của trình duyệt (URL, date...).

### AC 3: Nội dung hiển thị trên Biên bản in
**Given (Biết rằng):** Bản xem trước (Print Preview) được tạo ra.
**Then (Thì):** Biên bản in phải hiển thị đầy đủ và chính xác các thông tin sau:

1. **Phần Header:**
   - Logo Công ty.
   - Tiêu đề: **BIÊN BẢN TRẢ NGUYÊN LIỆU KHÁCH HÀNG**
   - **Số phiếu:** [Mã phiếu tiếp nhận gốc].
   - **Ngày lập biên bản:** [Ngày giờ in hiện tại (DD/MM/YYYY HH:mm)].

2. **Phần Thông tin lô hàng:**
   - **Khách hàng:** [Tên khách hàng].
   - **Mã khách hàng:** [Mã KH (nếu có)].
   - **Số Lô (Lot):** [Mã Lô của phiếu tiếp nhận].
   - **Ngày nhận hàng:** [Ngày ghi nhận trên phiếu tiếp nhận].

3. **Phần Chi tiết chênh lệch:** (Thiết kế dạng bảng)
   - **Tình trạng bao bì:** [Niêm phong / Rách / Bình thường].
   - **Trọng lượng khách báo:** [Giá trị do khách khai báo ban đầu].
   - **Trọng lượng cân thực tế:** [Giá trị cân được tại xưởng].
   - **Mức chênh lệch:** [Trọng lượng thực tế] - [Trọng lượng khách báo] (Hiển thị số âm/dương cùng đơn vị tính).
   - **Lý do trả hàng:** Chênh lệch trọng lượng bao bì vượt ngưỡng cho phép.
   - **Ghi chú xử lý:** [Nội dung ghi chú của Quản lý lúc phê duyệt "Yêu cầu trả NL"].

4. **Phần Footer (Chữ ký xác nhận):**
   - Hiển thị dòng ghi chú thời gian ký: *Ngày ..... tháng ..... năm .......*
   - Khung chữ ký (ký và ghi rõ họ tên) gồm 2 thành phần:
     - **Người nhận (Khách hàng / Đơn vị vận chuyển)**
     - **Người giao (Nhân viên MC)**
   - *Lưu ý:* Biểu mẫu không sử dụng Barcode hoặc QR Code.

## 3. THIẾT KẾ (UX/UI)
- *Link Figma mẫu in:* (Chờ cập nhật theo thiết kế thực tế của team UI).
- Bố cục (Layout) bắt buộc được thiết kế dọc (Portrait) chuẩn theo khổ giấy A5.

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Chỉ cho phép in Biên bản trả hàng khi có đầy đủ dữ liệu về Trọng lượng khách báo và Trọng lượng thực tế (dữ liệu là bắt buộc từ US-01).
- **BR-02:** Nút "In biên bản trả hàng" có thể được sử dụng nhiều lần để in lại khi cần thiết (Reprint), không giới hạn số lần in.

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)
- Khi gen HTML để in, cần sử dụng CSS Print Media Query (`@media print`) để:
  - Format lề (margin) phù hợp với khổ giấy A5 (Portrait).
  - Tự động duplicate (nhân bản) DOM nội dung thành 2 page để Print Dialog nhận diện là 2 trang.
  - Ẩn các button không cần thiết trên giao diện Web, chỉ giữ lại nội dung tài liệu.
  - Hỗ trợ auto page break (nếu bảng ghi chú xử lý quá dài).

## 6. GHI CHÚ CHO QC (TEST CASES)
- **TC1:** Kiểm tra nút "In biên bản trả hàng" có bị vô hiệu hóa khi phiếu mới ở trạng thái "Nháp" hoặc "Đang thực hiện" không.
- **TC2:** Dùng Data bị sai lệch lớn, có nội dung Ghi chú của quản lý rất dài, sau đó bấm in để kiểm tra xem Layout khổ A5 có bị vỡ chữ hay rớt dòng không hợp lý không.
- **TC3:** Xác minh đúng các thành phần ký tên là "Khách hàng" và "Nhân viên MC" (không dư thừa chữ ký của Quản lý).
