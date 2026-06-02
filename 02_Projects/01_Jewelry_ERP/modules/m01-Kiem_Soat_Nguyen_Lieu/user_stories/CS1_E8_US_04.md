# 🏷️ [CS1.E8.US-04] Tồn Kho - Phiếu Xuất Gộp NL và Hội (Combined Goods Issue)

**Epic:** Tồn kho (CS1.E8)
**Actor:** Nhân viên MC Nguyên Liệu

## 1. USER STORY
- **Là một:** Nhân viên MC cấp NL.
- **Tôi muốn:** Tạo 1 Phiếu xuất kho (Goods Issue) duy nhất để xuất cùng lúc Vàng từ Kho NL (Seva) và các thành phần phụ gia từ Kho Hội (Hàng ngày) khi thực hiện lệnh Đúc (Casting) hoặc Chuyển chế.
- **Để:** Tiết kiệm thời gian thao tác, giảm thiểu số lượng chứng từ, và vẫn đảm bảo truy xuất nguồn gốc (traceability) rõ ràng cho từng line hàng (dòng vật tư) được lấy từ kho nào.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Giao diện tạo phiếu xuất
- **Given:** Người dùng chọn một Yêu cầu cấp NL (VD: Đúc cây thông).
- **When:** Người dùng nhấn "Tạo Phiếu Xuất (Cấp NL)".
- **Then:** Hệ thống mở form tạo phiếu xuất, gợi ý sẵn danh sách các vật tư cần xuất dựa trên định mức (BOM/Recipe). Bao gồm:
    - Vàng tinh khiết (Au 99.99) hoặc Vàng 24K từ Kho NL.
    - Master Alloy, Bạc, Đồng... từ Kho Hội.

### AC2: Chi tiết Line Item ghi rõ Nguồn kho (Source Warehouse)
- **Given:** Người dùng đang chỉnh sửa form Phiếu Xuất.
- **When:** Người dùng thêm mới hoặc xem các dòng vật tư (Line Items) có trong phiếu.
- **Then:** Mỗi dòng (Line) bắt buộc phải hiển thị và cho phép chọn/xác nhận **Kho nguồn (Source Sub-inventory)** và **Mã Lot**.
    - *Line 1:* Xuất 100g Au 99.99 | Kho Nguồn: `Kho NL Seva - Fine Gold` | Lot: `LOT-SEVA-001`
    - *Line 2:* Xuất 10g Master Alloy | Kho Nguồn: `Kho Hội - Hàng ngày` | Lot: `LOT-ALLOY-005`
    - *Line 3:* Xuất 5g Bạc | Kho Nguồn: `Kho Hội - Hàng ngày` | Lot: `LOT-AG-012`

### AC3: Xử lý trừ tồn kho đồng thời
- **Given:** Người dùng hoàn tất thông tin và nhấn "Xác nhận Xuất Kho" (Commit).
- **When:** Hệ thống xử lý ghi nhận giao dịch.
- **Then:** 
    - Hệ thống kiểm tra Tồn khả dụng của tất cả các dòng. Nếu bất kỳ dòng nào bị thiếu (Gây ra tồn âm), hệ thống **Rollback toàn bộ phiếu** và báo lỗi chi tiết dòng nào thiếu.
    - Nếu đủ, hệ thống đồng thời trừ tồn kho ở `Kho NL Seva` và `Kho Hội` theo đúng thông tin Kho Nguồn của từng dòng. Phiếu chuyển sang trạng thái "Hoàn thành".

### AC4: In chứng từ xuất kho
- **Given:** Phiếu xuất đã hoàn thành.
- **When:** Người dùng nhấn "In Phiếu Xuất".
- **Then:** Layout phiếu in hiển thị rõ Header chung, và danh sách các Line Items được gom nhóm (Group By) theo Kho Nguồn để thủ kho dễ dàng đi nhặt hàng (Picking).

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

**Trạng thái View:**
- Màn hình tạo phiếu xuất (Form) dạng Master-Detail.
- Phần Detail (Grid) có các cột quan trọng: Mã Item, Tên Item, **Kho Nguồn (Dropdown readonly hoặc chọn được)**, Lô/Lot, Trọng lượng Yêu cầu, Trọng lượng Thực xuất.

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Phiếu xuất cấp NL cho sản xuất (Casting) là chứng từ gộp (Composite Document). Một mã phiếu (Issue Code) có thể chứa nhiều Transaction con trừ vào nhiều Sub-inventory khác nhau.
- **BR-02:** Nguyên tắc Atomicity (All or Nothing): Toàn bộ các dòng vật tư trong phiếu phải xuất thành công thì phiếu mới được ghi nhận. Không được phép xuất thiếu (Partially Issue) trong cùng một phiếu đúc để tránh sai lệch tuổi vàng của mẻ đúc.

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Kho Nguồn (Line level) | Source Sub-Inventory | Enum/FK | Ràng buộc theo loại Item |
| Lô xuất | Source Lot ID | FK | |
| Trọng lượng xuất | Issue Qty | Decimal(10,4) | > 0 và <= Tồn khả dụng |
