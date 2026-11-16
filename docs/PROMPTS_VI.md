# Prompt để sao chép — Y sinh / Life Sciences

[Hướng dẫn](CREATE_YOUR_REPORTS_VI.md) · [English](PROMPTS_EN.md) · [Định dạng dữ liệu](DATA_FORMAT_EN_VI.md)

Thay ngành, nước và múi giờ theo nhu cầu. Đính kèm **HTML/JSON mới nhất** để trợ lý có dữ liệu đối chiếu, không dựa vào trí nhớ của lần chat cũ.

## A — Tìm hội thảo 2027

```text
Tạo báo cáo hội thảo năm 2027 tích lũy cho hai ngành riêng:
Biomedical/Y sinh (kỹ thuật và khoa học y sinh, vật liệu sinh học, ảnh y khoa,
y học chuyển giao); Life Sciences (sinh học phân tử/tế bào, genomics, tin sinh
học, công nghệ sinh học, thần kinh học).

Trong mỗi ngành tách A Đài Loan, B Việt Nam, C online/hybrid toàn cầu; hội thảo
trực tiếp ở nước khác để mục bổ sung. Một sự kiện thuộc nhiều nhóm chỉ có một
bản ghi và được dẫn chiếu. Dùng web hiện tại, mở nguồn chính thức BTC/trường/
hiệp hội; chỉ xác nhận khi có kỳ 2027 chính thức. Sự kiện định kỳ chưa công bố
2027 để watchlist, không suy ngày. Danh bạ/kết quả tìm kiếm chỉ là đầu mối.

Mỗi mục gồm tên/viết tắt, phạm vi, tổ chức, thành phố/nước, ngày diễn ra, hình
thức, hạn abstract và full paper tách riêng kèm giờ/múi giờ, ngày kết quả,
camera-ready, hạn đăng ký, ngôn ngữ, phí tác giả/người nghe/sinh viên/online,
tiền tệ và điều kiện, liên hệ, URL chính thức và CFP, trạng thái/ngày kiểm tra.
Proceedings/indexing phải có bằng chứng chính thức và ghi rõ mức xác minh.

Xác minh quyền xem/tham dự online khác quyền trình bày từ xa. Ghi nền tảng,
lịch phiên gốc nếu công bố và giờ Việt Nam khi đủ dữ liệu để đổi. Ghi phí và
hạn đăng ký online. Dữ liệu thiếu ghi Chưa công bố/chưa xác minh; không gán 0.
Chỉ so phí cùng tiền và cùng đối tượng. APC tạp chí là khoản riêng.

Đối chiếu JSON mới nhất đính kèm: giữ mục còn phù hợp, kiểm tra tin cũ, thêm
mục mới đã xác minh, lưu trữ mục đã diễn ra/hủy. Hết hạn nộp bài để riêng nhưng
vẫn ghi đăng ký dự nghe. Đánh dấu mới, thay hạn và hạn trong 30 ngày. Ghi nhật
ký nguồn, lần kiểm tra thất bại và thay đổi. Nhóm không có sự kiện xác nhận
phải nêu rõ kết quả và nguồn đã kiểm tra.

Trả HTML tự chứa mặc định English có nút EN/VN và JSON đầy đủ tương thích bản
mẫu Y sinh đính kèm. Giữ mảng jobs cũ và github rỗng. Ngày thiếu để null và có
nhãn dễ đọc. Watchlist/nhật ký không giả thành sự kiện xác nhận; thêm phần hỗ
trợ nếu cần. Dịch trung thực, không coi ngày dịch là ngày xác minh nguồn.
Không email, không tự đăng GitHub; trả file trong chat để tôi kiểm tra.
```

## B — Tìm việc làm

```text
Tạo báo cáo tuyển dụng Y sinh/Life Sciences tích lũy đầy đủ. Phạm vi: Đài Loan,
Úc, Singapore, Việt Nam và remote toàn cầu có xác minh quốc gia đủ điều kiện.
Nhóm nghề: RA, postdoc, bioinformatician, research scientist, laboratory technician.
Không thêm vị trí hành nghề lâm sàng trừ khi tôi yêu cầu riêng và đã kiểm tra
điều kiện giấy phép. Không giới hạn tin tuyển dụng hiện tại vào hạn năm 2027;
giữ cả tin phù hợp đóng trong năm 2026.

Tìm nguồn employer/trường/viện/lab/PI hoặc trang tuyển dụng chính thức; danh
bạ chỉ để phát hiện rồi đối chiếu thông báo và cách nộp gốc. Mỗi tin có đơn
vị/lab, mã tin, ngành, thành phố/nước, onsite/hybrid/remote và giới hạn nước,
công việc, bằng cấp/kinh nghiệm/kỹ năng, ngôn ngữ, hợp đồng/thời hạn/ngày bắt
đầu, lương/tiền tệ/kỳ trả/gross-net, visa/sponsorship nếu nêu, hạn và múi giờ,
liên hệ, tài liệu/cách nộp, URL chính thức và ngày kiểm tra. Thiếu ghi chưa
công bố/chưa xác minh, không tự đoán.

Rà lại toàn bộ tin cũ trong JSON mới nhất. Giữ tin xác minh còn mở, thêm tin
mới, chuyển tin xác nhận đóng/hết hạn khỏi Active; không kiểm tra được thì
Unverified với chứng cứ lần trước. Until filled không chứng minh mở mãi.
Không suy remote từ phỏng vấn online hay chức danh làm dữ liệu. Chống trùng
bằng đơn vị + mã tin/URL chuẩn. Đánh dấu mới, đổi hạn và hạn trong 30 ngày.
Chỉ so lương cùng tiền, kỳ trả và gross/net; còn lại giữ nguyên chuỗi lương,
giá trị số dùng sắp xếp để null.

Trả HTML tự chứa mặc định English, EN/VN, bộ lọc/sắp xếp ghim, chi tiết đầy
đủ và nguồn; kèm JSON tương thích mẫu. Giữ mảng events cũ và github rỗng.
Lưu trữ/nhật ký nguồn và thay đổi ở phần hỗ trợ rõ ràng. Chỉ có đầu mối chưa
xác minh thì nêu rõ. Không email, không ứng tuyển thay tôi, không tự đăng GitHub.
```

