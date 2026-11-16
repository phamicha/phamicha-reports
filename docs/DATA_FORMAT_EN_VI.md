# Data format / Định dạng dữ liệu

[English guide](CREATE_YOUR_REPORTS_EN.md) · [Hướng dẫn Việt](CREATE_YOUR_REPORTS_VI.md) · [Synthetic practice JSON](../examples/biomedical-life-sciences/practice-demo.json)

## English

The starter reads a complete JSON object with `events`, `jobs` and `github` arrays. For this two-report starter **github stays `[]`**. An import replaces the whole dataset; preserve existing arrays when updating just one report. Use UTF-8 JSON, without Markdown fences or comments. The base narrative fields contain Vietnamese; `en` contains their English translations. Keep proper names/URLs/numbers unchanged.

| Field | Conference (`events`) | Vacancy (`jobs`) |
|---|---|---|
| `id`, `title` | Stable unique ID and source title | Stable unique ID and position title |
| `subject` | Exact `Biomedical` or `Life Sciences` | Store subject in `fields`; `category` is the job/subject filter |
| `kind` | Exact `Conference`; optional `Special Issue` or `Journal Topic` must be separate journal opportunities | Not used |
| `region` | `Taiwan`, `Vietnam` or `Global`; cities/countries also in `place` | `Taiwan`, `Australia`, `Singapore`, `Vietnam` or `Global` |
| `mode` | `In-person`, `Online`, `Hybrid`, or `Journal` for a journal call | A consistent `Onsite`, `Hybrid` or `Remote` value |
| `deadline` | Nearest relevant open **submission** milestone, ISO `YYYY-MM-DD`, else null; identify abstract/full paper in notes | Application deadline, ISO date, else null |
| `status`, `closed` | `Open at source check` and false, or `Closed for new submissions` and true, only with evidence | Status `Active`, `Closed`, `Unverified`, `Archived`; include original status in `historicalStatus` |
| `when`, `place` | Event timing/location; journal calls must say not a conference | Put location/start/contract details in `fields` |
| `fee`, `feeBasis` | Full tiers/conditions + basis for numeric comparison | Not used |
| `feeValue`, `feeCurrency` | Comparable fee number or null; ISO currency or blank. `0` + `FREE` only for officially confirmed free participation | Not used |
| `salary`, `salaryValue`, `salaryCurrency` | Not used | Original text; comparable number or null; currency or blank |
| `notes`, `fields` | `notes` holds organizers, all deadline rounds/time zones, remote rights, language, indexing and extra facts | `fields` is an object of human-readable labels and values, including contact/apply/eligibility |
| `urls` | Array of official page/CFP/fee links | Array of original vacancy/application links |
| `sourceDate`, `checked`, `verification` | Actual source-check ISO date; display date and explanation | `sourceDate` is the actual latest check; put verification explanations in `fields` |
| `en` | English overrides of narrative fields | English title/salary/fields overrides |

Dates lacking a cutoff time must not be described as midnight. Keep exact cutoff/time zone in notes; the date filter is date-level only. Preserve abstract, full manuscript, notification, registration and camera-ready as separate labelled facts in notes even though the summary has one sortable milestone.

Unknown dates/numbers must be JSON `null`, not strings `"null"`/`"N/A"` and not zero. Unknown narrative text can say “Chưa công bố/chưa xác minh” with its English equivalent. Set `salaryValue` only on a consistent comparison basis (for example verified gross monthly TWD); do not mix annual/monthly or gross/net just because a currency matches. The template does not normalize salaries for you.

Supported `en` keys: `title`, `when`, `place`, `fee`, `contact`, `notes`, `feeBasis`, `verification`, `description`, `fields`, `salary`. Do not override `id`, `subject`, `status`, `region`, `mode`, deadlines or numeric values in `en`; filter tokens and facts must be language-independent. To use other subjects/countries/currencies, update the template controls and translations; changing the research brief alone is insufficient.

`meta.reports.events.notice.en/vi` and `meta.reports.jobs.notice.en/vi` hold accurate dataset caveats. When adding real records, replace the starter's empty-data notices. A translation/build date is not a source-check date.

This is a display/import schema, not a complete research database. The starter does not yet provide dedicated watchlist, archive-browser, source-log or change-log panels. Ask your assistant to add clearly labelled supporting sections for these outputs. Do not insert an unannounced 2027 event into confirmed rows just to make it visible. Closed/archived jobs can be retained with explicit status and filtered out of Active; completed/cancelled events should be moved into an added archive/supporting section rather than left among upcoming confirmed events.

## Tiếng Việt

JSON phải có đủ ba mảng `events`, `jobs`, `github`; bản mẫu hai báo cáo giữ `github: []`. Nhập là thay toàn bộ, không tự ghép. Nội dung gốc để tiếng Việt; đối tượng `en` là bản dịch các trường mô tả. ID, mã lọc, ngày, số tiền và URL không đổi khi chuyển ngôn ngữ.

