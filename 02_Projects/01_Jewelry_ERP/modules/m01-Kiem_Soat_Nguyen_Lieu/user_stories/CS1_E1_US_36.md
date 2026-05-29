# 🏷️ [CS1.E1.US-36] Mua Hội (Phần 1) - Kiểm tra ngoại quan và Cân trọng lượng

**Epic:** Nhận nguyên liệu (CS1.E1)
**Actor:** Nhân viên Kho (Warehouse Staff), Nhân viên Mua hàng (Purchaser)

## 1. USER STORY
- **Là một (As a):** Nhân viên Kho.
- **Tôi muốn (I want):** Thực hiện bước đầu tiên của quy trình nhận Hội (kiểm tra ngoại quan, chứng từ, và mở niêm phong cân trọng lượng).
- **Để (So that):** Đảm bảo hàng hóa nhận được nguyên vẹn, khớp số lượng/trọng lượng với Đơn đặt hàng (PO) và Hóa đơn giao hàng trước khi chuyển đi kiểm định chất lượng sâu hơn.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC 1: Đánh giá Ngoại quan & Chứng từ
- **Given:** Lô hàng Hội vừa được NCC giao tới Kho.
- **When:** Nhân viên kho thực hiện kiểm tra và đối chiếu các thông tin: Ngoại quan bao bì, tem niêm phong, và chứng từ hóa đơn đi kèm so với PO trên hệ thống.
- **Then:** Hệ thống cho phép cập nhật kết quả: **"Đạt"** hoặc **"Không đạt"**.
- **And:** Nếu **"Không đạt"**, hệ thống sinh ra một "Yêu cầu xử lý ngoại lệ" gửi cho bộ phận Mua hàng. Lô hàng bị khóa (Hold), không thể qua bước Cân.

### AC 2: Mở niêm phong và Cân Trọng lượng
- **Given:** Lô hàng đã được đánh giá Ngoại quan là "Đạt" (hoặc "Không đạt" nhưng đã được Mua hàng duyệt "Chấp nhận").
- **When:** Nhân viên Kho mở niêm phong và thực hiện cân tổng trọng lượng thực tế cho từng loại Hội.
- **Then:** Nhân viên Kho nhập số liệu Cân thực tế vào hệ thống.
- **And:** Hệ thống tự động so sánh số liệu cân với số lượng đặt trên PO. Áp dụng giới hạn dung sai (Threshold) đã được thiết lập.
- **And:** Nếu phát hiện **"Lệch TL"** (vượt quá dung sai), hệ thống cảnh báo và tự động gửi thông báo cho Mua hàng. Lô hàng bị khóa ở bước cân.

### AC 3: Mua hàng xử lý chênh lệch (Ngoại quan / Trọng lượng)
- **Given:** Lô hàng bị khóa do Lỗi Ngoại quan hoặc Lệch TL.
- **When:** Nhân viên Mua hàng vào hệ thống xem chi tiết sai lệch và liên hệ với NCC để thương lượng.
- **Then:** Nhân viên Mua hàng có 2 tuỳ chọn xử lý:
    1. **"Chấp nhận chênh lệch":** Ghi chú lý do chấp nhận rủi ro/sai số. Lô hàng được mở khóa (Unlock) để Kho tiếp tục thao tác.
    2. **"Từ chối / Trả hàng":** Đóng quy trình tiếp nhận của lô này, đổi trạng thái thành **"Chờ xuất trả NCC"**.

### AC 4: Chuyển bước Kiểm định (Lab)
- **Given:** Lô hàng được Cân và "Đúng TL" (hoặc Lệch TL nhưng đã được Mua hàng Chấp nhận).
- **When:** Nhân viên kho xác nhận hoàn tất quy trình kiểm tra vật lý.
- **Then:** Hệ thống chuyển trạng thái lô hàng thành **"Chờ kiểm định Lab"**.

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

- **Giao diện:** Màn hình phiếu kiểm tra (Inspection Ticket) chia làm 2 phần: Section 1 (Ngoại quan/Chứng từ) dạng Checklist. Section 2 (Trọng lượng) dạng Grid nhập số liệu cân.
- **Trạng thái:** `Chờ kiểm chứng từ` -> `Chờ cân` -> `Chờ Mua hàng xử lý` -> `Chờ kiểm định Lab` / `Chờ trả hàng`.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)

- **BR-01:** Nhân viên Kho chỉ được phép ghi nhận số liệu thực tế, **không có quyền** tự quyết định bỏ qua lỗi. Việc "Chấp nhận" là thẩm quyền tuyệt đối của bộ phận Mua hàng.
- **BR-02:** Hàng hoá ở giai đoạn này chỉ nằm trong Khu vực tiếp nhận tạm (Receiving Area), chưa được hạch toán vào Tồn kho khả dụng (Available Inventory).

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU

| Tên trường (VN) | Tên trường (EN) | Nơi hiển thị | Ghi chú |
|---|---|---|---|
| Đánh giá ngoại quan | Visual Check | Section 1 | Dropdown: Đạt / Không đạt |
| Ghi chú ngoại quan | Visual Remarks | Section 1 | Text. Bắt buộc nhập nếu Không đạt. |
| TL PO | PO Weight | Section 2 | Read-only |
| TL Thực tế | Actual Weight | Section 2 | Decimal(10,4). User input. |
| Mức chênh lệch | Variance | Section 2 | Tự động tính = Thực tế - PO |
| Duyệt Ngoại lệ | Exception Approval| Popup/Tab Duyệt| Hành động của Mua hàng. |

---

## 6. GHI CHÚ CHO QC

- **Test Rule Lệch TL:** Nhập TL Thực tế lệch với PO quá 5% (hoặc mức cấu hình) -> Hệ thống phải bật cảnh báo và không cho user Kho bấm "Chuyển Lab".
- **Test Workflow:** Verify luồng Mua hàng bấm "Trả hàng" -> Phiếu tự động chuyển về trạng thái Hủy/Trả, kết thúc quy trình.
