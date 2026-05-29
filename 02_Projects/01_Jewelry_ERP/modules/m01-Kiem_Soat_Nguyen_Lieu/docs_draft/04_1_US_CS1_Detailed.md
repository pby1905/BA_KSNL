

# ✅CS1.E1.US-01_+[Nhận+NL+khách]+-+Tạo,+lưu,+lưu+nháp,+in+nhãn.doc
--------------------------------------------------------------------------------

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




# ✅CS1.E1.US-02_+[Nhận+NL+khách]+-+Thiết+lập_chỉnh+sửa+người+duyệt+và+mức+chênh+lệch.doc
--------------------------------------------------------------------------------

✅CS1.E1.US-02: [Nhận NL khách] - Thiết lập/chỉnh sửa người duyệt và mức chênh lệch✅CS1.E1.US-02: [Nhận NL khách] - Thiết lập/chỉnh sửa người duyệt và mức chênh lệch1. USER STORYLà một (As a):Trưởng bộ phận Material Control (TBP MC)
Tôi muốn (I want):Cấu hình danh sách người phê duyệt và thiết lập các ngưỡng chênh lệch cho phép đối:
TL bao bì;TL và tuổi dẻ;TL đá hàng hồi;TL, tuổi, giá công hàng hồi mới/hàng gửi sửaĐể (So that):Hệ thống có thể tự động kiểm soát dữ liệu đầu vào, ngăn chặn các sai sót vượt mức và đảm bảo quy trình phê duyệt diễn ra đúng thẩm quyền khi có biến động bất thường.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Cấu hình danh sách người phê duyệt (Approval Workflow)Given:TBP MC đang ở màn hình "Cấu hình phê duyệt chênh lệch".
When:Chọn loại nghiệp vụ (Kiểm bao bì/Kiểm dẻ/Kiểm hàng hồi/Kiểm hàng sửa) và chọn danh sách người dùng từ danh mục nhân viên để phân quyền phê duyệt.
Then:Hệ thống lưu lại danh sách
AC 2: Cấu hình ngưỡng chênh lệch Trọng lượng (TL) bao bìGiven:Đang thực hiện cấu hình cho mục Kiểm bao bì.
When:Nhập trị số chênh lệch tối đa cho phép giữa trọng lượng khách báo và trọng lượng thực tế và nhấn "Lưu".
Then:Hệ thống lưu lại cấu hình.
AC 3: Cấu hình chênh lệch Dẻ (TL & Tuổi dẻ)Given:Đang cấu hình thông số cho Kiểm dẻ.
When:Thiết lập ngưỡng sai số cho Trọng lượng và sai số Tuổi dẻ và nhấn "Lưu".
Then:Hệ thống lưu lại cấu hình.
AC 4: Cấu hình chênh lệch Hàng hồiGiven:Đang cấu hình cho Kiểm hàng hồi.
When:Nhập ngưỡng cho phép cho 2 chỉ số: TL đá và nhấn "Lưu".
Then:Hệ thống lưu lại cấu hình.
AC 4: Cấu hình chênh lệch Hàng hồi & Hàng gửi sửaGiven:Đang cấu hình cho Kiểm hàng sửa.
When:Nhập ngưỡng cho phép cho 3 chỉ số: Trọng lượng (TL), Tuổi vàng, Giá công và nhấn "Lưu".
Then:Hệ thống lưu lại cấu hình.3. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Một loại cấu hình chỉ được phép có01 phiên bản Hiệu lựctại một thời điểm.
BR-02:Mỗi loại chênh lệch cần có ít nhất 1 người duyệt4. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)
Tên trường | Kiểu dữ liệu | Required | Quy tắc Validation | 
Loại nghiệp vụ | Dropdown | Có | Kiểm bao bìKiểm dẻKiểm hàng hồiKiểm hàng sửa | 
Người phê duyệt | List (User) | Có | Chọn từ danh sách User | 
TL bao bì | Decimal (4,4) | Có | Cho phép nhập số dương. Đơn vị: lượng. | 
TL NL | Decimal (4,4) | Có | Cho phép nhập số dương. Đơn vị: lượng. | 
Tuổi | Decimal (2,2) | Có | Cho phép nhập số dương ( > 0, <= 99.99) | 
Trọng lượng đá | Decimal (4,4) | Có | Cho phép nhập số dương. Đơn vị: lượng. | 
Giá công | Amount | Có | Số tiền chênh lệch tối đa cho phép. | 
5. GHI CHÚ CHO QC




# ✅CS1.E1.US-03_+[Nhận+NL+khách]+-+Xóa+nháp.doc
--------------------------------------------------------------------------------

✅CS1.E1.US-03: [Nhận NL khách] - Xóa nháp✅CS1.E1.US-03: [Nhận NL khách] - Xóa nháp1. USER STORYLà một (As a):Nhân viên tiếp nhận nguyên liệu
Tôi muốn (I want):Xóa các phiếu tiếp nhận nguyên liệu đang ở trạng thái "Bản nháp".
Để (So that):Loại bỏ các phiếu tạo sai hoặc không còn nhu cầu xử lý, giúp danh sách phiếu tiếp nhận được gọn gàng và chính xác.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Xóa bản nháp thành công từ màn hình danh sáchGiven (Biết rằng):Nhân viên đang ở màn hình "Danh sách phiếu tiếp nhận NL".
And (Và):Phiếu tiếp nhận được chọn đang có trạng thái là"Bản nháp".
When (Khi):Nhân viên nhấn vào icon/nút "Xóa" và xác nhận tại pop-up "Bạn có chắc chắn muốn xóa bản nháp này?".
Then (Thì):Hệ thống hiển thị thông báo "Xóa bản nháp thành công", phiếu biến mất khỏi danh sách hiển thị.
AC 2: Không cho phép xóa phiếu đã lưu chính thứcGiven (Biết rằng):Phiếu tiếp nhận đang ở trạng thái khác "Bản nháp" (VD: Đang thực hiện, Hoàn thành).
When (Khi):Nhân viên nhấn vào icon/nút "Xóa" .Then (Thì):Nút "Xóa" bị ẩn (Hidden) hoặc bị vô hiệu hóa (Disabled) để ngăn chặn việc xóa các phiếu đã phát sinh nghiệp vụ.
AC 3: Hủy bỏ thao tác xóaGiven (Biết rằng):Pop-up xác nhận xóa đang hiển thị.
When (Khi):Nhân viên nhấn nút "Hủy" hoặc "Đóng".
Then (Thì):Hệ thống đóng pop-up, phiếu vẫn giữ nguyên trạng thái "Bản nháp" và không có thay đổi nào xảy ra.
3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01 (Trạng thái):Chỉ cho phép xóa các phiếu cóStatus = DRAFT.
BR-02 (Quyền hạn):Chỉ người tạo ra bản nháp đó hoặc người có Role "Quản lý/Admin" mới có quyền xóa. Nhân viên khác không nhìn thấy nút xóa trên bản nháp của người khác.
BR-03 (Lịch sử):Hệ thống thực hiệnSoft Delete(không xóa hẳn khỏi DB mà cập nhậtis_deleted = true) để phục vụ việc truy xuất log khi cần thiết.
5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Workflow validationKiểm tra trạng thái phiếu ở phía Backend trước khi thực hiện lệnh xóa để tránh trường hợp người dùng mở 2 tab, 1 tab đã nhấn Lưu chính thức nhưng tab kia vẫn nhấn Xóa nháp.
5.2 Field Definition Table (Action Button)
Field Name | Type | Description | Rules | 
Nút Xóa | Button | Thực hiện xóa bản nháp | Chỉ Enable khi phiếu ở trạng thái "Bản nháp". | 
Nút Xác nhận | Button | Xác nhận xóa trên Pop-up | Gọi API cập nhật trạng thái xóa. | 
Nút Hủy | Button | Hủy bỏ lệnh xóa | Đóng Modal. | 
6. GHI CHÚ CHO QCKiểm tra phân quyền:Dùng tài khoản Nhân viên A để xóa bản nháp của Nhân viên B (Kết quả mong đợi: Không thấy nút xóa).
Kiểm tra trạng thái:Thử dùng công cụ (Postman) gửi yêu cầu xóa một phiếu đã ở trạng thái "Chờ xử lý" (Kết quả mong đợi: Backend phải trả về lỗi 400 hoặc 403).
Kiểm tra luồng:Sau khi xóa thành công, quay lại màn hình danh sách và kiểm tra tổng số lượng phiếu (Total records) phải giảm đi 1.




# ✅CS1.E1.US-04_+[Nhận+NL+khách]+-+Kiểm+tra_+chênh+lệch+bao+bì+&+Gửi+thông+báo.doc
--------------------------------------------------------------------------------

