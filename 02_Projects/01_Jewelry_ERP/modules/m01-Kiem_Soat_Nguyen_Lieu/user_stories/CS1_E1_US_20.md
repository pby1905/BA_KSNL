# 🏷️ [CS1.E1.US-20] Phiếu trả NL - Tạo, lưu, lưu nháp (loại: lệch bao bì)

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** Nhân viên MC / Quản lý có quyền xử lý phiếu trả nguyên liệu

## 1. USER STORY
- **Là một (As a):** Nhân viên MC / Quản lý có quyền xử lý phiếu trả nguyên liệu
- **Tôi muốn (I want):** Tạo phiếu trả nguyên liệu khách với loại trả là Lệch bao bì, đồng thời có thể lưu hoặc lưu nháp phiếu trả.
- **Để (So that):** Hệ thống ghi nhận đầy đủ thông tin trả nguyên liệu phát sinh do chênh lệch bao bì vượt mức cho phép, phục vụ kiểm soát nghiệp vụ, theo dõi xử lý và làm căn cứ thực hiện trả hàng cho khách.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Khởi tạo phiếu trả NL từ phiếu tiếp nhận có quyết định “Yêu cầu trả NL”
- **Given (Biết rằng):** Phiếu tiếp nhận nguyên liệu khách đã phát sinh chênh lệch bao bì vượt mức và đã được người có thẩm quyền xử lý với quyết định “Yêu cầu trả NL”.
- **When (Khi):** Người dùng nhấn thao tác Tạo phiếu trả NL từ màn hình chi tiết phiếu tiếp nhận.
- **Then (Thì):** Hệ thống khởi tạo mới một phiếu trả nguyên liệu với:
  - Loại phiếu trả = Lệch bao bì
  - Liên kết với phiếu tiếp nhận nguyên liệu nguồn
  - Tự động kế thừa các thông tin từ phiếu tiếp nhận, bao gồm:
    - Mã phiếu tiếp nhận
    - Khách hàng
    - Lô
    - Loại nguyên liệu
    - Trọng lượng khách báo
    - Trọng lượng thực tế
    - Giá trị chênh lệch
    - Ghi chú xử lý chênh lệch (nếu có)

### AC 2: Hiển thị màn hình tạo phiếu trả NL
- **Given (Biết rằng):** Người dùng đã khởi tạo phiếu trả NL thành công từ phiếu tiếp nhận.
- **When (Khi):** Màn hình tạo phiếu trả được mở ra.
- **Then (Thì):** Hệ thống hiển thị đầy đủ các thông tin của phiếu trả NL, bao gồm tối thiểu:
  - **Thông tin chung**
    - Mã phiếu trả (auto sinh khi lưu chính thức, chưa sinh nếu đang tạo mới/lưu nháp)
    - Loại phiếu trả = Lệch bao bì
    - Phiếu tiếp nhận tham chiếu
    - Khách hàng
    - Lô
    - Ngày tạo phiếu
    - Người tạo
  - **Thông tin lý do trả**
    - Lý do trả
    - Trọng lượng khách báo
    - Trọng lượng thực tế
    - Chênh lệch
    - Ghi chú xử lý
  - **Thông tin trả hàng**
    - Nội dung trả
    - Ghi chú phiếu trả
  - **Hành động**
    - Lưu nháp
    - Lưu
    - Hủy

### AC 3: Hệ thống tự động đổ dữ liệu nguồn
- **Given (Biết rằng):** Phiếu trả NL được tạo từ phiếu tiếp nhận loại lệch bao bì.
- **When (Khi):** Người dùng mở màn hình tạo phiếu trả.
- **Then (Thì):** Hệ thống tự động điền sẵn các dữ liệu liên quan từ phiếu tiếp nhận và quyết định xử lý chênh lệch trước đó, bao gồm:
  - Mã phiếu tiếp nhận, Khách hàng, Lô, Loại trả = Lệch bao bì
  - Giá trị chênh lệch bao bì
  - Người phê duyệt trả hàng
  - Ghi chú phê duyệt / ghi chú xử lý chênh lệch (nếu có)
- **And (Và):** Người dùng không được chỉnh sửa các thông tin nguồn mang tính tham chiếu.

### AC 4: Lưu nháp phiếu trả NL
- **Given (Biết rằng):** Người dùng đang nhập thông tin phiếu trả NL nhưng chưa muốn hoàn tất.
- **When (Khi):** Người dùng nhấn Lưu nháp.
- **Then (Thì):** Hệ thống:
  - Cho phép lưu phiếu ở trạng thái Nháp.
  - Ghi nhận các thông tin đã nhập tại thời điểm lưu.
  - Chưa phát sinh mã phiếu chính thức nếu hệ thống thiết kế sinh mã khi lưu chính thức (hoặc sinh mã nháp theo cấu hình nếu có).
  - Cho phép người dùng mở lại để tiếp tục chỉnh sửa sau.

