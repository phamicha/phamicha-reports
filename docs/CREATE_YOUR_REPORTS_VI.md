# Tự tạo báo cáo hội thảo và tuyển dụng cho ngành Y sinh / Life Sciences

[English](CREATE_YOUR_REPORTS_EN.md) · [Các prompt để sao chép](PROMPTS_VI.md) · [Định dạng JSON và dữ liệu thực hành](DATA_FORMAT_EN_VI.md) · [Bộ khởi đầu trống](../examples/biomedical-life-sciences/)

Cập nhật hướng dẫn: **16/11/2026**. Đây là quy trình để tự làm báo cáo, không phải danh sách hội thảo hay việc làm Y sinh đã xác minh.

## Kết quả cần đạt

Bạn có một file HTML và website trên GitHub cá nhân, gồm hai báo cáo: **Hội thảo 2027** và **Việc làm hiện còn tuyển**. Mặc định tiếng Anh, có EN/VN, tìm kiếm, lọc, sắp xếp, thanh công cụ ghim, chi tiết kèm nguồn, tải HTML/JSON/CSV.

Ba phần cần phân biệt: trợ lý hỗ trợ **tìm và xác minh**; HTML **hiển thị dữ liệu**; GitHub Pages **xuất bản file đã tải lên**. Pages không tự tìm hội thảo hoặc việc làm mới.

| Địa chỉ bạn mở | Ý nghĩa |
|---|---|
| `C:\Users\TenBan\Downloads\index.html` | File offline trên máy bạn |
| `github.com/OWNER/REPO/blob/main/index.html` | Trang GitHub xem file/mã nguồn |
| `https://OWNER.github.io/REPO/` | Website hiển thị báo cáo sau khi bật Pages |