✅CS1.E1.US-04: [Nhận NL khách] - Kiểm tra: chênh lệch bao bì & Gửi thông báo✅CS1.E1.US-04: [Nhận NL khách] - Kiểm tra: chênh lệch bao bì & Gửi thông báo1. USER STORYLà một (As a):Nhân viên tiếp nhận nguyên liệu
Tôi muốn (I want):Hệ thống tự động kiểm tra và ngăn chặn các thao tác lưu dữ liệu khi phát sinh chênh lệch trọng lượng bao bì vượt mức cho phép, đồng thời gửi thông báo đến cấp quản lý có thẩm quyền.
Để (So that):Đảm bảo mọi rủi ro về thất thoát nguyên liệu được kiểm soát tức thời và việc tiếp nhận chỉ được thực hiện sau khi có sự đồng ý của người quản lý.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Gửi thông báo đến người phê duyệt (Notifications)Given (Biết rằng):Hệ thống đã xác định chênh lệch vượt ngưỡng (TL chênh lệch > Chênh lệch cấu hình).
When (Khi):Nhân viên nhấn"Lưu".
Then (Thì):
1. Trạng thái phiếu chuyển thành"Đang thực hiện"và hiển thị thêm trạng thái"Chờ xác nhận"
2. Hệ thống gửi thông báo tức thời (In-app notification) danh sách Người phê duyệt và người theo dõi đã được thiết lập cho nghiệp vụ này.
3. Nội dung thông báo hiển thị rõ:
VN: "Phiếu [Mã phiếu] cần phê duyệt do chênh lệch [Loại chênh lệch]: [Giá trị thực tế] (Vượt ngưỡng [Giá trị cho phép])".
EN: "Ticket [Ticket ID] requires approval due to [Variance Type] variance: [Actual Value] (Exceeds threshold of [Allowed Value])"3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Phiếu ở trạng thái "Chờ phê duyệt" sẽ bịkhóa sửa đổidữ liệu đối với nhân viên MC cho đến khi người quản lý có phản hồi (Duyệt hoặc Từ chối).5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Validation LogicLogic kiểm tra phải thực hiện ở cả Frontend (để hiển thị UI tức thời) và Backend (để đảm bảo an toàn dữ liệu).
Click vào thông báo sẽ dẫn trực tiếp đến màn hình chi tiết phiếu cần duyệt.
5.2 Technical Note (BA-level)Hệ thống phải ghi log:"Hệ thống chặn thao tác do chênh lệch vượt mức tại thời điểm [Timestamp]".6. GHI CHÚ CHO QC (TEST CASES)Kiểm tra ngưỡng cận biên:Ví dụ ngưỡng là0.05. Thử nghiệm với0.049(Pass),0.050(Pass),0.051(Block).
Kiểm tra gửi thông báo:Xác nhận người quản lý nhận được thông báo đúng nội dung và đúng mã phiếu
Kiểm tra quyền hạn:Đảm bảo nhân viên không thể tự ý chuyển trạng thái phiếu từ "Chờ phê duyệt" sang "Chờ xử lý" bằng cách F5 hoặc can thiệp API.




# ✅CS1.E1.US-05_+[Nhận+NL+khách]+-+Xử+lý_+chênh+lệch+TL+bao+bì+(Trả_Chấp+nhận).doc
--------------------------------------------------------------------------------

✅CS1.E1.US-05: [Nhận NL khách] - Xử lý: chênh lệch TL bao bì (Trả/Chấp nhận)✅CS1.E1.US-05: [Nhận NL khách] - Xử lý: chênh lệch TL bao bì (Trả/Chấp nhận)1. USER STORYLà một (As a):Nhân viên MC (Material Control)
Tôi muốn (I want):Hệ thống tự động phát hiện, đưa ra cảnh báo và chặn luồng xử lý khi trọng lượng thực tế sai lệch vượt mức cho phép so với thông tin khách báo.
Để (So that):Đảm bảo mọi rủi ro về thất thoát hoặc sai sót nguyên liệu đều phải được cấp quản lý phê duyệt trước khi đưa vào sản xuất/phân kim.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Hiển thị cảnh báo chênh lệch vượt mứcGiven (Biết rằng):Nhân viên đang ở màn hình chi tiết phiếu tiếp nhận NL (ví dụ:NNL-2601-00001).
When (Khi):Trọng lượng thực tế nhập vào có mức chênh lệch (Difference) so với khách báo lớn hơn giá trị cấu hình (ví dụ: > 1 phân).
Then (Thì):Hệ thống hiển thị Banner cảnh báo màu vàng ở đầu trang với nội dung:"Phát hiện chênh lệch (0.0104 lượng) vượt mức cho phép (0.0100 lượng). Vui lòng ra quyết định xử lý!".
And:Trường "Chênh lệch" được highlight màu đỏ để gây chú ý.
AC 2: Chặn luồng xử lý và yêu cầu phê duyệtGiven (Biết rằng):Phiếu đang có cảnh báo chênh lệch vượt mức.
When (Khi):Nhân viên MC cố gắng chuyển trạng thái sang bước tiếp theo ("Thông tin nguyên liệu khách").
Then (Thì):Hệ thống chặn thao tác, yêu cầu thực hiện "Chấp nhận chênh lệch" hoặc "Yêu cầu trả NL".
AC 3: Ghi nhận lịch sử xử lý chênh lệchGiven (Biết rằng):Phiếu đã từng phát sinh chênh lệch và được yêu cầu cân lại hoặc xử lý.
When (Khi):Người dùng xem bảng "Lịch sử xử lý chênh lệch".
Then (Thì):Hệ thống hiển thị đầy đủ thông tin: Lần xử lý, TL khách, TL Seva, Chênh lệch, Người thực hiện, Ngày thực hiện và Ghi chú.
AC 4: Ra quyết định xử lý (Quản lý)Given (Biết rằng):Người dùng có quyền duyệt chênh lệch theo cấu hình đang xem phiếu bị chặn.
When (Khi):Quản lý nhấn chọn một trong các hành động:
Chấp nhận chênh lệch (Accept Variance):
Cập nhật lịch sử xử lý chênh lệch
Cập nhật trạng thái sang → Chấp nhận chênh lệch
Ghi nhận người duyệt, ngày duyệt, ghi chú)
Cập nhật trạng thái phiếu NNLRemove trạng thái "Chờ xác nhận" (chỉ còn trạng thái: "Đang thực hiện")Cho phép thực hiện thao tác tiếp tục (bỏ chặn) ở màn hình Thông tin nguyên liệu khách
Yêu cầu trả NL (Request Return):
Cập nhật lịch sử xử lý chênh lệch
Cập nhật trạng thái sang → Trả hàng
Ghi nhận người duyệt, ngày duyệt, ghi chú)
Cập nhật trạng thái phiếu NNLChuyển trạng thái "Chờ xác nhận" sang → Trả hàng (lúc này: song song 2 trạng thái: Đang thực hiện và Trả hàng)
3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Chỉ những user có quyền"Phê duyệt chênh lệch"mới nhìn thấy và tương tác được nút "Chấp nhận chênh lệch"/"Yêu cầu trả NL".5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Validation Logic5.2 Field Definition (Action Buttons)6. GHI CHÚ CHO QCKiểm tra banner cảnh báo
Kiểm tra lịch sử xử lý
Kiểm tra phân quyền: Nhân viên MC bình thường không được phép nhấn "Chấp nhận chênh lệch".




# ✅CS1.E1.US-06_+[Nhận+NL+khách]+-+Kiểm+tra+TL+chi+tiết.doc
--------------------------------------------------------------------------------

✅CS1.E1.US-06: [Nhận NL khách] - Kiểm tra TL chi tiết✅CS1.E1.US-06: [Nhận NL khách] - Kiểm tra TL chi tiết1. USER STORYLà một (As a):Nhân viên Tiếp nhận Nguyên liệu
Tôi muốn (I want):Nhập liệu chi tiết phân loại nguyên liệu, trọng lượng khách báo, trọng lượng Seva cân thực tế và tuổi vàng cho từng dòng hàng
Để (So that):Hệ thống ghi nhận dữ liệu bóc tách chi tiết làm cơ sở tính toán quy đổi vàng ròng (Quy 9999) và đối chiếu sai lệch trước khi xử lý tiếp.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Hiển thị thông tin tiến trình và thông tin chungGiven (Biết rằng):Nhân viên đã xác nhận bao bì thành công ở bước 1.
When (Khi):Truy cập vào chi tiết phiếu
Then (Thì):
Hệ thống hiển thịSteppergồm 3 bước: 1. Xác nhận bao bì (đã hoàn thành), 2. Kiểm tra trọng lượng chi tiết (đang thực hiện), 3. Xử lý từng loại.
Hiển thịThông tin chung(Khách hàng, Lô, Ngày tiếp nhận...) vàLịch sử hoạt độngcủa phiếu.
AC 2: Tự động tính toán trên từng dòng (Row Calculation)Given (Biết rằng):Nhân viên nhập dữ liệu vào các cột tương ứng.
When (Khi):Dữ liệu thay đổi.
Then (Thì):Hệ thống tự động tính toán theo công thức:
TL - khách= [TL tổng - khách] - [TL đá - khách].
Quy 99.99 - khách= ([TL - khách] * [Tuổi - khách]) / 99.99.
AC 3: Tổng hợp dữ liệu cuối bảng (Footer Summary)Given (Biết rằng):Bảng có nhiều dòng dữ liệu.
Then (Thì):DòngTổngở cuối bảng phải tự động cập nhật tổng cộng của các cột: TL tổng - khách, TL đá - khách, TL - khách, Quy 9999 - khách, TL tổng - Seva, và Tiền công - khách.
AC 4: Ghi tồn Tiếp nhận NL kháchGiven (Biết rằng):Nhân đã hoàn thành nhập dữ liệu Kiểm tra TL chi tiết
When (Khi):Nhân viên chọn "Tiếp tục"
Then (Thì):
Hệ thống ghi nhận tồn kho theo thông tin trên vào kho đã được cấu hình là kho Tiếp nhận NL khách
Ghi nhận vào Khu vực "Chờ nhập"
Ghi nhận vào Vị tríNếu, tình trạng = NL khách → Vị trí: Nguyên liệuNếu, tính trạng = Đơn hàng → Vị trí: Đơn hàngGhi nhận vào Item = phân loại (Dẻ, hàng hồi nấu, hàng hồi mới,..)
Nguyên liệu | 
 | Tồn cần ghi | 