### AC 5: Lưu chính thức phiếu trả NL
- **Given (Biết rằng):** Người dùng đã nhập đầy đủ các trường bắt buộc của phiếu trả NL.
- **When (Khi):** Người dùng nhấn Lưu.
- **Then (Thì):** Hệ thống:
  - Thực hiện validate dữ liệu.
  - Tạo phiếu trả NL chính thức.
  - Sinh mã phiếu trả NL theo quy tắc đánh số của hệ thống.
  - Gắn liên kết giữa phiếu trả NL và phiếu tiếp nhận nguồn.
  - Ghi log người tạo, thời gian tạo.
- **And (Và):** Cập nhật trạng thái các đối tượng liên quan:
  - **Phiếu trả NL mới tạo:** Trạng thái là **"Mới tạo"**.
  - **Phiếu tiếp nhận gốc:** 
    - Cột Trạng thái phiếu: Chuyển thành **"Trả hàng"**.
    - Cột Trạng thái xử lý (chênh lệch/chi tiết): Chuyển thành **"Đã lên phiếu trả"** (khóa luồng tiếp nhận của kiện hàng này).

### AC 6: Validation khi lưu chính thức
- **Given (Biết rằng):** Người dùng nhấn Lưu phiếu trả NL.
- **When (Khi):** Thiếu dữ liệu bắt buộc hoặc dữ liệu không hợp lệ.
- **Then (Thì):** Hệ thống không cho phép lưu và hiển thị thông báo lỗi tương ứng tại từng trường hoặc dạng tổng quát.
  - *Ví dụ:* "Vui lòng nhập lý do trả", "Vui lòng nhập nội dung trả", "Không thể tạo phiếu trả khi phiếu nguồn chưa có quyết định Yêu cầu trả NL".

### AC 7: Ràng buộc tạo phiếu trả theo nguồn nghiệp vụ
- **Given (Biết rằng):** Phiếu tiếp nhận chưa được phê duyệt theo hướng Yêu cầu trả NL.
- **When (Khi):** Người dùng cố gắng tạo phiếu trả NL loại Lệch bao bì.
- **Then (Thì):** Hệ thống không cho phép tạo phiếu và hiển thị thông báo:
  - *"Chỉ được tạo phiếu trả NL khi phiếu tiếp nhận đã được xử lý theo quyết định Yêu cầu trả NL."*

### AC 8: Liên kết trạng thái với phiếu tiếp nhận nguồn
- **Given (Biết rằng):** Phiếu trả NL đã được lưu thành công.
- **When (Khi):** Người dùng quay lại xem phiếu tiếp nhận nguồn.
- **Then (Thì):** Hệ thống hiển thị thông tin tham chiếu đến phiếu trả NL đã tạo, bao gồm tối thiểu:
  - Mã phiếu trả
  - Loại trả = Lệch bao bì
  - Trạng thái phiếu trả
- **And (Và):** Đồng thời đảm bảo không cho tạo trùng nhiều phiếu trả cho cùng một quyết định xử lý, trừ khi cấu hình cho phép.

### AC 9: Hủy thao tác tạo phiếu
- **Given (Biết rằng):** Người dùng đang ở màn hình tạo phiếu trả.
- **When (Khi):** Người dùng nhấn Hủy.
- **Then (Thì):** Hệ thống đóng màn hình tạo phiếu / quay về màn hình trước đó.
- **And (Và):** Nếu có dữ liệu chưa lưu, hệ thống hiển thị popup xác nhận: *"Thông tin chưa được lưu. Bạn có chắc chắn muốn thoát?"*

---

## 3. THIẾT KẾ (UX/UI)
**Khu vực 1: Thông tin nguồn**
- Phiếu tiếp nhận nguồn
- Khách hàng
- Lô
- Loại trả
- Giá trị chênh lệch bao bì
- Người yêu cầu / người phê duyệt trả hàng

**Khu vực 2: Thông tin phiếu trả**
- Ngày tạo
- Người tạo
- Lý do trả
- Nội dung trả
- Ghi chú

**Khu vực 3: Action buttons**
- Lưu nháp
- Lưu
- Hủy

