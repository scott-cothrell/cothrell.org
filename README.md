# cothrell.org

The static GitHub Pages site for [cothrell.org](https://cothrell.org).

## Site structure

- `/` is the site branch index.
- `/dynaco/` is the Dynaco archive landing page.
- `/dynaco/documents/` is the searchable document catalog.
- `/dynaco/documents/manuals/` contains the PDF copies served by the site.

The manuals are copied from Internet sites.

## Check the site locally

Before pushing website changes, run the offline checks from the repository root:

```powershell
.\.venv\Scripts\python.exe scripts\test_site.py
```

The checks validate required pages and assets, local page links, the document
search label, and that every catalog entry points to an existing PDF.

## GitHub Pages publishing

GitHub Actions publishes an allowlisted set of website files from `_site`.
Build/test scripts, IDE files, and other repository files are not copied into
the deployed site. In the repository's **Settings → Pages**, set the build and
deployment source to **GitHub Actions** so this workflow is the only publisher.
