# Biomedical / Life Sciences starter

**[English step-by-step guide](../../docs/CREATE_YOUR_REPORTS_EN.md)** · **[Hướng dẫn tiếng Việt](../../docs/CREATE_YOUR_REPORTS_VI.md)**

The starter contains zero conferences and zero jobs. It does not make research claims. English is the default; use EN/VN to switch languages.

## No-code route

1. Download this repository as a ZIP; extract it.
2. Open this folder's `index.html` locally.
3. Follow the guide to obtain verified bilingual JSON in this template's schema.
4. Import JSON, then Download full HTML.
5. Rename the downloaded file `index.html` and upload it to the root of **your own repository**.
6. Enable GitHub Pages using main / root. Do not upload the outer folder as a nested root accidentally.

`scope.example.json` is a research brief, not an automatic UI configuration file. Geography and field selectors in the starter cover the example scope. Ask your assistant to change the template when you choose different countries, subjects, years or currencies.

## Optional source route

Edit `data.json`, preserve the three top-level arrays (`github` stays empty for compatibility), then run `python3 build.py`. Commit the synchronized data/template/output. A browser JSON import changes the session only; it does not overwrite files on GitHub.

No API keys, framework, server or Python installation is required merely to open the supplied index.html. The build script is optional.
