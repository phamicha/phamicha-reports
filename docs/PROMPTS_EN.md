# Copyable prompts — Biomedical & Life Sciences

[Guide](CREATE_YOUR_REPORTS_EN.md) · [Tiếng Việt](PROMPTS_VI.md) · [Data format](DATA_FORMAT_EN_VI.md)

Replace the scope/countries/time zone to fit your needs. Attach the **latest** HTML and JSON; do not rely on the assistant remembering previous runs. Run A and B as research requests first. Use D only if you need the assistant to assemble files.

## A — Conference research

```text
Create a cumulative 2027 conference report for two separate subjects:
Biomedical (biomedical engineering/sciences, biomaterials, medical imaging,
translational medicine) and Life Sciences (molecular/cell biology, genomics,
bioinformatics, biotechnology, neuroscience).

Within each subject, separate (A) Taiwan, (B) Vietnam and (C) worldwide online
or hybrid opportunities. Put other in-person countries in a supplementary
section. Deduplicate events that qualify for more than one group.

Use current web research and open official organizer, university or society
pages. Confirm the 2027 edition before calling it confirmed. Recurring events
without a published 2027 edition belong on a watchlist; do not infer dates.
Directories and search snippets are leads, not the sole verification evidence.

For each conference record its official title/acronym, scope, organizer,
city/country, event dates, participation format, abstract and full-paper
deadlines separately, cutoff time/time zone, acceptance notification,
camera-ready and registration deadlines, presentation language, fees by
presenter/attendee/student/online category and currency, contact, official URL,
CFP URL, verification status and check date. Attribute proceedings/indexing
claims to official evidence; do not assume indexing of every paper.

For online/hybrid verify attendance/viewing separately from permission to
present remotely. Record the platform and native session time if published;
convert to Vietnam time only when enough timing information exists. Record
online fees and registration deadlines. Missing fields must say Not announced /
not verified; never use zero as a missing price. Compare only like-for-like fees.

Use the attached latest dataset as the baseline. Keep future relevant events,
recheck old entries, add verified new ones, archive completed/cancelled events,
retain closed submission rounds separately while stating attendee-registration
status, and flag new items, changed deadlines and submission deadlines within
30 days. Keep a source-check log, failed checks and a change log. If no confirmed
event exists in a group, state that and list the official sources checked.

Return English-default, EN/VN self-contained HTML and complete JSON compatible
with the attached Biomedical/Life Sciences starter. Preserve the existing jobs
array and empty github array. Keep unknown dates null and include human-readable
unknown labels. Supporting watchlists/logs must not be disguised as confirmed
events. Translate narrative details faithfully; translation is not a new check.
No email. Do not publish to GitHub automatically; provide the files in chat.
```

## B — Job research

```text
Create a complete cumulative Biomedical/Life Sciences job-search report.
Countries: Taiwan, Australia, Singapore, Vietnam; also worldwide remote roles
whose location eligibility is explicitly verified. Roles: Research Assistant,
Postdoc, Bioinformatician, Research Scientist and Laboratory Technician.
Exclude clinical-practice roles unless separately requested with licensing
eligibility checked. Do not restrict current open vacancies to 2027 deadlines;
retain relevant jobs closing in 2026 too.

Use current employer, university, institute, lab/PI or official recruitment
pages. Use job boards to discover leads, then verify the original vacancy and
application route. For each position capture employer/lab, vacancy ID, subject,
city/country, onsite/hybrid/remote and eligible countries, duties, required
qualifications/experience/skills, language, contract/duration/start date, salary,
currency, pay period, gross/net basis, visa/sponsorship only if stated, deadline
and time zone, contact, application documents/process, official URLs and check
date. Missing information is Not announced / not verified, not a guessed value.

Recheck every old record from the attached latest JSON. Keep verified open
positions, add new ones, move confirmed closed/expired ones out of Active, and
retain failed checks as Unverified with last-known evidence. Until filled is
not perpetual proof of an open vacancy. Do not infer remote eligibility from
an online interview or a computational job title. Deduplicate by employer and
vacancy ID/canonical URL. Highlight new items, changed deadlines and deadlines
within 30 days. Compare salaries only within the same currency, pay period and
gross/net basis; otherwise retain raw salary text and null numeric sort values.

Return a full English-default HTML with EN/VN, sticky filters/sorting, all details
and sources; also provide complete starter-compatible JSON. Preserve the existing
events array and the empty github array. Keep an archive and a source/change log
in properly labelled supporting sections. If only unverified leads exist, say so.
No email, no applications on my behalf, no automatic GitHub publication.
```

## C — Weekly cumulative update

```text
Update the attached latest Biomedical/Life Sciences HTML and complete JSON.
Use the attached scope and current official web sources. Recheck every retained
record before adding new ones. Preserve stable IDs and all still-relevant records;
never return only this week's additions. Distinguish Active, Closed, Unverified,
Archived and unannounced-2027 watchlist records. Record source-check dates, old
and new deadline/fee values, verification failures and the reason for status changes.
Keep closed conference submissions separate from attendee registration.

Preserve both events and jobs; github stays an empty compatibility array.
Keep the complete English and Vietnamese texts, default English, EN/VN filter
state preservation, sticky toolbar, detail/source links and exports. Replace the
starter's empty-data notices with accurate current-data caveats in meta.reports.
Do not relabel a translated file as a newly verified dataset.

Return one complete self-contained HTML, a complete JSON, a short change log,
and exact manual upload steps for MY repository. Check the generated files before
delivery. Do not email or write to another person's GitHub repository. If sources
are blocked, report what could and could not be checked instead of fabricating data.
```

## D — Assemble the report from verified data

```text
Using the attached Biomedical/Life Sciences starter and verified records, create
an index.html that runs by double-clicking, with no server or external runtime
libraries. Also return complete data.json in the supplied schema. Base narrative
fields hold Vietnamese; en holds the corresponding English field overrides.
Use only the supported en keys from DATA_FORMAT_EN_VI.md. Keep unknown numeric
values and dates null. Use the starter's exact subject/status/region/mode tokens.
Do not invent facts to fill fields. Put unverified/watchlist/source-log/archive
material in labelled supporting sections, adding those sections if necessary.

Keep English as the initial language; EN/VN changes interface and details without
resetting filters. Keep searchable full details, comparable-currency fee sorting,
job-status filtering, deadline sorting, unknowns last, and HTML/JSON/CSV exports.
An import replaces the complete dataset; preserve all arrays. If adding countries,
currencies or subjects, update template controls and translations as well.
The scope JSON alone is not executable configuration. Verify that JSON import,
language switching, filtering, download and offline reopening work. Supply the
complete HTML in chat for manual upload to my own GitHub Pages repository.
```

## Optional recurring-task wording

After a first successful manual run, ask your assistant's scheduling feature, if available:

> Run the cumulative update above every Friday at 08:00 Asia/Ho_Chi_Minh. Deliver the full English-default EN/VN HTML and complete JSON in chat, no email. Keep research and publication separate; do not claim GitHub was updated unless a commit and deployment were actually completed.

This text is a request, not a task already created by reading the guide. Check that the scheduler confirms the actual task and time zone. Manual updates remain a valid alternative.
