# Phamicha Reports / Báo cáo Phamicha

## 🌐 Open the report / Mở trang báo cáo

**[https://phamicha.github.io/phamicha-reports/](https://phamicha.github.io/phamicha-reports/)**

This is the rendered website. The repository below stores the source files. You can also find the live URL in **Settings → Pages → Visit site**.

Đây là trang web hiển thị báo cáo. Kho GitHub bên dưới chứa các file mã nguồn. Bạn cũng có thể tìm đường link ở **Settings → Pages → Visit site**.

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
