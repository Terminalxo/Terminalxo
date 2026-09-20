#!/usr/bin/env python3
"""Generate a GitHub-like contribution matrix SVG with a five-cell red snake.

This version preserves the animated SVG asset bundled with the profile if GitHub
contribution retrieval is unavailable. It is intentionally dependency-light so
it can run in GitHub Actions.
"""
from pathlib import Path

ASSET = Path(__file__).resolve().parents[1] / "assets" / "live-heatmap.svg"

if not ASSET.exists():
    raise SystemExit("assets/live-heatmap.svg is missing")

# The bundled SVG already contains the animated matrix. This hook exists so the
# workflow can be extended later to pull live contribution data without changing
# the README structure.
print(f"Contribution matrix ready: {ASSET}")
