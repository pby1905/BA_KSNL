# 🏷️ [CS1.E1.US-07] Nhận NL khách - Xử lý: Đo phổ (XRF analysis)

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** Nhân viên Tiếp nhận Nguyên liệu

## 1. USER STORY
- **Là một:** Nhân viên Tiếp nhận Nguyên liệu
- **Tôi muốn:** Ghi nhận kết quả đo phổ chi tiết cho dẻ trong phiếu tiếp nhận.
- **Để:** Xác định chính xác hàm lượng vàng (tuổi vàng) và các kim loại đi kèm, làm căn cứ tính toán trọng lượng vàng nguyên chất (vàng tinh) cho quá trình gia công.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Đo phổ
- **Given:** Nhân viên đo phổ mở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhận ở bước trước.
- **And:** Nhân viên chọn các dòng nguyên liệu có loại = "Dẻ" nhấn vào nút "Đo phổ".
- **When:** Hệ thống hiển thị Modal "Đo phổ" (như hình ảnh thiết kế).
- **Then:** Nhân viên có thể nhập các thành phần kim loại.

### AC 2: Kiểm tra tổng tỷ lệ thành phần (Validation %)
- **Given:** Nhân viên nhập tỷ lệ % cho các kim loại.
- **When:** Nhấn "Lưu" trong Modal kết quả đo.
- **Then:** Hệ thống kiểm tra tổng %. Nếu tổng% > 100%, hiển thị cảnh báo và không cho lưu.
  - **VN:** "Tổng tỷ lệ các thành phần kim loại không được vượt quá 100%. Vui lòng kiểm tra lại (Hiện tại: {Total}%)."
  - **EN:** "The total percentage of metal components cannot exceed 100%. Please verify your input (Current: {Total}%)."

### AC 3: Có tạp
- **Given:** Nhân viên hoàn thành nhập liệu 1 dòng ở Modal "Đo phổ".
- **When:** Checkbox "Tạp chất" = checked (tự động check khi có thành phần ngoài Bạc Đồng Kẽm).
- **Then:** Hệ thống hiển thị form nhập "Có tạp".

### AC 4: Đo lại & hủy xác nhận chênh lệch
- **Given:** Nhân viên chọn các dòng nguyên liệu có loại = "Dẻ", trạng thái "Đang xử lý".
- **And:** Dòng nguyên liệu này có xử lý chênh lệch.
- **When:** Nhân viên nhấn vào nút "Đo phổ".
- **Then:** Hiển thị popup xác nhận:
  - **VN:** Phiếu Xử lý Chênh lệch tại các dòng {line 1, line 2...} sẽ chuyển sang trạng thái "Hủy". Bạn có chắc chắn muốn tiếp tục? "Có / Không"
  - **EN:** The Variance Processing Ticket for lines {line 1, line 2...} will be changed to 'Cancelled' status. Are you sure you want to proceed? 'Yes / No'
- **Hành động tiếp:**
  - Nhập **Có**: → Mở Modal "Đo phổ" và cho phép edit → Khi Submit kết quả Modal "Đo phổ" → Chuyển trạng thái phiếu "Xử lý chênh lệch" sang trạng thái → "Hủy".

---

## 3. THIẾT KẾ (UX/UI)
- (Tham chiếu thiết kế)

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Chỉ những dòng nguyên liệu thỏa mãn điều kiện sau có thể thực hiện Đo phổ, kiểm tra theo thứ tự sau:
  - Phân loại = Dẻ → Vi phạm, cảnh báo: "Chỉ nguyên liệu 'Dẻ' có thể thực hiện Đo phổ" (Only "Dẻ" materials can perform XRF analysis).
  - Tình trạng/Trạng thái = Đang xử lý → Vi phạm, cảnh báo: "Chỉ trạng thái 'Đang xử lý' có thể thực hiện Đo phổ" (XRF analysis can only be performed when the status is "In Progress").
- **BR-02:** Kết quả đo phổ sau khi "Hoàn tất" sẽ được lưu log lịch sử (Audit Trail) để truy vết nếu có khiếu nại từ khách hàng về sau.

---

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)

### 5.1 Workflow validation
- Logic validate đảm bảo không save vượt quá 100% của kim loại.

### 5.2 Field Definition Table (Modal đo phổ)

| Tên trường (VN) | EN Field Name | Type | Required | Rules |
|---|---|---|---|---|
| Tuổi - Seva | Purity (Seva) | Decimal(4,2) | Có | Default = 0. Validate < 100. |
| TL - Seva sau đo | Post-XRF Weight(Seva) | Decimal(10,4) | Có | > 0 |
| TL hao hụt | Scraping Loss | Decimal(10,4) | Read-only | = "TL Seva" - "TL - Seva sau đo" |
| % Ag | % Ag | Decimal(4,2) | Không | Default = 0. Validate < 100. |
| % Cu | % Cu | Decimal(4,2) | Không | Default = 0. Validate < 100. |
| % Zn | % Zn | Decimal(4,2) | Không | Default = 0. Validate < 100. |
| % Ni | % Ni | Decimal(4,2) | Không | Default = 0. Validate < 100. |
| % Pd | % Pd | Decimal(4,2) | Không | Default = 0. Validate < 100. |
| % M | % M | Decimal(4,2) | Không | Default = 0. Validate < 100. |
| % Fe | % Fe | Decimal(4,2) | Không | Default = 0. Validate < 100. |
| Có tạp chất | Has Impurities | Checkbox | Không | Tự động check khi có thành phần ngoài: Ag, Cu, Zn. Người dùng cũng có thể manual check/uncheck. |
| Ghi chú | Remarks | Text Area | Không | Max 500 ký tự |
| Line | Line | Number | Read-only | Số thứ tự dòng của NL ở bảng danh sách NL. |
| Số tuổi trừ (dự kiến) | Purity Deduction (Est.) | Decimal(4,2) | Có | Default = 0.3. Validate > 0 và < 100. |
| Tuổi - Seva (dự kiến) | Purity (Seva) (Est.) | Decimal(4,2) | Read-only | = "Tuổi - Seva" - "Số tuổi trừ (dự kiến)" |
| Quy 99.99 - Seva (dự kiến) | 99.99 Equiv. (Seva) (Est.) | Decimal(10,4) | Read-only | = `"TL Seva" * "Tuổi - Seva (dự kiến)" / 99.99` |
| Quy 99.99 - Khách bù (dự kiến) | 99.99 Cust Compensation (Est.) | Decimal(10,4) | Read-only | = `"Quy 99.99 - Khách" - "Quy 99.99 - Seva"` |

---

## 6. GHI CHÚ CHO QC
- Cần validation pop-ups nếu tổng % > 100.
- Test case chuyển luồng "Đo lại" khi dòng đang có trạng thái "Xử lý chênh lệch".
