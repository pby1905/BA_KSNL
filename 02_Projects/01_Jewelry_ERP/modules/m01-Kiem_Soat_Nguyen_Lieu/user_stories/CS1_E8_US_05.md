# 🏷️ [CS1.E8.US-05] Tồn kho - Báo cáo Xuất Nhập Tồn

**Epic:** Tồn kho (CS1.E8)
**Actor:** Nhân viên MC / Quản lý kho

## 1. USER STORY
- **Là một (As a):** Người quản lý kho hoặc Nhân viên MC.
- **Tôi muốn (I want):** Xem Báo cáo Xuất Nhập Tồn tổng hợp theo từng Mã Item trong một khoảng thời gian nhất định tại một Kho cụ thể.
- **Để (So that):** Có cái nhìn tổng quan về tình hình luân chuyển nguyên liệu (tồn đầu kỳ, tổng lượng nhập vào, tổng lượng xuất ra, và tồn cuối kỳ), phục vụ việc quản lý, ra quyết định và đối soát kiểm kê.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA - AC)

### AC1: Bộ lọc báo cáo (Search Filters)
- **Given (Biết rằng):** Người dùng truy cập vào chức năng "Báo cáo XNT" (từ Sidebar: Kho & Tồn kho > Báo cáo XNT).
- **When (Khi):** Màn hình hiển thị khu vực "Bộ lọc tìm kiếm" ở phía trên cùng.
- **Then (Thì):** Hệ thống cung cấp các tiêu chí lọc sau:
    - **Từ ngày - Đến ngày:** Khoảng thời gian xuất báo cáo (Bắt buộc).
    - **Kho đích:** Dropdown chọn Kho cần xem (VD: Kho NL - Trạm Đồng Bộ). Bắt buộc phải chọn 1 kho.
    - **Mã Item:** Ô text input để tìm kiếm/lọc riêng một mã cụ thể (Không bắt buộc, nhập text "Ví dụ: BALL3.0...").
    - **Nút "Tìm kiếm":** Khi click, hệ thống tiến hành query và tải dữ liệu lên lưới (Data Grid).
    - **Nút "Export Excel":** Đặt ở góc phải trên cùng để xuất báo cáo ra file Excel.

### AC2: Giao diện Bảng dữ liệu (Data Table)
- **Given (Biết rằng):** Người dùng đã bấm "Tìm kiếm" và có kết quả trả về.
- **When (Khi):** Bảng "Dữ liệu Xuất Nhập Tồn (Tổng hợp theo Mã Item)" được render.
- **Then (Thì):** 
    - Hiển thị thông tin Kho đang được chọn ở góc trên bên phải của bảng (VD: `Kho: Kho NL - Trạm Đồng Bộ`).
    - Bảng hiển thị dạng Header phân nhóm (Group Headers) với các cột như sau:
        1. **MÃ ITEM**: Tên mã hàng (VD: BALL3.0).
        2. **LOẠI NL / HÀM LƯỢNG / MÀU**: Thuộc tính item (VD: Au / 75.00 / Y).
        3. Nhóm **TỒN ĐẦU KỲ**: Gồm 2 cột con `SL` và `TỔNG TL`.
        4. Nhóm **TỔNG NHẬP**: Gồm 2 cột con `SL` (chữ màu xanh, kèm dấu `+`) và `TỔNG TL` (chữ màu xanh, kèm dấu `+`).
        5. Nhóm **TỔNG XUẤT**: Gồm 2 cột con `SL` (chữ màu đỏ, kèm dấu `-`) và `TỔNG TL` (chữ màu đỏ, kèm dấu `-`).
        6. Nhóm **TỒN CUỐI KỲ**: Gồm 2 cột con `SL` và `TỔNG TL` (màu mặc định/xanh biển).
    - Có hỗ trợ Phân trang (Pagination) ở dưới cùng của bảng (VD: Hiển thị 1 - 3 của 3 Item).

### AC3: Logic Hiển thị và Tính toán
- **Given (Biết rằng):** Hệ thống tiến hành tổng hợp dữ liệu giao dịch của các Mã Item trong Kho đích đã chọn.
- **Then (Thì):**
    - Các giá trị trống hoặc bằng 0 sẽ hiển thị số `0` hoặc dấu `-` tùy theo chuẩn UI (Trên UI đang hiển thị số 0 cho SL và `-` hoặc `0.0000` cho TỔNG TL).
    - Danh sách chỉ hiển thị các Mã Item có phát sinh **giao dịch trong kỳ**, hoặc không có giao dịch nhưng **có Tồn Đầu Kỳ** (nghĩa là Tồn cuối khác 0 hoặc Tồn đầu khác 0).

---

## 3. CÔNG THỨC TÍNH TOÁN & QUY TẮC NGHIỆP VỤ (BUSINESS RULES)

