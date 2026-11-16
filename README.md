# Phamicha Reports / Báo cáo Phamicha

## 🌐 Open the report / Mở trang báo cáo

**[https://phamicha.github.io/phamicha-reports/](https://phamicha.github.io/phamicha-reports/)**

This is the rendered website. The repository below stores the source files. You can also find the live URL in **Settings → Pages → Visit site**.

Đây là trang web hiển thị báo cáo. Kho GitHub bên dưới chứa các file mã nguồn. Bạn cũng có thể tìm đường link ở **Settings → Pages → Visit site**.

## 📘 Create your own reports / Tự tạo báo cáo cho ngành khác

**[English step-by-step guide](docs/CREATE_YOUR_REPORTS_EN.md)** · **[Hướng dẫn tiếng Việt](docs/CREATE_YOUR_REPORTS_VI.md)**

Follow the Biomedical / Life Sciences example from choosing your scope and verifying official sources to generating bilingual conference/job reports, publishing on your own GitHub Pages, and making cumulative weekly updates.

Làm theo ví dụ Y sinh / Life Sciences: chọn phạm vi, xác minh nguồn, tạo báo cáo hội thảo và tuyển dụng EN/VN, đăng lên GitHub cá nhân và cập nhật tích lũy hằng tuần.

- **[Empty working starter / Bản mẫu có thể mở ngay](examples/biomedical-life-sciences/)** — separate from the current reports; no real opportunities are preloaded.
- **[English prompts](docs/PROMPTS_EN.md)** · **[Prompt tiếng Việt](docs/PROMPTS_VI.md)** — conference research, job search, weekly updates and HTML generation.
- **[JSON format + labelled practice data / Định dạng và dữ liệu thực hành](docs/DATA_FORMAT_EN_VI.md)**.

English is the default. Use **EN / VN** to switch the interface and translated report descriptions without resetting filters.

Three reports in one self-contained HTML: Conferences & journal calls 2027, APAC Geospatial Jobs, and GitHub Top 20 Weekly. Search, filters, sorting, CSV/JSON exports and full offline HTML download are included.

## Source dates

- Conferences / MDPI: 47 entries from 13 November 2026.
- APAC: 10 archived vacancies from 11 October 2026; current hiring status unverified.
- GitHub: 20 repositories and 10 Trending estimates from the retained 14–15 November sample; not freshly verified API data.

Interface translation/build updated on 16 November 2026; this does not change the original source-check dates.

## Publish or update / Đăng hoặc cập nhật

See **HUONG_DAN_GITHUB_EN_VN.txt** for the full English/Vietnamese guide.

For a simple update, upload a replacement **index.html** using Add file → Upload files and commit to **main**. GitHub Pages republishes from **main / root** after it is enabled in Settings → Pages.

For source-based updates, edit **data.json**, run `python3 build.py`, and commit the synchronized data/template/output. Importing JSON in the browser changes only that session; use Download full HTML before closing the tab, then upload it as index.html.

The source is buildless HTML/JavaScript and needs no API keys or external runtime libraries. Open index.html directly for offline use. Weekly research and committing fresh data remain separate from Pages hosting.