`OWNER` và `REPO` là chỗ cần thay bằng tài khoản/tên kho của bạn. Ví dụ website hiện có của dự án này là [Phamicha Reports](https://phamicha.github.io/phamicha-reports/). Bấm index.html trong danh sách file không phải cách mở giao diện website.

## Bước 1 — Chốt phạm vi

Dùng [scope.example.json](../examples/biomedical-life-sciences/scope.example.json) làm bản yêu cầu; file này **không tự thay các bộ lọc HTML**.

- **Y sinh/Biomedical:** kỹ thuật y sinh, khoa học y sinh, vật liệu sinh học, ảnh y khoa, y học chuyển giao.
- **Life Sciences:** sinh học phân tử/tế bào, genomics, tin sinh học, công nghệ sinh học, thần kinh học.
- **Hội thảo năm 2027:** tách Đài Loan, Việt Nam, online/hybrid toàn cầu; hội thảo trực tiếp ở nước khác để mục bổ sung. Một hội thảo chỉ có một bản ghi, dù thuộc nhiều nhóm.
- **Việc làm:** ví dụ Đài Loan, Úc, Singapore, Việt Nam và remote toàn cầu; RA, postdoc, bioinformatician, research scientist, kỹ thuật viên phòng thí nghiệm. Có thể đổi nước và nhóm nghề.
- **Không nhầm năm:** năm 2027 là năm diễn ra hội thảo. Tin việc làm đang mở có hạn cuối năm 2026 vẫn hữu ích; chỉ lọc việc bắt đầu năm 2027 nếu bạn yêu cầu rõ.
- **Lịch ví dụ:** thứ Sáu 08:00, `Asia/Ho_Chi_Minh`. Người ở Đài Loan có thể chọn `Asia/Taipei`; phải ghi đúng múi giờ.

## Bước 2 — Mở bộ khởi đầu

1. Ở trang chính của kho này, chọn **Code → Download ZIP**, rồi giải nén.
2. Vào thư mục `examples/biomedical-life-sciences/`.
3. Mở **index.html** bằng Chrome/Edge. Có thể nhấn Ctrl+O trong trình duyệt rồi chọn file.
4. Bản mẫu sẽ có **0 hội thảo, 0 việc làm**. Thử chuyển VN/EN và chuyển hai tab. Đây là trạng thái chủ động để trống, không phải lỗi.
5. Giữ một bản gốc của thư mục. Có HTML, template, JSON, build.py và bản yêu cầu; không cần cài Python chỉ để mở HTML.

Không lấy dữ liệu Geomatics/APAC cũ rồi đổi nhãn thành Y sinh. Bản mẫu riêng đã đổi ngành và bỏ các cơ hội cũ. Mảng `github` vẫn để trống để tương thích định dạng nhưng không có tab GitHub.

## Bước 3 — Chọn nguồn

Các đầu mối chính thức dưới đây được kiểm tra ngày **16/11/2026**. Mỗi cơ hội vẫn phải mở thông báo chi tiết để xác minh lại.

| Nguồn | Cách dùng |
|---|---|
| [EMBL events](https://www.embl.org/about/info/course-and-conference-office/events/) | Tìm hội thảo khoa học sự sống; phân biệt conference, course và webinar |
| [FEBS events](https://www.febs.org/events/) / [Congress](https://www.febs.org/events/congress/) | Theo liên kết CFP và đăng ký của đúng ban tổ chức |
| [ISCB conferences](https://www.iscb.org/conferences-events) | Tin sinh học/sinh học tính toán; kiểm tra đúng kỳ năm 2027 |
| [EMBL careers](https://www.embl.org/careers/) | Mở trang từng vị trí và trang ứng tuyển |
| [Academia Sinica](https://www.sinica.edu.tw/en/recruitment/53) | Tìm viện/lab, mã tin và hạn tuyển tại Đài Loan |
| [NHRI](https://www.nhri.edu.tw/) / [IBPR careers](https://ibpr.nhri.edu.tw/zhtw/index.php/careers/) | Đọc từng thông báo; một trang có thể chứa cả tin cũ và tin mới |
| [HCMUS tuyển dụng](https://hcmus.edu.vn/category/tuyen-dung-viec-lam/) | Mở thông báo/PDF có ngày và hướng dẫn ứng tuyển |
| [EURAXESS](https://euraxess.ec.europa.eu/jobs/search) | Dùng để phát hiện vị trí rồi đối chiếu nguồn của đơn vị tuyển; phân biệt việc làm với học bổng/hosting |

Bổ sung trang trường, bệnh viện và hiệp hội chuyên ngành phù hợp với phạm vi của bạn. Trang chủ trường/bệnh viện không thay thế CFP. Danh bạ hội nghị, kết quả tìm kiếm, mạng xã hội chỉ là đầu mối nếu chưa kiểm tra được nguồn chính thức.

## Bước 4 — Tìm theo bộ từ khóa

```text
biomedical engineering conference 2027 Taiwan abstract deadline
life sciences conference 2027 Vietnam call for papers
2027 bioinformatics conference virtual presentation registration
site:edu.tw 2027 生醫 研討會 徵稿
site:edu.vn 2027 hội nghị khoa học y sinh hạn nộp
site:sinica.edu.tw bioinformatics research assistant recruitment
site:nhri.edu.tw 博士後 研究助理 徵才
site:edu.vn tuyển dụng nghiên cứu sinh học công nghệ sinh học
bioinformatics remote research scientist eligible countries
```

Ghi tên, URL chính thức, ngày tìm thấy, kết quả truy cập/kiểm tra. Kiểm tra phân trang, file đính kèm và CFP PDF. Trang không truy cập được không có nghĩa hội thảo đã hủy hoặc việc làm đã đóng.

## Bước 5 — Xác minh hội thảo

Làm kỹ một mục trước, sau đó mở rộng:

- Nguồn chính thức xác nhận **kỳ 2027**, ban tổ chức, phạm vi học thuật.
- Ngày diễn ra, thành phố/quốc gia, in-person/online/hybrid.
- Hạn **abstract**, **full paper**, thông báo chấp nhận, camera-ready và đăng ký dự nghe: tách riêng, kèm múi giờ nếu công bố.
- Quyền xem/tham dự online khác với **quyền báo cáo từ xa**. Ghi nền tảng, live/ghi hình; chỉ đổi sang giờ Việt Nam khi đã có giờ phiên gốc.
- Phí tác giả/báo cáo, người nghe, sinh viên, online; tiền tệ, mức sớm/thường, thuế và điều kiện.
- Ngôn ngữ, liên hệ, trang chính, CFP, ngày kiểm tra; proceedings/indexing chỉ ghi khi có nguồn, phân biệt tuyên bố của BTC với xác minh độc lập.

Thiếu dữ liệu ghi **Chưa công bố/chưa xác minh**, không điền ngày dự đoán hay phí 0. Chỉ dùng 0 khi nguồn xác nhận miễn phí. So phí cùng tiền và cùng đối tượng. APC tạp chí không phải phí hội thảo; chuyên đề tạp chí là nhóm tùy chọn riêng.

Ví dụ cách đánh giá chứng cứ: [trang FEBS Congress chính thức](https://www.febs.org/events/congress/) xác nhận kỳ 2027 tại Riga, 3–7/7/2027. Chỉ thông tin đó chưa xác nhận hạn abstract, phí hay quyền báo cáo online. Đây là mục bổ sung nếu ưu tiên Đài Loan/Việt Nam. Bản mẫu trống không tự biến ví dụ này thành một mục nghiên cứu đã hoàn chỉnh.

Hội thảo định kỳ chưa công bố kỳ 2027 phải ở **watchlist**, không tự suy ngày năm sau.

## Bước 6 — Xác minh tin tuyển dụng

Dùng trang nhà tuyển dụng/PI/HR và mã tin. Ghi chức danh, ngành, viện/lab, địa điểm, onsite/hybrid/remote và giới hạn quốc gia, công việc, bằng cấp/kinh nghiệm, kỹ năng, ngôn ngữ, hợp đồng, lương/tiền tệ/kỳ trả/gross-net, hạn/múi giờ, liên hệ và cách nộp.

Công việc wet-lab, động vật thí nghiệm hoặc lâm sàng không mặc định làm remote được. Nếu thêm vị trí hành nghề lâm sàng, cần kiểm tra giấy phép/điều kiện hành nghề riêng. “Until filled” không có nghĩa mở mãi; không công bố hạn thì để null và ghi rõ.

Rà lại trang Apply rồi phân loại **Active / Closed / Unverified / Archived**, kèm ngày kiểm tra. Link hỏng hoặc không phản hồi không đủ để kết luận đã đóng. Chỉ so lương khi cùng tiền, kỳ trả và gross/net; nếu chưa so được, giữ nguyên chuỗi lương nguồn và để số dùng sắp xếp là null.

## Bước 7 — Yêu cầu báo cáo đầu tiên

Sao chép Prompt A và B trong [PROMPTS_VI.md](PROMPTS_VI.md), đính kèm HTML/JSON trống từ bước 2. Yêu cầu một HTML đầy đủ và một JSON tương thích, mặc định English, có bản dịch tiếng Việt. Khi chỉ cập nhật một báo cáo phải giữ mảng báo cáo còn lại.

Chọn khối lượng vừa đủ để xác minh. Không đặt số lượng tối thiểu khiến trợ lý bịa mục. Nhóm nào chưa có sự kiện xác nhận thì ghi rõ kết quả và nguồn đã kiểm tra. Watchlist, nhật ký nguồn và thay đổi phải ở phần hỗ trợ, không giả thành mục đã xác nhận; yêu cầu thêm phần đó nếu bản mẫu chưa có.

Nếu trợ lý không tạo được JSON đúng định dạng, yêu cầu nó dựng HTML tự chứa hoàn chỉnh từ dữ liệu đã kiểm tra. Cách đó vẫn đăng GitHub trực tiếp được, không bắt buộc nhập JSON.

## Bước 8 — Nhập, thử và lưu

1. Mở mẫu, chọn **Import updated JSON** và chọn file đầy đủ. Nhập là **thay toàn bộ**, không tự ghép.
2. Kiểm tra số lượng, ngành, nước, hình thức, trạng thái việc làm và thứ tự sắp xếp.
3. Chuyển EN/VN, bảo đảm vẫn giữ điều kiện đang lọc.
4. Mở chi tiết vài mục, đối chiếu hạn, phí, nguồn. Thử dữ liệu thiếu và hội thảo đã hết hạn nộp.
5. Chọn tiền tệ trước khi so phí/lương. Không tự đổi tỷ giá.
6. Nhấn **Download full HTML** và **Export all data (JSON)**. Hai file này giữ toàn bộ mục; CSV chỉ xuất phần đang lọc.
7. Đóng tab rồi mở lại HTML vừa tải để chắc chắn dữ liệu đã được lưu. Không giữ bản mới duy nhất trong một tab đang mở.

Có ví dụ kỹ thuật ở [DATA_FORMAT_EN_VI.md](DATA_FORMAT_EN_VI.md). Các mục thực hành có nhãn DEMO rõ ràng, không phải cơ hội thật.

## Bước 9 — Tạo kho GitHub cá nhân

1. Đăng nhập tài khoản **của bạn**, chọn **New repository**.
2. Chọn đúng Owner, đặt tên ví dụ `biomedical-reports`.
3. Nếu dùng GitHub Free Pages, chọn **Public**. Nội dung báo cáo và mã nguồn sẽ công khai; chỉ đưa thông tin công khai định chia sẻ.
4. Tạo repository; có thể thêm README mô tả phạm vi/ngày nguồn.
5. Đổi tên HTML hoàn chỉnh thành **index.html**. Trên Windows bật hiển thị phần mở rộng để tránh `index.html.html` hoặc `index.html.txt`.
6. **Add file → Upload files**, tải index.html vào **gốc kho**, không lồng thêm một thư mục ngoài. Commit vào main nếu được phép; nếu kho bảo vệ nhánh thì tạo nhánh/PR rồi merge.

Cách đơn giản chỉ cần **index.html tự chứa**. Giữ JSON ở máy để sao lưu; source là tùy chọn. Upload ZIP không thay cho index.html ở gốc. Đuôi .html đúng chưa chắc nội dung đúng: đừng lưu trang xem mã nguồn GitHub rồi dùng nó thay báo cáo.

## Bước 10 — Bật Pages và mở đúng link

**Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main → /(root) → Save.** Nếu nhánh mặc định tên khác thì chọn đúng nhánh đó. Chờ deployment hoàn tất; có lỗi thì xem **Actions**. Mở **Visit site** mà Pages hiển thị.

Địa chỉ thường theo mẫu `https://TEN-TAI-KHOAN.github.io/biomedical-reports/`; thay bằng thông tin thực của bạn. Đường dẫn `C:\...` chỉ dùng trên máy bạn, không phải link website. Mở offline bằng **Open with → Chrome/Edge**, hoặc Ctrl+O trong trình duyệt.

Tài liệu GitHub: [tạo kho](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [upload file](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository), [bật Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Bước 11 — Cập nhật tích lũy hằng tuần

Mỗi thứ Sáu, đưa **HTML/JSON mới nhất** cho trợ lý và dùng Prompt C. Rà soát tin cũ, giữ mục còn phù hợp, thêm mục mới đã kiểm tra, chống trùng theo mã hội thảo/vacancy. Mục đã diễn ra/hủy/đóng chuyển lưu trữ rõ ràng. Không kiểm tra được thì giữ chứng cứ lần trước và đánh dấu Unverified; không trình bày tin cũ như Active hôm nay.

Giữ ID ổn định, nhật ký nguồn và thay đổi: mới thêm, đổi hạn/phí, đổi trạng thái, nguồn kiểm tra thất bại. Đánh dấu hạn trong 30 ngày. Hội thảo hết hạn nộp vẫn có thể còn đăng ký dự nghe.

Tải bản HTML/JSON có ngày rồi thay **index.html trong kho của bạn**, commit có mô tả ngày, mở lại link Pages và kiểm tra một thay đổi đã biết. Có thể lưu HTML từng tuần vào `archive/` và thêm liên kết; bản mẫu không tự tạo trang duyệt kho lưu trữ.

Nếu trợ lý/tài khoản hỗ trợ tác vụ định kỳ, yêu cầu thứ Sáu 08:00 với múi giờ cụ thể và trả báo cáo trong chat, rồi kiểm tra tác vụ thật sự đã được tạo. Nếu không, dùng lịch nhắc và tự chạy Prompt C. **Lập lịch nghiên cứu, tạo HTML và đẩy commit lên GitHub là ba khả năng riêng.** Nên bắt đầu bằng upload thủ công; tác vụ không mặc định đọc được Downloads trên máy bạn.

## Bước 12 — Xử lý lỗi

| Hiện tượng | Việc cần kiểm tra |
|---|---|
| GitHub chỉ hiện mã | Mở Pages → Visit site, không mở `/blob/main/index.html` |
| HTML mở trong trình soạn thảo | Open with trình duyệt; kiểm tra có phải .html.txt không |
| Website 404 | Đúng nhánh/thư mục, tên index.html chữ thường, deployment thành công |
| Chỉ có tiêu đề, bảng trống | Mẫu trống là bình thường; nếu đã nhập thì kiểm tra mảng dữ liệu/bộ lọc |
| Đóng rồi mất cập nhật | Nhập JSON chỉ có hiệu lực trong phiên; phải tải HTML mới |
| Sửa JSON nhưng web không đổi | Nhập + tải HTML + upload index.html, hoặc chạy build.py |
| Lọc ngành bị mất mục | Dùng đúng `Biomedical` / `Life Sciences`; đổi ngành phải sửa bộ chọn |
| Không thấy nước/tiền mới | Yêu cầu sửa bộ lọc và bản dịch trong template; scope.json không tự làm |
| Vẫn thấy bản cũ | Kiểm tra commit/deployment, tải lại hoặc thử cửa sổ riêng tư |
| File vẫn không mở | Đính kèm HTML thật cùng ảnh/lỗi. Gửi đường dẫn C: không trao quyền đọc file từ xa |

Hoàn tất khi link GitHub của chính bạn mở được, mặc định EN, nút VN/bộ lọc chạy, dữ liệu có nguồn/ngày kiểm tra, HTML mở lại offline được và cập nhật không làm mất các mục cũ còn hiệu lực.
