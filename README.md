# Phamicha Reports

Kho báo cáo: https://github.com/phamicha/phamicha-reports


Báo cáo HTML tiếng Việt: Hội thảo khoa học 2027, APAC Geospatial Jobs và GitHub Top 20 Weekly.

## Sử dụng

Mở `index.html` trực tiếp trong trình duyệt để dùng offline. Sau khi bật GitHub Pages, cùng file này chạy trên web với menu, bộ lọc và sắp xếp.

## Ngày dữ liệu

- Hội thảo/MDPI: 47 mục từ bản nguồn 13/11/2026.
- APAC: 10 tin lưu trữ 11/10/2026; chưa xác minh đang mở hiện tại.
- GitHub: 20 repo và 10 mục Trending từ bản mẫu 14–15/11/2026; chưa xác minh API.

## Xuất bản

Trong repository: Settings → Pages → Deploy from a branch → main → /(root) → Save.

Chỉ dùng tệp tĩnh, không có dịch vụ máy chủ, khóa API hoặc thư viện bên ngoài.

## Cập nhật

Nhập JSON trong giao diện chỉ thay dữ liệu của phiên đang mở. Nhấn Tải toàn bộ web HTML, đổi tên file thành index.html rồi commit vào kho để cập nhật cho mọi người xem.

Hoặc sửa `data.json` và chạy `python3 build.py`, commit cả dữ liệu, template và index.html tương ứng.

Báo cáo trong chat vẫn được tạo theo các tác vụ đã thiết lập. GitHub Pages tự xuất bản khi file thay đổi; việc tự nghiên cứu và đưa dữ liệu mới lên kho chưa được thiết lập.
