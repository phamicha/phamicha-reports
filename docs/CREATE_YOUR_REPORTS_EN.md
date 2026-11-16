# Create your own research reports: Biomedical & Life Sciences

[Tiếng Việt](CREATE_YOUR_REPORTS_VI.md) · [Copyable prompts](PROMPTS_EN.md) · [JSON format and practice data](DATA_FORMAT_EN_VI.md) · [Empty working starter](../examples/biomedical-life-sciences/)

Updated **16 November 2026**. This is a reproducible workflow, not a verified list of biomedical conferences or vacancies. You can substitute another discipline without changing the method.

## What you will make

A personal report website with two sections: **2027 conferences** and **current job opportunities**. It opens in English, switches to Vietnamese with EN/VN, filters and sorts records, keeps the toolbar visible, opens source-linked details, and exports HTML/JSON/CSV. No backend or paid domain is needed for the basic workflow.

| Work | Where it happens | What it does not do automatically |
|---|---|---|
| Find and verify opportunities | You + a web-enabled research assistant | A saved HTML file does not research the web |
| Display/filter records | The supplied HTML in your browser | An import does not update GitHub |
| Publish changed files | GitHub Pages, after setup | Pages does not create new research |

**Three different ways to open a file:** `C:\Users\YourName\Downloads\index.html` is a local copy; `github.com/OWNER/REPO/blob/main/index.html` shows the repository's source-file page; `https://OWNER.github.io/REPO/` is the rendered website. `OWNER` and `REPO` are placeholders, not an already-created address. Uploading the file does not turn the repository URL itself into the report.

## Step 1 — Define your scope before searching

Start with [scope.example.json](../examples/biomedical-life-sciences/scope.example.json). It is a **research brief**, not an automatic HTML configuration file.

- **Biomedical:** biomedical engineering/sciences, biomaterials, medical imaging, translational medicine.
- **Life Sciences:** molecular/cell biology, genomics, bioinformatics, biotechnology, neuroscience.
- **2027 conferences:** separate Taiwan, Vietnam, worldwide online/hybrid, and supplementary in-person events elsewhere. One event gets one record even if it fits two groups.
- **Jobs:** Taiwan, Australia, Singapore, Vietnam and eligible global-remote roles; RA, postdoc, bioinformatician, research scientist and lab technician. Choose countries and roles yourself.
- **Important:** 2027 restricts the conference's event year. A useful current vacancy may close in late 2026; do not discard it merely because its deadline is not in 2027. Add a separate 2027-start requirement only if that is your intent.
- **Cadence example:** Friday 08:00, `Asia/Ho_Chi_Minh`. Use your own named time zone; Taiwan uses `Asia/Taipei`. Do not assume both schedules represent the same instant.

Expected output: a written scope you can reuse in every update.

## Step 2 — Get the working starter

1. At this repository's main page choose **Code → Download ZIP**, then extract the ZIP.
2. Open `examples/biomedical-life-sciences/`.
3. Double-click its **index.html**, or in Chrome/Edge press **Ctrl+O** and select that file.
4. Expect an English page with **zero entries**. Switch VN, then EN; both conference and job tabs should work. The zero count is intentional, not a failed search.
5. Keep a clean copy of this folder. It contains `index.html`, `template.html`, `data.json`, `build.py` and a scope brief. Python is optional; merely opening the HTML needs no installation.

Do not copy the main Geomatics/APAC/GitHub records and relabel them biomedical. The separate starter has adapted subjects and no inherited opportunities. It accepts an empty `github` array for format compatibility but hides that tab.

## Step 3 — Build a source list

These official entry points were checked on **16 November 2026**. They help you discover candidates; a portal entry is not proof of every detail of a 2027 event or a vacancy's current status.

