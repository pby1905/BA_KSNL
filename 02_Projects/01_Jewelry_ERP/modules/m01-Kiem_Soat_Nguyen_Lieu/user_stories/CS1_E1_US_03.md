# 🏷️ [CS1.E1.US-03] Nhận NL khách - Xóa nháp

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** Nhân viên tiếp nhận nguyên liệu

## 1. USER STORY
- **Là một (As a):** Nhân viên tiếp nhận nguyên liệu
- **Tôi muốn (I want):** Xóa các phiếu tiếp nhận nguyên liệu đang ở trạng thái "Bản nháp".
- **Để (So that):** Loại bỏ các phiếu tạo sai hoặc không còn nhu cầu xử lý, giúp danh sách phiếu tiếp nhận được gọn gàng và chính xác.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Xóa bản nháp thành công từ màn hình danh sách
- **Given (Biết rằng):** Nhân viên đang ở màn hình "Danh sách phiếu tiếp nhận NL".
- **And (Và):** Phiếu tiếp nhận được chọn đang có trạng thái là "Bản nháp".
- **When (Khi):** Nhân viên nhấn vào icon/nút "Xóa" và xác nhận tại pop-up "Bạn có chắc chắn muốn xóa bản nháp này?".
- **Then (Thì):** Hệ thống hiển thị thông báo "Xóa bản nháp thành công", phiếu biến mất khỏi danh sách hiển thị.

### AC 2: Không cho phép xóa phiếu đã lưu chính thức
- **Given (Biết rằng):** Phiếu tiếp nhận đang ở trạng thái khác "Bản nháp" (VD: Đang thực hiện, Hoàn thành).
- **When (Khi):** Nhân viên nhấn vào icon/nút "Xóa".
- **Then (Thì):** Nút "Xóa" bị ẩn (Hidden) hoặc bị vô hiệu hóa (Disabled) để ngăn chặn việc xóa các phiếu đã phát sinh nghiệp vụ.

### AC 3: Hủy bỏ thao tác xóa
- **Given (Biết rằng):** Pop-up xác nhận xóa đang hiển thị.
- **When (Khi):** Nhân viên nhấn nút "Hủy" hoặc "Đóng".
- **Then (Thì):** Hệ thống đóng pop-up, phiếu vẫn giữ nguyên trạng thái "Bản nháp" và không có thay đổi nào xảy ra.

---

## 3. THIẾT KẾ (UX/UI)
- (Theo link mẫu của dự án)

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01 (Trạng thái):** Chỉ cho phép xóa các phiếu có `Status = DRAFT`.
- **BR-02 (Quyền hạn):** Chỉ người tạo ra bản nháp đó hoặc người có Role "Quản lý/Admin" mới có quyền xóa. Nhân viên khác không nhìn thấy nút xóa trên bản nháp của người khác.
- **BR-03 (Lịch sử):** Hệ thống thực hiện Soft Delete (không xóa hẳn khỏi DB mà cập nhật `is_deleted = true`) để phục vụ việc truy xuất log khi cần thiết.

---

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)

### 5.1 Workflow validation
- Kiểm tra trạng thái phiếu ở phía Backend trước khi thực hiện lệnh xóa để tránh trường hợp người dùng mở 2 tab, 1 tab đã nhấn Lưu chính thức nhưng tab kia vẫn nhấn Xóa nháp.

### 5.2 Field Definition Table (Action Button)
| Field Name | Type | Description | Rules |
|---|---|---|---|
| Nút Xóa | Button | Thực hiện xóa bản nháp | Chỉ Enable khi phiếu ở trạng thái "Bản nháp". |
| Nút Xác nhận | Button | Xác nhận xóa trên Pop-up | Gọi API cập nhật trạng thái xóa. |
| Nút Hủy | Button | Hủy bỏ lệnh xóa | Đóng Modal. |

---

## 6. GHI CHÚ CHO QC
- **Kiểm tra phân quyền:** Dùng tài khoản Nhân viên A để xóa bản nháp của Nhân viên B (Kết quả mong đợi: Không thấy nút xóa).
- **Kiểm tra trạng thái:** Thử dùng công cụ (Postman) gửi yêu cầu xóa một phiếu đã ở trạng thái "Chờ xử lý" (Kết quả mong đợi: Backend phải trả về lỗi 400 hoặc 403).
- **Kiểm tra luồng:** Sau khi xóa thành công, quay lại màn hình danh sách và kiểm tra tổng số lượng phiếu (Total records) phải giảm đi 1.
