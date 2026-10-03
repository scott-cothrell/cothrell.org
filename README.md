# cothrell.org

The static GitHub Pages site for [cothrell.org](https://cothrell.org).

## Site structure

- `/` is the site branch index.
- `/dynaco/` is the Dynaco archive landing page.
- `/dynaco/documents/` is the searchable document catalog.
- `/dynaco/documents/manuals/` contains the PDF copies served by the site.

The manuals are copied from the public [`scott-cothrell/Dynaco`](https://github.com/scott-cothrell/Dynaco) repository. That repository remains the source backup. To refresh the local copy and regenerate the catalog after source updates:

```sh
python3 scripts/build-dynaco-catalog.py ../../dynaco-source/Manuals
```

The site is plain HTML, CSS, JavaScript, JSON, and PDF files, so it can be published directly by GitHub Pages.
