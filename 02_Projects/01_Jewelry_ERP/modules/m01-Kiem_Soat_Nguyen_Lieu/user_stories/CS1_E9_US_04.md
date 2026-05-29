# 🏷️ [CS1.E9.US-04] Kiểm kê kho - Tạo phiếu yêu cầu điều chỉnh (Create Adjustment Request)

**Epic:** Kiểm kê kho & Điều chỉnh (CS1.E9)
**Actor:** Trưởng bộ phận MC (TBP MC), Kế toán

## 1. USER STORY
- **Là một:** TBP MC hoặc Kế toán kho.
- **Tôi muốn:** Tạo phiếu yêu cầu điều chỉnh tồn kho (tăng/giảm) dựa trên danh sách các Lot có chênh lệch sau khi kiểm kê, hoặc điều chỉnh hao hụt tự nhiên trong quá trình lưu kho/sản xuất.
- **Để:** Hợp thức hóa số dư tồn kho sổ sách cho khớp với tồn kho thực tế, đồng thời ghi nhận rõ nguyên nhân hao hụt.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Tạo từ Phiếu kiểm kê
- **Given:** Có một Phiếu kiểm kê đang ở trạng thái `Reviewing` với các Lot bị chênh lệch.
- **When:** Người dùng chọn "Tạo phiếu điều chỉnh" từ Phiếu kiểm kê.
- **Then:** Hệ thống tự động tạo một Phiếu yêu cầu điều chỉnh (Adjustment Request) chứa toàn bộ các dòng có chênh lệch. Trọng lượng cần điều chỉnh (Adjustment Qty) = Variance Qty.

### AC2: Tạo thủ công (Manual Adjustment)
- **Given:** Hàng hóa có hao hụt bất thường cần xuất hủy mà không nằm trong đợt kiểm kê.
- **When:** Người dùng tạo mới Phiếu điều chỉnh tự do.
- **Then:** Hệ thống cho phép chọn Lot, nhập số lượng điều chỉnh (âm hoặc dương), và bắt buộc chọn "Lý do điều chỉnh" (Reason Code) (Ví dụ: Hao hụt tự nhiên, Xuất hủy, Cân sai, Bụi vàng).

### AC3: Yêu cầu giải trình đính kèm
- **Given:** Người dùng lưu phiếu điều chỉnh.
- **When:** Tổng trọng lượng chênh lệch (đặc biệt là hao hụt Vàng/Bạc) vượt quá định mức cấu hình cho phép.
- **Then:** Hệ thống bắt buộc người dùng nhập "Ghi chú giải trình" và đính kèm file (Biên bản xử lý, Hình ảnh).

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- Giao diện có khu vực Attachments (Đính kèm file).
- Loại điều chỉnh (Adj Type): Tăng (Positive) / Giảm (Negative).

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Phiếu điều chỉnh ở trạng thái Draft chưa làm thay đổi tồn kho. Phải qua bước phê duyệt (Approve) mới được cộng/trừ vào Tồn khả dụng.
- **BR-02:** Chỉ những tài khoản có vai trò TBP MC/Kế toán mới được quyền tạo phiếu này.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Mã điều chỉnh | Adj ID | Text | Tự động sinh |
| Nguồn gốc | Source | Text | Tham chiếu đến Count ID (nếu từ kiểm kê) |
| Lý do | Reason Code | Enum | Hao hụt tự nhiên / Xuất hủy / Cân sai... |
| Giải trình | Explanation | Text | Bắt buộc nếu vượt định mức |