Tình trạng | Loại | → | Kho | Khu vực | Vị trí | Item
(= "loại")
 | Lô
 | Tuổi
 | Màu
 | Tổng TL
 | TL đá
 | TL
 | Quy 99.99
 | 
NL khách | Dẻ | → | [kho tiếp nhận NL khách] | Chờ nhập | Nguyên liệu | Dẻ | = "Lô phiếu tiếp nhận NL" | = "Tuổi - khách" | null | = "Tổng TL - khách" | = "TL đá - khách" | = "TL khách" | = "Quy 99.99 - khách | 
NL khách | Hàng hồi nấu | → | [kho tiếp nhận NL khách] | Chờ nhập | Nguyên liệu | Hàng hồi nấu | = "Lô phiếu tiếp nhận NL" | = "Tuổi - khách" | null | = "Tổng TL - khách" | = "TL đá - khách" | = "TL khách" | = "Quy 99.99 - khách | 
NL khách | hàng hồi mới | → | [kho tiếp nhận NL khách] | Chờ nhập | Nguyên liệu | Hàng hồi mới | = "Lô phiếu tiếp nhận NL" | = "Tuổi - khách" | null | = "Tổng TL - khách" | = "TL đá - khách" | = "TL khách" | = "Quy 99.99 - khách | 
Đơn hàng | Hàng hồi mới | → | [kho tiếp nhận NL khách] | Chờ nhập | TP chờ sửa | Hàng hồi mới | = "Lô phiếu tiếp nhận NL" | = "Tuổi - khách" | null | = "Tổng TL - khách" | = "TL đá - khách" | = "TL khách" | = "Quy 99.99 - khách | 
Đơn hàng | Hàng gửi sửa | → | [kho tiếp nhận NL khách] | Chờ nhập | TP chờ sửa | Hàng gửi sửa | = "Lô phiếu tiếp nhận NL" | = "Tuổi - khách" | null | = "Tổng TL - khách" | = "TL đá - khách" | = "TL khách" | = "Quy 99.99 - khách | 
Notes: Cần thiết lập trước Khu vực và Vị trí cho Kho tiếp nhận NL, bao gồm:
Kho: tiếp nhận NL kháchKhu vực: Chờ nhậpVị trí: Nguyên liệuVị trí: TP chờ sửaKhu vực: Chờ trảVị trí: Nguyên liệuVị trí: TP chờ sửa3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Tất cả các ô nhập trọng lượng phải cho phép nhập tối đa 4 chữ số thập phân (ví dụ: 10.4740).
BR-02:Cột "Tiền công - khách" chỉ bắt buộc nhập nếu tình trạng = "Đơn hàng"
BR-03:Nếu "TL tổng - Seva" chưa được nhập đủ cho tất cả các dòng, nút "Tiếp tục" sẽ bị disabled.
5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1. Validation Logic5.2. Field Definition Table (Bảng định nghĩa trường dữ liệu)
Tên trường (VN) | EN Field Name | Loại dữ liệu | Bắt buộc | Quy tắc / Ghi chú (Rules) | 
Phân loại | Classification | Dropdown | Có | Chọn từ danh sách: Dẻ (Scrap), Hàng hồi nấu (Recycle-Melt), Hàng hồi mới (Recycle-New), Hàng gửi sửa (Repair). | 
Tình trạng | Origin | Dropdown | Có | Xác định nguồn gốc: NL từ khách (Customer Material), Đơn hàng (Sales Order). | 
Tuổi - khách | Purity (Cust) | Decimal(4,2) | Có | 0 < {Value} < 100
 | 
TL tổng - khách | Total Weight (Cust) | Decimal(10,4) | Có | 0 < {Value} | 
TL đá - khách | Stone Weight (Cust) | Decimal(10,4) | Có | Default = 0
0 <= {Value}
 | 
TL - khách | Metal Weight (Cust) | Decimal(10,4) | Read-only | = [Total Weight (Cust)] - [Stone Weight (Cust)] | 
Quy 99.99 - khách | 99.99 Equiv. (Cust) | Decimal(10,4) | Read-only | = ([Metal Weight (Cust)] * [Purity (Cust)]) / 99.99 | 
TL tổng - Seva | Total Weight (Seva) | Decimal(10,4) | Có | 0 < {Value} | 
Tiền công - khách | Labour Cost (Cust) | Currency | Điều kiện | Bắt buộc nếu tình trạng = "Đơn hàng" | 
Ghi chú | Remarks | Text Area | Không | Max 100 ký tự | 
6. GHI CHÚ CHO DEV & QCQC:Kiểm tra việc thêm/xóa dòng có làm sai lệch số tổng ở dòng cuối cùng hay không.




# ✅CS1.E1.US-07_+[Nhận+NL+khách]+-+Xử+lý_+Đo+phổ+(XRF+analysis).doc
--------------------------------------------------------------------------------

✅CS1.E1.US-07: [Nhận NL khách] - Xử lý: Đo phổ (XRF analysis)✅CS1.E1.US-07: [Nhận NL khách] - Xử lý: Đo phổ (XRF analysis)1. USER STORYLà một:Nhân viên Tiếp nhận Nguyên liệu
Tôi muốn:Ghi nhận kết quả đo phổ chi tiết cho dẻ trong phiếu tiếp nhận.
Để:Xác định chính xác hàm lượng vàng (tuổi vàng) và các kim loại đi kèm, làm căn cứ tính toán trọng lượng vàng nguyên chất (vàng tinh) cho quá trình gia công.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Đo phổ
Given:Nhân viên đo phổ mở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhận ở bước trước.
And:Nhân viên chọn các dòng nguyên liệu có loại = "Dẻ" nhấn vào nút "Đo phổ".When:Hệ thống hiển thị Modal "Đo phổ" (như hình ảnh thiết kế).
Then:Nhân viên có thể nhập các thành phần kim loại.
AC 2: Kiểm tra tổng tỷ lệ thành phần (Validation %)
Given:Nhân viên nhập tỷ lệ % cho các kim loại.
When:Nhấn "Lưu" trong Modal kết quả đo.
Then:Hệ thống kiểm tra tổng %. Nếu tổng% > 100%, hiển thị cảnh báo và không cho lưu.
VN:"Tổng tỷ lệ các thành phần kim loại không được vượt quá100%. Vui lòng kiểm tra lại (Hiện tại:{Total}%)."
EN:"The total percentage of metal components cannot exceed100%. Please verify your input (Current:{Total}%)."
AC 3: Có tạp
Given:Nhân viên hoàn thành nhập liệu 1 dòng ở Modal "Đo phổ"When:Checkbox "Tạp chất" = checked (tự động check khi có thành phần ngoài Bạc Đồng Kẽm)Then:Hệ thống hiển thị form nhập "Có tạp"AC 4: Đo lại & hủy xác nhận chênh lệch
Given:Nhân viên chọn các dòng nguyên liệu có loại = "Dẻ", trạng thái "Đang xử lý"And:Dòng nguyên liệu này có xử lý chênh lệchWhen:Nhân viên nhấn vào nút "Đo phổ"Then:Hiển thị popup xác nhậnVN: Phiếu Xử lý Chênh lệch tại các dòng {line 1, line 2...} sẽ chuyển sang trạng thái "Hủy". Bạn có chắc chắn muốn tiếp tục? "Có / Không"EN: The Variance Processing Ticket for lines {line 1, line 2...} will be changed to 'Cancelled' status. Are you sure you want to proceed? 'Yes / No'Có:→ Mở Modal "Đo phổ" và cho phép edit→ Khi Submit kết quả Modal "Đo phổ" → Chuyển trạng thái phiếu "Xử lý chênh lệch" sang trạng thái → "Hủy"
3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Chỉ những dòng nguyên liệu thõa mãn điều kiện sau có thể thực hiện Đo phổ, kiểm tra theo thứ tự sau:
Phân loại = Dẻ → Vi phạm, cảnh báo:Chỉ nguyên liệu "Dẻ" có thể thực hiện Đo phổOnly "Dẻ" materials can perform XRF analysisvà, trạng thái = Đang xử lý → Vi phạm, cảnh báo:Chỉ trạng thái "Đang xử lý" có thể thực hiện Đo phổXRF analysis can only be performed when the status is "In Progress"BR-02:Kết quả đo phổ sau khi "Hoàn tất" sẽ được lưu log lịch sử (Audit Trail) để truy vết nếu có khiếu nại từ khách hàng về sau.
5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Workflow validation5.2 Field Definition Table (Modal đo phổ)
Tên trường (VN) | EN Field Name | Type | Required | Rules | 
Đo phổ | 
Tuổi - Seva | Purity (Seva) | Decimal(4,2) | Có | Default = 0
Validate < 100 | 
TL - Seva sau đo | Post-XRF Weight(Seva) | Decimal(10,4) | Có | > 0 | 
TL hao hụt | Scraping Loss | Decimal(10,4) | Read-only | = "TL Seva" - "TL - Seva sau đo" | 
% Ag | % Ag | Decimal(4,2) | Không | Default = 0
Validate < 100 | 
% Cu | % Cu | Decimal(4,2) | Không | Default = 0
Validate < 100 | 
% Zn | % Zn | Decimal(4,2) | Không | Default = 0
Validate < 100 | 
% Ni | % Ni | Decimal(4,2) | Không | Default = 0
Validate < 100 | 
% Pd | % Pd | Decimal(4,2) | Không | Default = 0
Validate < 100 | 
% M | % M | Decimal(4,2) | Không | Default = 0
Validate < 100 | 
% Fe | % Fe | Decimal(4,2) | Không | Default = 0
Validate < 100 | 
Có tạp chất | Has Impurities | Checkbox | Không | Tự động check khi có thành phần ngoài: Ag, Cu, Zn
Người dùng cũng có thể manual check/uncheck
 | 
