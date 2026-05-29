# 🏷️ [CS1.E1.US-14] Nhận NL khách - Xử lý: Yêu cầu trả hàng (Request Return)

**Epic:** Nhận NL khách (CS1.E1)
**Actor:** Người phê duyệt chênh lệch.

## 1. USER STORY
- **Là một (As a):** Người phê duyệt chênh lệch.
- **Tôi muốn (I want):** Xem xét các dòng nguyên liệu có sai lệch vượt ngưỡng và thực hiện đưa ra quyết định.
- **Để (So that):** Chính thức ghi nhận các thông số đo đạc thực tế vào hệ thống và cho phép tiếp tục quy trình.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Yêu cầu trả hàng (Request Return)
- **Given (Biết rằng):** Người dùng mở phiếu tiếp nhận, Hệ thống hiển thị danh sách các dòng nguyên liệu đã tiếp nhận.
- **When (Khi):** Người dùng chọn dòng nguyên liệu ở trạng thái "Chờ xác nhận".
- **And (Và):** Chọn "Yêu cầu trả NL" (từng phiếu, không phê duyệt cùng lúc nhiều phiếu).
- **Then (Thì):** Hệ thống mở popup xác nhận Y/N.
- **And (Và):** Người dùng chọn Yes và nhập Ghi chú.
- **Then (Thì):**
  1. Cập nhật trạng thái dòng nguyên liệu: Từ "Chờ xác nhận" sang → "Yêu cầu trả".
  2. Cập nhật trạng thái phiếu xử lý chênh lệch: Từ "Chờ xác nhận" sang → "Yêu cầu trả".
  3. Ghi nhận ghi chú vào phiếu xử lý chênh lệch.

---

## 3. THIẾT KẾ (UX/UI)
- (Chưa có link đính kèm - theo tiêu chuẩn dự án)

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Chỉ những user có quyền "Phê duyệt chênh lệch" mới nhìn thấy và tương tác được nút "Chấp nhận chênh lệch"/"Yêu cầu trả NL".

---

## 5. GHI CHÚ KỸ THUẬT & VALIDATION (TECH NOTES)

### 5.1 Validation Logic
- Logic kiểm tra trạng thái tương tự như nghiệp vụ Chấp nhận chênh lệch.

### 5.2 Field Definition (Action Buttons)
- Nút "Yêu cầu trả NL": Disable nếu người dùng không đủ phân quyền.

---

## 6. GHI CHÚ CHO QC
- (Draft gốc không chỉ định Test Case cụ thể, QC nên test tương tự AC1 của các luồng xử lý chênh lệch khác).
