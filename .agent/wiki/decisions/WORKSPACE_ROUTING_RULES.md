# QUY TẮC ĐỊNH TUYẾN DỮ LIỆU & AN TOÀN (WORKSPACE RULES V2.0)

Tài liệu này là "Trí nhớ cứng" (Hard-coded memory) cho mọi phiên làm việc của nhóm đặc vụ (Agents) thuộc BA-Kit tại Work Station này. Bất kể phiên làm việc mới hay cũ, các Agents BẮT BUỘC tuân thủ:

## 1. Dữ Liệu Đầu Vào (As-Is / Raw)
- **Vị trí gốc:** `D:\Work Station\01_Raw_Inputs\`
- **Quy tắc Người dùng:** Người dùng được phép thả mọi file thô, lộn xộn vào thẳng thư mục gốc này để tiết kiệm thời gian.
- **Quy tắc Agent (Tự động dọn dẹp):** Bất kỳ Agent nào khi được yêu cầu đọc và phân tích file tại mục này, TRƯỚC KHI kết thúc tác vụ, BẮT BUỘC phải tạo thư mục gom nhóm (Ví dụ: `01_Raw_Inputs/Project_A_Inbox/`) và dùng lệnh hệ thống di chuyển file thô đó vào thư mục tương ứng.

## 2. Tri Thức Dùng Chung (Shared Knowledge / Wiki)
- **Vị trí bắt buộc:** `D:\Work Station\.agent\wiki\concepts\`
- **Quy tắc Tránh phân mảnh (Anti-Fragmentation):** Tuyệt đối KHÔNG tạo nhiều file cho cùng một khái niệm (Ví dụ: Không tạo `WMS-User.md` và `TMS-User.md`). Chỉ tạo duy nhất 1 file `User.md`. Nếu định nghĩa của các dự án khác nhau, Agent phải dùng thẻ Markdown Heading (`## Ngữ cảnh dự án A`, `## Ngữ cảnh dự án B`) để phân tách nội dung NẰM BÊN TRONG file duy nhất đó.

## 3. Tạo Tác Dự Án (Project Artifacts)
- **Vị trí bắt buộc:** `D:\Work Station\02_Projects\[Tên_Dự_Án]\modules\mXX-[Tên_Module]\`
- **Quy tắc:** Mọi Spec, User Story, Diagram được tạo ra phải lưu đúng vào folder của module.

## 4. An Toàn Dữ Liệu AI (AI Failsafe - KHÔNG DÙNG GIT)
- **Quy tắc Backup vật lý:** Hệ thống không phụ thuộc vào việc người dùng nhớ chạy lệnh `git commit`. Thay vào đó, MỌI AGENT khi nhận lệnh **sửa đổi khối lượng lớn (Overwrite)** trên một file Markdown/JSON đang có sẵn, BẮT BUỘC phải tạo một bản sao lưu vật lý bằng lệnh copy (Ví dụ: từ `US-01.md` thành `US-01_backup_truoc_khi_sua.md`) rồi mới tiến hành ghi đè dữ liệu mới. Lỗi hệ thống nếu không tuân thủ quy tắc này.