Ghi chú | Remarks | Text | Không | Max 100 ký tự | 
 |  |  |  |  | 
Có tạp | 
Line | Line | Number | Read-only | Số thứ tự dòng của NL ở bảng danh sách NL | 
Số tuổi trừ (dự kiến) | Purity Deduction (Est.) | Decimal(4,2) | Có | Default = 0.3
Validate > 0 và < 100
 | 
Tuổi - Seva (dự kiến) | Purity (Seva) (Est.) | Decimal(4,2) | Read-only | = "Tuổi - Seva" - "Số tuổi trừ (dự kiến)" | 
Quy 99.99 - Seva (dự kiến) | 99.99 Equiv. (Seva) (Est.) | Decimal(10,4) | Read-only | = "TL Seva" x "Tuổi - Seva (dự kiến)" / 99.99 | 
Quy 99.99 - Khách bù (dự kiến) | 99.99 Cust Compensation (Est.) | Decimal(10,4) | Read-only | = "Quy 99.99 - Khách" - "Quy 99.99 - Seva" | 
6. GHI CHÚ CHO QC




# ✅CS1.E1.US-08_+[Nhận+NL+khách]+-+Kiểm+tra_+chênh+lệch+đo+phổ+&+Gửi+thông+báo.doc
--------------------------------------------------------------------------------

✅CS1.E1.US-08: [Nhận NL khách] - Kiểm tra: chênh lệch đo phổ & Gửi thông báo✅CS1.E1.US-08: [Nhận NL khách] - Kiểm tra: chênh lệch đo phổ & Gửi thông báo1. USER STORYLà một (As a):Nhân viên tiếp nhận nguyên liệu
Tôi muốn (I want):Hệ thống tự động kiểm tra và ngăn chặn các thao tác lưu dữ liệu khi phát sinh chênh lệch trọng lượng dẻ vượt mức cho phép/có tạp sau Đo phổ, đồng thời gửi thông báo đến cấp quản lý có thẩm quyền.
Để (So that):Đảm bảo mọi rủi ro về thất thoát nguyên liệu được kiểm soát tức thời và việc tiếp nhận chỉ được thực hiện sau khi có sự đồng ý của người quản lý.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Gửi thông báo đến người phê duyệt (Notifications)Given (Biết rằng):Sau khi nhân viên xác nhận ở Modal "Đo phổ"
Hệ thống đã xác định chênh lệch vượt ngưỡng (TL chênh lệch ("TL khách" - "TL Seva")  > Chênh lệch cấu hình).
hoặc, có tạp chấtWhen (Khi):Nhân viên nhấn"Lưu".
Then (Thì):
1. Trạng thái phiếu chuyển thành"Đang thực hiện"và hiển thị thêm trạng thái"Chờ xác nhận"
2. Hệ thống gửi thông báo tức thời (In-app notification) danh sách Người phê duyệt và người theo dõi đã được thiết lập cho nghiệp vụ này.
3. Nội dung thông báo hiển thị rõ:
1. Cấu trúc Thông báo (Notification Structure)
Mẫu chung (Template):
VN:"Phiếu[Mã phiếu]cần phê duyệt do chênh lệch[Loại chênh lệch]:[Lý do]"
EN:"Ticket[Ticket ID]requires approval due to[Variance Type]variance:[Reason]"
2. Chi tiết các kịch bản Lý do (Reason Scenarios)
Dưới đây là 3 kịch bản hiển thị lý do tương ứng với dữ liệu thực tế từ Đo phổ:
Kịch bản A: Chỉ vi phạm Vượt ngưỡng (Threshold Violation)
VN:Chênh lệch TL[Giá trị thực tế](Vượt ngưỡng[Giá trị cho phép])
EN:Metal Weigh Variance[Actual Value](Exceeds threshold of[Allowed Value])
Ví dụ:Chênh lệch TL0.5214(Vượt ngưỡng0.3000)
Kịch bản B: Chỉ vi phạm Có tạp chất (Impurities Detected)
VN:Có tạp chất
EN:Impurities detected
Logic:Hiển thị khi Checkbox"Has Impurities"được tích chọn.
Kịch bản C: Vi phạm cả Vượt ngưỡng và Có tạp chất (Mixed Violation)
VN:[Giá trị thực tế](Vượt ngưỡng[Giá trị cho phép]) và Có tạp chất
EN:[Actual Value](Exceeds threshold of[Allowed Value]) and Impurities detected
3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Phiếu ở trạng thái "Chờ phê duyệt" sẽ bịkhóa sửa đổidữ liệu đối với nhân viên MC cho đến khi người quản lý có phản hồi (Duyệt hoặc Từ chối).5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Validation LogicLogic kiểm tra phải thực hiện ở cả Frontend (để hiển thị UI tức thời) và Backend (để đảm bảo an toàn dữ liệu).
Notification Payload:
DeepLink: Click vào thông báo sẽ dẫn trực tiếp đến màn hình chi tiết phiếu cần duyệt.
5.2 Technical Note (BA-level)Hệ thống phải ghi log:"Hệ thống chặn thao tác do chênh lệch vượt mức tại thời điểm [Timestamp]".6. GHI CHÚ CHO QC (TEST CASES)Kiểm tra ngưỡng cận biên:Ví dụ ngưỡng là0.05. Thử nghiệm với0.049(Pass),0.050(Pass),0.051(Block).
Kiểm tra gửi thông báo:Xác nhận người quản lý nhận được thông báo đúng nội dung và đúng mã phiếu
Kiểm tra quyền hạn:Đảm bảo nhân viên không thể tự ý chuyển trạng thái phiếu từ "Chờ phê duyệt" sang "Chờ xử lý" bằng cách F5 hoặc can thiệp API.




# ✅CS1.E1.US-09_+[Nhận+NL+khách]+-+Xử+lý_+Kiểm+tem+-+Tính+đá+(Tag+&+Stone+Verification).doc
--------------------------------------------------------------------------------

✅CS1.E1.US-09: [Nhận NL khách] - Xử lý: Kiểm tem - Tính đá (Tag & Stone Verification)✅CS1.E1.US-09: [Nhận NL khách] - Xử lý: Kiểm tem - Tính đá (Tag & Stone Verification)1. USER STORYLà một:Nhân viên Tiếp nhận Nguyên liệu
Tôi muốn:Ghi nhận trọng lượng đá với nguyên liệu hàng hồi.
Để:Hệ thống tự động tính toán Trọng lượng vàng thực tế (TL - Seva) làm cơ sở cho việc đo phổ và đối soát giá trị.
2. TIÊU CHÍ CHẤP NHẬN (AC)AC 1: Kiểm tem - Tính đá (Tag & Stone Verification)Given:Nhân viên mở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhận ở bước trước.
And:Nhân viênchọn các dòng nguyên liệu có:Loại = "Hàng hồi mới" hoặc "Hàng hồi nấu"và, tình trạng = "NL từ khách"nhấn vào nút "Kiểm tem - Tính đá".When:Hệ thống hiển thị Modal "Kiểm tem - Tính đá" (như hình ảnh thiết kế).
Then:Nhân viên có thể nhập thông TL đá
AC 2: Kiểm lại & hủy xác nhận chênh lệch
Given:Nhân viên chọn các dòng nguyên liệu có:Loại = "Hàng hồi mới" hoặc "Hàng hồi nấu".và, tình trạng = "NL từ khách"và, trạng thái = "Đang xử lý"And:Dòng nguyên liệu này có xử lý chênh lệchWhen:Nhân viên nhấn vào nút "Kiểm tem - Tính đá"Then:Hiển thị popup xác nhậnVN: Phiếu Xử lý Chênh lệch tại các dòng {line 1, line 2...} sẽ chuyển sang trạng thái "Hủy". Bạn có chắc chắn muốn tiếp tục? "Có / Không"EN: The Variance Processing Ticket for lines {line 1, line 2...} will be changed to 'Cancelled' status. Are you sure you want to proceed? 'Yes / No'Có:→ Mở Modal "Kiểm tem - Tính đá" và cho phép edit→ Khi Submit kết quả Modal "Kiểm tem - Tính đá" → Chuyển trạng thái phiếu "Xử lý chênh lệch" sang trạng thái → "Hủy"3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Chỉ những dòng nguyên liệu thõa mãn điều kiện sau có thể thực hiện Kiểm tem - Tính đá, kiểm tra theo thứ tự sau:
Phân loại = Hàng hồi mới / Hàng hồi nấu → Vi phạm, cảnh báo:Chỉ nguyên liệu "Hàng hồi" có thể thực hiện Kiểm tem - Tính đáOnly "Hàng hồi" materials can perform Tag & Stone Verificationvà, tình trạng = "NL từ khách" → Vi phạm, cảnh báo:Chỉ "NL từ khách" có thể thực hiện Kiểm tem - Tính đáTag & Stone Verification can only be performed when the origin is "Customer Meterial"và, trạng thái = Đang xử lý → Vi phạm, cảnh báo:Chỉ trạng thái "Đang xử lý" có thể thực hiện Kiểm tem - Tính đáTag & Stone Verification can only be performed when the status is "In Progress"BR-02:Kết quả sau khi "Hoàn tất" sẽ được lưu log lịch sử (Audit Trail) để truy vết nếu có khiếu nại từ khách hàng về sau.
BR-03:TL đá - Seva phải < TL tổng - Seva
5. GHI CHÚ KỸ THUẬT & FIELD DEFINITION5.1 Workflow validation5.2 Field Definition Table (Modal Kiểm tem - Tính đá)
Tên trường (VN) | EN Field Name | Type | Required | Rules & Logic | 
TL đá - Seva | Stone Weight (Seva) | Decimal(10,4) | Có | 0 <= {value}
 | 