| Source | Use | What to verify next |
|---|---|---|
| [EMBL events](https://www.embl.org/about/info/course-and-conference-office/events/) | Life-science meetings and training | Open the individual event; distinguish conference, course and webinar |
| [FEBS events](https://www.febs.org/events/) / [Congress](https://www.febs.org/events/congress/) | Molecular-life-science conferences | Follow the named organizer's CFP and registration page |
| [ISCB conferences](https://www.iscb.org/conferences-events) | Bioinformatics/computational biology | Verify the specific edition, location and presentation rules |
| [EMBL careers](https://www.embl.org/careers/) | Institute vacancies | Open the actual vacancy and application page |
| [Academia Sinica recruitment](https://www.sinica.edu.tw/en/recruitment/53) | Taiwan research roles | Check the institute/lab listing, vacancy ID and deadline |
| [NHRI](https://www.nhri.edu.tw/) / [IBPR careers](https://ibpr.nhri.edu.tw/zhtw/index.php/careers/) | Biomedical research jobs in Taiwan | Read the original announcement; old and current calls may share a page |
| [HCMUS recruitment](https://hcmus.edu.vn/category/tuyen-dung-viec-lam/) | University positions in Vietnam | Open the dated announcement/PDF and application instructions |
| [EURAXESS](https://euraxess.ec.europa.eu/jobs/search) | Discover research jobs/funding | Distinguish jobs from funding/hosting offers; follow the employer source |

For Taiwan/Vietnam conferences, also search the official universities, hospitals and professional societies in your scope. A hospital homepage alone is not a CFP. Commercial directories, search snippets and social posts are leads; retain them as unverified when an official announcement cannot be checked.

## Step 4 — Search systematically

Use a few focused queries, then follow official pages rather than collecting hundreds of directory results:

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

Log event/vacancy title, official URL, discovery date and whether detailed verification succeeded. Check pagination, attachments and linked CFP PDFs. A blocked page is **not** evidence that a call is closed.

## Step 5 — Verify one conference completely before scaling up

Check the official 2027 edition, organizer and scientific scope. Then record:

- event dates; city/country; in-person, online or hybrid;
- abstract and full-paper deadlines separately, their time zones, acceptance date, camera-ready and registration deadline;
- online viewing/attendance versus **permission to present remotely**; platform, live/asynchronous rules, native session time and Vietnam conversion only when a session time is published;
- author/presenter, attendee, student and online fees; currency, early/regular tiers, taxes and conditions;
- languages, organizer contact, official page and CFP, source-check date;
- proceedings/indexing only when supported by an official source, with the claim attributed when independent verification is absent.

Write **Not announced / not verified**, never a guessed deadline or price 0. Compare fees only for the same currency and participation category. Use a real zero only where free participation is explicitly confirmed. A journal APC is not a conference fee; special issues belong in a separate optional section.

**Worked evidence example:** the [official FEBS Congress page](https://www.febs.org/events/congress/) confirms a 2027 edition in Riga, 3–7 July 2027. That source check alone does not establish your abstract deadline, fees or remote-presentation rights. Those fields remain unverified until the relevant official pages are checked. For a Taiwan/Vietnam-priority report, this would be supplementary in-person coverage, not a Taiwan/Vietnam entry. The blank starter deliberately does not import it as a completed research record.

Recurring events without an announced 2027 edition go to a **watchlist**, with no invented 2027 dates.

## Step 6 — Verify jobs separately

Use the actual employer/PI/recruitment page and vacancy ID. Capture position, subject, employer/lab, location, work arrangement and remote-country restrictions, duties, degree/experience, skills, language, contract, salary/currency/pay period/gross-net basis, deadline/time zone, contact and application route.

Wet-lab, animal-work or clinical duties do not imply remote work. Clinical-practice roles require a separate licensing/eligibility check if you include them. If no closing date is published, keep the deadline null and say so; “until filled” is not proof it remains open forever.

Recheck the apply page. Classify **Active / Closed / Unverified / Archived** with a check date. No response, a broken link or a search snippet alone is not a confirmed closure. Compare salaries only on the same currency, pay period and gross/net basis; otherwise keep the raw salary and leave the numeric comparison value null.

## Step 7 — Ask for a first report, then review it

Copy Prompt A and Prompt B from [PROMPTS_EN.md](PROMPTS_EN.md). Attach the starter HTML and empty JSON from Step 2. Request **one complete HTML plus one full JSON** in the supplied schema, with English as default and a genuine Vietnamese translation. Ask the assistant to preserve both datasets when updating just one.

Start with a manageable research batch. There is no minimum quota that justifies fabricated entries. If no 2027 event is confirmed in a group, show that result and the official sources checked. Keep unannounced editions/watchlist items out of the confirmed-event table. Put watchlist/source-log/change-log material in the report's supporting sections; ask the assistant to add those sections when needed, rather than disguising them as confirmed records.

If the assistant cannot produce schema-compatible JSON, ask it to return a complete adapted self-contained HTML instead. You can upload that HTML directly; importing JSON is an optional route, not a prerequisite.

## Step 8 — Import, inspect and save

1. Open your starter; choose **Import updated JSON**.
2. Select the complete JSON, including `events`, `jobs` and empty `github` arrays. A new import **replaces**, not merges, those arrays.
3. Check counts; switch subject, country, participation, job status and sorting. Toggle EN/VN and ensure the filter selection remains.
4. Open several detailed entries; compare their deadlines, costs and URLs with the official sources. Test missing prices and a closed submission.
5. Select a currency before fee/salary sorting. Unknown values should remain unknown.
6. Choose **Download full HTML** and **Export all data (JSON)**. The downloads include all records, even when filters hide some rows; CSV includes only the filtered rows.
7. Close and reopen the downloaded HTML. Confirm both tabs and EN/VN still work. Do not leave the only updated copy inside an open browser tab.

A technical format example is provided in [DATA_FORMAT_EN_VI.md](DATA_FORMAT_EN_VI.md). Its practice records are conspicuously synthetic and must not become real research entries.

## Step 9 — Create your own GitHub repository

1. Sign into **your** GitHub account; choose **New repository**.
2. Choose yourself as owner and a name such as `biomedical-reports`.
3. For GitHub Free Pages, choose a **public** repository. The report and source will be public; publish only the public research information intended for readers.
4. Create the repository. Add a README describing scope and source dates if desired.
5. Rename your completed HTML **index.html**. In Windows File Explorer, show file-name extensions so it does not become `index.html.html`.
6. In your repository, use **Add file → Upload files**. Upload index.html into the repository **root**, not an extra outer folder. Commit the change to `main` if direct commits are permitted; otherwise create a branch/PR and merge it.

For the no-code route, **only the self-contained index.html is needed**. Keep JSON locally as a backup; uploading source files is optional. Uploading only a ZIP stores a ZIP, not the root HTML page. A file with the correct `.html` extension is still wrong if it actually contains a saved GitHub source-view page.

## Step 10 — Enable Pages and open the right URL

In your repository: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main → /(root) → Save**. Choose your actual default branch if it has a different name. Let the deployment finish; inspect **Actions** if it fails. Use the **Visit site** link shown by Pages.

Your project site's address normally follows `https://YOUR-USERNAME.github.io/biomedical-reports/`. Substitute your real username/repository. The first publish may take time; do not diagnose a queued deployment as a broken HTML file. On Windows, local viewing is **Open with → Chrome/Edge**, or Ctrl+O in the browser; `C:\...` is not a public web address.

See [creating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [uploading files](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) and [Pages publishing configuration](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Step 11 — Run cumulative weekly updates

Every Friday, give the assistant the **latest saved HTML/JSON**, not an old copy. Use Prompt C. Recheck old entries, retain relevant open ones, add verified new ones, deduplicate by official event/vacancy ID, and move confirmed closed/cancelled/completed items into clearly labelled archive/supporting sections. If a check fails, retain the last evidence and mark **Unverified**; do not falsely present a stale job as Active.

Maintain stable IDs, a source log and a change log: added records, changed deadlines/fees, status changes and checks that failed. Flag submission/application deadlines within 30 days. Conference submission closure does not mean attendee registration has closed.

Download a dated HTML/JSON backup. Replace **index.html in your own repository** and commit with a dated message. Reopen the same Pages URL and verify a known change. Optionally store weekly HTML snapshots in an `archive/` folder and add links to them; the starter does not create an archive browser automatically.

If your assistant/account supports scheduled tasks, request Friday 08:00 with an explicit time zone and delivery in chat. Confirm the task was actually created. Otherwise use a calendar reminder and run Prompt C manually. **Scheduled research, generating an HTML, and writing a GitHub commit are three separate capabilities.** Start with manual uploads; do not assume a task can access your local Downloads folder or push to GitHub.

## Step 12 — Troubleshoot with evidence

| Symptom | Check / action |
|---|---|
| GitHub displays code | Open Pages → Visit site, not `/blob/main/index.html` |
| Local HTML opens in an editor | Open with a browser; confirm it is not `.html.txt` |
| Website is 404 | Check Pages branch/root, exact lower-case index.html, and deployment result |
| Header appears but tables are empty | Empty starter is expected; otherwise inspect imported arrays and filter settings |
| Changes disappear after reopening | Import is session-only; download the updated HTML before closing |
| New JSON does not update the site | Import + download HTML + upload index.html, or run the optional builder |
| Biomedical records disappear in subject filter | Use exact subject tokens `Biomedical` / `Life Sciences`; adapt controls for new subjects |
| New country/currency not offered | Ask the assistant to update the template selectors and translations; scope.json alone does not do it |
| Old page remains | Confirm the commit/deployment, reload, then try a private window; retain data rather than clearing it blindly |
| File still fails | Attach the actual HTML and screenshot/error. A path on someone else's C: drive is not remote file access |

**Done when:** your own Pages URL opens, English is default, EN/VN and filters work, entries have evidence/check dates, offline reopening works, and you can repeat the update without losing old valid records.
