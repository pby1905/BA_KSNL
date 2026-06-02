✅CS1.E1.US-01: [Nhận NL khách] - Tạo, lưu, lưu nháp, in nhãn✅CS1.E1.US-01: [Nhận NL khách] - Tạo, lưu, lưu nháp, in nhãn1. USER STORY *Là một (As a):Nhân viên tiếp nhận nguyên liệu
Tôi muốn (I want):Tạo phiếu tiếp nhận nguyên liệu từ khách hàng, ghi nhận thông tin bao bì và trọng lượng ban đầu.
Để (So that):Tôi có thể thiết lập cơ sở dữ liệu ban đầu cho việc gia công, đảm bảo tính minh bạch về trọng lượng nguyên liệu giữa khách hàng và xưởng.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC) *AC 1: Tạo mới phiếu tiếp nhận thành công (Lưu)Given (Biết rằng):Nhân viên tiếp nhận đang ở màn hình "Tạo phiếu tiếp nhận NL".
When (Khi):Nhân viên nhập đầy đủ các trường bắt buộc (Khách hàng, Ngày nhận, Tình trạng bao bì, Trọng lượng thực tế) và nhấn"Lưu".
Then (Thì):Hệ thống hiển thị thông báo "Tạo phiếu tiếp nhận thành công", dữ liệu được lưu vào trạng thái "Đang thực hiện" và hệ thống chuyển hướng đến bước Kiểm tra trọng lượng chi tiết.
AC 2: Tính toán chênh lệch trọng lượng tự độngGiven (Biết rằng):Nhân viên đang nhập thông tin tại phần "Xác nhận bao bì".
When (Khi):Nhân viên nhập "Trọng lượng gồm bao bì khách báo" và "Trọng lượng thực tế".
Then (Thì):Hệ thống tự động tính toán trường "Chênh lệch" = [Trọng lượng gồm bao bì khách báo] - [Trọng lượng thực tế]
AC 3: Lưu nháp phiếu tiếp nhậnGiven (Biết rằng):Nhân viên đã nhập một phần thông tin nhưng chưa xong.
When (Khi):Nhân viên nhấn"Lưu nháp".
Then (Thì):Hệ thống lưu lại các thông tin đã nhập, trạng thái phiếu là "Nháp", dữ liệu không bị kiểm tra các ràng buộc bắt buộc (ngoại trừ trường Khách hàng).
AC 4: Lưu & In nhãn thành côngGiven (Biết rằng):Nhân viên đã nhập đầy đủ thông tin bắt buộc.
When (Khi):Nhân viên nhấn"Lưu & In nhãn".
Then (Thì):Hệ thống thực hiện Lưu phiếu đồng thời hiển thị pop-up/màn hình xem trước bản in (Label) bao gồm: Mã phiếu, Tên khách hàng, Trọng lượng thực tế, Ngày nhận.
AC 5: Kiểm tra bỏ trống trường bắt buộcGiven (Biết rằng):Nhân viên để trống các trường có dấu (*).
When (Khi):Nhân viên nhấn "Lưu" hoặc "Lưu & In nhãn".
Then (Thì):Hệ thống hiển thị cảnh báo đỏ tại các trường tương ứng: "[Tên trường] là bắt buộc" và không cho phép lưu.
3. THIẾT KẾ (UX/UI) *Link Figma:(Theo link mẫu của dự án)
Mô tả Layout:Giao diện chia làm 2 khu vực chính: Thông tin chung và Xác nhận bao bì. Các nút hành động nằm cố định ở footer.
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES) *BR-01:Mã phiếu tiếp nhận được hệ thống sinh tự động (tham chiếu →Phụ lục A - Mã hóa) và duy nhất.
BR-02:Ngày nhận mặc định là ngày hiện tại của hệ thống nhưng cho phép người dùng điều chỉnh (không được chọn ngày trong tương lai).
BR-03:Giá trị chênh lệch cho phép hiển thị số âm (để ghi nhận việc dư nguyên liệu so với khách báo).
BR-04:Trường "Trọng lượng gồm bao bì khách báo" chỉ cho phép nhập (hiển thị) nếu chọn Radio Button "Có". Nếu chọn "Không có", trường này sẽ bị ẩn.
5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES) *5.1 Workflow validationĐịnh dạng trọng lượng: Cho phép nhập tối đa 4 chữ số thập phân (đặc thù ngành vàng cần độ chính xác cao).
Khách hàng: Searchable dropdown (tìm kiếm theo tên hoặc mã khách hàng).
5.2 Field Definition Table
Field Name (VN) | Field Name (EN) | Type | Required | Rules | 
Khách hàng | Customer | Dropdown | Có | Lấy từ Master Data Khách hàng. | 
Lô | Lot | Text | N/A | Read-only. Lô NL khách tự động sinh theo cấu trúc →Phụ lục A - Mã hóa | 
Ngày nhận | Receipt date | Datepicker | Có | Định dạng DD-MM-YYYY. | 
Tình trạng bao bì | Packaging condition | Dropdown | Có | Lấy từ Master Data Tình trạng bao bì. | 
Trọng lượng khách báo | Declared gross weight | Decimal (10,4) | Không | Chỉ nhập khi có bao bì. Đơn vị mặc định: lượng. | 
Trọng lượng thực tế | Actual gross weight | Decimal (10,4) | Có | Trọng lượng cân thực tế tại xưởng. | 
Chênh lệch | Weight Discrepancy | Decimal (10,4) | N/A | Read-only. Tự động tính toán. | 
Ghi chú | Remarks | Text Area | Không | Tối đa 500 ký tự. | 
6. GHI CHÚ CHO QCKiểm tra logic tính toán trường "Chênh lệch" với cả số dương và số âm.
Kiểm tra tính năng "Lưu & In nhãn": Phải đảm bảo in đúng mẫu label quy định cho bao bì nguyên liệu.
Kiểm tra trường hợp khách hàng không có bao bì (Radio "Không có") thì không cần nhập trọng lượng khách báo.