Có sai tem | Tag Discrepancy | Checkbox | Không | Default = uncheck | 
Tuổi - Seva | Purity (Seva) | Decimal(4,2) | Read-only | Tự động lấy "Tuổi - Khách" nếu "Có sai tem" = Uncheck. |
TL - Seva | Metal Weight (Seva) | Decimal(10,4) | Read-only | = "TL tổng - Seva" - "TL đá - Seva" |
Quy 99.99 - Seva | 99.99 Equiv. (Seva) | Decimal(10,4) | Read-only | = ("TL - Seva" x "Tuổi - Seva") / 99.99 (Làm cơ sở để nhập kho) |
Ghi chú | Remarks | Text | Không | Max 100 ký tự | 
6. GHI CHÚ CHO QCKiểm tra logic trừ trọng lượng: Đảm bảo tổng trọng lượng các loại đá không vượt quá trọng lượng thực tế của món hàng.




# ✅CS1.E1.US-10_+[Nhận+NL+khách]+-+Kiểm+tra_+chênh+lệch+Kiểm+tem+-+Tính+đá+&+Gửi+thông+báo.doc
--------------------------------------------------------------------------------

✅CS1.E1.US-10: [Nhận NL khách] - Kiểm tra: chênh lệch Kiểm tem - Tính đá & Gửi thông báo✅CS1.E1.US-10: [Nhận NL khách] - Kiểm tra: chênh lệch Kiểm tem - Tính đá & Gửi thông báo1. USER STORYLà một (As a):Nhân viên tiếp nhận nguyên liệu
Tôi muốn (I want):Hệ thống tự động kiểm tra và ngăn chặn các thao tác lưu dữ liệu khi phát sinh chênh lệch trọng lượng đá vượt mức cho phép/có sai tem sau Kiểm tem - Tính đá, đồng thời gửi thông báo đến cấp quản lý có thẩm quyền.
Để (So that):Đảm bảo mọi rủi ro về thất thoát nguyên liệu được kiểm soát tức thời và việc tiếp nhận chỉ được thực hiện sau khi có sự đồng ý của người quản lý.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Gửi thông báo đến người phê duyệt (Notifications)Given (Biết rằng):Sau khi nhân viên xác nhận ở Modal "Kiểm tem - Tính đá"
Hệ thống đã xác định chênh lệch vượt ngưỡng (TL chênh lệch ("TL đá khách" - "TL đá Seva")  > Chênh lệch cấu hình).
hoặc, có sai temWhen (Khi):Nhân viên nhấn"Lưu".
Then (Thì):
1. Trạng thái phiếu chuyển thành"Đang thực hiện"và hiển thị thêm trạng thái"Chờ xác nhận"
2. Hệ thống gửi thông báo tức thời (In-app notification) danh sách Người phê duyệt và người theo dõi đã được thiết lập cho nghiệp vụ này.
3. Nội dung thông báo hiển thị rõ:
1. Cấu trúc Thông báo (Notification Structure)
Mẫu chung (Template):
VN:"Phiếu[Mã phiếu]cần phê duyệt do chênh lệch[Loại chênh lệch]:[Lý do]"
EN:"Ticket[Ticket ID]requires approval due to[Variance Type]variance:[Reason]"
2. Chi tiết các kịch bản Lý do (Reason Scenarios)
Dưới đây là 3 kịch bản hiển thị lý do tương ứng với dữ liệu thực tế từ Kiểm tem - Tính đá:
Kịch bản A: Chỉ vi phạm Vượt ngưỡng (Threshold Violation)
VN:Chênh lệch TL đá[Giá trị thực tế](Vượt ngưỡng[Giá trị cho phép])
EN:Stone Weight Variance[Actual Value](Exceeds threshold of[Allowed Value])
Ví dụ:Chênh lệch TL đá0.5214(Vượt ngưỡng0.3000)
Kịch bản B: Chỉ vi phạm Có sai tem (Tag discrepancy detected)
VN:Sai tem
EN:Tag discrepancy detected
Logic:Hiển thị khi Checkbox"Tag descrepancy"được tích chọn.
Kịch bản C: Vi phạm cả Vượt ngưỡng và Có sai tem (Mixed Violation)
VN:Chênh lệch TL đá[Giá trị thực tế](Vượt ngưỡng[Giá trị cho phép]) và Sai tem
EN:Stone Weight Variance[Actual Value](Exceeds threshold of[Allowed Value]) and Tag discrepancy detected
3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Phiếu ở trạng thái "Chờ phê duyệt" sẽ bịkhóa sửa đổidữ liệu đối với nhân viên MC cho đến khi người quản lý có phản hồi (Duyệt hoặc Từ chối).5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Validation LogicLogic kiểm tra phải thực hiện ở cả Frontend (để hiển thị UI tức thời) và Backend (để đảm bảo an toàn dữ liệu).
Notification Payload:
DeepLink: Click vào thông báo sẽ dẫn trực tiếp đến màn hình chi tiết phiếu cần duyệt.
5.2 Technical Note (BA-level)Hệ thống phải ghi log:"Hệ thống chặn thao tác do chênh lệch vượt mức tại thời điểm [Timestamp]".6. GHI CHÚ CHO QC (TEST CASES)Kiểm tra ngưỡng cận biên:Ví dụ ngưỡng là0.05. Thử nghiệm với0.049(Pass),0.050(Pass),0.051(Block).
Kiểm tra gửi thông báo:Xác nhận người quản lý nhận được thông báo đúng nội dung và đúng mã phiếu
Kiểm tra quyền hạn:Đảm bảo nhân viên không thể tự ý chuyển trạng thái phiếu từ "Chờ phê duyệt" sang "Chờ xử lý" bằng cách F5 hoặc can thiệp API.




# ✅CS1.E1.US-11_+[Nhận+NL+khách]+-+Xử+lý_+Kiểm+mã+hàng+(Item+Verification).doc
--------------------------------------------------------------------------------

