# Sơ đồ Trạng thái (State Machine Diagram) - Tiếp nhận Nguyên liệu

Dựa theo phản hồi của bạn, tôi đã tái cấu trúc lại các sơ đồ, loại bỏ toàn bộ các trạng thái "tự đặt" và **chỉ sử dụng đúng danh sách các trạng thái (Statuses)** đã được định nghĩa cứng trong tài liệu User Stories của Epic `CS1.E1`. Các bước hành động (như Cân Gross, Cân Net) sẽ được chuyển thành các sự kiện (arrows) kích hoạt chuyển đổi trạng thái thay vì làm node.

---

## 1. Trạng thái của Phiếu Tiếp nhận Nguyên liệu (Receipt Ticket)

Phiếu NNL quản lý toàn bộ lô hàng giao đến. Các trạng thái được lấy chính xác từ `US-01`, `US-04`, `US-05`.

```mermaid
stateDiagram-v2
    Ban_nhap: Bản nháp
    Dang_thuc_hien: Đang thực hiện
    Cho_xac_nhan: Chờ xác nhận (Trạng thái kép)
    Tra_hang: Trả hàng (Trạng thái kép)
    Hoan_thanh: Hoàn thành

    [*] --> Ban_nhap : Khởi tạo phiếu
    
    Ban_nhap --> [*] : Xóa nháp
    Ban_nhap --> Dang_thuc_hien : Submit
    
    Dang_thuc_hien --> Cho_xac_nhan : Cân bị lệch trọng lượng (Lúc có bao bì hoặc Đã bóc bao bì)
    Cho_xac_nhan --> Dang_thuc_hien : Quản lý "Chấp nhận chênh lệch"
    
    Cho_xac_nhan --> Tra_hang : Quản lý "Từ chối"
    Dang_thuc_hien --> Tra_hang : Rớt kiểm tra kỹ thuật (Đo phổ/Đá/Tem)
    
    Dang_thuc_hien --> Hoan_thanh : Nhập kho 100% đạt
    Tra_hang --> Hoan_thanh : Đã xử lý (Nhập kho phần đạt + Lập Biên bản trả hàng cho các dòng Yêu cầu trả NL)
    Hoan_thanh --> [*]
```

> [!NOTE]
> **Giải thích chi tiết về cơ chế Trạng thái kép (Dual-State):**
> 
> Theo tài liệu `CS1_E1_US_04` và `CS1_E1_US_05`, Phiếu NNL không chỉ có một cột Status duy nhất, mà hoạt động với cơ chế 2 trạng thái chạy song song (Primary Status và Sub-Status) khi xảy ra sự cố:
> 
> 1. **Primary Status (Trạng thái chính):** Khi Submit phiếu, trạng thái chính luôn là `Đang thực hiện`. Nó giữ nguyên như vậy suốt quá trình xử lý các line bên trong.
> 2. **Sub-Status (Trạng thái phụ/Ngoại lệ):** 
>    - Khi hệ thống phát hiện lệch cân nặng/bao bì, hệ thống sẽ **"đính kèm thêm"** trạng thái `Chờ xác nhận` vào phiếu. Lúc này phiếu hiển thị: `Đang thực hiện` + `Chờ xác nhận`. Lập tức khóa mọi thao tác của MC.
>    - Khi Quản lý bấm "Từ chối" (Yêu cầu trả NL) cho một line nào đó, trạng thái phụ `Chờ xác nhận` sẽ biến đổi thành `Trả hàng`. Lúc này phiếu hiển thị: `Đang thực hiện` + `Trả hàng`.
>    - Khi Quản lý bấm "Chấp nhận chênh lệch", trạng thái phụ sẽ bị **gỡ bỏ (remove)**, phiếu quay trở lại trạng thái đơn lẻ là `Đang thực hiện` để MC tiếp tục làm việc.
>
> Cách thiết kế này giúp hệ thống biết được tổng thể phiếu vẫn đang "Work in Progress", nhưng đồng thời đang bị "Block" cục bộ ở một điểm nào đó chờ Quản lý giải quyết.

---

## 2. Trạng thái của Từng Dòng Nguyên Liệu (Material Line Item)

Vòng đời độc lập của mỗi dòng chi tiết. Trạng thái lấy từ `US-13`, `US-24.1` và các US đo phổ/kỹ thuật.

```mermaid
stateDiagram-v2
    Khoi_tao: Khởi tạo
    Cho_xac_nhan: Chờ xác nhận
    Dang_xu_ly: Đang xử lý
    Yeu_cau_tra_NL: Yêu cầu trả NL
    Cho_nhap_kho: Chờ nhập kho
    Da_nhap_kho: Đã nhập kho
    Da_len_phieu_tra: Đã lên phiếu trả

    [*] --> Khoi_tao
    
    Khoi_tao --> Cho_xac_nhan : Cân bị lệch trọng lượng (Lúc có bao bì hoặc Đã bóc bao bì)
    Khoi_tao --> Dang_xu_ly : Cân khớp số liệu
    
    Cho_xac_nhan --> Dang_xu_ly : Quản lý duyệt "Chấp nhận"
    Cho_xac_nhan --> Yeu_cau_tra_NL : Quản lý duyệt "Từ chối"
    
    Dang_xu_ly --> Cho_nhap_kho : Đạt kiểm định kỹ thuật (Đo phổ/Tính đá)
    Dang_xu_ly --> Yeu_cau_tra_NL : Rớt kiểm định kỹ thuật
    
    Cho_nhap_kho --> Da_nhap_kho : Nhập Zone/Bin thành công
    Da_nhap_kho --> [*]
    
    Yeu_cau_tra_NL --> Da_len_phieu_tra : Gom vào Biên bản trả hàng
    Da_len_phieu_tra --> [*]
```

---

## 3. Trạng thái của Phiếu Trả NL & Dòng NL Phiếu Trả (Return Ticket)

Biên bản trả hàng (`CS1_E1_US_24.1`) gom các dòng `Yêu cầu trả NL`.

```mermaid
stateDiagram-v2
    Nhap_R: Nháp
    Moi_tao_R: Mới tạo
    Cho_khach_nhan_R: Chờ khách nhận
    Hoan_thanh_R: Hoàn thành
    Da_huy_R: Đã hủy

    [*] --> Nhap_R : Khởi tạo từ các Line "Yêu cầu trả NL"
    Nhap_R --> Da_huy_R : Xóa nháp
    Nhap_R --> Moi_tao_R : Lưu chính thức
    Moi_tao_R --> Da_huy_R : Hủy lệnh trả hàng (Rollback)
    Moi_tao_R --> Cho_khach_nhan_R : Xác nhận bàn giao
    Cho_khach_nhan_R --> Hoan_thanh_R : Khách/Kinh doanh ký nhận
    Hoan_thanh_R --> [*]
    Da_huy_R --> [*]
```
