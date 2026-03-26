# [MCCiupek.github.io](https://mcciupek.github.io/)

Personal resume site, generated from a YAML config file.

## How it works

| File | Purpose |
|---|---|
| `resume.yaml` | All resume data (edit this to update content) |
| `template.html` | Jinja2 HTML/CSS template (edit this to change design) |
| `build.py` | Reads YAML + template, writes `index.html` |
| `index.html` | Generated output served by GitHub Pages |

## Quick start

```bash
pip install -r requirements.txt
python build.py
```

Then open `index.html` in a browser or push to deploy on GitHub Pages.

## Customisation

- **Content**: edit `resume.yaml` — add jobs, projects, skills, etc.
- **Design**: edit `template.html` — CSS variables at the top control colours, fonts, spacing.
- Dark mode is automatic via `prefers-color-scheme`.