✅CS1.E1.US-11: [Nhận NL khách] - Xử lý: Kiểm mã hàng (Item Verification)✅CS1.E1.US-11: [Nhận NL khách] - Xử lý: Kiểm mã hàng (Item Verification)1. USER STORYLà một:Nhân viên Tiếp nhận Nguyên liệu
Tôi muốn:Thực hiện đối soát mã sản phẩm thực tế của khách hàng so với danh mục hàng hóa (Item) của công ty.
Để:Xác định chính xác thông tin hàng hóa, đảm bảo tính nguyên bản của sản phẩm và ghi nhận các sai lệch về thông tin mã hàng nếu có.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Kiểm mã hàng
Given:Nhân viên đo phổ mở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhận ở bước trước.
And:Nhân viên chọn các dòng nguyên liệu có:Loại = "Hàng hồi mới" hoặc "Hàng gửi sửa".và, tình trạng = "Đơn hàng"And:Nhấn vào nút "Kiểm mã hàng".When:Hệ thống hiển thị Modal "Kiểm mã hàng" (như hình ảnh thiết kế).
Then:Nhân viên có thể nhập thông tin mã hàng tương ứng cho từng dòng được chọn.
AC 2: Kiểm lại & hủy xác nhận chênh lệch
Given:Nhân viên chọn các dòng nguyên liệu có:Loại = "Hàng hồi mới" hoặc "Hàng gửi sửa".và, tình trạng = "Đơn hàng"và, trạng thái = "Đang xử lý"And:Dòng nguyên liệu này có xử lý chênh lệchWhen:Nhân viên nhấn vào nút "Kiểm mã hàng"Then:Hiển thị popup xác nhậnVN: Phiếu Xử lý Chênh lệch tại các dòng {line 1, line 2...} sẽ chuyển sang trạng thái "Hủy". Bạn có chắc chắn muốn tiếp tục? "Có / Không"EN: The Variance Processing Ticket for lines {line 1, line 2...} will be changed to 'Cancelled' status. Are you sure you want to proceed? 'Yes / No'Có:→ Mở Modal "Kiểm mã hàng" và cho phép edit→ Khi Submit kết quả Modal "Kiểm mã hàng" → Chuyển trạng thái phiếu "Xử lý chênh lệch" sang trạng thái → "Hủy"
3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Chỉ những dòng nguyên liệu thõa mãn điều kiện sau có thể thực hiện Kiểm mã hàng, kiểm tra theo thứ tự sau:
Phân loại = "Hàng hồi mới / Hàng gửi sửa" → Vi phạm, cảnh báo:Chỉ nguyên liệu "Hàng hồi mới / Hàng gửi sửa" có thể thực hiện Kiểm mã hàngOnly "Hàng hồi mới / Hàng gửi sửa" materials can perform Item Verificationvà, tình trạng = "Đơn hàng"  → Vi phạm, cảnh báo:Chỉ tình trạng "Đơn hàng" có thể thực hiện Kiểm mã hàngItem Verification can only be performed when the origin is "Order"và, trạng thái = "Đang xử lý" → Vi phạm, cảnh báo:Chỉ trạng thái "Đang xử lý" có thể thực hiện Đo phổItem Verification can only be performed when the status is "In Progress"BR-02:Kết quả sau khi "Hoàn tất" sẽ được lưu log lịch sử (Audit Trail) để truy vết nếu có khiếu nại từ khách hàng về sau.
5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Workflow validation5.2 Field Definition Table (Modal đo phổ)
Tên trường (VN) | EN Field Name | Type | Required | Rules | 
Thông tin mã hàng | 
Hàng sai tem | Tag discrepancy detected | Checkbox | Không | Default = uncheck | 
Mã hàng | Item code | Search select | Default: Có
Không required nếu "Hàng sai tem" = checked | Cho phép search like các mã thành phẩm; Status = Active/InactiveChọn 1 từ gợi ý | 
Số bag | Bag number | Search select | Không | Cho phép search like các mã bag (Sales Order / Repair Prrder / G Order / Sample Order / Proto Order); Tất cả StatusChọn 1 từ gợi ý | 
PO khách | Cust PO | Text | Không | Max 20 ký tự | 
Số lượng | Qty | Interger | Có | {value} > 0 | 
Tuổi | Purity | Decimal (4,2) | Có | 0 < {value} < 100
Validate, tuổi từ dòng thứ 2 tự động update theo dòng thứ 1 (Tất cả các dòng mã hàng trong 1 dòng nguyên liệu phải cùng tuổi)
 | 
Màu | Color | Dropdown | Có | Chọn từ Master Data màu
 | 
TL tổng | Total Weight | Decimal (10,4) | Có | {value} > 0 | 
TL đá / bao | Stone Weight / bag | Decimal (10,4) | Có | {value} > 0
 | 
TL đá tổng | Total Stone Weight | Decimal (10,4) | Read-only | = "Số lượng" x "TL đá / bao" | 
TL | Metal Weight | Decimal (10,4) | Read-only | = "TL tổng" - "TL đá tổng" | 
Giá công / bao | Labour Cost / bag | Currency | Có | {value} > 0 | 
Giá công tổng | Total Labour Cost | Currency | Read-only | = "Số lượng" x "Giá công / bao" | 
Ghi chú lỗi | Remarks | Dropdown | Không | Chọn từ Master Data ghi chú lỗi | 
Kiểm mã hàng | 
Tuổi - Seva | Purity (Seva) | Decimal (4,2) | Read-only | = "Tuổi" ở dòng đầu tiên của bảng thông tin mã hàng | 
TL - Seva | Metal Weight (Seva) | Decimal (10,4) | Read-only | = Sum của cột "TL tổng" bảng Thông tin mã hàng | 
Quy 99.99 - Seva | 99.99 Equiv. (Seva) | Decimal (10,4) | Read-only | = "Tuổi - Seva" x "TL - Seva" / 99.99 | 
Giá công - Seva | Labour Cost (Seva) | Currency | Read-only | = Sum của cột "Giá công tổng" bảng Thông tin mã hàng | 
6. GHI CHÚ CHO QC




# ✅CS1.E1.US-12_+[Nhận+NL+khách]+-+Kiểm+tra_+chênh+lệch+Kiểm+mã+hàng+&+Gửi+thông+báo.doc
--------------------------------------------------------------------------------

✅CS1.E1.US-12: [Nhận NL khách] - Kiểm tra: chênh lệch Kiểm mã hàng & Gửi thông báo✅CS1.E1.US-12: [Nhận NL khách] - Kiểm tra: chênh lệch Kiểm mã hàng & Gửi thông báo1. USER STORYLà một (As a):Nhân viên tiếp nhận nguyên liệu
Tôi muốn (I want):Hệ thống tự động kiểm tra và ngăn chặn các thao tác lưu dữ liệu khi phát sinh chênh lệch trọng lượng đá vượt mức cho phép/có sai mã hàng sau Kiểm mã hàng, đồng thời gửi thông báo đến cấp quản lý có thẩm quyền.
Để (So that):Đảm bảo mọi rủi ro về thất thoát nguyên liệu được kiểm soát tức thời và việc tiếp nhận chỉ được thực hiện sau khi có sự đồng ý của người quản lý.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Gửi thông báo đến người phê duyệt (Notifications)Given (Biết rằng):Sau khi nhân viên xác nhận ở Modal "Kiểm mã hàng"
Hệ thống đã xác định chênh lệch vượt ngưỡng (chênh lệch tuổi, giá công tổng, TL đá tổng)
hoặc, có sai temWhen (Khi):Nhân viên nhấn"Lưu".
Then (Thì):
1. Trạng thái phiếu chuyển thành"Đang thực hiện"và hiển thị thêm trạng thái"Chờ xác nhận"
2. Hệ thống gửi thông báo tức thời (In-app notification) danh sách Người phê duyệt và người theo dõi đã được thiết lập cho nghiệp vụ này.
3. Nội dung thông báo hiển thị rõ:
1. Cấu trúc Thông báo (Notification Structure)
Mẫu chung (Template):
VN:"Phiếu[Mã phiếu]cần phê duyệt do chênh lệch[Loại chênh lệch]:[Lý do]"
EN:"Ticket[Ticket ID]requires approval due to[Variance Type]variance:[Reason]"
2. Chi tiết các kịch bản Lý do (Reason Scenarios)
Dưới đây là 3 kịch bản hiển thị lý do tương ứng với dữ liệu thực tế từ Kiểm mã hàng:
Kịch bản A: Chỉ vi phạm Vượt ngưỡng (Threshold Violation)
VN:Chênh lệch [TL đá tổng/ giá công tổng/ tuổi][Giá trị thực tế](Vượt ngưỡng[Giá trị cho phép])
EN:[Total Stone Weight/ Puriry/ Total Labour Cost] Variance[Actual Value](Exceeds threshold of[Allowed Value])
Ví dụ:Chênh lệch TL đá tổng0.5214(Vượt ngưỡng0.3000)
Kịch bản B: Chỉ vi phạm Có sai tem (Tag discrepancy detected)
VN:Sai tem
EN:Tag discrepancy detected
Logic:Hiển thị khi Checkbox"Tag descrepancy"được tích chọn.
Kịch bản C: Vi phạm cả Vượt ngưỡng và Có sai tem (Mixed Violation)
VN:Chênh lệch [TL đá tổng/ giá công tổng/ tuổi][Giá trị thực tế](Vượt ngưỡng[Giá trị cho phép]) và Sai tem
EN:[Total Stone Weight/ Puriry/ Total Labour Cost] Variance[Actual Value](Exceeds threshold of[Allowed Value]) and Tag discrepancy detected
3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Phiếu ở trạng thái "Chờ phê duyệt" sẽ bịkhóa sửa đổidữ liệu đối với nhân viên MC cho đến khi người quản lý có phản hồi (Duyệt hoặc Từ chối).5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Validation LogicLogic kiểm tra phải thực hiện ở cả Frontend (để hiển thị UI tức thời) và Backend (để đảm bảo an toàn dữ liệu).
Notification Payload:
DeepLink: Click vào thông báo sẽ dẫn trực tiếp đến màn hình chi tiết phiếu cần duyệt.
5.2 Technical Note (BA-level)Hệ thống phải ghi log:"Hệ thống chặn thao tác do chênh lệch vượt mức tại thời điểm [Timestamp]".6. GHI CHÚ CHO QC (TEST CASES)Kiểm tra ngưỡng cận biên:Ví dụ ngưỡng là0.05. Thử nghiệm với0.049(Pass),0.050(Pass),0.051(Block).
Kiểm tra gửi thông báo:Xác nhận người quản lý nhận được thông báo đúng nội dung và đúng mã phiếu
Kiểm tra quyền hạn:Đảm bảo nhân viên không thể tự ý chuyển trạng thái phiếu từ "Chờ phê duyệt" sang "Chờ xử lý" bằng cách F5 hoặc can thiệp API.




