# ✅CS1.E1.US-27: [Phiếu trả NL] - Xem chi tiết

--------------------------------------------------------------------------------

✅CS1.E1.US-27: [Phiếu trả NL] - Xem chi tiết

## 1. USER STORY
**Là một (As a):** Quản lý / Nhân viên MC / Kế toán kho có thẩm quyền.
**Tôi muốn (I want):** Xem chi tiết nội dung của một "Phiếu trả NL" (Material Return Ticket).
**Để (So that):** Tôi nắm bắt chính xác thông tin khách hàng, danh sách các nguyên liệu bị trả lại, lý do lỗi và trạng thái hiện tại của phiếu, từ đó thực hiện các bước tiếp theo (như liên hệ khách, in biên bản bàn giao, hoặc lưu trữ chứng từ).

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Truy cập và Hiển thị thông tin chung (Header)
**Given (Biết rằng):** Người dùng đang ở màn hình Danh sách Phiếu trả NL.
**When (Khi):** Người dùng click vào Mã phiếu hoặc nút "Xem chi tiết" của một dòng dữ liệu.
**Then (Thì):** Hệ thống chuyển hướng sang màn hình Chi tiết Phiếu trả NL và hiển thị các thông tin chung:
- Mã phiếu trả (Return Ticket ID).
- Trạng thái phiếu (Ví dụ: Mới tạo, Chờ khách nhận, Hoàn thành, Đã hủy).
- Thông tin khách hàng / Nhà cung cấp (Tên, Số điện thoại, Mã KH).
- Thông tin tham chiếu: Mã Phiếu tiếp nhận gốc (Clickable - có thể click để xem phiếu gốc).
- Ngày tạo phiếu & Người tạo (Nhân viên MC).

### AC 2: Hiển thị Danh sách nguyên liệu trả (Line Items)
**Given (Biết rằng):** Người dùng đang ở màn hình Chi tiết Phiếu trả NL.
**Then (Thì):** Hệ thống hiển thị một bảng danh sách các món nguyên liệu cần trả lại, bao gồm các cột:
- STT, Mã NL / Mã Lot, Tên loại NL (Vàng/Bạc/Đá...).
- Số lượng / Trọng lượng bị trả.
- Lý do trả hàng (Lệch bao bì, Không đạt đo phổ, Sai kích thước đá...).
- Hình ảnh/Video bằng chứng lỗi (Thumbnail có thể click để phóng to xem chi tiết).
- Nút "Hành động" cho từng dòng (nếu có, ví dụ: Hủy trả - theo US-26.1).

### AC 3: Hiển thị Lịch sử hoạt động (Activity History / Audit Trail)
**Given (Biết rằng):** Người dùng cuộn xuống phần Lịch sử hoạt động hoặc chuyển sang tab "Lịch sử".
**Then (Thì):** Hệ thống hiển thị dòng thời gian (Timeline) ghi nhận các sự kiện:
- [Thời gian] - [Người thực hiện] đã tạo phiếu trả NL từ Phiếu tiếp nhận [Mã PTN].
- [Thời gian] - [Người thực hiện] đã in Biên bản trả hàng.
- [Thời gian] - [Người thực hiện] đã chuyển trạng thái sang "Hoàn thành" / "Đã hủy" kèm lý do (nếu có).

### AC 4: Cấp quyền truy cập (RBAC)
**Given (Biết rằng):** Một người dùng đăng nhập vào hệ thống.
**Then (Thì):** 
- Nếu là **Nhân viên MC/Quản lý** thuộc chi nhánh/xưởng đó: Có quyền xem toàn bộ thông tin chi tiết.
- Nếu là **Nhân viên khác** không được phân quyền: Hệ thống báo lỗi "Bạn không có quyền truy cập Phiếu này" (Error 403) nếu cố tình truy cập qua URL.

## 3. THIẾT KẾ (UX/UI)
- Giao diện chia Layout rõ ràng: Header thông tin chung ở trên, Danh sách NL ở giữa, Lịch sử và Ghi chú ở cuối (hoặc chia 2 cột: Cột trái lớn hiển thị danh sách, cột phải nhỏ hiển thị thông tin chung & Lịch sử).
- Trạng thái phiếu nên sử dụng Badge (Nhãn màu) để dễ nhận biết (VD: Hoàn thành - Xanh lá, Đã hủy - Xám, Chờ xử lý - Vàng).
- Hình ảnh lỗi phải hỗ trợ tính năng Lightbox (click để phóng to) để quản lý có thể nhìn rõ vết xước/sai màu của đá.

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01 (Tính nhất quán dữ liệu):** Dữ liệu trên Phiếu trả NL (đặc biệt là trọng lượng và số lượng) là dạng "Snapshot" (chụp lại) từ thời điểm quyết định trả hàng. Nếu phiếu gốc bị Hủy (như US-26/26.1), trạng thái Phiếu trả NL tương ứng cũng sẽ tự động đồng bộ (ẩn hoặc chuyển Đã hủy).
- **BR-02 (Không chỉnh sửa):** Phiếu trả NL là chứng từ mang tính chất ghi nhận kết quả lỗi, người dùng KHÔNG ĐƯỢC PHÉP chỉnh sửa số lượng hay loại nguyên liệu trực tiếp trên màn hình này. Mọi thay đổi phải diễn ra từ luồng Xử lý chênh lệch gốc.

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)
- Tối ưu hóa truy vấn (Lazy load / Pagination) nếu Phiếu trả có danh sách hàng hóa quá lớn (> 100 dòng). Tuy nhiên thực tế ngành trang sức thường không quá dài, có thể load all.
- Chú ý quan hệ bảng DB: `ReturnTicket` 1-n `ReturnTicketLineItem`.
- API cần trả về URL hình ảnh lỗi dạng Signed URL hoặc Public URL hợp lệ để frontend render.

## 6. GHI CHÚ CHO QC (TEST CASES)
- **TC1:** Truy cập chi tiết phiếu có chứa hình ảnh lỗi -> Click vào hình ảnh xem có phóng to (Lightbox) hoạt động đúng không.
- **TC2:** Dùng tài khoản nhân viên không có quyền (VD: Sale cửa hàng) copy URL chi tiết phiếu trả của xưởng và dán vào trình duyệt -> Xác minh hệ thống chặn và báo lỗi 403.
- **TC3:** Kiểm tra xem trạng thái của phiếu trả có khớp với tiến trình đã thực hiện hay không (VD: Phiếu mới tạo vs Phiếu đã in biên bản vs Phiếu đã hủy do lệnh US-26).
- **TC4:** Click vào "Mã Phiếu tiếp nhận gốc" -> Đảm bảo mở đúng tab/cửa sổ chứa chi tiết PTN đó.
