# 🏷️ [CS1.E1.US-25] Phiếu trả NL - Xác nhận xuất trả

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** Thủ kho / Nhân viên MC phụ trách trả hàng

## 1. USER STORY
- **Là một (As a):** Thủ kho hoặc Nhân viên MC có trách nhiệm giao trả hàng.
- **Tôi muốn (I want):** Xác nhận xuất trả nguyên liệu cho khách hàng trên hệ thống sau khi khách hàng đã nhận lại hàng vật lý và ký biên bản.
- **Để (So that):** Hệ thống chốt trạng thái hoàn thành của Phiếu trả NL, đóng lại quy trình xử lý, và cập nhật chính xác trạng thái tồn kho ảo/thực tế của các nguyên liệu bị trả.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC 1: Điều kiện hiển thị nút "Xác nhận xuất trả"
- **Given:** Người dùng đang xem chi tiết một Phiếu trả NL.
- **And:** Phiếu trả đang ở trạng thái **"Mới tạo"** (hoặc "Chờ khách nhận").
- **When:** Người dùng có đủ quyền hạn truy cập.
- **Then:** Hệ thống hiển thị nút **"Xác nhận xuất trả"** (hoặc "Hoàn thành phiếu").

### AC 2: Xác nhận hoàn tất trả hàng
- **Given:** Khách hàng đã nhận lại hàng và ký xác nhận Biên bản trả hàng.
- **When:** Người dùng nhấn nút **"Xác nhận xuất trả"**.
- **Then:** Hệ thống hiển thị Pop-up xác nhận: *"Bạn có chắc chắn muốn xác nhận xuất trả nguyên liệu cho phiếu [Mã phiếu]? Hành động này không thể hoàn tác."*
- **And:** Nếu người dùng chọn **Đồng ý**, hệ thống tiến hành xử lý giao dịch.

### AC 3: Logic cập nhật trạng thái (Output States)
- **Given:** Người dùng đã chọn Đồng ý xác nhận xuất trả.
- **Then:** Hệ thống tự động cập nhật trạng thái các đối tượng:
  - **Phiếu trả NL:** Chuyển sang trạng thái **"Hoàn thành"** (không cho phép chỉnh sửa hay Hủy nữa).
  - **Dòng nguyên liệu gốc (Line items):** Chuyển từ "Đã lên phiếu trả" sang **"Đã xuất trả"** (Returned).
  - **Phiếu tiếp nhận gốc:** Giữ nguyên trạng thái **"Trả hàng"** (nếu trả toàn bộ) hoặc **"Đang thực hiện"** (nếu trả một phần), nhưng hệ thống ghi nhận luồng trả hàng của kiện/dòng nguyên liệu này đã chính thức đóng.

### AC 4: Logic tồn kho (Inventory Logic)
- **Given:** Phiếu trả NL được hoàn thành.
- **Then:** Hệ thống xử lý kho tùy theo loại phiếu trả:
  - **Trường hợp lệch bao bì:** Do nguyên liệu chưa được nhập kho chính thức (chưa qua bước sinh mã Lô nhập kho), hệ thống **KHÔNG** phát sinh bút toán xuất kho. Chỉ ghi nhận hoàn tất vòng đời Workflow State.
  - **Trường hợp không đạt kiểm chi tiết:** Nếu ở các bước trước nguyên liệu đã được nhập vào "kho tạm chờ xử lý", hệ thống sẽ phát sinh bút toán **Xuất kho trả khách** để trừ tồn kho tạm thời, đảm bảo số liệu kho khớp với thực tế.

### AC 5: Ghi nhận Lịch sử hoạt động (Audit Trail)
- **Given:** Quá trình xuất trả hoàn tất.
- **Then:** Hệ thống ghi lại log vào Lịch sử hoạt động của Phiếu trả:
  - *"[Tên User] đã xác nhận xuất trả nguyên liệu thành công vào lúc [Thời gian]."*

---

## 3. THIẾT KẾ (UX/UI)
- Nút "Xác nhận xuất trả" sử dụng Primary Button (màu nổi bật) do đây là Call-to-action chính chốt lại vòng đời của phiếu trả.
- Sau khi phiếu chuyển trạng thái "Hoàn thành", toàn bộ form dữ liệu chuyển sang chế độ Read-only.
- Các nút "Chỉnh sửa", "Hủy phiếu" tại màn hình này sẽ bị ẩn đi hoàn toàn.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01 (Phân quyền):** Chỉ những user thuộc nhóm Thủ kho hoặc Quản lý được phân quyền mới có thể thực hiện thao tác Xác nhận xuất trả.
- **BR-02 (Không thể hoàn tác):** Thao tác này là thao tác chốt giao dịch vật lý (hàng đã ra khỏi xưởng). Không hỗ trợ Hủy (Cancel) hay Revert sau khi đã Hoàn thành. Nếu có sai sót, cần xử lý bằng quy trình ngoại lệ (Exception Handling) có biên bản ký tay.
- **BR-03 (Điều kiện tiên quyết):** Biên bản in trả hàng (US-24.1) nên được in và ký với khách trước khi thao tác bấm Xác nhận này trên hệ thống.

---

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)
- Backend cần thiết lập **Database Transaction** bao bọc toàn bộ khối lệnh: (1) Cập nhật trạng thái Phiếu trả + (2) Cập nhật trạng thái dòng Line items gốc + (3) Ghi nhận bút toán kho (nếu có). Đảm bảo tính nhất quán dữ liệu (Data Consistency), nếu lỗi 1 khâu thì rollback toàn bộ.
- Có cơ chế khóa chống click đúp (Double-click prevention) trên UI và Idempotency key trên API để ngăn việc trừ kho 2 lần do lỡ tay nhấp đúp.

---

## 6. GHI CHÚ CHO QC (TEST CASES)
- **TC1:** Xác nhận xuất trả với loại phiếu "Lệch bao bì" -> Verify trạng thái các bảng cập nhật thành công, và đảm bảo KHÔNG có bút toán kho nào bị sinh nhầm.
- **TC2:** Xác nhận xuất trả với loại phiếu "Không đạt kiểm chi tiết" (có nhập kho tạm) -> Verify hệ thống có sinh ra phiếu xuất kho tương ứng để trừ tồn.
- **TC3:** Sau khi phiếu đã Hoàn thành, cố tình dùng Postman/Swagger gọi lại API Hủy phiếu (Cancel Return) -> Đảm bảo Backend chặn đứng và trả về HTTP 400 (Status Validation).
- **TC4:** Dùng tool giả lập nhấp đúp chuỗi thao tác "Xác nhận xuất trả" siêu nhanh -> Đảm bảo API chỉ ghi nhận 1 lần giao dịch duy nhất.
