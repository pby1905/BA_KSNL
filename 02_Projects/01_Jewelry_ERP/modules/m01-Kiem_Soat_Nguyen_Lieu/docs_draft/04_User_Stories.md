5. YÊU CẦU CHI TIẾT (DETAILED REQUIREMENTS -
(Functional Requirement ) & User Stories)
No
Tên Luồng / Tính năng
Mô tả (Description)
Thiết kế (UX/UI)
User Stories
Quy tắc Nghiệp vụ (Business Rules) liên quan
CONTROL STAGE #1: KHO NL & KIỂM SOÁT XỬ LÝ NGUYÊN LIỆU
Epic
Nhận NL từ khách/mua
Tiếp nhận NL
Tiếp nhận và kiểm tra NL từ khách (NL khách trả / từ PO mua dẻ/hội)
Xác nhận bao bì
Kiểm tra trọng lượng chi tiết
Kiểm tra dẻ
Kiểm tra hàng hồi nấu/hàng hồi mới (nguyên liệu)
Kiểm tra hàng hồi mới/hàng gửi sửa (thành phẩm chờ sửa)
Kiểm tra hội
Xử lý chênh lệch
Phân loại và Nhập kho (xử lý ghi nhận công nợ được tính)
US-01:
Là MC NL, tôi muốn tạo phiếu nhận NL từ khách, bao gồm thông tin bao bì của khách và bao bì thực tế
US-02:
Là MC NL, tôi muốn hệ thống chặn thao tác và gửi thông báo đến người duyệt chênh lệch đã cấu hình khi phát sinh chênh lệch vượt mức đã cấu hình
US-03:
Là người duyệt chênh lệch (Phòng mua hàng/Trưởng phòng MC...), tôi muốn nhận thông báo và đến chi tiết thông tin phiếu nhập
US-04:
Là người duyệt chênh lệch, tôi muốn thực hiện phê duyệt, bao gồm: chấp nhận chênh lệch và yêu cầu trả hàng
US-05:
Là MC NL, tôi muốn tạo phiếu trả hàng (chênh lệch TL tổng cả bao bì) khi có yêu cầu trả hàng
US-06:
Là MC NL, tôi muốn ghi nhận thông tin NL khách (phân loại, TL...) và so sánh TL khách với TL thực tế sau khi mở niêm phong (đã xác nhận bao bì) và tạo Lô tự động
US-07:
Là MC NL, tôi muốn hệ thống chặn thao tác của hàng có chênh lệch vượt mứt cấu hình và gửi thông báo đến người duyệt chênh lệch
US-08:
Là MC NL, tôi muốn ghi nhận thông tin đo quang phổ cho dẻ
US-09:
Là MC NL, tôi muốn ghi nhận thông tin (số xi trừ dự kiến → TL 9999 khách cần trả) khi đo quang phổ có tạp chất
US-10:
Là MC NL, tôi muốn hệ thống chặn thao tác của hàng có chênh lệch tuổi vượt mức hoặc có tạp và gửi thông báo đến người duyệt chênh lệch
US-11:
Là MC NL, tôi muốn ghi nhận thông tin Kiểm tem - Tính đá (Ghi nhận TL đá thực) cho hàng hồi nấu/hàng hồi mới
US-12:
Là MC NL, tôi muốn hệ thống chặn thao tác của hàng có chênh lệch TL đá vượt mức hoặc có sai tem và gửi thông báo đến người duyệt chênh lệch
US-13:
Là MC NL, tôi muốn kiểm mã hàng (ghi nhận thông tin các mã hàng thuộc line, TL cùng giá công) cho hàng hồi mới/hàng gửi sửa (loại đơn hàng)
US-14:
Là MC NL, tôi muốn hệ thống chặn thao tác của hàng có chênh lệch TL, giá công hoặc hàng sai tem và gửi thông báo đến người duyệt chênh lệch
US-15:
Là người duyệt chênh lệch, tôi muốn nhận thông báo mỗi khi phát sinh chênh lệch ở công đoạn kiểm tra chi tiết (theo từng line hàng)
US-16:
Là người duyệt chênh lệch, tôi muốn thực hiện phê duyệt, bao gồm: chấp nhận chênh lệch và yêu cầu trả hàng (theo từng line hàng)
US-17:
Là MC NL, tôi muốn tạo phiếu trả hàng (chênh lệch TL tổng cả bao bì) khi có yêu cầu trả hàng (theo từng line hàng, có thể tạo phiếu với nhiều line)
US-18:
Là MC NL, tôi muốn nhập kho các line đã có đầy đủ thông tin TL vào kho
US-19:
Là MC NL, tôi muốn ghi nhận tách line hàng hồi mới cho NL và đơn hàng khi nhập kho
US-20:
Là MC NL, tôi muốn ghi nhận công nợ vàng NL cho khách và giá công cho đơn hàng khách
BR-01: Số Lô là duy nhất (không trùng với số Lô đã có) và tất cả line hàng trong cùng đơn hàng nhập có cùng Lô
BR-02: Hệ thống tự nhận diện có tạp khi dẻ có thành phần ngoài: Bạc, Đồng, Kẽm
BR-03: Mã hàng phải tồn tại
BR-04: Số bag phải tồn tại
BR-05: Hàng sai tem, không bắt buộc mã hàng
BR-06: Số PO khách không bắt buộc
BR-07: Những line đang chờ duyệt không thể nhập kho
BR-08: Những line chưa có thông tin xử lý tương ứng (đo phổ, tính đá, kiểm mã hàng) không thể nhập kho
Phiếu nhập
Quản lý danh sách NL đã nhập kho từ khách và phân loại nguyên liệu
Thành phẩm chờ sửa
Hàng hồi mới
Hàng hồi nấu
Nguyên liệu chờ xử
Dẻ
Hàng hồi
Nguyên liệu chờ phân kim
Dẻ
Hàng hồi
Hội
US-01:
Là MC NL, tôi muốn tìm kiếm, xem phiếu nhập
US-02:
Là MC NL, tôi muốn xem chi tiết thông tin phiếu nhập
Trả NL
Quản lý phiếu trả hàng
Xác nhận trả hàng
Hủy phiếu trả hàng
US-01:
Là MC NL, tôi muốn tìm kiếm, xem và theo dõi trạng thái phiếu trả hàng
US-02:
Là MC NL, tôi muốn xem chi tiết thông tin phiếu trả hàng
US-03:
Là MC NL, tôi muốn in nhãn trả hàng và biên bản trả hàng
US-04:
Là MC NL, tôi muốn xác nhận trả hàng
US-05:
Là MC NL, tôi muốn hủy phiếu trả hàng
BR-01: Chỉ có thể Hủy phiếu ở trạng thái chờ trả, khi hủy phiếu NL cần quay
Cấu hình
Cấu hình mức chênh lệch
Người duyệt
Mức chênh lệch bao bì
Mức chênh lệch dẻ, hàng hồi, hàng hồi mới, hàng gửi sửa
US-01:
Là TBP MC, tôi muốn cấu hình danh sách người phê duyệt chênh lệch NL khi tiếp nhận NL từ khách
US-02:
Là TBP MC, tôi muốn cấu hình mức chênh lệch TL bao bì cho phép
US-03:
Là TBP MC, tôi muốn cấu hình mức chênh lệch TL, tuổi dẻ; TL đá hàng hồi; TL, tuổi, giá công hàng hồi mới/hàng gửi sửa
BR-01: Mỗi loại chênh lệch cần có ít nhất 1 người duyệt
Epic
Nhận Vụn
Vụn chờ nhập
Quản lý vụn chờ nhập
Danh sách vụn chờ nhập
Phân loại và nhập kho
US-01:
Là MC NL, tôi muốn xem danh sách vụn được gửi từ MC về Kho NL
US-02:
Là MC NL, tôi muốn xem chi tiết thông tin vụn
US-03:
Là MC NL, tôi muốn thực hiện nhận vụn bằng cách phân loại và nhập kho NL
US-04:
Là MC NL, tôi muốn nhận thông báo khi có vụn chờ nhập được gửi đến
BR-01: Mỗi vụn trả về cần có mã tham chiếu đến đơn phát sinh
Phiếu nhập kho
Quản lý danh sách phiếu nhập vụn vào kho và phân loại nguyên liệu
NL chờ xử
NL chờ phân kim
NL đúc HTJ
NL đúc Cast
Au 99.99
US-01:
Là MC NL, tôi muốn tìm kiếm và xem danh sách phiếu nhập vụn
US-02:
Là MC NL, tôi muốn xem chi tiết thông tin phiếu nhập
Epic
Phiếu sửa hàng (Repair Order/G Order) - KHSX
Hàng chờ sửa
Quản lý hàng chờ sửa
Danh sách và trạng thái hàng
Hàng hồi mới
Hàng gửi sửa
Hàng mẫu
Tạo phiếu sửa
Soạn hàng cho phiếu sửa
US-01:
Là KHSX, tôi muốn xem danh sách các mã hàng chờ xử lý (mã hàng đã nhập, chưa tạo phiếu sửa)
US-02:
Là KHSX, tôi muốn tìm kiếm, sắp xếp, lọc các mã hàng chờ xử lý
US-03:
Là KHSX, tôi muốn tạo phiếu sửa nguyên liệu cho các mã hàng chờ xử lý tương ứng (có thể tạo cùng lúc nhiều phiếu) và ghi nhận WC cần đến
US-04:
Là MC, tôi muốn soạn hàng cho phiếu sửa (ghi nhận TP vào phiếu)
Phiếu sửa
Quản lý phiếu sửa
Danh sách và trạng thái phiếu
In nhãn
Hủy phiếu
US-02:
Là MC NL, tôi muốn in phiếu sửa nguyên liệu
US-03:
Là KHSX, tôi muốn tìm kiếm, xem, theo dõi trạng thái và công đoạn xử lý của phiếu sửa
Cấu hình và thông báo
Cấu hình thông báo nhắc xử lý Item chưa tạo phiếu
US-01:
Là KHSX, tôi muốn cấu hình thông báo nhắc xử lý hàng chờ sửa khi hàng chưa được xử lý sau các mốc thời gian.
US-02:
Là KHSX, tôi muốn nhận thông báo cho hàng chưa được xử lý sau các mốc thời gian đã cấu hình
Epic
Xử lý NL
Quản lý NL chờ xử lý
Quản lý danh sách NL nhận từ khách chưa xử lý
Tạo phiếu xử lý nguyên liệu (xử, phân kim)
Tự động đề xuất hội
US-01:
Là MC NL, tôi muốn tìm kiếm, lọc, xem danh sách các NL chờ xử lý (NL nhận từ khách, từ sản xuất, từ thu hồi)
US-02:
Là MC NL, tôi muốn tạo phiếu xử cho các NL được chọn
US-03:
Là MC NL, tôi muốn tạo phiếu nấu NL (bao gồm NL chờ xử lý và hội)
US-04:
Là MC NL, tôi muốn tạo phiếu phân kim từ phiếu nấu NL
US-05:
Là MC NL, tôi muốn hệ thống tự động đề xuất hội theo tỷ lệ đã cấu hình
Quản lý phiếu xử
Quản lý danh sách phiếu xử
Cập nhật thông tin NL sau Out từ IOOO
Phân loại và nhập kho
Au 99.99
NL chờ xử
NL chờ phân kim
NL Đúc Cast
NL Đúc HTJ
Hủy phiếu
US-01:
Là MC NL, tôi muốn tìm kiếm, lọc, xem, theo dõi trạng thái và công đoạn xử lý của phiếu xử
US-02:
Là MC NL, tôi muốn xem thông tin NL sau khi xử xong (thông tin NL hoàn thành từ WC được ghi nhận ở Module IOOO)
US-03:
Là MC NL, tôi muốn phân loại và nhập kho NL sau xử (tạo Lô)
US-04:
Là MC NL, tôi muốn hủy phiếu xử
US-05:
Là MC NL, tôi muốn in nhãn phiếu xử
Quản lý phiếu phân kim
Quản lý danh sách phiếu phân kim
Cập nhật thông tin NL sau Out từ IOOO
Phân loại và nhập kho
Au 99.99
NL chờ xử
NL chờ phân kim
Hội
Hủy phiếu
US-01:
Là MC NL, tôi muốn tìm kiếm, lọc, xem, theo dõi trạng thái và công đoạn xử lý của phiếu nấu/phiếu phân kim
US-02:
Là MC NL, tôi muốn xem thông tin NL mỗi khi thay đổi trạng thái/TL (từ IOOO)
US-03:
Là MC NL, tôi muốn in nhãn phiếu nấu/phiếu phân kim
US-04:
Là MC NL, tôi muốn hủy phiếu nấu
US-05:
Là MC NL, tôi muốn phân loại và nhập kho NL sau phân kim (tạo Lô)
Cấu hình
Cấu hình tỷ lệ hội dùng cho phân kim
US-01:
Là Trưởng phòng MC/Tổ trưởng MC Nguyên liệu, tôi muốn cấu hình tỷ lệ hội dùng cho phân kim
Epic
Cấp NL
Yêu cầu cấp NL
Quản lý danh sách các phiếu yêu cầu cấp NL
Phiếu đúc Cast - Casting Order
Phiếu đúc HTJ - PHTJ Order (MFtempOrder)
US-01:
Là MC NL, tôi muốn tìm kiếm, sắp xếp, lọc và xem chi tiết danh sách các yêu cầu nguyên liệu cho cây thông và cho bag HTJ
US-02:
Là MC NL, tôi muốn nhận được thông báo khi có yêu cầu cấp NL mới
NL sẵn sàng cho SX
Quản lý NL sẵn sàng cho sản xuất (NL tồn đã xử, Au 99.99, hội)
Soạn NL cấp cho phiếu yêu cầu
Tạo phiếu chuyển chế NL
Tự động đề xuất hội
US-01:
Là MC NL, tôi muốn tìm kiếm, sắp xếp, lọc danh sách NL sẵn sàng cho sản xuất
US-02:
Là MC NL, tôi muốn soạn NL cấp cho yêu cầu cấp NL (cây thông/bag HTJ)
US-03:
Là MC NL, tôi muốn hệ thống gợi ý hội dùng cho chuyển chế theo tỷ lệ được cấu hình
US-04:
Là MC NL, tôi muốn tạo phiếu chuyển chế NL
US-05:
Là MC NL, tôi muốn hệ thống tự động đề xuất hội dựa trên tỷ lệ đã cấu hình
US-06:
Là MC NL, tôi muốn tạo lại phiếu chuyển chế NL cho yêu cầu đã cấp NL có phát sinh đúc sai
Chuyển chế NL
Quản lý danh sách phiếu chuyển chế được tạo
US-01:
Là MC NL, tôi muốn in nhãn chuyển chế NL
US-02:
Là MC NL, tôi muốn xem thông tin NL sau khi chuyển chế xong (từ IOOO)
US-03:
Là MC NL, tôi muốn phân loại và nhập NL vào kho
Cấp NL
Cấp NL sau chuyển chế cho phiếu yêu cầu
Tạo phiếu cấp NL
Nhập lại NL đúc sai về kho
Cấp lại NL mới (quay lại chuyển chế NL mới và cấp lại)
US-01:
Là MC NL, tôi muốn tạo phiếu cấp NL, cấp NL đã nhập kho sau chuyển chế cho SX
US-02:
Là MC NL, tôi muốn in nhãn cấp NL
US-03:
Là MC NL, tôi muốn nhập lại NL đã đúc sai về kho Metal và cấp lại NL mới (chuyển chế → đúc lại)
Cấu hình
Cấu hình tỷ lệ hội dùng cho chuyển chế
US-01:
Là Trưởng phòng MC/Tổ trưởng MC Nguyên liệu, tôi muốn cấu hình tỷ lệ hội dùng cho chuyển chế
Epic
Tồn kho
Kho NL khách
Quản lý tồn kho NL khách (đang xử lý) theo phân loại
Chờ nhập
Nguyên liệu
TP chờ sửa
Chờ trả
Nguyên liệu
TP chờ sửa
US-01:
Là MC NL, tôi muốn tìm kiếm, xem tồn Kho NL khách
Kho NL
Quản lý tồn kho NL theo phân loại
NL chờ xử
Dẻ KH
Hàng hồi
Từ SX
NL chờ phân kim
NL AU 0-59
NL AU 60-99
Fine Gold
Fine Gold
NL Đúc
NL Đúc Cast
NL Đúc HTJ
TP chờ sửa
Hàng hồi mới
Hàng hồi nấu
Hàng mẫu
US-01:
Là MC NL, tôi muốn tìm kiếm, xem tồn Kho NL
Kho hội
Hội Lưu trữ
AG/CU/STEEL/INOX
Phụ gia
Hội hàng ngày
AG/CU/STEEL/INOX
Phụ gia
Hội chờ nhập
Hội chờ trả
US-01:
Là MC NL, tôi muốn tìm kiếm, xem tồn Kho Hội
Epic
Chuyển kho
Chuyển kho hội
Quản lý việc điều chuyển hội
Chuyển hội giữa khu vực lưu trữ và hàng ngày
Lịch sử điều chuyển
US-01:
Là MC NL, tôi muốn thực hiện chuyển hội từ khu vực "Hội lưu trữ" sang khu vực "Hội hàng ngày" và ngược lại
US-02:
Là MC NL, tôi muốn tìm kiếm và xem lịch sử điều chuyển nguyên liệu
CONTROL STAGE #2: KIỂM SOÁT TIỀN SẢN XUẤT
Epic
Theo dõi đơn
Casting Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái Casting Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử Casting Order
PHTJ Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái PHTJ Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử PHTJ Order
HTJ Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái HTJ Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử HTJ Order
Sales Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái Sales Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử Sales Order
Proto Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái Proto Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử Proto Order
Sample Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái Sample Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử Sample Order
Repair Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái Repair Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử Repair Order
G Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái G Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử G Order
B Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái B Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử B Order
Epic
Điều phối
Đơn đang giữ
Xem danh sách đơn đang giữ
Đơn MC đang giữ
Đơn ở WC thuộc khu vực kiểm soát
US-01:
Là MC, tôi muốn xem danh sách đơn mình đang giữ và đưa vào WC
US-02:
Là Tổ trưởng MC, tôi muốn xem danh sách đơn thuộc khu vực kiểm soát của tôi
US-03:
Là MC, tôi muốn xem chi tiết đơn
Nhận đơn
Danh sách và trạng thái đơn chờ nhận
Xác nhận nhận đơn
Lịch sử nhận đơn
US-01:
Là MC, tôi muốn xem danh sách đơn chờ nhận (được chuyển từ MC khác)
US-02:
Là Tổ trường MC, tôi muốn xem danh sách đơn chờ nhận thuộc khu vực kiểm soát của tôi
US-03:
Là MC, tôi muốn xác nhận nhận đơn
US-04:
Là MC, tôi muỗn xem lịch sử nhận đơn
US-05:
Là MC, tôi muốn nhận thông báo khi có đơn được gửi đến
Chuyển đơn
Danh sách và trạng thái đơn đang chuyển
Chuyển đơn
Hủy chuyển đơn
Lịch sử chuyển đơn
US-01:
Là MC, tôi muốn xem danh sách đơn đang chuyển (chuyển sang MC khác)
US-02:
Là Tổ trưởng MC, tôi muốn xem danh sách đơn đang chuyển thuộc khu vực kiểm soát của tôi
US-03:
Là MC, tôi muốn chuyển đơn sang khu vực kiểm soát khác
US-04:
Là MC, tôi muốn chuyển đơn đến trạm đồng bộ
US-05:
Là MC, tôi muốn hủy chuyển đơn
US-06:
Là MC, tôi muốn xem lịch sử chuyển đơn
Epic
Vụn
Vụn đang giữ
Quản lý vụn
Danh sách vụn đang giữ
Chuyển vụn cho MC khác
Trả vụn
US-01:
Là MC, tôi muốn xem danh sách vụn đang giữ
US-02:
Là Tổ trưởng MC, tôi muốn xem danh sách vụn của MC toàn khu vực kiểm soát của tôi
US-03:
Là MC, tôi muốn tạo yêu cầu trả vụn tôi đang giữ
US-04:
Là Tổ trường MC, tôi muốn tạo yêu cầu trả vụn cho toàn bộ vụn trong khu vực kiểm soát của tôi
Trả vụn
Danh sách quản lý yêu cầu trả vụn
Danh sách yêu cầu trả vụn
Hủy yêu cầu trả vụn
US-01:
Là MC, tôi muốn xem danh sách yêu cầu trả vụn của tôi
US-02:
Là MC, tôi muốn xem danh sách yêu cầu trả vụn của MC toàn khu vực kiểm soát của tôi
US-03:
Là MC, tôi muốn hủy yêu cầu trả vụn
US-04:
Là MC, tôi muốn nhận được thông báo khi yêu cầu trả vụn bị từ chối
CONTROL STAGE #3: TRẠM ĐỒNG BỘ
Epic
Xử lý đơn
Tiếp nhận đơn
Danh sách đơn được gửi từ MC đến trạm đồng bộ chờ nhận
Bao gồm các đơn:
Casting Order
PHTJ Order
HTJ Order
Sales Order
Proto Order
Sample Order
Repair Order
G Order
B Order
Finding Order
Các tính năng
Danh sách và theo dõi trạng thái
Lọc các đơn được gửi đến trạm đồng bộ chờ nhận
US-01:
Là MC Đồng bộ, tôi muốn tìm kiếm, xem và theo dõi trạng thái đơn hàng được gửi đến trạm đồng bộ
US-02:
Là MC Đồng bộ, tôi muốn xem chi tiết đơn hàng
Nhập kho
Quản lý NL nhập vào trạm đồng bộ
Đóng bag - nhận NL
Nhập Cast
Nhập Finding
Nhập NL tiêu hao
Nhập Vụn
Nhập NL (không đóng bag)
Nhập Finding
Trả Casting Order → chọn MC + công đoạn
Lịch sử nhập kho
US-01:
Là MC Đồng bộ, tôi muốn thực hiện đóng bag, phân loại hàng và nhập NL vào Trạm Đồng bộ
US-02:
Là MC Đồng bộ, tôi muốn nhận NL từ bag (không đóng bag), phân loại hàng và nhập NL vào Trạm Đồng bộ
US-03:
Là MC Đồng bộ, tôi muốn tìm kiếm, xem lịch sử nhập NL
US-04:
Là MC Đồng bộ, tôi muốn trả Casting Order về MC TSX
Xuất kho
Quản lý NL xuất ra khỏi trạm đồng bộ
Cấp NL cho đơn
Cấp Cast
Cấp Finding
Xuất đổi bể
Lịch sử xuất kho
US-01:
Là MC Đồng bộ, tôi muốn cấp (xuất kho) NL cho đơn hàng
US-02:
Là MC Đồng bộ, tôi muốn cấp đổi bể NL cho đơn hàng và nhập NL đổi vào Khu vực Vụn ở Trạm Đồng bộ
US-03:
Là MC Đồng bộ, tôi muốn tìm kiếm và xem lịch sử cấp NL
Khai báo thiếu NL
Khai báo thiếu NL
Khai báo thiếu Cast
Khai báo thiếu Finding
Danh sách và trạng thái khai báo
Cập nhật trạng thái khai báo
US-01:
Là MC Đồng bộ, tôi muốn khai báo đơn hàng thiếu NL (Cast/MTO/Finding)
US-02:
Là MC Đồng bộ, tôi muốn hủy khai báo đơn hàng thiếu NL
US-03:
Là MC Đồng bộ/KHSX, tôi muốn tìm kiếm, xem và theo dõi trạng thái khai báo thiếu NL
US-04:
Là KHSX, tôi muốn cập nhật trạng thái của khai báo thiếu NL
US-05:
Là MC Đồng bộ/KHSX, tôi muốn trạng thái phiếu khai báo thiếu NL (Cast) tự động cập nhật trạng thái khi phiếu B Cast tương ứng được tạo và thay đổi trạng thái
US-06:
Là TBP MC/Trưởng MC Đồng bộ/KHSX, tôi muốn nhận được thông báo khi có khai báo thiếu NL mới được tạo
Epic
Điều phối
Đơn đang giữ
Xem danh sách đơn đang giữ
Đơn MC đang giữ
Đơn ở WC thuộc khu vực kiểm soát
US-01:
Là MC Đồng bộ, tôi muốn xem danh sách đơn mình đang giữ và đưa vào WC
US-02:
Là Tổ trưởng MC, tôi muốn xem danh sách đơn thuộc khu vực kiểm soát của tôi
US-03:
Là MC Đồng bộ, tôi muốn xem chi tiết đơn
Chuyển đơn
Danh sách và trạng thái đơn đang chuyển
Chuyển đơn
Hủy chuyển đơn
Lịch sử chuyển đơn
US-01:
Là MC Đồng bộ, tôi muốn xem danh sách đơn đang chuyển (chuyển sang MC khác)
US-02:
Là Tổ trưởng MC, tôi muốn xem danh sách đơn đang chuyển thuộc khu vực kiểm soát của tôi
US-03:
Là MC Đồng bộ, tôi muốn chuyển đơn sang khu vực kiểm soát khác
US-04:
Là MC Đồng bộ, tôi muốn hủy chuyển đơn
US-05:
Là MC Đồng bộ, tôi muốn xem lịch sử chuyển đơn
US-06:
Là MC Đồng bộ, tôi muốn nhận được thông báo khi yêu cầu chuyển đơn bị từ chối
Epic
NL tiêu hao
Tồn NL tiêu hao
Quản lý tồn NL tiêu hao tại MC TSX/SX (theo khu vực kiểm soát
Danh sách NL tồn
US-01:
Là MC Đồng bộ, tôi muốn xem tồn kho NL tiêu hao tại trạm đồng bộ
Yêu cầu cấp NL tiêu hao
Quản lý yêu cầu cấp NL tiêu hao từ MC
Danh sách yêu cầu cấp và theo dõi trạng thái
Cấp NL tiêu hao
Lịch sử cấp NL tiêu hao
US-01:
Là MC Đồng bộ, tôi muốn xem danh sách yêu cầu cấp NL tiêu hao
US-02:
Là MC Đồng bộ, tôi muốn cấp NL tiêu hao cho yêu cầu (cấp đủ, cấp một phần)
US-03:
Là MC Đồng bộ, tôi muốn từ chối cấp NL tiêu hao cho yêu cầu
US-04:
Là MC Đồng bộ, tôi muốn đóng yêu cầu cấp NL tiêu hao đã cấp một phần
US-05:
Là MC Đồng bộ, tôi muốn xem lịch sử cấp NL tiêu hao
US-06:
Là MC Đồng bộ, tôi muốn nhận được thông báo khi có yêu cầu cấp NL tiêu hao mới
Yêu cầu trả NL tiêu hao
Quản lý yêu cầu trả NL từ hao từ MC
Danh sách yêu cầu trả và theo dõi trạng thái
Nhập NL tiêu hao
Lịch sử nhận NL tiêu hao
US-01:
Là MC Đồng bộ, tôi muốn xem danh yêu cầu trả NL về Trạm Đồng bộ
US-02:
Là MC Đồng bộ, tôi muốn nhận NL tiêu hao từ yêu cầu
US-03:
Là MC Đồng bộ, tôi muốn xem lịch sử nhận NL tiêu hao về Trạm Đồng bộ
US-04:
Là MC Đồng bộ, tôi muốn nhận được thông báo khi có yêu cầu cấp NL tiêu hao mới
Epic
Tồn kho
Tồn trạm đồng bộ
Quản lý tồn kho tại trạm đồng bộ
Tồn Cast
Tồn WIP
Tồn Finding
Tồn NL tiêu hao
Tồn Vụn
US-01:
Là MC Đồng bộ, tôi muốn tìm kiếm và xem tồn chi tiết NL tại Trạm Đồng bộ theo từng Item
Chuyển vụn
Chuyển tồn kho về kho Metal dưới dạng vụn (reject)
Chuyển tồn thành vụn
Lịch sử chuyển
US-01:
Là MC Đồng bộ, tôi muốn thực hiện chuyển Item cụ thể trong Trạm Đồng bộ thành Vụn để trả về Kho NL
US-02:
Là MC Đồng bộ, tôi muốn tìm kiếm và xem lịch sử chuyển hàng trong Trạm Đồng bộ
Trả vụn
Danh sách quản lý yêu cầu trả vụn
Danh sách yêu cầu trả vụn
Chuyển vụn sang MC khác
Hủy yêu cầu trả vụn
US-01:
Là MC Đồng bộ, tôi muốn lập yêu cầu trả vụn về Kho NL
US-02:
Là MC Đồng bộ, tôi muốn xem danh sách yêu cầu trả vụn của tôi
US-03:
Là MC Đồng bộ, tôi muốn xem danh sách yêu cầu trả vụn của MC toàn khu vực kiểm soát của tôi
US-04:
Là MC Đồng bộ, tôi muốn hủy yêu cầu trả vụn
US-05:
Là MC Đồng bộ, tôi muốn nhận được thông báo khi yêu cầu trả vụn bị từ chối
Định mức tồn kho
Theo dõi định mức tồn kho
Đối tượng
Tồn Finding
Tồn NL tiêu hao
Theo dõi TL bao gồm:
Tồn dự kiến (NL đang ở PHTJ/HTJ Order)
Tồn onhand (TL thực tại trạm đồng bộ)
TL chờ xuất (TL cần xuất cho các bag theo BOM)
Tồn khả dụng (TL dự kiến + onhand - chờ xuất)
Cảnh báo tồn
US-01:
Là KHSX, tôi muốn tìm kiếm và xem định mức tồn kho
US-02:
Là KHSX, tôi muốn nhận cảnh báo khi có hàng tồn kho có ngày xuất gần nhất vượt số ngày cho phép
US-03:
Là KHSX, tôi muốn nhận cảnh báo khi có hàng tồn kho có tồn dưới định mức cho phép
US-04:
Là KHSX, tôi muốn lọc và xem danh sách hàng tồn cảnh báo (tồn lâu, thiếu tồn)
Cấu hình định mức tồn kho
Cấu hình
Item quản lý định mức + mức tồn cho phép
Mức cảnh báo
Mức tồn lâu
Mức thiếu tồn
US-01:
Là KHSX, tôi muốn thiết lập các mã hàng, khu vực hàng cần quản lý định mức
US-02:
Là KHSX, tôi muốn thiết lập định mức tồn an toàn cho từng Item quản lý định mức
US-03:
Là KHSX, tôi muốn thiết lập số ngày tồn kho tối đa (số ngày kể từ ngày xuất gần nhất) đối với từng Item
Epic
B Order
Đơn thiếu Cast
Quản lý đơn hàng thiếu Cast
Danh sách và theo dõi trạng thái đơn thiếu Cast
Tạo phiếu B Order
US-01:
Là MC Đồng bộ/KHSX, tôi muốn tìm kiếm, xem và theo dõi trạng thái các đơn đã khai báo thiếu Cast
US-02:
Là MC Đồng bộ/KHSX, tôi muốn xem chi tiết đơn hàng thiếu Cast
US-03:
Là MC Đồng bộ/ MC SX, tôi muốn tạo B Order
Phiếu bù Cast
Quản lý phiếu bù Cast
Danh sách và theo dõi trạng thái B Order
Chuyển TL B → SalesOrder/Sample/Proto/Repair/G Order → Tự động close (khi TL B = 0)
Hủy phiếu
In phiếu
US-01:
Là MC Đồng bộ/KHSX, tôi muốn tìm kiếm, xem và theo dõi trạng thái B Order
US-02:
Là MC Đồng bộ/KHSX, tôi muốn xem chi tiết B Order
US-03:
Là MC Đồng bộ/KHSX, tôi muốn chuyển toàn bộ TL từ B Order sang Order khác và B Order tự động close
US-04:
Là MC Đồng bộ/KHSX, tôi muốn in B Order
BR-01: Không thể hủy phiếu khi phiếu đã vào Casting Order (vào cây thông)
BR-02: Khi chuyển TL B Order cần chuyển toàn bộ TL và tự động close khi TL B Order = 0
Epic
Finding Order
Phiếu sửa NL
Quản lý phiếu sửa NL
Tạo và xuất NL cho Finding Order
In phiếu
Hủy phiếu
Danh sách và theo dõi trạng thái Finding Order
US-01:
Là MC Đồng bộ, tôi muốn tạo Finding Order và xuất NL cho Finding Order
US-02:
Là MC Đồng bộ, tôi muốn In phiếu Finding Order
US-03:
Là MC Đồng bộ, tôi muốn hủy Finding Order
US-04:
Lầ MC Đồng bộ, tôi muốn tìm kiếm, xem và theo dõi trạng thái Finding Order
BR-01: Không thể hủy phiếu khi đã từng xuất NL cho phiếu (phiếu cần được đóng và nhập NL trong phiếu và Trạm Đồng bộ
CONTROL STAGE #4: KIỂM SOÁT NL SẢN XUẤT
Epic
Theo dõi đơn
HTJ Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái HTJ Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử HTJ Order
Sales Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái Sales Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử Sales Order
Proto Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái Proto Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử Proto Order
Sample Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái Sample Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử Sample Order
Repair Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái Repair Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử Repair Order
G Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái G Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử G Order
B Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái B Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử B Order
Finding Order
Danh sách và trạng thái đơn
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái Finding Order
US-02:
Là MC, tôi muốn xem chi tiết thông tin và lịch sử Finding Order
Epic
Điều phối
Đơn đang giữ
Xem danh sách đơn đang giữ
Đơn MC đang giữ (thời gian giữ bag)
Đơn ở WC thuộc khu vực kiểm soát
US-01:
Là MC, tôi muốn xem danh sách đơn mình đang giữ và đưa vào WC
US-02:
Là Tổ trưởng MC, tôi muốn xem danh sách đơn thuộc khu vực kiểm soát của tôi
US-03:
Là MC, tôi muốn xem chi tiết đơn
Nhận đơn
Danh sách và trạng thái đơn chờ nhận
Xác nhận nhận đơn
Lịch sử nhận đơn
US-01:
Là MC, tôi muốn xem danh sách đơn chờ nhận (được chuyển từ MC khác)
US-02:
Là Tổ trưởng MC MC, tôi muốn xem danh sách đơn chờ nhận thuộc khu vực kiểm soát của tôi
US-03:
Là MC, tôi muốn xác nhận nhận đơn
US-04:
Là MC, tôi muốn xem lịch sử nhận đơn
US-05:
Là MC, tôi muốn nhận thông báo khi có đơn được chuyển đến
Chuyển đơn
Danh sách và trạng thái đơn đang chuyển
Chuyển đơn
Hủy chuyển đơn
Lịch sử chuyển đơn
US-01:
Là MC, tôi muốn xem danh sách đơn đang chuyển (chuyển sang MC khác)
US-02:
Là Tổ trưởng MC, tôi muốn xem danh sách đơn đang chuyển thuộc khu vực kiểm soát của tôi
US-03:
Là MC, tôi muốn chuyển đơn sang khu vực kiểm soát khác
US-04:
Là MC, tôi muốn chuyển đơn đến trạm đồng bộ
US-05:
Là MC, tôi muốn chuyển đơn đến Kho thành phẩm
US-06:
Là MC, tôi muốn chuyển đơn đến Kho mẫu
US-07:
Là MC, tôi muốn hủy chuyển đơn
US-08:
Là MC, tôi muốn xem lịch sử chuyển đơn
US-09:
Là MC, tôi muốn nhận thông báo khi yêu cầu chuyển đơn bị từ chối
Epic
Vụn
Vụn đang giữ
Quản lý vụn
Danh sách vụn đang giữ
Lịch sử trả vụn của công nhân về MC (theo từng bag)
Chuyển vụn
Nhận vụn chuyển
Lịch sử chuyển vụn
Trả vụn (hạn chế quyền tự trả)
US-01:
Là MC, tôi muốn xem danh sách vụn đang giữ
US-02:
Là Tổ trưởng MC, tôi muốn xem danh sách vụn của MC toàn khu vực kiểm soát của tôi
US-03:
Là MC, tôi muốn tạo yêu cầu trả vụn tôi đang giữ
US-04:
Là Tổ trường MC, tôi muốn tạo yêu cầu trả vụn cho toàn bộ vụn trong khu vực kiểm soát của tôi
Trả vụn
Danh sách quản lý yêu cầu trả vụn
Danh sách yêu cầu trả vụn
Hủy yêu cầu trả vụn
US-01:
Là MC, tôi muốn xem danh sách yêu cầu trả vụn của tôi
US-02:
Là MC, tôi muốn xem danh sách yêu cầu trả vụn của MC toàn khu vực kiểm soát của tôi
US-03:
Là MC, tôi muốn hủy yêu cầu trả vụn
US-04:
Là MC, tôi muốn nhận thông báo khi yêu cầu trả vụn bị từ chối
Epic
NL tiêu hao
NL tiêu hao đang giữ
Quản lý tồn NL tiêu hao tại MC TSX/SX (theo khu vực kiểm soát
Danh sách NL đang giữ
Cấp NL tiêu hao
US-01:
Là MC, tôi muốn xem tồn kho NL tiêu hao tại khu vực kiểm soát của mình
US-02:
Là MC, tôi muốn cấp NL tiêu hao cho Công nhân
Điều phối
Quản lý giao dịch giữa MC và Công nhân
Nhận NL tiêu hao trả từ Công nhân
Lịch sử cấp và nhận NL tiêu hao từ Công nhân
Ghi nhận dữ liệu và tính hao hụt vào công nhân
Báo cáo sử dụng NL tiêu hao theo từng Công nhân theo kỳ
US-01:
Là MC, tôi muốn nhận NL tiêu hao trả từ Công nhân
US-03:
Là MC, tôi muốn xem lịch sử cấp NL tiêu hao cho Công nhân
US-04:
Là MC, tôi muốn xem lịch sử nhận NL tiêu hao trả từ Công nhân
US-05:
Là MC, tôi muốn xem báo cáo sử dụng NL tiêu hao theo từng Công nhân theo kỳ (tổng sự dụng thực sao khi đối chiếu tổng cấp và tổng trả)
Nhận trả NL tiêu hao
Quản lý giao dịch giữa MC TSX/SX và MC đồng bộ
Yêu cầu cấp NL tiêu hao
Nhận và trả NL tiêu hao về trạm đồng bộ
Lịch sử nhận và trả NL tiêu hao về trạm đồng bộ
US-01:
Là Bộ phận SX, tôi muốn tạo yêu cầu cấp NL tiêu hao đến Trạm đồng bộ
US-02:
Là MC, tôi muốn xem danh sách và theo dõi trạng thái yêu cầu cấp NL tiêu hao
US-03:
Là MC, tôi muốn nhận NL tiêu hao đã được cấp
US-04:
Là MC, tôi muốn trả NL tiêu hao về Trạm đồng bộ
US-05:
Là MC, tôi muốn xem lịch sử nhận và trả NL tiêu hao về trạm đồng bộ
US-06:
Là MC, tôi muốn nhận thông báo khi yêu cầu cấp NL tiêu hao bị từ chối
US-07:
Là MC, tôi muốn nhận được thông báo khi Trạm Đồng bộ đã cấp NL tiêu hao
Epic
B Order
Đơn thiếu Cast
Quản lý đơn hàng thiếu Cast
Danh sách và theo dõi trạng thái đơn thiếu Cast
Tạo phiếu B Order
US-01:
Là MC SX/KHSX, tôi muốn tìm kiếm, xem và theo dõi trạng thái các đơn đã khai báo thiếu Cast
US-02:
Là MC SX/KHSX, tôi muốn xem chi tiết đơn hàng thiếu Cast
US-03:
Là MC SX/KHSX, tôi muốn tạo B Order
Phiếu bù Cast
Quản lý phiếu bù Cast
Danh sách và theo dõi trạng thái B Order
Chuyển TL B → SalesOrder/Sample/Proto/Repair/G Order → Tự động close (khi TL B = 0)
Hủy phiếu
In phiếu
US-01:
Là MC SX/KHSX, tôi muốn tìm kiếm, xem và theo dõi trạng thái B Order
US-02:
Là MC SX/KHSX, tôi muốn xem chi tiết B Order
US-03:
Là MC SX/KHSX, tôi muốn chuyển toàn bộ TL từ B Order sang Order khác và B Order tự động close
US-04:
Là MC SX/KHSX, tôi muốn in B Order
BR-01: Không thể hủy phiếu khi phiếu đã vào Casting Order (vào cây thông)
BR-02: Khi chuyển TL B Order cần chuyển toàn bộ TL và tự động close khi TL B Order = 0
CONTROL STAGE #5: KHO THÀNH PHẨM
Epic
Nhập kho
Yêu cầu nhập kho
Quản lý danh sách các đơn được gửi đến kho thành phẩm
Bao gồm các đơn
Sales Order
Repair Order
G Order
Các tính năng
Danh sách đơn và theo dõi trạng thái
US-01:
Là MC Đóng gói, tôi muốn tìm kiếm, xem và theo dõi trạng thái đơn gửi đến Kho Thành phẩm
US-02:
Là MC Đóng gói, tôi muốn xem chi tiết thông tin đơn
US-03:
Là MC Đóng gói, tôi muốn nhận thông báo khi có yêu cầu được gửi đến
Nhập kho
Quản lý đơn nhập vào Kho TP
Đóng bag nhập kho
Nhập thành phẩm
Lịch sử nhập kho
US-01:
Là MC Đóng gói, tôi muốn đóng bag và nhập thành phẩm vào kho
US-02:
Là MC Đóng gói, tôi muốn tìm kiếm và xem lịch xử nhập kho
Trả đơn
Quản lý các đơn trả về SX
Trả đơn
Lịch sử trả đơn
US-01:
Là MC Đóng gói, tôi muốn chuyển đơn về MC SX (WC)
US-02:
Là MC Đóng gói, tôi muốn tìm kiếm và xem lịch sử trả đơn
Epic
Xuất kho
Đơn hàng
Quản lý danh sách đơn hàng chờ xuất kho
Danh sách và theo dõi trạng thái
Phân bổ đơn hàng (phân bổ tự động)
Tạo phiếu xuất kho
US-01:
Là MC Đóng gói, tôi muốn tìm kiếm, xem và theo dõi trạng thái đơn hàng khách
US-02:
Là MC Đóng gói, tôi muốn hệ thống tự động phân bổ hàng khi nhập kho cho đơn hàng tương ứng
US-03:
Là MC Đóng gói, tôi muốn tạo phiếu xuất kho cho đơn hàng
Trả về SX (chờ SX lại)
Xử lý đơn hàng Hủy đơn
Danh sách hàng đã hủy đơn (chờ SX lại)
Chuyển đơn chờ sx lại về MC ở WC waiting infomation
US-01:
Là MC Đóng gói, tôi muốn chuyển hàng về MC SX tại WC Waiting Information
Phiếu xuất kho
Quản lý danh sách phiếu xuất kho và xử lý xuất kho
Danh sách và theo dõi trạng thái
Soạn hàng
Xác nhận xuất kho
In phiếu xuất kho
US-01:
Là MC Đóng gói, tôi muốn tìm kiếm, xem và theo dõi trạng thái phiếu xuất kho
US-02:
Là MC Đóng gói, tôi muốn soạn hàng xuất kho (chọn thành phẩm cho phiếu xuất kho)
US-03:
Là MC Đóng gói, tôi muốn xác nhận xuất kho cho phiếu xuất kho
US-04:
Là MC Đóng gói, tôi muốn in phiếu xuất kho và chứng từ giao hàng
Phiếu giao hàng
Quản lý danh sách phiếu giao hàng
Tạo phiếu giao hàng tự động
Danh sách và theo dõi trạng thái
Xuất phát giao hàng
Giao hàng thất bại
Giao hàng thành công
Giao lại
Hủy đơn - nhập kho
US-01:
Là MC Đóng gói, tôi muốn hệ thống tạo tự động phiếu giao hàng khi xác nhận xuất kho
US-02:
Là MC Đóng gói, tôi muốn tìm kiếm, xem và theo dõi trạng thái phiếu giao hàng
US-03:
Là MC Đóng gói, tôi muốn cập nhật ngày xuất phát giao hàng
US-04:
Là MC Đóng gói, tôi muốn cập nhật giao hàng thất bại, chọn ngày giao lại
US-05:
Là MC Đóng gói, tôi muốn cập nhật giao hàng thành công, ghi nhận ngày hoàn thành
US-06:
Là MC Đóng gói, tôi muốn thao tác giao lại đơn hàng giao hàng thất bại
US-07:
Là MC Đóng gói, tôi muốn hủy đơn - nhập hàng trong đơn vào Kho thành phẩm
US-08:
Là MC Đóng gói, tôi muốn xem chi tiết phiếu giao hàng
US-09:
Là Kế toán, tôi muốn nhận được thông báo khi đơn hàng đã giao thành công hoặc đã Hủy đơn
BR-01: Chỉ có thể Hủy đơn - nhập kho đối với đơn hàng chờ giao/giao hàng thất bại
Epic
Tồn kho
Tồn kho TP
Quản lý tồn kho tại kho TP
Sales Order
Repair Order
G Order
US-01:
Là MC Đóng gói, tôi muốn tìm kiếm và xem tồn Kho Thành phẩm
WIP giao hàng
Quản lý hàng đang giao
Sales Order
Repair Order
G Order
US-01:
Là MC Đóng gói, tôi muốn tìm kiếm và xem hàng đang giao
Epic
Hóa đơn (Kế toán)
Hóa đơn
Quản lý hóa đơn
Tạo hóa đơn tự động từ phiếu giao hàng
Tính giá
Danh sách và theo dõi trạng thái hóa đơn
US-01:
Là MC Đóng gói, tôi muốn hệ thống tạo hóa đơn tự động từ phiếu giao hàng ngay khi hệ phiếu giao hàng được tạo
US-02:
Là MC Đóng gói, tôi muốn hệ thống cập nhật trạng thái hóa đơn khi phiếu giao hàng thay đổi trạng thái
US-03:
Là MC Đóng gói, tôi muốn kiểm tra và khác nhận thông tin giá được hệ thống tính dựa trên cấu hình giá
US-04:
Là MC Đóng gói/Kế toán, tôi muốn tìm kiếm, xem và theo dõi trạng thái của hóa đơn
CONTROL STAGE #6: KHO MẪU (anh Hiệp)
Epic
Nhập kho
Yêu cầu nhập kho
Quản lý danh sách các đơn được gửi đến kho thành phẩm
Nhập kho từ đơn
Sample
Proto
Các tính năng
Danh sách đơn và theo dõi trạng thái
US-01:
Là MC/P.KD/KTCT, tôi muốn tìm kiếm, xem và theo dõi trạng thái đơn gửi đến Kho Thành phẩm
US-02:
Là MC/P.KD/KTCT, tôi muốn xem chi tiết thông tin đơn
US-03:
Là MC/P.KD/KTCT, tôi muốn nhận thông báo khi có đơn được gửi đến
Nhập kho
Quản lý đơn nhập vào Kho TP
Đóng bag nhập kho
Nhập mẫu (sample/proto)
Lịch sử nhập kho
US-01:
Là P.KD/KTCT, tôi muốn đóng bag và nhập thành phẩm vào kho
US-02:
Là P.KD/KTCT, tôi muốn tìm kiếm và xem lịch xử nhập kho
Trả đơn
Quản lý các đơn trả về SX
Trả đơn
Lịch sử trả đơn
US-01:
Là P.KD/KTCT, tôi muốn chuyển đơn về MC SX (WC)
US-02:
Là P.KD/KTCT, tôi muốn tìm kiếm và xem lịch sử trả đơn
Epic
Xuất kho
Phiếu xuất kho
Quản lý danh sách phiếu xuất kho và xử lý xuất kho
Danh sách và theo dõi trạng thái
Soạn hàng
Xác nhận xuất kho
In phiếu xuất kho
Loại xuất
Xuất mượn
Xuất tặng
US-01:
Là P.KD/KTCT, tôi muốn tìm kiếm, xem và theo dõi trạng thái phiếu xuất kho
US-02:
Là P.KD/KTCT, tôi muốn tạo phiếu xuất kho
US-03:
Là P.KD/KTCT, tôi muốn soạn hàng xuất kho (chọn mẫu cho phiếu xuất kho)
US-04:
Là P.KD/KTCT, tôi muốn xác nhận xuất kho cho phiếu xuất kho
US-05:
Là P.KD/KTCT, tôi muốn in phiếu xuất kho và chứng từ giao hàng
Phiếu trả
Quản lý phiếu trả hàng mượn
Danh sách phiếu trả
US-01:
Là P.KD/KTCT, tôi muốn tìm kiếm, xem danh sách phiếu trả
Epic
Tồn kho
Tồn kho mẫu
Quản lý tồn kho tại Kho Mẫu
Sample
Proto
US-01:
Là P.KD/KTCT, tôi muốn tìm kiếm và xem tồn Kho Mẫu
CONTROL STAGE #7: HAO HỤT VÀ THU HỒI
Epic
Kỳ thu hồi
Kỳ thu hồi
Quản lý kỳ thu hồi (hao hụt và thu hồi trong kỳ)
Danh sách và trạng thái từng kỳ
Tạo kỳ thu hồi
Xem chi tiết thông tin kỳ thu hồi
Đóng kỳ thu hồi
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái của kỳ thu hồi
US-02:
Là TBP MC, tôi muốn tạo kỳ thu hồi
US-03:
Là MC, tôi muốn xem chi tiết thông tin kỳ thu hồi
US-04:
Là TBP MC, tôi muốn đóng kỳ thu hồi (chốt sổ)
Cấu hình kỳ thu hồi
Cấu hình thông tin kỳ thu hồi
Quản lý Worker Team
Cập nhật nhân viên Worker Team trong kỳ
Thêm nhân sự
Thay đổi nhân sự (nghỉ việc - bàn giao NV khác kế thừa thu hồi)
US-01:
Là MC, tôi muốn tìm kiếm và xem danh sách Worker Team
US-02:
Là MC, tôi muốn xem chi tiết Worker Team
US-03:
Là MC, tôi muốn tạo, chỉnh sửa, xóa Worker Team
US-04:
Là MC, tôi muốn cập nhật Worker Team của Công nhân
US-05:
Là MC, tôi muốn Công nhân mới kế thừa thông tin thu hồi từ Công nhân cũ đã nghĩ việc
Epic
Hao hụt
Hao hụt
Quản lý hao hụt theo Worker Team theo kỳ
Tổng quan hao hụt theo từng Team
Tổng hao hụt theo từng Công nhân
Hao hụt chi tiết
US-01:
Là MC, tôi muốn tìm kiếm, xem danh sách hao hụt theo Worker Team
US-02:
Là MC, tôi muốn xem chi tiết hao hụt tổng theo từng Worker Team
US-03:
Là MC, tôi muốn xem chi tiết hao hụt theo từng Công nhân
US-04:
Là MC, tôi muỗn xem chi tiết từng bản ghi phát sinh hao hụt
Epic
Phiếu thu hồi
Phiếu thu hồi
Quản lý phiếu thu hồi
Danh sách và trạng thái phiếu thu hồi
Tạo phiếu thu hồi (ghi nhận SL và TL)
Bụi vàng (ghi nhận TL)
Bụi HTJ (dây, DCP, Ball)
Bụi móc máy
Bụi nguội
Bụi SET
Bụi đánh bóng
Bụi dơ
Rác thu hồi
Nước thu hồi
Tấm đồng
Tấm lọc
Hủy phiếu thu hồi
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái phiếu thu hồi
US-02:
Là MC, tôi muốn tạo phiếu thu hồi
US-03:
Là MC, tôi muốn hệ thống tự động chuyển phiếu thu hồi đến công đoạn tiếp theo được cấu hình
US-04:
Là MC, tôi muốn hủy phiếu thu hồi
US-05:
Là MC, tôi muốn nhận được thông báo khi phiếu thu hồi được trả về
Công đoạn Đốt
Quản lý task đốt
Danh sách các phiếu chờ/đang xử lý đốt
Ghi nhận TL bụi trước đốt và TL dẻ sau đốt
Trả NL về công đoạn trước
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái phiếu thu hồi đang ở Công đoạn Đốt
US-02:
Là MC, tôi muốn ghi nhận kết quả xử lý đốt
US-03:
Là MC, tôi muốn hệ thống tự động chuyển phiếu thu hồi đến công đoạn tiếp theo được cấu hình
US-04:
Là MC, tôi muốn trả NL về công đoạn trước
US-05:
Là MC, tôi muốn nhận được thông báo khi có phiếu thu hồi mới được gửi đến hoặc được trả về
Công đoạn Phân kim Thu hồi
Quản lý task phân kim
Danh sách các phiếu chờ/đang xử lý phân kim
Ghi nhận TL trước và sau phân kim
Trả NL về công đoạn trước
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái phiếu thu hồi đang ở Công đoạn Phân kim
US-02:
Là MC, tôi muốn ghi nhận kết quả xử lý Phân kim
US-03:
Là MC, tôi muốn hệ thống tự động chuyển phiếu thu hồi đến công đoạn tiếp theo được cấu hình
US-04:
Là MC, tôi muốn trả NL về công đoạn trước
US-05:
Là MC, tôi muốn nhận được thông báo khi có phiếu thu hồi mới được gửi đến hoặc được trả về
Công đoạn Xử
Quản lý task xử NL
Danh sách các phiếu chờ/đang xử lý xử
Ghi nhận TL trước xử; Thành phần và TL sau phân kim
Trả NL về công đoạn trước
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái phiếu thu hồi đang ở Công đoạn Phân kim
US-02:
Là MC, tôi muốn ghi nhận kết quả xử lý Phân kim
US-03:
Là MC, tôi muốn hệ thống tự động chuyển phiếu thu hồi đến công đoạn tiếp theo được cấu hình
US-04:
Là MC, tôi muốn trả NL về công đoạn trước
US-05:
Là MC, tôi muốn nhận được thông báo khi có phiếu thu hồi mới được gửi đến hoặc được trả về
Nhập kho NL
Quản lý danh sách NL chờ nhập kho
Danh sách các phiếu chờ nhập kho
Phân loại và nhập kho
Trả NL về công đoạn trước
Lịch sử nhập kho
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái phiếu thu hồi chờ nhập Kho NL
US-02:
Là MC NL, tôi muốn phân loại NL và nhập vào Kho NL
US-03:
Là MC, tôi muốn trả NL về công đoạn trước
US-04:
Là MC, tôi muốn tìm kiếm và xem lịch sử nhập kho từ thu hồi
US-05:
Là MC tạo phiếu, tôi muốn nhận thông báo khi phiếu thu hồi đã nhập kho
US-05:
Là MC, tôi muốn nhận được thông báo khi có phiếu thu hồi mới được gửi đến
Cấu hình
Cấu hình phiếu thu hồi
Cấu hình loại thu hồi
Cấu hình công đoạn thực hiện phiếu thu hồi
US-01:
Là MC, tôi muốn tạo, sửa, xóa danh sách loại thu hồi
US-02:
Là MC, tôi muốn cấu hình công đoạn thực hiện phiếu thu hồi cho từng loại thu hồi
Epic
Vật tư thu hồi
Tồn vật tư thu hồi
Quản lý tồn kho vật tư thu hồi (tấm đồng, tấm lọc, túi bụi)
US-01:
Là MC, tôi muốn tìm kiếm, xem tồn vật tư thu hồi
Nhập vật tư thu hồi
Quản lý nhập vật tư
Danh sách phiếu nhập
Nhập vật tư thu hồi từ Phiếu xuất kho (kho nội bộ)
US-01:
Là MC, tôi muốn tìm kiếm, xem danh sách phiếu nhập vật tư thu hồi
US-02:
Là MC, tôi muốn nhập vật tư thu hồi từ mã phiếu xuất kho (kho nội bộ)
US-03:
Là MC, tôi muốn xem lịch sử nhập kho vật tư thu hồi
Cấp phát vật tư thu hồi
Quản lý cấp phát vật tư cho các bộ phận
Danh sách phiếu cấp phát
Ghi nhận đối tượng nhận
Ghi nhận khi phát
Tạo phiếu cấp vật tư thu hồi
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái cấp phát vật tư theo kỳ thu hồi
US-02:
Là MC, tôi muốn cấp phát vật tư thu hồi
US-03:
Là MC, tôi muốn xem lịch sử cấp phát vật tư thu hồi
#8: KIỂM KHO
Epic
Kiểm kho NL vàng
Phiếu kiểm kho
Quản lý phiếu kiểm kho
Danh sách và trạng thái phiếu
Tạo phiếu kiểm kho
Xem chi tiết phiếu kiểm kho
Kiểm tồn kho
Kiểm tồn đơn hàng
US-01:
Là MC, tôi muốn tìm kiếm, xem và theo dõi trạng thái phiếu kiểm kho
US-02:
Là TBP MC, tôi muốn tạo phiếu kiểm kho
US-03:
Là TBP MC, tôi muốn chọn kho, trạm, wip cần kiểm kho
US-04:
Là MC, tôi muốn xem chi tiết phiếu kiểm kho
US-05:
Là TBP MC, tôi muốn hệ thống chặn mọi giao dịch kho trong quá trình kiểm kho
US-06:
Là TBP MC, tôi muốn xác nhận hoàn thành phiếu kiểm kho
Thực hiện kiểm kho
Thực hiện kiểm kho
Kiểm tồn đơn hàng
Kiểm tồn NL trong kho
US-01:
Là MC, tôi muốn thực hiện kiểm kho tồn đơn hàng tại các WIP
US-02:
Là MC, tôi muốn thực hiện kiểm kho tồn kho tại các Kho/Trạm
#9: ĐIỀU CHỈNH
Epic
Đề xuất điều chỉnh
Kho NL
Đề xuất điều chỉnh các lỗi thao tác
Nhầm tuổi vàng
Nhầm TL
US-01:
Là MC NL, tôi muốn tạo đề xuất điều chỉnh cho lỗi thao tác nhầm tuổi vàng
US-02:
Là MC NL, tôi muốn tạo đề xuất điều chỉnh cho lỗi thao tác nhầm TL
US-03:
Là TBP MC, tôi muốn đề xuất điều chỉnh được gửi đến người duyệt
US-04:
Là MC NL, tôi muốn tìm kiếm, xem và theo dõi trạng thái đề xuất điều chỉnh3
US-05:
Là MC NL, tôi muốn hủy đề xuất điều chỉnh
US-06:
Là MC NL, tôi muốn nhận được thông báo khi đề xuất của tôi được duyệt/từ chối/trả lại
TSX & SX
Đề xuất điều chỉnh các lỗi thao tác
Nhầm tuổi khi nhận SOL từ công nhân
Nhầm TL
US-01:
Là MC TSX/SX, tôi muốn tạo đề xuất điều chỉnh cho lỗi thao tác nhầm tuổi khi nhận SOL từ công nhân
US-02:
Là MC TSX/SX, tôi muốn tạo đề xuất điều chỉnh cho lỗi thao tác nhầm TL
US-03:
Là TBP MC, tôi muốn đề xuất điều chỉnh được gửi đến người duyệt
US-04:
Là MC TSX/SX, tôi muốn tìm kiếm, xem và theo dõi trạng thái đề xuất điều chỉnh
US-05:
Là MC TSX/SX, tôi muốn hủy đề xuất điều chỉnh
US-06:
Là MC TSX/SX, tôi muốn nhận được thông báo khi đề xuất của tôi được duyệt/từ chối/trả lại
Trạm Đồng bộ
Đề xuất điều chỉnh các lỗi thao tác
Nhầm SL
Nhầm TL
Nhầm chiều dài
US-01:
Là MC Đồng bộ, tôi muốn tạo đề xuất điều chỉnh cho lỗi thao tác nhầm SL
US-02:
Là MC Đồng bộ, tôi muốn tạo đề xuất điều chỉnh cho lỗi thao tác nhầm TL
US-03:
Là MC Đồng bộ, tôi muốn tạo đề xuất điều chỉnh cho lỗi thao tác nhầm chiều dài
US-04:
Là TBP MC, tôi muốn đề xuất điều chỉnh được gửi đến người duyệt.
US-05:
Là MC Đồng bộ, tôi muốn tìm kiếm, xem và theo dõi trạng thái đề xuất điều chỉnh
US-06:
Là MC Đồng bộ, tôi muốn hủy đề xuất điều chỉnh
US-07:
Là MC Đồng bộ, tôi muốn nhận được thông báo khi đề xuất của tôi được duyệt/từ chối/trả lại
Kho Thành phẩm
Điều chỉnh TL -> không cần duyệt (điều chỉnh trong khoảng TL quy định do lệch cân)
US-01:
Là MC Đóng gói, tôi muốn tạo đề xuất điều chỉnh TL
US-02:
Là TBP MC, tôi muốn đề xuất điều chỉnh được tự động duyệt nếu TL điều chỉnh nằm trong khoảng quy định
US-03:
Là TBP MC, tôi muốn đề xuất điều chỉnh được gửi đến người duyệt khi TL vượt mức quy định
US-04:
Là MC Đóng gói, tôi muốn tìm kiếm, xem và theo dõi trạng thái đề xuất điều chỉnh
US-05:
Là MC Đóng gói, tôi muốn hủy đề xuất điều chỉnh
US-06:
Là MC Đóng gói, tôi muốn nhận được thông báo khi đề xuất của tôi được duyệt/từ chối/trả lại
BR-01: Chỉ áp dụng tự động duyệt 1 lần cho một đối tượng điều chỉnh, một đối tượng khi điều chỉnh từ lần thứ 2 đều cần duyệt
BR-02: Khi điều chỉnh được thực hiện, tất cả những phát sinh có liên quan điều cần được cập nhật tương ứng
Epic
Xử lý điều chỉnh
Phê duyệt
Danh sách yêu cầu điều chỉnh và theo dõi trạng thái
Phê duyệt/Từ chối
US-01:
Là người duyệt, tôi muốn tìm kiếm, xem và theo dõi trạng thái yêu cầu điều chỉnh
US-02:
Là người duyệt, tôi muốn phê duyệt/từ chối/trả lại yêu cầu điều chỉnh
BR-01: Khi điều chỉnh được thực hiện, tất cả những phát sinh có liên quan điều cần được cập nhật tương ứng
Epic
Lịch sử
Lịch sử đề xuất điều chỉnh
Lịch sử các điều chỉnh đã hoàn thành
US-01:
Là MC, tôi muốn tìm kiếm, xem danh sách các điều chỉnh đã hoàn thành
US-02:
Là MC, tôi muốn xem chi tiết các thay đổi gây ra bởi điều chỉnh
Epic
Cấu hình
Người duyệt
Cấu hình người duyệt điều chỉnh cho từng loại điều chỉnh
US-01:
Là TBP MC, tôi muốn cấu hình người duyệt đề xuất điều chỉnh cho từng loại điều chỉnh của từng nhóm kiểm soát
BR-01: Mỗi loại ứng với từng nhóm kiểm soát cần có ít nhất 1 người duyệt để đề xuất được khả dụng
TL thành phẩm được phép điều chỉnh
Cấu hình khoảng TL cho phép điều chỉnh đối với Thành phẩm tại Kho Thành phẩm
US-01:
Là TBP MC, tôi muốn cấu hình khoảng TL cho phép điều chỉnh TL đối với Thành phẩm tại Kho Thành phẩm
#10: KIỂM SOÁT & BÁO CÁO
Epic
Theo dõi NL
Tổng tồn 24K
Tổng tồn TL 24k NL tất cả điểm kiểm soát
Tồn NL khách
Chờ nhận
Chờ xuất
Tồn kho NL
NL chờ xử
NL chờ phân kim
Find Gold
NL đúc
TP chờ sửa
WIP xử lý
Shooting Order
Alloy Order
WIP tiền sản xuất
Casting Order
PHTJ Order
HTJ Order
Reject
NL tiêu hao
Trạm đồng bộ
Cast
MTO
Finding
Tiêu hao
WIP SX
HTJ Order
Sales Order
Repair Order
G Order
Finding Order
B order
Kho thành phẩm
Sales Order
Repair Order
G Order
WIP Giao hàng
Chờ giao
Đang giao
US-01:
Là MC, tôi muốn theo dõi tồn 24K NL tại tất cả điểm kiểm soát
Epic
Báo cáo
Báo cáo Xuất - Nhập - Tồn 24K
Xuất - Nhập - Tồn 24K toàn Chi nhánh
Theo từng kho
Theo từng khu vực
Theo từng vị trí
Chi tiết từng hoạt động
US-01:
Là MC, tôi muốn xem báo cáo tổng Xuất - Nhập - Tồn 24K
Báo cáo Xuất - Nhập - Tồn Hội
Xuất - Nhập - Tồn Hội
Theo từng kho
Theo từng khu vực
Theo từng vị trí
Chi tiết từng hoạt động
US-01:
Là MC, tôi muốn xem báo cáo tổng Xuất - Nhập - Tồn Hội
Báo cáo Xuất - Nhập - Tồn Kho Thành phẩm
Xuất - Nhập - Tồn Kho Thành phẩm
Theo từng khu vực
Theo từng vị trí
Chi tiết từng hoạt động
US-01:
Là MC, tôi muốn xem báo cáo tổng Xuất - Nhập - Tồn Kho Thành phẩ
Báo cáo Xuất - Nhập - Tồn Kho Mẫu
Xuất - Nhập - Tồn Kho Mẫu
Theo từng khu vực
Theo từng vị trí
Chi tiết từng hoạt động
US-01:
Là MC, tôi muốn xem báo cáo tổng Xuất - Nhập - Tồn Kho Mẫu
Báo cáo hao hụt, thu hồi
Báo cáo hao hụt, thu hồi
Tổng quan theo kỳ
Theo từng Worker Team trong kỳ
Chi tiết từng hoạt động
US-01:
Là MC, tôi muốn xem báo cáo tổng hao hụt
Báo cáo đổi bể Finding
Báo cáo đổi bể Finding
Danh sách
SL, TL và tỉ lệ theo Item
SL, TL và tỉ lệ theo WC
US-01:
Là MC, tôi muốn xem báo cáo danh sách ghi nhận đổi bể
US-02:
Là MC, tôi muốn xem số lượng, TL và tỉ lệ đổi bể theo Item
US-03:
Là MC, tôi muốn xem số lượng, TL và tỉ lệ đổi bể theo WC
Báo cáo đổi bể đá
Báo cáo đổi bể đá
Danh sách
SL, TL và tỉ lệ theo Item
SL, TL và tỉ lệ theo WC
US-01:
Là MC, tôi muốn xem báo cáo danh sách ghi nhận đổi bể
US-02:
Là MC, tôi muốn xem số lượng, TL và tỉ lệ đổi bể theo Item
US-03:
Là MC, tôi muốn xem số lượng, TL và tỉ lệ đổi bể theo WC
Báo cáo phân kim
Báo cáo phân kim
US-01:
Là MC, tôi muốn xem báo cáo phân kim
Tra cứu nguồn gốc nguyên liệu
Quản lý gia phả (tra cứu nguồn gốc)
Cây thông
Nguyên liệu (Lô)
US-01:
Là MC, tôi muốn tra cứu nguồn gốc cây thông (Tree Number Tracking)
US-02:
Là MC, tôi muốn tra cứu nguồn gốc nguyên liệu (LOT Tracking)
US-03:
Là MC/QC, tôi muốn tra cứu thông tin các Thành phẩm được tạo ra từ Lô tương ứng
Vòng quay vàng
Thời gian xử lý vàng ở từng công đoạn / nhóm công đoạn
Vòng lớn từ NL → khách trả
Các vòng quay vụn, cà rót, phân kim quay về kho
US-01:
Là TBP MC, tôi muốn xem thời gian và TL vàng xử lý từ NL cho đến kho hoàn thành nhận NL khác trả
US-02:
Là TBP MC, tôi muốn xem chi tiết thời gian và TL vàng xử lý tại từng nhóm công đoạn/công đoạn
US-03:
Là TBP MC, tôi muốn xem chi tiết thời gian và TL vàng xử lý theo từng đối tượng
#11: CẤU HÌNH DỮ LIỆU & TÍCH HỢP
Quản lý NL (kim loại)
Quản lý các dữ liệu:
Nhóm NL
Hội
Nguyên liệu
Phế phẩm
Bán thành phẩm
Thành phẩm
Mẫu
Proto
US-01
: Là Trưởng phòng MC, tôi muốn tìm kiếm, xem danh sách nhóm nguyên liệu
US-02:
Là Trưởng phòng MC, tôi muốn tìm kiếm, xem danh sách hội
US-03:
Là Trưởng phòng MC, tôi muốn tìm kiếm, xem danh sách nguyên liệu
US-04:
Là Trưởng phòng MC, tôi muốn tìm kiếm, xem danh sách phế phẩm
US-05:
Là Trưởng phòng MC, tôi muốn tìm kiếm, xem danh sách bán thành phẩm
US-06:
Là Trưởng phòng MC, tôi muốn tìm kiếm, xem danh sách thành phẩm
US-07:
Là Trưởng phòng MC, tôi muốn tìm kiếm, xem danh sách mẫu
US-08:
Là Trưởng phòng MC, tôi muốn tìm kiếm, xem danh sách proto
BR-01: Mã NL là duy nhất
BR-02: Không thể xóa NL khi có tồn NL đó (ở bất kỳ khâu nào trong SX)
Quản lý khu vực kiểm soát
Khu vực kiểm soát dùng để:
Phân tách phạm vi quản lý của MC.
Kiểm soát luồng điều chuyển nguyên liệu giữa các khu vực.
US-01:
Là Trưởng phòng MC, tôi muốn tạo mới, lưu nháp, chỉnh sửa, xóa khu vực kiểm soát
US-02:
Là Trường phòng MC, tôi muốn thiết lập trưởng khu vực kiểm soát
US-03:
Là TBP MC, tôi muốn thiết lập khu vực kiểm soát cho các MC
Quản lý đội Công nhân (Worker Team)
Quản lý các đội Công nhân tham gia sản xuất, phục vụ việc:
Gán trách nhiệm kiểm soát.
Ghi nhận thu hồi/hao hụt
US-01:
Là Trưởng phòng MC, tôi muốn tạo mới, lưu nháp, chỉnh sửa, xóa đội Công nhân
US-02:
Là Trưởng phòng MC, tôi muốn cấu hình danh sách WC theo đội Công nhân
BR-01: Mã đội Công nhân là duy nhất
BR-02: Mỗi đội Công nhân thuộc một khu vực kiểm soát
BR-03: Mỗi đội Công nhân có nhiều WC và mỗi WC chỉ thuộc một đội Công nhân
Ghi chú lỗi
Danh sách các ghi chú lỗi khi nhận hàng hàng hồi mới/hàng gửi sửa từ khách
US-01:
Là Trưởng phòng MC, tôi muốn tạo mới, lưu nháp, chỉnh sửa, xóa ghi chú lỗi
BR-01: Không thể xóa ghi chú lỗi khi đã được sử dụng
Tích hợp thiết bị
Tích hợp thiết bị
Tích hợp hệ thống và cân
Tích hợp hệ thống và thiết bị quét mã
Tích hợp hệ thống và máy đo phổ
Tích hợp máy in và máy đo phổ
Tích hợp hệ thống với máy in
US-01:
Là MC, tôi muốn hệ thống đọc và điền dữ liệu TL tự động từ cân điện tử
US-02:
Là MC, tôi muốn hệ thống đọc dữ liệu từ thiết bị đọc mã vạch để quét mã nhãn/bag và điền vào hệ thống
US-03:
Là MC, tôi muốn hệ thống đọc và điền dữ liệu thành phần tự động từ máy đo phổ
US-04:
Là MC, tôi muốn kết nối máy in với máy đo phổ nhằm in nhanh nhãn thành phần mỗi khi đo
Khác
Sử dụng thiết bị Mobile truy cập ERP bằng Browser
US-01:
Là MC, KHSX và Phòng Kinh doanh, tôi muốn có thể dùng thiết bị Mobile để nhận thông báo và truy cập hệ thống trong phạm vi công ty (bằng thiết bị của công ty)