## C — Cập nhật hằng tuần

```text
Cập nhật HTML và JSON Y sinh/Life Sciences mới nhất đính kèm theo phạm vi đã
chốt và nguồn chính thức hiện tại. Rà lại mọi mục cũ trước khi thêm mới. Giữ
ID ổn định và mọi mục còn phù hợp; không chỉ trả mục mới trong tuần. Phân
biệt Active, Closed, Unverified, Archived và watchlist chưa công bố kỳ 2027.
Ghi ngày kiểm tra, giá trị hạn/phí cũ và mới, nguồn kiểm tra thất bại và lý do
đổi trạng thái. Hết hạn nộp hội thảo khác với hết đăng ký dự nghe.

Giữ cả events và jobs; github rỗng để tương thích. Giữ nội dung EN/VN đầy đủ,
mặc định English, giữ điều kiện lọc khi đổi ngôn ngữ, công cụ ghim và xuất
file. Thay các cảnh báo dữ liệu trống trong meta.reports bằng cảnh báo đúng
với dữ liệu hiện tại. Không coi bản dịch mới là dữ liệu vừa xác minh.

Trả một HTML tự chứa đầy đủ, một JSON đầy đủ, nhật ký thay đổi ngắn và các
bước upload vào kho GitHub CỦA TÔI. Kiểm tra file trước khi giao. Không email,
không ghi vào GitHub của người khác. Nguồn bị chặn thì nêu phần kiểm tra được/
chưa được, không bịa dữ liệu.
```

## D — Ghép dữ liệu đã xác minh thành HTML

```text
Dùng bản mẫu Y sinh/Life Sciences và dữ liệu đã xác minh đính kèm để tạo
index.html tự chứa, mở bằng double-click không cần server/thư viện ngoài.
Kèm data.json đầy đủ đúng schema. Các trường mô tả gốc chứa tiếng Việt;
đối tượng en chứa bản tiếng Anh của đúng trường đó. Chỉ dùng khóa en được
cho phép trong DATA_FORMAT_EN_VI.md. Ngày/số chưa biết là null, dùng đúng
mã subject/status/region/mode của mẫu. Không bịa để lấp trường trống.
Watchlist, nguồn, lưu trữ ở phần hỗ trợ rõ ràng; thêm phần đó khi cần.

Mặc định English, nút EN/VN đổi cả giao diện/chi tiết và giữ bộ lọc. Giữ tìm
kiếm, chi tiết nguồn, lọc trạng thái việc làm, sắp theo hạn/phí cùng tiền,
thiếu dữ liệu cuối và xuất HTML/JSON/CSV. Nhập JSON thay toàn bộ dữ liệu,
phải giữ đủ các mảng. Thêm nước/tiền/ngành phải cập nhật cả bộ chọn và bản
dịch; scope JSON không tự sửa giao diện. Kiểm tra nhập JSON, EN/VN, lọc,
tải và mở lại offline. Trả HTML trong chat để tôi tự đăng GitHub Pages.
```

## Ví dụ yêu cầu lập lịch (tùy chọn)

Sau khi đã chạy thủ công thành công, nếu trợ lý/tài khoản có chức năng lập lịch, yêu cầu:

> Chạy cập nhật tích lũy ở trên vào thứ Sáu hằng tuần lúc 08:00 Asia/Ho_Chi_Minh. Trả HTML đầy đủ mặc định English có EN/VN và JSON đầy đủ trong chat, không email. Tách nghiên cứu khỏi xuất bản; chỉ báo đã cập nhật GitHub khi thực sự có commit và deployment thành công.

Đọc tài liệu này **không tự tạo tác vụ**. Kiểm tra trợ lý đã xác nhận tạo lịch với đúng múi giờ. Nếu không hỗ trợ, dùng nhắc lịch rồi tự chạy Prompt C.
