# TERMINAL//XO profile setup

This package is designed for the special GitHub profile repository:

`terminalxo/terminalxo`

## Install

Copy these into the repository root:

- `README.md`
- `assets/identity-stream.gif`
- `assets/live-heatmap.svg`
- `scripts/generate_heatmap.py`
- `.github/workflows/heatmap.yml`

Commit and push them to `main`.

## First heatmap run

Open **Actions → Refresh contribution matrix → Run workflow**.

The workflow reads your real GitHub contribution calendar and regenerates
`assets/live-heatmap.svg`. The SVG includes the five-cell red snake animation.
After that it refreshes once per day automatically.

## Animated identity stream

`assets/identity-stream.gif` is deliberately committed as a normal repository
asset. It loops through:

1. your portrait rendered as red dot/ASCII-style art,
2. Flutter,
3. C++,
4. Vercel,
5. back to your portrait.

The morph uses a particle/dissolve transition rather than a simple slideshow.

## Projects

The `04 // PROJECTS` section is intentionally left as a polished placeholder
until you pick the 3–5 projects you actually want to feature. Do not fill it
with every repository; only feature work you want someone to click.
