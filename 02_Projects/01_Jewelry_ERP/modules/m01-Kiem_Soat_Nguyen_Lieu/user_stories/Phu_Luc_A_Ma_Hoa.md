# 📖 Phụ lục A: Chuẩn Mã Hóa (Coding Standards)

## 1. MỤC TIÊU
Thiết lập chuẩn mã hóa thống nhất cho toàn bộ các đối tượng trong hệ thống MC (Material Control), đảm bảo mã **ngắn gọn, duy nhất và dễ tra cứu** trong toàn bộ hệ thống ERP và trong các báo cáo vận hành.

---

## 2. QUY TẮC MÃ HÓA

| Nhóm mã | Tên đối tượng | Cấu trúc Template | Ví dụ | Quy tắc Tạo Mã & Ghi chú |
|:---|:---|:---|:---|:---|
| **Nhập** | **Phiếu tiếp nhận nguyên liệu** | `NNL-[YYMM][XXXX]` | `NNL-25100001` | Prefix **(NNL)** + Năm + Tháng + 4 số thứ tự.<br>*(Lưu ý: Số thứ tự XXXX tự động reset 0001 vào đầu mỗi tháng).* |
| | **Phiếu trả NL** | `TNL-[YYMM][XXXX]` | `TNL-25100001` | Prefix **(TNL)** + Năm + Tháng + 4 số thứ tự.<br>*(Lưu ý: Reset theo tháng).* |
| | **Phiếu nhập kho (Goods Receipt)** | `PNK-[YYMM][XXXX]` | `PNK-25100001` | Prefix **(PNK)** + Năm + Tháng + 4 số thứ tự.<br>*(Lưu ý: Reset theo tháng).* |
| **Item (Vật tư)** | **Mã Item Nguyên liệu** | `[Nhóm]-[Phân loại]-[Loại NL]-[Tuổi](-[Màu])` | `L-DEK-AU-64.34`<br>`DEK-AU-64.34`<br>`DE-AU-64.34` | **Công thức Backend (Dùng dấu `-` phân cách):**<br><br>**1. Nhóm:** Giá trị `L` (Nguyên liệu khách). Còn lại là `null`. *(Lưu ý IF-ELSE: bỏ cắt ký tự `-` thừa ở đầu nếu giá trị Nhóm là null)*.<br>**2. Phân loại:** `DEK` (Dẻ khách hàng), `HHN` (Hàng hồi nấu), `HHM` (Hàng hồi mới), `HGS` (Hàng gửi sửa), `DE` (Dẻ), `CAR` (Carot)...<br>**3. Loại NL:** `AU` (Vàng), `AG` (Bạc), `CU` (Đồng), `ZN` (Kẽm), `ST` (Thép), `IN` (Inox), `AL` (Phụ gia như GE, IN, NI, RU, SI, W84-AN1518, W88-N16H, WA1481T2...).<br>**4. Tuổi:** Format 5 ký tự (đính kèm phần thập phân, ví dụ: định dạng thành `64.34` / `99.99` / `100.0` - đảm bảo đủ 5 character length).<br>**5. Màu (nếu có):** `W` (Trắng), `R` (Đỏ), `P` (Hồng), `Y` (Vàng). *(Lưu ý IF-ELSE: bỏ ký tự `-` ở cuối nếu không có màu)*. |
| **Lô (Lot Number)** | **Lô NL Nhận của Khách** | `[Mã khách hàng][YYMM][XXXX]` | `PNJ26030001` | Prefix **(Mã KH)** + Năm + Tháng + 4 số thứ tự.<br>*(Lưu ý: Reset theo tháng).* |
| | **Lô NL nội bộ Seva**<br>*(Vàng, Bạc công ty...)* | `[Loại NL][Nguồn gốc][YYMM][XXXX]` | `AUL26030001` | **1. Loại NL (2 ký tự):**<br>- `AU`: Vàng<br>- `AG`: Bạc<br>- `CU`: Đồng<br>- `ZN`: Kẽm<br>- `ST`: Thép<br>- `IN`: Inox<br>- `AL`: Phụ gia (GE, IN, NI, RU, SI...)*<br><br>**2. Nguồn gốc (1 ký tự):**<br>- `L`: Công nợ (Liability Receipt)<br>- `G`: Hàng khách gửi (Guest)<br>- `P`: Công ty tự mua (Purchased)<br>- `S`: Vụn từ xưởng (Scrap)<br>- `R`: Từ thu hồi (Recovery)<br>- `C`: Từ đúc Cast<br>- `H`: Từ đúc HTJ |
| | **Lô Thành Phẩm** | `[Loại][Loại NL][YYMM][XXXX]` | `FAU26030001` | **1. Loại Thành Phẩm (1 ký tự):**<br>- `F`: Công nợ (Debt Payment)<br>- `S`: Công ty tự mua (Purchased)<br>- `P`: Thu hồi/ vụn từ xưởng (Recycle/Scrap)<br><br>**2. Loại NL (2 ký tự):**<br>Tương tự như trên (`AU`, `AG`, `CU`...) |

---

## 3. NGUYÊN TẮC CHUNG (GLOBAL CONSTRAINTS)

Để đảm bảo hệ thống Database được trong sạch và Frontend không bị lỗi hiển thị, mọi Developer Outsource phải tuân thủ các NFR sau đây:

1. **Tính Unique:** Mã phải là **duy nhất (Unique)** trên toàn hệ thống và không được chứa bất kỳ ký tự đặc biệt nào (như `@, #, $, khoảng trắng`).
2. **Chiều dài (Max-length):** Chiều dài tối đa là **20 ký tự**, ngoại trừ các biến thể mã Item có thể mở rộng đặc thù. Vui lòng set `VARCHAR(20)` ở dưới DB.
3. **Automated Generation:** Tất cả các mã trên đều do **Hệ thống (Backend) tự động sinh (auto-generate)**, không cho phép User gõ tay để tránh sai sót, trừ một số trường hợp được chỉ định explicit "nhập tay".
4. **Prefix Convention:** Sử dụng prefix cứng rõ nghĩa để khi nhìn vào màn hình tra cứu, User phân biệt nhanh được đối tượng là gì (Ví dụ nhìn thấy chữ `GR` là thừa hiểu đây là Phiếu nhập kho).
