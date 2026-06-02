# 🏷️ [CS1.E9.US-01] Kiểm kê kho - Tạo và lên lịch kiểm kê (Create Inventory Count)

**Epic:** Kiểm kê kho & Điều chỉnh (CS1.E9)
**Actor:** Trưởng bộ phận Material Control (TBP MC), Kế toán

## 1. USER STORY
- **Là một:** TBP MC hoặc Kế toán kho.
- **Tôi muốn:** Tạo phiếu kiểm kê kho, chọn các khu vực kho hoặc danh sách Item cụ thể cần đếm.
- **Để:** Hệ thống tự động chốt số dư tồn kho sổ sách tại thời điểm kiểm kê và có thể khóa các giao dịch xuất/nhập của các Item đó để đảm bảo tính chính xác trong quá trình đếm thực tế.

---

## 2. TIÊU CHÍ CHẤP NHẬN (AC)

### AC1: Tạo mới phiếu kiểm kê
- **Given:** Người dùng ở màn hình Quản lý Kiểm kê.
- **When:** Người dùng chọn "Tạo phiếu kiểm kê mới".
- **Then:** Hệ thống yêu cầu nhập:
    - Tên đợt kiểm kê (Ví dụ: Kiểm kê định kỳ tháng 10 Kho Seva).
    - Ngày dự kiến kiểm đếm.
    - Người phụ trách kiểm đếm.
    - Phạm vi kiểm kê (chọn một trong các loại): Toàn bộ kho, Theo khu vực (Kho NL Khách, Kho Hội, Trạm Đồng Bộ), hoặc Theo Lot/Item cụ thể.

### AC2: Khóa giao dịch (Freeze Inventory)
- **Given:** Người dùng đã chọn phạm vi kiểm kê.
- **When:** Người dùng lưu và chuyển trạng thái phiếu kiểm kê sang "Đang kiểm đếm" (In Progress).
- **Then:** Hệ thống ghi nhận "Tồn sổ sách" (Snapshot Qty) của các Item tại thời điểm đó và KHÓA (hoặc cảnh báo) mọi giao dịch nhập/xuất liên quan đến các Lot/Item nằm trong phạm vi kiểm kê cho đến khi phiếu kiểm kê được hoàn tất.

---

## 3. THIẾT KẾ (UX/UI) & DATA MODEL

**Trạng thái Phiếu Kiểm kê:**
- `Draft` (Nháp) -> `In Progress` (Đang kiểm đếm) -> `Reviewing` (Chờ xử lý chênh lệch) -> `Completed` (Hoàn tất) / `Canceled` (Hủy).

---

## 4. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)
- **BR-01:** Chỉ TBP MC hoặc Kế toán có quyền phân quyền mới được tạo Phiếu kiểm kê.
- **BR-02:** Không thể tạo 2 phiếu kiểm kê trùng lặp phạm vi Lot/Item có trạng thái `In Progress` cùng một lúc (tránh conflict khóa tồn kho).

---

## 5. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (FIELD DEFINITION)

| Tên trường (VN) | Tên trường (EN) | Kiểu dữ liệu | Quy tắc Validation/Note |
|---|---|---|---|
| Mã Phiếu | Count ID | Text | Tự động sinh (VD: INV-202310-001) |
| Phạm vi | Scope | Enum | All / Location / Specific Items |
| Tồn sổ sách | Snapshot Qty | Decimal | Lấy tại thời điểm Start Counting |
