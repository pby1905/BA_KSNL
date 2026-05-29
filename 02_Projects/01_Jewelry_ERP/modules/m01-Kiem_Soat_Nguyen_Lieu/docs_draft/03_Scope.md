4. PHẠM VI & LỘ TRÌNH (SCOPE & RELEASE PLAN)
Hạng mục
Mô tả
Trong phạm vi (In-Scope)
1. Quản lý Kho Nguyên liệu & Xử lý đầu vào (Control Stage #1)
Tiếp nhận:
Nhận NL từ khách, mua dẻ/hội, xử lý chênh lệch trọng lượng/tuổi vàng, ghi nhận công nợ
.
Xử lý Vụn:
Quản lý vụn chờ nhập, phân loại và nhập kho.
Xử lý Nguyên liệu:
Tạo và quản lý phiếu xử, phiếu phân kim.
Cấp phát:
Cấp nguyên liệu cho đúc Casting, đúc HTJ, tạo phiếu chuyển chế.
Quản lý kho:
Theo dõi tồn kho NL, kho Hội, và thực hiện chuyển kho nội bộ.
2. WIP - Kiểm soát dòng chảy sản xuất (Control Stages #2, #3, #4)
Phạm vi bao gồm việc theo dõi và điều phối vật tư qua 3 giai đoạn: Tiền sản xuất (TSX), Trạm Đồng bộ, và Sản xuất (SX).
Theo dõi đơn hàng:
Theo dõi trạng thái đơn (Casting, HTJ, Sales, Proto, Sample, Repair, G Order, Finding Order)
.
Điều phối:
Quản lý việc nhận đơn, giữ đơn và chuyển đơn giữa các bộ phận.
Quản lý Trạm Đồng bộ (Hub trung tâm):
Nhập/Xuất kho tại trạm (đóng bag, cấp finding/cast, cấp vảy hàn).
Khai báo thiếu nguyên liệu (thiếu Cast/Finding) và xử lý (tạo
B Order
).
Quản lý định mức tồn kho an toàn cho Finding/Vật tư tiêu hao.
Quản lý tồn tại trạm và xử lý hàng không đạt (tạo Finding Order/chuyển tồn thành vụn).
Quản lý Vụn & Hao hụt:
Thu hồi vụn và nguyên liệu tiêu hao từ công nhân/bộ phận sản xuất trả về hoặc vụn được chuyển từ tồn tại Trạm Đồng bộ.
3. Đầu ra - Thành phẩm & Mẫu (Control Stages #5, #6)
Kho Thành phẩm:
Nhập kho thành phẩm từ sản xuất.
Tạo phiếu xuất kho và phiếu giao hàng.
Tích hợp Kế toán:
Tự động tạo hóa đơn từ phiếu giao hàng và tính giá
.
Kho Mẫu:
Quản lý nhập/xuất/tồn cho hàng Mẫu (Sample) và hàng làm thử (Proto), bao gồm xuất mượn/xuất tặng.
4. Kiểm soát Hao hụt & Thu hồi (Control Stage #7)
Kỳ thu hồi:
Thiết lập và đóng kỳ thu hồi (chốt sổ).
Theo dõi Hao hụt:
Tính toán hao hụt theo từng Đội công nhân (Worker Team) và từng cá nhân.
Quy trình Thu hồi:
Quản lý phiếu thu hồi qua các công đoạn xử lý thu hồi: Đốt -> Phân kim -> Xử lý -> Nhập lại kho NL.
5. Các chức năng Quản trị & Hỗ trợ
Kiểm kê (#8):
Tạo phiếu kiểm kho, chặn giao dịch toàn hệ thống khi đang kiểm đếm
.
Điều chỉnh (#9):
Quy trình đề xuất và phê duyệt điều chỉnh dữ liệu sai lệch (nhầm tuổi, nhầm trọng lượng, nhầm số lượng) có phân quyền người duyệt.
Kiểm soát & Báo cáo (#10):
Báo cáo Xuất - Nhập - Tồn (NL, Hội, Thành phẩm, Mẫu).
Báo cáo Hao hụt & Thu hồi.
Báo cáo Vòng quay vàng.
Tra cứu nguồn gốc (Tree Tracking, Lot Tracking).
Cấu hình & Tích hợp (#11):
Quản lý danh mục (NL, Hội, Khu vực kiểm soát, Đội công nhân).
Tích hợp phần cứng:
Kết nối cân điện tử, máy quét mã vạch, máy đo phổ và máy in
Ngoài phạm vi (Out-of-Scope)
1. Kế hoạch Sản xuất
Module
MC (Material Control)
có bao gồm
một số nghiệp vụ cụ thể của
Phòng Kế hoạch sản xuất (KHSX)
, nhưng chủ yếu tập trung vào khía cạnh
kiểm soát vật tư, định mức tồn kho và xử lý các sự cố thiếu hụt/sửa chữa
, không bao gồm toàn bộ quy trình lập kế hoạch sản xuất tổng thể.
2. Quy trình Thực thi Sản xuất
MC không trực tiếp điều khiển máy móc hay ghi nhận các thao tác kỹ thuật tại Work Center (WC). MC chỉ thực hiện nhiệm vụ "Handshake" (Bắt tay dữ liệu): Nhận kết quả đầu ra từ Module IOOO (như trọng lượng sau đúc, trạng thái hoàn thành) để cập nhật tồn kho, kiểm soát TL và ghi nhận hao hụt.
3. Quản trị Nhân sự & Tiền lương
Hệ thống chỉ quản lý cấu trúc Worker Team và danh sách nhân sự kế thừa số liệu thu hồi. Các nghiệp vụ tính lương theo sản phẩm, bảo hiểm hay hồ sơ nhân sự thuộc phân hệ HR.
4. Kế toán
Module MC tập trung vào việc
tự động hóa dữ liệu đầu vào cho kế toán
(hóa đơn, số liệu công nợ) từ các hoạt động, thay vì thực hiện các bút toán kế toán tài chính phức tạp.
Lộ trình phát hành (Release Plan)