# ✅CS1.E1.US-13_+[Nhận+NL+khách]+-+Xử+lý_+Chấp+nhận+chênh+lệch+(Accept+Variance).doc
--------------------------------------------------------------------------------

✅CS1.E1.US-13: [Nhận NL khách] - Xử lý: Chấp nhận chênh lệch (Accept Variance)✅CS1.E1.US-13: [Nhận NL khách] - Xử lý: Chấp nhận chênh lệch (Accept Variance)1. USER STORYLà một:Người phê duyệt chênh lệch.
Tôi muốn:Xem xét các dòng nguyên liệu có sai lệch vượt ngưỡng và thực hiện đưa ra quyết định.
Để:Chính thức ghi nhận các thông số đo đạc thực tế vào hệ thống và cho phép tiếp tục quy trình.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC1: Chấp nhận chênh lệch (Accept Variance) - Chênh lệch Đo phổGiven:Người dùngmở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhậnWhen:Người dùng chọn dòng nguyên liệu ở trạng thái "Chờ xác nhận"And:Chọn "Chấp nhận chênh lệch" (từng phiếu, không phê duyệt cùng lúc nhiều phiếu)If:Lệch tuổi → Mở popup xác nhận Y/N, nhập ghi chú → chọn YCó tạp → Mở popup chấp nhận chênh lệch (điền số tuổi trừ thực tế) → Xác nhậnThen:
Cập nhật trạng thái dòng nguyên liệu: Từ "Chờ xác nhận" sang → "Đang xử lý"Cập nhật trạng thái phiếu xử lý chênh lệch: Từ "Chờ xác nhận" sang → "Chấp nhận chênh lệch"Nếu có tạp → Ghi nhận các thông tin sau vào bảng Có tạp tương ứng ở Tab ghi nhận Đo phổSố tuổi trừ (thực)Tuổi - Seva đã trừ (thực)Quy 99.99 - Seva đã trừ (thực)Quy 99.99 - Tổng khách bù (thực)Ghi nhận ghi chú vào phiếu xử lý chênh lệchAC2: Chấp nhận chênh lệch (Accept Variance) - Chênh lệch Kiểm tem - Tính đá & Kiểm Mã hàngGiven:Người dùngmở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhậnWhen:Người dùng chọn dòng nguyên liệu ở trạng thái "Chờ xác nhận"And:Chọn "Chấp nhận chênh lệch" (từng phiếu, không phê duyệt cùng lúc nhiều phiếu)Then:Hệ thống mở popup xác nhận Y/NAnd:Người dùng chọn Yes và nhập Ghi chúThen:
Cập nhật trạng thái dòng nguyên liệu: Từ "Chờ xác nhận" sang → "Đang xử lý"Cập nhật trạng thái phiếu xử lý chênh lệch: Từ "Chờ xác nhận" sang → "Chấp nhận chênh lệch"Ghi nhận ghi chú vào phiếu xử lý chênh lệch3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Chỉ những user có quyền"Phê duyệt chênh lệch"mới nhìn thấy và tương tác được nút "Chấp nhận chênh lệch"/"Yêu cầu trả NL".5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Validation Logic5.2 Field Definition (Action Buttons)6. GHI CHÚ CHO QC




# ✅CS1.E1.US-14_+[Nhận+NL+khách]+-+Xử+lý_+Yêu+cầu+trả+hàng+(Request+Return).doc
--------------------------------------------------------------------------------

✅CS1.E1.US-14: [Nhận NL khách] - Xử lý: Yêu cầu trả hàng (Request Return)✅CS1.E1.US-14: [Nhận NL khách] - Xử lý: Yêu cầu trả hàng (Request Return)1. USER STORYLà một:Người phê duyệt chênh lệch.
Tôi muốn:Xem xét các dòng nguyên liệu có sai lệch vượt ngưỡng và thực hiện đưa ra quyết định.
Để:Chính thức ghi nhận các thông số đo đạc thực tế vào hệ thống và cho phép tiếp tục quy trình.
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC1: Yêu cầu trả hàng (Request Return)Given:Người dùngmở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhậnWhen:Người dùng chọn dòng nguyên liệu ở trạng thái "Chờ xác nhận"And:Chọn "Yêu cầu trả NL" (từng phiếu, không phê duyệt cùng lúc nhiều phiếu)Then:Hệ thống mở popup xác nhận Y/NAnd:Người dùng chọn Yes và nhập Ghi chúThen:
Cập nhật trạng thái dòng nguyên liệu: Từ "Chờ xác nhận" sang → "Yêu cầu trả"Cập nhật trạng thái phiếu xử lý chênh lệch: Từ "Chờ xác nhận" sang → "Yêu cầu trả"Ghi nhận ghi chú vào phiếu xử lý chênh lệch3. THIẾT KẾ (UX/UI)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Chỉ những user có quyền"Phê duyệt chênh lệch"mới nhìn thấy và tương tác được nút "Chấp nhận chênh lệch"/"Yêu cầu trả NL".5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)5.1 Validation Logic5.2 Field Definition (Action Buttons)6. GHI CHÚ CHO QC




# ✅CS1.E1.US-15_+[Nhận+NL+khách]+-+Thiết+lập_chỉnh+sửa+kho+nhận+NL+khách+mặc+định.doc
--------------------------------------------------------------------------------

✅CS1.E1.US-15: [Nhận NL khách] - Thiết lập/chỉnh sửa kho nhận NL khách mặc định✅CS1.E1.US-15: [Nhận NL khách] - Thiết lập/chỉnh sửa kho nhận NL khách mặc định1. USER STORYLà một (As a):Trưởng bộ phận Material Control (TBP MC)
Tôi muốn (I want):Cấu hình nhà kho mặc định khi tiếp nhận NL khách và khi nhập kho
Để (So that):Hệ thống có thể tự động ghi nhận tồn kho tương ứng khi người dùng thao tác
2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)AC 1: Cấu hình kho nhận NLWhen:TBP MC mở màn hình "Cấu hình nhà kho tiếp nhận NL khách"Then:Hệ thống hiển thị Form chọn nhà kho choKho tiếp nhận NL kháchKho nhập NL đã kiểmAnd:Chọn nhà kho tương ứng và nhấn "Xác nhận"Then:Hệ thống khi nhận nhà kho được chọn3. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)BR-01:Một loại cấu hình chỉ được phép có01 phiên bản Hiệu lựctại một thời điểm.
BR-02:Mỗi loại chênh lệch cần có ít nhất 1 người duyệt4. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)
Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Required | Quy tắc Validation | 
Nhà kho | Sub Warehouse | Dropdown | Có | Chọn từ Master Data Sub Warehoude; Chỉ show Sub Warehouse có loại = Kho nguyên liệu / WIP | 
5. GHI CHÚ CHO QC




# ✅CS1.E1.US-16_+[Nhận+NL+khách]+-+Xử+lý_+Nhập+kho+(Stock+Inbound)+(tạo+Lô+&+in+nhãn).doc
--------------------------------------------------------------------------------

✅CS1.E1.US-16: [Nhận NL khách] - Xử lý: Nhập kho (Stock Inbound) (tạo Lô & in nhãn)✅CS1.E1.US-16: [Nhận NL khách] - Xử lý: Nhập kho (Stock Inbound) (tạo Lô & in nhãn)1. USER STORYLà một:Nhân viên tiếp nhận nguyên liệu.
Tôi muốn:Thực hiện nhập kho các dòng nguyên liệu đã hoàn tất đối soát, hệ thống tự động sinh mã Lô (Lot Number) và in nhãn định danh.
Để:Chính thức ghi tăng tồn kho, sẵn sàng cho công đoạn cấp phát sản xuất và đảm bảo tính truy xuất nguồn gốc của vàng.
2. TIÊU CHÍ CHẤP NHẬN (AC)AC1: Nhập khoGiven:Các dòng nguyên liệu đang ở trạng thái"Đang xử lý"(đã qua đo phổ/kiểm mã).
When:Nhân viên chọn các dòng có
Trạng thái = "Đang xử lý"và, "Quy 99.99 - Seva" không rỗng (> 0)And:Nhân viên chọn hành động"Nhập kho" (Stock Inbound)từ menu thao tác.
Then:Hệ thống hiển thị Modal "Nhập kho"
When:Nhân viên hoàn thành Form là nhấn "Xác nhận"Then:Hệ thống cập nhậtTrạng thái dòng nguyên liệu: từ "Đang xử lý" → "Đã nhập kho"Xóa tồn kho NL kháchXóa tồn các dòng tương ứng tại [kho tiếp nhận NL khách]Tạo phiếu nhập NL (Goods Receipt, bao gồm header và dtl) (ghi nhận trước, sẽ có màn hình show dữ liệu bảng này. Note ngoài action này, còn nhiều action khác/nguồn khác ghi nhận vào bảng này)
Goods Receipt - Header | 
 | 
 | 