### 3.1 Công thức Tồn Đầu Kỳ
Dựa vào mốc `Từ ngày` của bộ lọc và `Kho` đã chọn:
- `Tồn Đầu Kỳ [SL]` = `Σ (Tổng SL Nhập vào kho trước [Từ ngày])` - `Σ (Tổng SL Xuất khỏi kho trước [Từ ngày])`.
- `Tồn Đầu Kỳ [TỔNG TL]` = Tính tương tự như trên theo giá trị Trọng lượng.

### 3.2 Công thức Tổng Nhập / Tổng Xuất trong kỳ
Chỉ thống kê các giao dịch xảy ra trong khoảng thời gian `[Từ ngày] -> [Đến ngày]` tại Kho được chọn:
- **TỔNG NHẬP:** 
  - `SL Nhập` = Tổng SL của tất cả các giao dịch có loại là "Nhập" vào kho (VD: Nhập từ sản xuất, Nhập trả lại...). Hiển thị trên UI số dương.
  - `TỔNG TL Nhập` = Tổng TL các giao dịch "Nhập".
- **TỔNG XUẤT:**
  - `SL Xuất` = Tổng SL của tất cả các giao dịch có loại là "Xuất" khỏi kho. **Lưu ý:** UI yêu cầu hiển thị số âm (VD: `-15`), do đó khi show ra view cần thêm dấu trừ hoặc format màu đỏ.
  - `TỔNG TL Xuất` = Tổng TL các giao dịch "Xuất" (hiển thị số âm).

### 3.3 Công thức Tồn Cuối Kỳ
- `Tồn Cuối Kỳ [SL]` = `Tồn Đầu Kỳ [SL]` + `TỔNG NHẬP [SL]` - `|TỔNG XUẤT [SL]|` (Hoặc cộng thẳng nếu giá trị Tổng xuất đang lưu dưới dạng số âm).
- `Tồn Cuối Kỳ [TỔNG TL]` = `Tồn Đầu Kỳ [TỔNG TL]` + `TỔNG NHẬP [TỔNG TL]` - `|TỔNG XUẤT [TỔNG TL]|`.

> **Tính toàn vẹn (Integrity Rule):** Nếu người dùng lọc `Đến ngày` là ngày hiện tại, thì `Tồn Cuối Kỳ` của báo cáo này phải khớp 100% với `Tồn kho On-hand` đang ghi nhận thực tế trên hệ thống của kho đó.

---

## 4. BẢNG ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU (DATA DICTIONARY)

| Tên hiển thị | Format / Kiểu dữ liệu | Mô tả & Validation |
|---|---|---|
| **MÃ ITEM** | Text | Tên hoặc mã nguyên liệu |
| **LOẠI NL / HÀM LƯỢNG / MÀU** | Text | Chuỗi nối các thuộc tính sản phẩm. VD: `Au / 75.00 / Y` |
| **TỒN ĐẦU KỲ (SL)** | Integer | Dữ liệu aggregate |
| **TỒN ĐẦU KỲ (TỔNG TL)** | Decimal(10,4) | Dữ liệu aggregate |
| **TỔNG NHẬP (SL)** | Integer | Kèm ký tự `+` (Color: Green) |
| **TỔNG NHẬP (TỔNG TL)** | Decimal(10,4) | Kèm ký tự `+` (Color: Green) |
| **TỔNG XUẤT (SL)** | Integer | Kèm ký tự `-` (Color: Red) |
| **TỔNG XUẤT (TỔNG TL)** | Decimal(10,4) | Kèm ký tự `-` (Color: Red) |
| **TỒN CUỐI KỲ (SL)** | Integer | (Tồn đầu + Nhập) - Xuất |
| **TỒN CUỐI KỲ (TỔNG TL)** | Decimal(10,4) | (Tồn đầu + Nhập) - Xuất |

---

## 5. CÁC TRƯỜNG HỢP NGOẠI LỆ (EDGE CASES)

1. **Mã Item không có biến động:** Nếu một mã Item có số Tồn đầu kỳ = 0, và trong khoảng thời gian lọc cũng không phát sinh bất kỳ Nhập/Xuất nào (Tồn cuối = 0) -> Hệ thống tự động **ẨN** (loại bỏ) Mã Item này khỏi kết quả báo cáo để tránh loãng dữ liệu.
2. **Kho chưa có dữ liệu:** Nếu Kho được chọn hoàn toàn chưa có bất kỳ giao dịch nào từ trước đến nay, bảng hiển thị "Không có dữ liệu".
3. **Export Excel:** Khi xuất Excel, dữ liệu phải giữ nguyên các số liệu (bỏ dấu + / màu sắc đi để dễ dàng sum/cộng trừ bằng hàm Excel). Tức là Tổng nhập lưu số dương, Tổng xuất có thể lưu số âm (tùy chuẩn quy định xuất file của dự án) để tiện dùng hàm `SUM`.