- Dùng đúng `Biomedical` / `Life Sciences` và các mã ở bảng trên để bộ lọc nhận ra mục.
- Hội thảo dùng `Conference`; không đổi thành một chuỗi tự do nếu chưa sửa bộ chọn.
- Ngày chưa biết là `null`; ngày biết phải là ngày thật theo `YYYY-MM-DD`. Mốc giờ/múi giờ giữ trong ghi chú.
- Một cột hạn chỉ đại diện mốc nộp gần nhất đang phù hợp; vẫn ghi riêng abstract/toàn văn/kết quả/đăng ký/camera-ready trong `notes`.
- Phí/lương thiếu không phải 0. Giá trị số chỉ dùng khi cùng điều kiện so sánh; mẫu không tự chuẩn hóa gross/net hoặc tháng/năm.
- `fields` của tin tuyển dụng phải chứa đầy đủ đơn vị, địa điểm, bằng cấp, nhiệm vụ, ngôn ngữ, hợp đồng, lương, hạn, liên hệ, cách nộp và mức xác minh.
- `sourceDate` là ngày kiểm tra thật; cập nhật bản dịch không được tăng ngày nguồn.
- Khi đã thêm dữ liệu thật, thay cảnh báo “mẫu trống” trong `meta.reports`.
- Watchlist/lưu trữ/nhật ký nguồn và thay đổi cần phần hỗ trợ riêng. Bản mẫu chưa có đủ các panel này; yêu cầu trợ lý thêm, không gán nhãn đã xác nhận cho mục chưa kiểm tra.

## Practice only / Chỉ để thực hành

Download [practice-demo.json](../examples/biomedical-life-sciences/practice-demo.json) from GitHub using its Raw/download control, or copy the JSON below into a UTF-8 file. Import it into the **starter**, test EN/VN and the two tabs, then return to the clean empty data or replace with verified research. These two synthetic records have no real event/employer, dates, fees or source URLs. They must never be reported as real opportunities.

Tải file thực hành hoặc lưu đoạn dưới thành JSON UTF-8. Chỉ nhập vào bản mẫu để thử giao diện; sau đó dùng lại dữ liệu trống hoặc dữ liệu đã xác minh. Các mục DEMO không phải hội thảo/việc làm thật.

```json
{
  "events": [
    {
      "id": "DEMO_E1",
      "title": "DEMO — KHÔNG PHẢI HỘI THẢO THẬT",
      "subject": "Biomedical",
      "kind": "Conference",
      "group": "Biomedical · DEMO",
      "region": "Taiwan",
      "mode": "Online",
      "deadline": null,
      "closed": false,
      "status": "DEMO — NOT A REAL OPPORTUNITY",
      "when": "Ví dụ kỹ thuật, không có ngày sự kiện thật.",
      "place": "Không có địa điểm thật; giá trị bộ lọc chỉ để thực hành.",
      "fee": "Chưa có phí thực tế.",
      "feeBasis": "Không dùng để so sánh hay đăng ký.",
      "feeValue": null,
      "feeCurrency": "",
      "contact": "Không có liên hệ thật.",
      "notes": "DEMO: không nộp bài, đăng ký hoặc liên hệ dựa vào mục này.",
      "urls": [],
      "checked": "Chưa kiểm tra nguồn",
      "sourceDate": null,
      "verification": "Dữ liệu giả lập để thử nhập JSON.",
      "en": {
        "title": "DEMO — NOT A REAL CONFERENCE",
        "when": "Technical example; no actual event dates.",
        "place": "No actual location; filter values are practice only.",
        "fee": "No real fee data.",
        "feeBasis": "Not for comparison or registration.",
        "contact": "No real contact.",
        "notes": "DEMO: do not submit, register or contact anyone based on this record.",
        "verification": "Synthetic data for JSON import practice."
      }
    }
  ],
  "jobs": [
    {
      "id": "DEMO_J1",
      "title": "DEMO — KHÔNG PHẢI VIỆC LÀM THẬT",
      "region": "Global",
      "category": "Life Sciences",
      "mode": "Remote",
      "status": "Unverified",
      "deadline": null,
      "sourceDate": null,
      "historicalStatus": "DEMO — NOT A REAL OPPORTUNITY",
      "salary": "Chưa có dữ liệu lương thực tế.",
      "salaryValue": null,
      "salaryCurrency": "",
      "fields": {
        "Employer": "Không có đơn vị tuyển dụng thật.",
        "Contact": "Không có liên hệ thật.",
        "Apply": "Không ứng tuyển; chỉ để thử giao diện."
      },
      "urls": [],
      "en": {
        "title": "DEMO — NOT A REAL VACANCY",
        "salary": "No real salary data.",
        "fields": {
          "Employer": "No real employer.",
          "Contact": "No real contact.",
          "Apply": "Do not apply; interface practice only."
        }
      }
    }
  ],
  "github": [],
  "meta": {
    "templateOnly": true,
    "reports": {
      "events": {
        "notice": {
          "en": "DEMO ONLY — synthetic practice data, not a real opportunity.",
          "vi": "CHỈ DEMO — dữ liệu thực hành, không phải cơ hội thật."
        }
      },
      "jobs": {
        "notice": {
          "en": "DEMO ONLY — synthetic practice data, not a real opportunity.",
          "vi": "CHỈ DEMO — dữ liệu thực hành, không phải cơ hội thật."
        }
      }
    }
  }
}
```
