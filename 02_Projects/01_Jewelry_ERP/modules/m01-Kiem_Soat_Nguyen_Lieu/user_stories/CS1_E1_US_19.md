# ✅CS1.E1.US-19: [Nhận NL khách] - Search/Sort/Filter

--------------------------------------------------------------------------------

✅CS1.E1.US-19: [Nhận NL khách] - Search/Sort/Filter

## 1. USER STORY
**Là một (As a):** Nhân viên tiếp nhận nguyên liệu / Trưởng bộ phận Material Control (MC).
**Tôi muốn (I want):** Tìm kiếm, lọc và sắp xếp danh sách các phiếu tiếp nhận nguyên liệu.
**Để (So that):** Tôi có thể dễ dàng tra cứu, quản lý khối lượng công việc, và theo dõi tiến độ xử lý của từng phiếu tiếp nhận một cách nhanh chóng và chính xác.

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Tìm kiếm nhanh (Global Search)
**Given (Biết rằng):** Người dùng đang ở màn hình "Danh sách phiếu tiếp nhận NL".
**When (Khi):** Người dùng nhập từ khóa vào ô tìm kiếm (Search bar) và nhấn Enter (hoặc Icon Search).
**Then (Thì):** Hệ thống tìm kiếm và hiển thị các phiếu tiếp nhận có chứa từ khóa (Tìm kiếm tương đối - Like) tại một trong các trường sau:
- Mã phiếu tiếp nhận
- Tên Khách hàng
- Mã Khách hàng
- Lô (Lot)

### AC 2: Bộ lọc (Filter) theo danh mục có sẵn và thời gian
**Given (Biết rằng):** Người dùng mở khu vực/popup Bộ lọc nâng cao.
**When (Khi):** Người dùng thao tác chọn các điều kiện lọc:
1. **Thời gian nhận (Date Range):** Chọn "Từ ngày" (From) và "Đến ngày" (To).
2. **Trường có danh sách (Master Data / Dropdown):** Cho phép chọn một hoặc nhiều (Multi-select) các giá trị trong danh sách có sẵn:
   - Trạng thái phiếu (Nháp, Đang thực hiện, Chờ xác nhận, Hoàn thành, Trả hàng, Hủy)
   - Khách hàng
   - Tình trạng bao bì
   - Người tạo / Người phụ trách
**Then (Thì):** Hệ thống lập tức (hoặc sau khi bấm nút "Áp dụng") lọc danh sách theo điều kiện kết hợp (Logic AND) giữa các trường đã chọn và trả về kết quả tương ứng.

### AC 3: Sắp xếp dữ liệu (Sort)
**Given (Biết rằng):** Danh sách phiếu tiếp nhận đang hiển thị dữ liệu.
**Then (Thì):** 
1. **Sắp xếp mặc định:** Dữ liệu hiển thị sắp xếp theo **"Ngày nhận" mới nhất lên đầu** (Descending).
2. **Sắp xếp tùy chọn:** Người dùng có thể click vào tiêu đề các cột (Column Header) để sắp xếp Tăng dần (Ascending) hoặc Giảm dần (Descending) theo các cột sau:
   - Mã phiếu tiếp nhận
   - Ngày nhận
   - Khách hàng
   - Trạng thái

### AC 4: Trạng thái tương tác bộ lọc
**Given (Biết rằng):** Người dùng đang thao tác tìm kiếm/lọc.
**Then (Thì):**
- **Trường hợp không có kết quả:** Nếu không có phiếu nào khớp với điều kiện, lưới dữ liệu (Grid) trống và hiển thị thông báo "Không tìm thấy dữ liệu phù hợp với điều kiện tìm kiếm".
- **Xóa bộ lọc (Clear Filters):** Hệ thống hiển thị nút "Xóa bộ lọc". Khi click vào, tất cả các tham số Search/Filter sẽ bị reset và danh sách quay lại trạng thái hiển thị mặc định (xem AC 3).

## 3. THIẾT KẾ (UX/UI)
- *Link Figma:* (Chờ cập nhật theo thiết kế dự án).
- Khung tìm kiếm (Search bar) đặt ở góc trên bên phải hoặc bên trái phía trên lưới danh sách.
- Nút "Bộ lọc" (Filter) nằm cạnh Search bar, có thể hiển thị số lượng điều kiện đang được áp dụng (VD: Filter (2)).

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Ràng buộc lọc thời gian: "Từ ngày" (From Date) phải luôn nhỏ hơn hoặc bằng "Đến ngày" (To Date). Nếu người dùng chọn sai, hệ thống cảnh báo hoặc tự động disable các ngày không hợp lệ.
- **BR-02:** Reset Pagination: Khi có bất kỳ thay đổi nào về tham số Search/Filter/Sort, hệ thống phải tự động load lại trang danh sách về Trang 1 (Page 1).
- **BR-03:** Các trường có danh sách (Dropdown Filter) chỉ hiển thị các giá trị Master Data đang được active (Hiệu lực).

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)
- **Performance:** Tìm kiếm theo "Tên Khách hàng" (Text) trên dữ liệu lớn cần đảm bảo query tối ưu hoặc sử dụng index ở Database.
- Khi người dùng click vào xem chi tiết 1 phiếu, sau đó bấm nút "Back" hoặc quay lại danh sách, hệ thống nên **giữ nguyên (retain)** các tham số bộ lọc/sort/pagination trước đó.

## 6. GHI CHÚ CHO QC (TEST CASES)
- **TC1:** Kiểm thử nhập ký tự đặc biệt (!@#$%^) vào ô Search xem hệ thống có bị lỗi SQL Injection hoặc crash không.
- **TC2:** Kiểm thử logic kết hợp (AND): Vừa nhập Search từ khóa, vừa chọn Filter trạng thái = "Đang thực hiện", kiểm tra xem kết quả trả về có thỏa mãn cả 2 điều kiện không.
- **TC3:** Kiểm thử ngày "Từ ngày" và "Đến ngày" trùng nhau (VD: cùng chọn ngày hôm nay) -> Phải ra các phiếu nhận trong ngày hôm nay.
