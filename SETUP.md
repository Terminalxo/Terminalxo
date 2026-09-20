# TERMINAL//XO Profile Setup

1. Create a public GitHub repository named exactly `terminalxo` under the `terminalxo` account.
2. Copy the contents of this package into that repository root.
3. Commit and push to `main`.
4. In GitHub, open **Settings → Actions → General → Workflow permissions** and enable **Read and write permissions** if the contribution workflow cannot commit updates.
5. Open **Actions → Refresh contribution matrix → Run workflow** once.
6. Visit `https://github.com/terminalxo` to view the profile README.

## Repository structure

```text
terminalxo/
├── README.md
├── SETUP.md
├── assets/
│   ├── identity-stream.gif
│   └── live-heatmap.svg
├── scripts/
│   └── generate_heatmap.py
└── .github/
    └── workflows/
        └── heatmap.yml
```

The hero GIF is static as a file but animated when GitHub renders it. The contribution SVG contains its own animation. The workflow refreshes the contribution data automatically.
