2. CHỈ SỐ THÀNH CÔNG (SUCCESS METRICS)
Chỉ số (Metric)
Giá trị Hiện tại (Baseline)
Giá trị Mục tiêu (Target)
Tra cứu thông tin xác nhận chênh lệch NL khách giao
Xác nhận ngoài hệ thống
Hard-block
nếu chưa duyệt tại hệ thống
Tra cứu thông tin NL khách giao không nhập kho
Lưu trữ excel và xử ngoài hệ thống
Lưu trữ thông tin và tra cứu trong hệ thống
Các phép tính thủ công mà người dùng cần làm ngoài hệ thống
> 3
< 3
, tự động tính và lưu trữ
Số lần chỉnh sửa trực tiếp dữ liệu ở DB do lỗi thao tác
Cho phép sửa trực tiếp tại DB
0 lần
sửa DB; 100% qua Approval Workflow
Thời gian trung bình để truy vết nguồn gốc của một Lô nguyên liệu
Tra cứu thủ công, có thể mất nhiều thời gian và phụ thuộc vào kinh nghiệp người dùng
< 1 phút, tra cứu qua
Gia phả (Ancestry)
& Lot Tracking
Tra cứu thông tin tồn kho khả dụng
Tra cứu tồn khả dụng mất nhiều thời gian so sánh đối chiếu
Real-time
24/7 cho cả Finding & Metal
Thông báo/Cảnh báo
Không
Thông báo được gửi ngay khi phát sinh tác vụ/cảnh báo
Tra cứu thông tin chuyến và lịch sử giao hàng Thành phẩm cho khách
Không
Lưu trữ và tra cứu trong hệ thống
3. BỐI CẢNH NGƯỜI DÙNG (USER CONTEXT)
Hạng mục
Mô tả
Chân dung người dùng (Personas)
Ban Giám Đốc.
Trưởng bộ phận MC
Tổ trưởng MC & MC
Phòng Kinh doanh
Phòng Kế hoạch sản xuất
Phòng Kế hoạch chế tác
Phòng Kế toán
Admin hệ thống.
Kịch bản người dùng (User Scenarios)
A. Ban Giám Đốc
Theo dõi tình hình sản xuất, tiến độ đơn hàng, và tình trạng tồn kho.
B. Trưởng bộ phận MC
Quản lý công việc của nhân viên MC, bao gồm giám sát việc tiếp nhận, kiểm tra, phân loại nguyên liệu.
Cấu hình các mức chênh lệch chấp nhận được trong quá trình tiếp nhận nguyên liệu từ khách.
Kiểm soát các phiếu nhập và phiếu trả nguyên liệu để đảm bảo quy trình chính xác.
Kiểm soát tồn kho, hao hụt và thu hồi
Xem báo cáo về các hoạt động và tình trạng nguyên liệu trong kho.
C. MC Nguyên liệu
Tiếp nhận, kiểm tra, phân loại và xử lý nguyên liệu từ khách hàng (bao gồm trả nguyên liệu)
Tiếp nhận và xử lý nguyên liệu nhận từ sản xuất.
Tiếp nhận và xử lý nguyên liệu nhận từ thu hồi.
Xử lý chuẩn bị nguyên liệu và cấp nguyên liệu đúc.
Kiểm soát và điều phối các phiếu xử lý nguyên liệu (Shooting Order/Alloy Order) và phiếu đúc (Casting Order/PHTJ Order/HTJ Order).
Quản lý và kiểm soát tồn các kho nguyên liệu (Kho NL khách, Kho NL, Kho Hội)
D. MC Tiền Sản xuất
Tiếp nhận và điều phối đơn hàng ở công đoạn Tiền Sản xuất
Quản lý và cấp phát nguyên liệu tiêu hao cho công nhân (Vảy hàn, Fill laser)
Tiếp nhận, kiểm soát và trả vụn về Kho NL
E. MC Đồng bộ
Quản lý nhập kho các nguyên liệu từ các công đoạn tiền sản xuất/sản xuất, đảm bảo không có sai sót trong quá trình nhập kho.
Cấp phát nguyên liệu cho các đơn hàng đưa đến các công đoạn sản xuất, đồng thời theo dõi tình trạng kho và các yêu cầu cấp phát nguyên liệu.
Kiểm soát tình trạng nguyên liệu trong kho, bao gồm việc phân loại nguyên liệu, kiểm tra tồn kho và điều chuyển nguyên liệu khi cần thiết.
F. MC Sản xuất
Tiếp nhận và điều phối đơn ở công đoạn Sản xuất
Quản lý và cấp phát nguyên liệu tiêu hao cho công nhân (Vảy hàn, Fill laser)
Tiếp nhận, kiểm soát và trả vụn về Kho NL
G. MC Đóng gói
Tiếp nhận, kiểm tra và nhập Kho Thành phẩm
Quản lý và kiểm soát tồn Kho Thành phẩm
Thực hiện soạn hàng xuất kho cho đơn hàng khách và kiểm soát phiếu giao hàng
Kiểm soát giá thành thành phẩm cho hóa đơn
H. Phòng Kinh doanh
Trao đổi với khách hàng và ra quyết định xử lý nguyên liệu khác khi có chênh lệch về trọng lượng hoặc chất lượng nếu vượt quá mức cho phép.
Tiếp nhận, kiểm tra và nhập Kho Mẫu
Quản lý và kiểm soát tồn Kho Mẫu
I. Kế toán
Tiếp nhận và xử lý hóa đơn đã giao hàng thành công
J. Kế hoạch chế tác
Tiếp nhận, kiểm tra và nhập Kho Proto
Quản lý và kiểm soát tồn Kho Proto
K. Kế hoạch sản xuất
Theo dõi tồn Kho NL
Theo dõi và kiểm soát tồn Trạm Đồng bộ
Theo dõi thành phẩm chờ sửa từ khách và thực hiện tạo lệnh Repair
Theo dõi khai báo thiếu NL (thiếu Cast/MTO/Finding) tại Đồng bộ và thực hiện tạo lệnh B Order/HTJ Order
M. Admin hệ thống
Admin hệ thống cần phân quyền người dùng linh hoạt và đúng chức năng.
Admin hệ thống cần theo dõi nhật ký hệ thống để truy vết khi có sự cố hoặc sai lệch.
