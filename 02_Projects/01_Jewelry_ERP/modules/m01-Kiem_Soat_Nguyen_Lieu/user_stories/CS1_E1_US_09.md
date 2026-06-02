# 🏷️ [CS1.E1.US-09] Nhận NL khách - Xử lý: Kiểm tem - Tính đá (Tag & Stone Verification)

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** Nhân viên Tiếp nhận Nguyên liệu

## 1. USER STORY
- **Là một (As a):** Nhân viên Tiếp nhận Nguyên liệu
- **Tôi muốn (I want):** Ghi nhận trọng lượng đá với nguyên liệu hàng hồi.
- **Để (So that):** Hệ thống tự động tính toán Trọng lượng vàng thực tế (TL - Seva) làm cơ sở cho việc đo phổ và đối soát giá trị.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Kiểm tem - Tính đá (Tag & Stone Verification)
- **Given (Biết rằng):** Nhân viên mở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhận ở bước trước.
- **And (Và):** Nhân viên chọn các dòng nguyên liệu có:
  - Loại = "Hàng hồi mới" hoặc "Hàng hồi nấu"
  - Tình trạng = "NL từ khách"
  - Đồng thời nhấn vào nút "Kiểm tem - Tính đá".
- **When (Khi):** Hệ thống hiển thị Modal "Kiểm tem - Tính đá" (như hình ảnh thiết kế).
- **Then (Thì):** Nhân viên có thể nhập thông tin TL đá.

### AC 2: Kiểm lại & hủy xác nhận chênh lệch
- **Given (Biết rằng):** Nhân viên chọn các dòng nguyên liệu có:
  - Loại = "Hàng hồi mới" hoặc "Hàng hồi nấu".
  - Tình trạng = "NL từ khách".
  - Trạng thái = "Đang xử lý".
- **And (Và):** Dòng nguyên liệu này đang có xử lý chênh lệch.
- **When (Khi):** Nhân viên nhấn vào nút "Kiểm tem - Tính đá".
- **Then (Thì):** Hiển thị popup xác nhận:
  - **VN:** Phiếu Xử lý Chênh lệch tại các dòng {line 1, line 2...} sẽ chuyển sang trạng thái "Hủy". Bạn có chắc chắn muốn tiếp tục? "Có / Không"
  - **EN:** The Variance Processing Ticket for lines {line 1, line 2...} will be changed to 'Cancelled' status. Are you sure you want to proceed? 'Yes / No'
- **Hành động tiếp:**
  - Nhập **Có**: → Mở Modal "Kiểm tem - Tính đá" và cho phép edit → Khi Submit kết quả Modal "Kiểm tem - Tính đá" → Chuyển trạng thái phiếu "Xử lý chênh lệch" sang trạng thái → "Hủy".

---

## 3. THIẾT KẾ (UX/UI)
- (Tham chiếu thiết kế)

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Chỉ những dòng nguyên liệu thỏa mãn điều kiện sau có thể thực hiện Kiểm tem - Tính đá, kiểm tra theo thứ tự:
  - Phân loại = Hàng hồi mới / Hàng hồi nấu → Vi phạm, cảnh báo: "Chỉ nguyên liệu 'Hàng hồi' có thể thực hiện Kiểm tem - Tính đá" (Only "Hàng hồi" materials can perform Tag & Stone Verification).
  - Tình trạng = "NL từ khách" → Vi phạm, cảnh báo: "Chỉ 'NL từ khách' có thể thực hiện Kiểm tem - Tính đá" (Tag & Stone Verification can only be performed when the origin is "Customer Material").
  - Trạng thái = "Đang xử lý" → Vi phạm, cảnh báo: "Chỉ trạng thái 'Đang xử lý' có thể thực hiện Kiểm tem - Tính đá" (Tag & Stone Verification can only be performed when the status is "In Progress").
- **BR-02:** Kết quả sau khi "Hoàn tất" sẽ được lưu log lịch sử (Audit Trail) để truy vết nếu có khiếu nại từ khách hàng về sau.
- **BR-03:** TL đá - Seva phải < TL tổng - Seva.

---

## 5. GHI CHÚ KỸ THUẬT & FIELD DEFINITION

### 5.1 Workflow validation
- Logic validate theo các rule định nghĩa (tuổi vàng, chênh lệch TL).

### 5.2 Field Definition Table (Modal Kiểm tem - Tính đá)

| Tên trường (VN) | EN Field Name | Type | Required | Rules & Logic |
|---|---|---|---|---|
| TL đá - Seva | Stone Weight (Seva) | Decimal(10,4) | Có | `0 <= value` |
| Có sai tem | Tag Discrepancy | Checkbox | Không | Default = uncheck |
| Tuổi - Seva | Purity (Seva) | Decimal(4,2) | Read-only | Tự động lấy "Tuổi - Khách" nếu "Có sai tem" = Uncheck. |
| TL - Seva | Metal Weight (Seva) | Decimal(10,4) | Read-only | `= "TL tổng - Seva" - "TL đá - Seva"` |
| Quy 99.99 - Seva | 99.99 Equiv. (Seva) | Decimal(10,4) | Read-only | `= ("TL - Seva" * "Tuổi - Seva") / 99.99` (Làm cơ sở để nhập kho) |
| Ghi chú | Remarks | Text Area | Không | Max 500 ký tự |

---

## 6. GHI CHÚ CHO QC
- **Kiểm tra logic trừ trọng lượng:** Đảm bảo tổng trọng lượng các loại đá không vượt quá trọng lượng thực tế của món hàng.
