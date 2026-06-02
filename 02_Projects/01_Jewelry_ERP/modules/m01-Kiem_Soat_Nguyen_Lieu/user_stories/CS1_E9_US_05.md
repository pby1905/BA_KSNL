# 🏷️ [CS1.E9.US-05] Kiểm kê kho - Phê duyệt điều chỉnh tồn kho (Approve Adjustment)

**Epic:** Kiểm kê kho & Điều chỉnh (CS1.E9)
**Actor:** Người phê duyệt (Trưởng phòng MC)

## 1. USER STORY
- **Là một:** Người phê duyệt (Trưởng phòng MC).
- **Tôi muốn:** Xem xét, từ chối hoặc phê duyệt các Phiếu yêu cầu điều chỉnh tồn kho có phát sinh hao hụt giá trị lớn.
- **Để:** Hệ thống chính thức cập nhật Tồn kho sổ sách bằng với Tồn thực tế và đóng Phiếu kiểm kê.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Xem chi tiết yêu cầu
- **Given:** Có một Phiếu yêu cầu điều chỉnh chờ duyệt (`Pending Approval`).
- **When:** Người phê duyệt mở phiếu.
- **Then:** Có thể xem đầy đủ danh sách Lot chênh lệch, giá trị hao hụt ước tính, lý do, ghi chú giải trình và file đính kèm.

### AC2: Phê duyệt (Approve)
- **Given:** Người phê duyệt đồng ý với giải trình.
- **When:** Bấm "Phê duyệt" (Approve).
- **Then:** Hệ thống thực hiện giao dịch Tăng/Giảm (In/Out) cho từng Lot tương ứng. Tồn kho sổ sách (On-hand) được cập nhật bằng số thực tế. Trạng thái phiếu thành `Approved`. Phiếu kiểm kê gốc (nếu có) chuyển thành `Completed`. Ghi nhận lịch sử (Log) giao dịch vào Thẻ kho với loại chứng từ là "Adjustment".

### AC3: Từ chối (Reject)
- **Given:** Người phê duyệt không đồng ý.
- **When:** Bấm "Từ chối" (Reject) và nhập lý do.
- **Then:** Phiếu điều chỉnh chuyển sang `Rejected`. Tồn kho không bị thay đổi. Phiếu kiểm kê gốc (nếu có) quay về trạng thái `Reviewing`.

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- Giao diện có Box "Lịch sử phê duyệt" (Approval History) hiển thị thời gian và người đã thao tác.
- Gửi thông báo (Push Notification/Email) cho Người duyệt khi có yêu cầu mới và cho Người tạo khi có kết quả duyệt.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Việc cập nhật tồn kho (Inventory Transaction) chỉ diễn ra 1 lần duy nhất tại thời điểm Approval thành công.
- **BR-02:** Đối với các vật tư phụ (Consumables/Packaging) có giá trị thấp, hệ thống có thể cấu hình Auto-Approve (Tự động duyệt) nếu giá trị chênh lệch dưới 1 định mức (Ví dụ: < 100,000 VNĐ). Vàng/Bạc bắt buộc duyệt thủ công.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Người duyệt | Approved By | User ID | Lấy ID của người đang đăng nhập thực hiện thao tác |
| Ngày duyệt | Approved Date | Datetime | Timestamp hiện tại |
| Lý do từ chối | Reject Reason | Text | Bắt buộc khi Reject |
