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