MC-1. Product Requirement
MC-1. Product Requirement
Metadata
Thuộc tính
Giá trị
Ghi chú
Owner
Nguyễn Hữu Nghĩa
Người chịu trách nhiệm về tài liệu
Stakeholders
Sếp Nhân, Sếp Chính, Sếp Sỹ Phương, Sếp Đồng, Chị Thuận, Chị Liên, Chị Dung, Chị Thủy, Chị Huệ, Chị Lan Anh, Chị Hồi, Chị Hải, Chị Lê
Tên những người review và đóng góp ý kiến
Status
InProgress
Jira Epic
Liên kết đến Epic tương ứng để theo dõi tiến độ
Target Release
Version 1.0 (MVP) - Tháng 6/2026
Phiên bản hoặc thời điểm dự kiến ra mắt
Version History
Version
Ngày
Người thay đổi
Ghi chú thay đổi
1.0
09 Feb 2026
Nguyễn Hữu Nghĩa
Tạo mới
1. TỔNG QUAN (OVERVIEW)
Hạng mục
Mô tả
Tuyên bố Vấn đề (Problem Statement)
Các quy trình nghiệp vụ hiện trạng đã và đang được xử lý tốt với phần mềm ERP WF
Tuy nhiên:
Bối cảnh cần chuyển đổi hệ thống, đồng bộ kiến trúc, ngôn ngữ và kết nối các hệ thống toàn công ty.
Người dùng còn sử dụng và xác nhận thông tin quan trọng bên ngoài hệ thống (VD: chênh lệch tuổi, có tạp chất nguyên liệu khách giao,...).
Quy trình thu hồi vàng còn thực hiện độc lập ở phần mềm khác (Base) và user nhập liệu lại vào phần mềm.
Có sử dụng lưu trữ thông tin bên ngoài (VD: thẻ kho) và thao tác tính toán bên ngoài hệ thống (VD: tỷ lệ chuyển chế, tính giá thành phẩm...)
Tồn tại tình trạng chỉnh sửa dữ liệu trọng lượng khi có sai sót trọng lượng chưa có phê duyệt trên hệ thống.
Giải pháp đề xuất (Proposed Solution)
Triển khai Module Kiểm soát Nguyên liệu nhằm
Kiểm soát toàn bộ dòng chảy của nguyên liệu:
Từ khi nhận từ khách hàng cho đến khi nhập kho/trả nguyên liệu khách,
xử lý nguyên liệu,
kiểm soát tiền sản xuất,
trạm đồng bộ,
kiểm soát sản xuất,
kiểm soát hao hụt cùng quy trình thu hồi,
kiểm soát thành phẩm bao gồm cả sample và proto,
cho đến xuất kho giao khách.
Kiểm soát chênh lệch nguyên liệu khách và ghi nhận quyết định và xác nhận được đưa ra.
Kiểm soát điều chỉnh sai sót nhập liệu bằng cách phê duyệt bởi người có thẩm quyền.
Theo dõi, quản lý và nhận biết tồn khả dụng trong sản xuất
Song song đó thiết kế giảm thiểu nhất thao tác người dùng và hỗ trợ tính toán/gợi bằng các cấu hình hệ thống (tỷ lệ chuyển chế, tính giá,..)
Truy xuất nguồn gốc (Traceability)
thông qua
Lot Tracking
và
Tree Number Tracking
.
Mục tiêu Nghiệp vụ (Business Goal)
Nâng cao hiệu quả xử lý nguyên liệu.
Giảm thiểu thao tác, ghi nhận và xử lý ngoài hệ thống.
Tăng cường khả năng theo dõi và kiểm soát dòng chảy nguyên liệu.
Tăng cường minh bạch, giảm thiểu xác nhận ngoài hệ thống và sửa chữa dữ liệu trực tiếp.
Thiết lập một trục xương sống dữ liệu minh bạch, chuyển đổi từ cơ chế "ghi nhận sau" sang "kiểm soát tại nguồn" và "phê duyệt theo luồng".