**UI Notes**
- Các trường dữ liệu nguồn từ phiếu tiếp nhận hiển thị ở dạng read-only.
- Các trường nghiệp vụ nhập tay phải phân biệt rõ bằng editable input.
- Nếu phiếu đang ở trạng thái nháp, cần hiển thị badge/trạng thái Nháp.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Chỉ được tạo phiếu trả NL loại Lệch bao bì khi phiếu tiếp nhận nguồn đã có quyết định xử lý là Yêu cầu trả NL.
- **BR-02:** Một quyết định xử lý trả hàng từ một phiếu tiếp nhận chỉ được phép sinh ra tối đa 1 phiếu trả NL đang hiệu lực, trừ khi có cấu hình cho phép tạo lại.
- **BR-03:** Các thông tin tham chiếu từ phiếu tiếp nhận nguồn không được chỉnh sửa trên phiếu trả.
- **BR-04:** Phiếu lưu nháp được phép chỉnh sửa lại bởi người có quyền phù hợp.
- **BR-05:** Phiếu đã lưu chính thức thì không còn là dữ liệu tạm; việc chỉnh sửa sau đó phụ thuộc vào trạng thái phiếu và phân quyền hệ thống.
- **BR-06:** Trường Loại phiếu trả của US này được cố định là Lệch bao bì.
- **BR-07:** Nếu phiếu tiếp nhận nguồn đã bị hủy hoặc không còn hợp lệ nghiệp vụ, hệ thống không cho phép tiếp tục tạo/lưu phiếu trả.

---

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)
### 5.1 Validation Logic
- Bắt buộc có phiếu tiếp nhận nguồn hợp lệ
- Bắt buộc phiếu nguồn đã có quyết định Yêu cầu trả NL
- Bắt buộc nhập: Lý do trả, Nội dung trả
- Kiểm tra trùng phiếu trả theo nguồn
- Kiểm tra quyền người thao tác: quyền tạo phiếu trả, quyền lưu nháp, quyền lưu chính thức

### 5.2 Field Definition Table

| Tên trường (VN) | EN Field Name | Loại dữ liệu | Bắt buộc | Quy tắc / Ghi chú |
| --- | --- | --- | --- | --- |
| Loại phiếu trả | Return Type | Dropdown/Label | Có | Cố định = Lệch bao bì |
| Phiếu tiếp nhận nguồn | Source Receipt No. | Text/Lookup | Có | Read-only, lấy từ phiếu nguồn |
| Khách hàng | Customer | Text | Có | Read-only |
| Lô | Lot | Text | Có | Read-only |
| Trọng lượng khách báo | Reported Weight | Decimal(10,4) | Có | Read-only |
| Trọng lượng thực tế | Actual Weight | Decimal(10,4) | Có | Read-only |
| Chênh lệch | Difference Weight | Decimal(10,4) | Có | Read-only |
| Lý do trả | Return Reason | Text Area / Dropdown | Có | Nhập hoặc chọn theo cấu hình |
| Nội dung trả | Return Content | Text Area | Có | Mô tả nội dung hoàn trả |
| Ghi chú | Remark | Text Area | Không | Tối đa theo cấu hình hệ thống |
| Người tạo | Created By | Text | Có | Tự động theo user đăng nhập |
| Ngày tạo | Created Date | Datetime | Có | Tự động theo thời gian hệ thống |
| Trạng thái phiếu | Status | Text/Tag | Có | Nháp / Mới tạo / Chờ khách nhận ... |

### 5.3 Action Buttons

| Nút | Điều kiện hiển thị | Hành động |
| --- | --- | --- |
| Lưu nháp | Có quyền tạo/sửa nháp | Lưu dữ liệu ở trạng thái Nháp |
| Lưu | Có quyền tạo phiếu | Lưu chính thức và sinh phiếu |
| Hủy | Luôn hiển thị | Thoát màn hình tạo phiếu |

---

## 6. GHI CHÚ CHO QC
- Kiểm tra chỉ tạo được phiếu trả khi phiếu nguồn đã có quyết định Yêu cầu trả NL.
- Kiểm tra dữ liệu nguồn được tự động đổ đúng từ phiếu tiếp nhận.
- Kiểm tra chức năng Lưu nháp.
- Kiểm tra chức năng Lưu.
- Kiểm tra không cho tạo trùng phiếu trả cho cùng 1 nguồn xử lý.
- Kiểm tra popup cảnh báo khi thoát màn hình mà chưa lưu.
- Kiểm tra phân quyền:
  - User không có quyền không được tạo phiếu.
  - User không có quyền không được lưu chính thức.
- Kiểm tra log hệ thống khi tạo nháp và lưu chính thức.