Code | Type | Ref Code | Received by | Received at | 
Mã | Loại | Mã tham chiếu | Người nhận | Ngày nhận | 
Mã phiếu nhập
→Phụ lục A - Mã hóa | 
Tình trạng | → | Loại | 
NL khách | → | L: Công nợ | 
Hàng chờ sửa | → | G: Hàng khách gửi | 
 | Mã phiếu tiếp nhận NL | User thao tác | Datetime | 
 | Loại bao gồm:
Mã: tên VN (Tên EN)L: Công nợ (Liability Receipt)
G: Hàng khách gửi (Guest)P: Công ty tự mua (Purchased)
S: Vụn từ xưởng (Scrap)
R: Từ thu hồi (Recovery)C: Từ đúc CastH: Từ đúc HTJ | 
 | 
 | 
 | 
#Ghi chú: Mỗi loại là 1 GR khác nhau, tách mỗi loại 1 GR khi nhập 1 lần nhiều loại
Goods Receipt - Detail | 
 | 
 | 
 | 
 | 
SubWarehouse | Zone | Location | Item | LOT | Qty | Lenght | Purity | Color | Total Weight | Stone Weight | Metal Weight | 99.99 Equiv. | Liability Impact | 99.99 Equiv. Liability Adjustment | Net 99.99 Equiv. Liability Receipt | Labour Cost | 
Kho | Khu vực | Vị trí | Item | Lô | SL | Chiều dài | Tuổi | Màu | Tổng TL | TL đá | TL | Quy 99.99 | Tính công nợ | Quy 99.99 - Công nợ điều chỉnh | Quy 99.99 - Công nợ | Giá công | 
 | 
 | 
 | 
 | 
 | 
 | Decimal (10,4) | 
 | 
 | 
 | 
 | 
 | 
 | 
 | 
 | 
 | 
 | 
Notes: Value ghi tương tự bảng ghi tồn bên dưới | 
 | 
 | 
 | 
 | 
Ghi tồn kho NL theo GR detail (ghi nhận trước, sẽ có màn hình show dữ liệu bảng này. Note ngoài action này, còn nhiều action khác/nguồn khác ghi nhận/cập nhật vào bảng này)
Nguyên liệu | 
 | Tồn cần ghi | 
Tình trạng | Loại | → | Kho | Khu vực | Vị trí | Item | Lô | Tuổi | Màu | SL | Chiều dài | Tổng TL | TL đá | TL | Quy 99.99 | Phương thức quản lý tồn | 
Condition | Classification | 
 | SubWarehouse | Zone | Location | Item | LOT | Purity | Color | Qty | Lenght | Total Weight | Stone Weight | Metal Weight | 99.99 Equiv. | Track Mode | 
NL khách | Dẻ | → | [kho nhập NL đã kiểm] | NL Chờ xử | Dẻ KH | Mã Item NL khách
→Phụ lục A - Mã hóa | Mã Lô nhập NL đã kiểm
→Phụ lục A - Mã hóa | = "Tuổi - Seva" | N/A | N/A | N/A | = "Tổng TL - Seva" | = "TL đá - Seva" | = "TL - Seva" | = "Quy 99.99 - Seva" | W | 
NL khách | Hàng hồi nấu | → | [kho nhập NL đã kiểm] | NL Chờ xử | Hàng hồi | Mã Item NL khách
→Phụ lục A - Mã hóa | Mã Lô nhập NL đã kiểm
→Phụ lục A - Mã hóa | = "Tuổi - Seva" | N/A | N/A | N/A | = "Tổng TL - Seva" | = "TL đá - Seva" | = "TL - Seva" | = "Quy 99.99 - Seva" | W | 
NL khách | hàng hồi mới | → | [kho nhập NL đã kiểm] | NL Chờ xử | Hàng hồi | Mã Item NL khách
→Phụ lục A - Mã hóa | Mã Lô nhập NL đã kiểm
→Phụ lục A - Mã hóa | = "Tuổi - Seva" | N/A | N/A | N/A | = "Tổng TL - Seva" | = "TL đá - Seva" | = "TL - Seva" | = "Quy 99.99 - Seva" | W | 
Đơn hàng | Hàng hồi mới | → | [kho nhập NL đã kiểm] | TP Chờ sửa | Hàng hồi mới | Mã Item NL khách
→Phụ lục A - Mã hóa | Mã Lô nhập NL đã kiểm
→Phụ lục A - Mã hóa | = "Tuổi - Seva" | N/A | = SL Item | N/A | = "Tổng TL - Seva" | = "TL đá - Seva" | = "TL - Seva" | = "Quy 99.99 - Seva" | Q+W | 
Đơn hàng | Hàng gửi sửa | → | [kho nhập NL đã kiểm] | TP Chờ sửa | Hàng gửi sửa | Mã Item NL khách
→Phụ lục A - Mã hóa | Mã Lô nhập NL đã kiểm
→Phụ lục A - Mã hóa | = "Tuổi - Seva" | N/A | = SL Item | N/A | = "Tổng TL - Seva" | = "TL đá - Seva" | = "TL - Seva" | = "Quy 99.99 - Seva" | Q+W | 
#Ghi chú:TrackMode bao gồmW: chỉ quản lý trọng lượngQ+W: quản lý bằng số lượng và trọng lượngQ+W+H: quản lý bằng số lượng, trọng lượng và chiều dàiTrackMode ghi nhận nhằm phục vụ công tác nhập/xuất tồn, nhằm xác định key và dữ liệu cần đối chiếu khi ghi nhận hoặc trừ tồnVí dụ:Với record có TrackMode = W → Khi xuất kho, cần xác định trọng lượng xuất, trừ trọng lượng tương ứng khi xuấtVới record có TrackMode = Q+W → Khi xuất kho, cần xác định cả số lượng và trọng lượng, trừ số lượng và trọng lượng tương ứng khi xuất...Với thành phần nào không có ở TrackMode, khi ghi tồn → thành phần đó ghinullVD: Nếu record có TrackMode = W → Khi ghi tồn, trường Qty và Lenght =N/AIf:Phiếu NL không còn dòng nguyên liệu ở trạng thái: "Đang xử lý" / "Chờ xác nhận"Then:Hệ thống cập nhật trạng thái Phiếu tiếp nhận NL từ: "Đang thực hiện" sang → "Hoàn thành"3. THIẾT KẾ (UX/UI) *Link Figma:(Theo link mẫu của dự án)
4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES) *BR-01:Một GR chỉ bao gồm 1 loại nhập kho (công nợ/công ty mua/,...)
5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES) *5.1 Workflow validation5.2 Field Definition Table
Field Name (VN) | Field Name (EN) | Type | Required | Rules | 
Tính công nợ | Liability Impact | Checkbox | Read-only | 
Phân loại | Tình trạng | → | Tính công nợ | 
Dẻ | NL từ khách | → | Checked | 
Hàng hồi nấu | NL từ khách | → | Checked | 
Hàng hồi mới | NL từ khách | → | Checked | 
Hàng hồi mới | Đơn hàng | → | Unchecked | 
Hàng gửi sửa | Đơn hàng | → | Unchecked | 
 | 
Quy 99.99 - Công nợ điều chỉnh | 99.99 Equiv. Liability Adjustment | Decimal(10,4) | N | Chỉ show khi Tính công nợ = checked
Default = 0, enable cho phép editNếu, dòng NL là dẻ và có Phiếu xử lý chênh lệch→ = "Có tạp"."Quy 99.99 - Tổng khách bù"Notes: "Quy 99.99 - Tổng khách bù" ghi nhận giá trị "âm" | 
Quy 99.99 - Công nợ | Net 99.99 Equiv. Liability Receipt | Decimal(10,4) | Read-only | Chỉ show khi Tính công nợ = checked
= "Quy 99.99 - Seva" + "Quy 99.99 - Công nợ điều chỉnh"
Notes: "Quy 99.99 - Công nợ điều chỉnh" có thể mang giá trị âm/dương → Khi đó cộng đúng giá trị âm/dương của "Quy 99.99 - Công nợ điều chỉnh"
VD: 100.0000 + (-50.0000) = 50.0000Validate: {value} > = 0 | 
Giá công - Seva | Labour Cost (Seva) | Currency | N | Chỉ show khi: field "tình trạng" = đơn hàng | 
Khu vực nhập kho | Storage Zone | Dropdown | Y | Value = List danh sách khu vực thuộc [kho nhập NL đã kiểm]
Default:
Tình trạng | → | Kho | Khu vực | 
NL từ khách | → | [kho nhập NL đã kiểm] | NL chờ xử | 
Đơn hàng | → | [kho nhập NL đã kiểm] | TP chờ sửa | 
 | 
Ghi chú | Remarks | Text | N | Max 100 ký tự | 
6. GHI CHÚ CHO QCKiểm tra phiếu GR được tạo, kiểm tra TH 2 loại có tạo thành 2 phiếu riêngKiểm tra thông tin công nợKiểm tra bảng tồnKiểm tra các field SL, chiều dài, TL ở tồnLuật thép: Trọng lượng không được sai




# ✅CS1.E1.US-18_+[Nhận+NL+khách]+-+Xem+danh+sách.doc
--------------------------------------------------------------------------------

✅CS1.E1.US-18: [Nhận NL khách] - Xem danh sách✅CS1.E1.US-18: [Nhận NL khách] - Xem danh sách


