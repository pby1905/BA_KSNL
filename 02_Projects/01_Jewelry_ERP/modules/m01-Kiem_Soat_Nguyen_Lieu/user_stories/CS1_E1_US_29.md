# 🏷️ [CS1.E1.US-29] Phiếu trả NL - Search/Sort/Filter

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** Nhân viên MC / Quản lý / Thủ kho

## 1. USER STORY
- **Là một (As a):** Nhân viên thao tác hoặc Quản lý.
- **Tôi muốn (I want):** Tìm kiếm, sắp xếp và lọc danh sách các Phiếu trả nguyên liệu theo nhiều tiêu chí khác nhau (Mã phiếu, Khách hàng, Trạng thái, Loại phiếu...).
- **Để (So that):** Có thể tra cứu nhanh chóng, quản lý tiến độ xử lý trả hàng và thống kê dữ liệu một cách hiệu quả.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC 1: Tìm kiếm cơ bản (Global Search)
- **Given:** Người dùng đang ở màn hình danh sách Phiếu trả NL.
- **When:** Người dùng nhập từ khóa vào thanh tìm kiếm (Search Bar) và nhấn Enter hoặc icon Kính lúp.
- **Then:** Hệ thống hiển thị danh sách các phiếu có chứa từ khóa (so khớp dạng `%like%`).
- **And:** Các trường được hỗ trợ tìm kiếm text bao gồm:
  - Mã phiếu trả
  - Mã phiếu tiếp nhận gốc (Tham chiếu)
  - Tên Khách hàng
  - Số điện thoại Khách hàng (nếu có hiển thị)
  - Ghi chú (tùy chọn)

### AC 2: Lọc dữ liệu (Filter)
- **Given:** Người dùng mở bảng bộ lọc (Filter Panel) tại danh sách Phiếu trả NL.
- **Then:** Hệ thống cung cấp các tùy chọn lọc đa luồng:
  - **Theo Loại phiếu trả (Dropdown/Multi-select):** Lệch bao bì / Không đạt kiểm chi tiết.
  - **Theo Trạng thái (Dropdown/Multi-select):** Nháp / Mới tạo / Hoàn thành / Đã hủy.
  - **Theo Ngày tạo (Date Range Picker):** Từ ngày - Đến ngày.
  - **Theo Người tạo (Dropdown/Autocomplete):** Danh sách user trong hệ thống.
- **When:** Người dùng chọn một hoặc kết hợp nhiều điều kiện lọc và nhấn "Áp dụng" (Apply).
- **Then:** Danh sách cập nhật ngay lập tức theo chuẩn logic `AND` giữa các nhóm điều kiện.

### AC 3: Sắp xếp dữ liệu (Sort)
- **Given:** Cột dữ liệu trên bảng danh sách hỗ trợ tính năng sắp xếp.
- **When:** Người dùng click vào tiêu đề của một cột (Ví dụ: Ngày tạo).
- **Then:** Bảng danh sách sẽ sắp xếp lại theo chiều Tăng dần (Ascending).
- **And:** Click lần 2 sẽ đảo chiều thành Giảm dần (Descending). Click lần 3 để xóa sort (về mặc định).
- **Default Sort:** Mặc định khi mới load trang, danh sách được sắp xếp theo **Ngày tạo - Mới nhất xếp trên (Descending)**.
- **Các cột hỗ trợ Sort:** Mã phiếu, Ngày tạo, Tên khách hàng, Trạng thái.

### AC 4: Lưu giữ trạng thái Filter/Sort (Retain State)
- **Given:** Người dùng đã áp dụng bộ lọc (vd: Lọc trạng thái "Hoàn thành") và đang xem kết quả.
- **When:** Người dùng click vào chi tiết một phiếu trả, sau đó nhấn "Quay lại" (Back) hoặc dùng breadcrumb để ra ngoài danh sách.
- **Then:** Hệ thống vẫn giữ nguyên các điều kiện Filter/Sort/Search và trang (Pagination) trước đó, không bị reset về ban đầu.

---

## 3. THIẾT KẾ (UX/UI)
- Thanh tìm kiếm (Search box) đặt ở góc trên bên trái hoặc phải danh sách.
- Các bộ lọc nhanh (Quick Filters) như Trạng thái (Tabs: Tất cả / Mới tạo / Hoàn thành) có thể thiết kế dạng tab ngang để click nhanh.
- Nút "Bộ lọc nâng cao" (Advanced Filter) mở ra popup hoặc drawer bên phải để chứa các trường lọc chi tiết (Ngày tạo, Loại phiếu...).
- Phải có nút **"Xóa bộ lọc" (Clear Filters)** hiển thị rõ ràng nếu đang có bất kỳ điều kiện lọc nào được áp dụng.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01 (Phân quyền dữ liệu):** Kết quả tìm kiếm và lọc phải tuân thủ phân quyền (Data Visibility) của user đang đăng nhập. (VD: Nếu có quản lý chi nhánh, user nhánh nào chỉ tìm thấy phiếu trả của nhánh đó).
- **BR-02 (Thời gian lọc tối đa):** Để tối ưu hiệu năng DB, Date Range Picker (Từ ngày - Đến ngày) có thể giới hạn tối đa khoảng thời gian là 3 tháng hoặc 6 tháng cho mỗi lần truy vấn (tùy theo chính sách cấu hình hệ thống).

---

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)
- Backend nên áp dụng phân trang (Pagination) kết hợp với Filter/Search ở phía Server-side (không query toàn bộ DB ra frontend rồi mới lọc).
- Sử dụng Index (Đánh chỉ mục DB) cho các cột thường xuyên được truy vấn: `ma_phieu_tra`, `ma_phieu_tiep_nhan`, `khach_hang_id`, `trang_thai`, `ngay_tao`.
- Xử lý debounce (delay ~300ms-500ms) trên UI khi người dùng gõ vào ô Search tự động, để tránh spam API liên tục.
- Query Ngày tạo cần chú ý múi giờ (Timezone) để không bị bỏ sót data (vd Start Date: `00:00:00` đến End Date: `23:59:59`).

---

## 6. GHI CHÚ CHO QC (TEST CASES)
- **TC1:** Tìm kiếm một phần mã phiếu (Partial match) xem có ra đúng kết quả không.
- **TC2:** Nhập ngày bắt đầu lớn hơn ngày kết thúc -> Form Filter UI phải disable nút Apply hoặc báo lỗi logic.
- **TC3:** Lọc kết hợp (Trạng thái = Mới tạo AND Loại = Lệch bao bì) -> Đảm bảo data trả về thỏa mãn giao của 2 tập hợp.
- **TC4:** Mở chi tiết một phiếu trả, rồi ấn nút Back của trình duyệt hoặc UI -> Đảm bảo list vẫn giữ filter cũ và đúng trang (page) hiện tại.
- **TC5:** Nhập các ký tự đặc biệt (%, _, ', ", <script>) vào ô Search để test lỗi SQL Injection và XSS.
