# ✅CS1.E1.US-26: [Phiếu trả NL] - Hủy phiếu - lệch bao bì

--------------------------------------------------------------------------------

✅CS1.E1.US-26: [Phiếu trả NL] - Hủy phiếu - lệch bao bì

## 1. USER STORY
**Là một (As a):** Quản lý / Nhân viên MC có thẩm quyền.
**Tôi muốn (I want):** Hủy lệnh "Yêu cầu trả NL" (Hủy phiếu trả) do nguyên nhân lệch bao bì.
**Để (So that):** Có thể hoàn tác (rollback) quyết định trả hàng khi xưởng và khách hàng đàm phán lại thành công về mức hao hụt, đưa phiếu quay trở lại luồng xử lý tiếp nhận để duyệt "Chấp nhận chênh lệch" mà không cần tạo mới toàn bộ từ đầu.

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Điều kiện hiển thị và cho phép Hủy
**Given (Biết rằng):** Người dùng đang xem chi tiết một Phiếu tiếp nhận NL.
**And (Và):** Phiếu đang có tình trạng **"Trả hàng"** (được sinh ra từ quyết định Yêu cầu trả NL do lệch bao bì).
**When (Khi):** Hàng hóa thực tế vẫn **chưa** rời khỏi xưởng (Khách hàng chưa ký biên bản nhận lại hàng / Phiếu trả chưa chuyển sang trạng thái "Hoàn thành").
**Then (Thì):** Hệ thống hiển thị nút **"Hủy lệnh trả hàng"** (Cancel Return). 
*Lưu ý: Nếu phiếu trả đã Hoàn thành, nút này sẽ bị ẩn.*

### AC 2: Bắt buộc nhập Lý do hủy
**Given (Biết rằng):** Người dùng nhấn nút "Hủy lệnh trả hàng".
**When (Khi):** Hành động được kích hoạt.
**Then (Thì):** Hệ thống hiển thị Pop-up xác nhận kèm theo một ô văn bản (Textarea) yêu cầu nhập **"Lý do hủy"**.
**And (Và):** Ô nhập lý do là bắt buộc (Mandatory). Nếu người dùng để trống và nhấn Xác nhận, hệ thống báo lỗi: "Vui lòng nhập lý do hủy lệnh trả hàng".

### AC 3: Logic Rollback (Cập nhật trạng thái)
**Given (Biết rằng):** Người dùng đã nhập lý do hợp lệ và nhấn "Xác nhận".
**When (Khi):** Hệ thống xử lý lệnh Hủy.
**Then (Thì):** 
1. Hệ thống xóa bỏ trạng thái "Trả hàng" của Phiếu tiếp nhận.
2. Trạng thái của **Phiếu tiếp nhận gốc** được khôi phục (rollback) về lại trạng thái **"Chờ trả"** (Trạng thái đang bị kẹt ở bước Xử lý chênh lệch bao bì).
3. Trạng thái của **Phiếu trả NL** tương ứng sẽ được chuyển thành **"Đã hủy"** (để giữ lịch sử cùng với lý do hủy).
4. Người Quản lý lúc này có thể thấy lại các nút hành động "Chấp nhận chênh lệch" để đi tiếp quy trình.

### AC 4: Ghi nhận Lịch sử hoạt động (Audit Trail)
**Given (Biết rằng):** Lệnh Hủy thực hiện thành công.
**Then (Thì):** Hệ thống tự động ghi lại log vào phần Lịch sử hoạt động (Activity History) của phiếu với nội dung:
*"[Tên User] đã Hủy lệnh trả hàng vào lúc [DD/MM/YYYY HH:mm]. Lý do: [Nội dung lý do người dùng vừa nhập]."*.

## 3. THIẾT KẾ (UX/UI)
- Nút "Hủy lệnh trả hàng" nên được thiết kế dưới dạng Secondary Button (nút phụ, màu xám hoặc Outline đỏ) đặt trong khu vực Action Menu để tránh bấm nhầm.

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01 (Phân quyền):** Chỉ những User có quyền "Phê duyệt chênh lệch" (Quản lý) mới có thể thực hiện thao tác Hủy lệnh trả hàng. Nhân viên MC thông thường chỉ được phép in biên bản.
- **BR-02 (Tồn kho ảo):** Do ở bước "Lệch bao bì", nguyên liệu chưa được sinh mã Lô nhập kho, nên việc Hủy phiếu trả này không phát sinh bất kỳ bút toán cộng/trừ nào vào kho. Hệ thống chỉ xử lý luồng trạng thái (Workflow State).

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)
- Backend cần kiểm tra kỹ Transaction: Cập nhật lại bản ghi lịch sử xử lý chênh lệch tương ứng từ "Yêu cầu trả" thành "Đã hủy quyết định trả".
- API xử lý cần validate chặt chẽ status hiện tại của phiếu trước khi cho phép rollback, tránh tình trạng race condition.

## 6. GHI CHÚ CHO QC (TEST CASES)
- **TC1:** Kiểm tra phân quyền: Dùng tài khoản nhân viên không có quyền duyệt, mở phiếu đang ở trạng thái Trả hàng -> Đảm bảo không thấy nút "Hủy lệnh trả hàng".
- **TC2:** Bấm hủy và để trống lý do -> Hệ thống chặn và báo lỗi đúng UX.
- **TC3:** Sau khi hủy thành công, kiểm tra xem phiếu có quay về đúng trạng thái "Chờ trả" không, và giao diện có hiển thị lại luồng xử lý chênh lệch không.
