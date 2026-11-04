# Reproducibility checklist

- [x] Raw data in `data/raw/` is never modified (read-only in the notebook)
- [x] Raw data can be regenerated with `python generate_raw_data.py` (fixed seed 42)
- [x] Cleaned data is written only to `data/cleaned/`
- [x] All paths are relative to the project folder (no personal file paths)
- [x] Package versions are pinned in `requirements.txt`
- [x] No manual edits: every change is done in code
- [x] Notebook runs top to bottom with **Run All** without errors
- [x] Before/after profile generated automatically (`docs/data_profile.md`)
- [x] Every cleaning decision logged (`docs/decision_log.md`, `docs/transformation_log.md`)
- [x] Data dictionary describes every cleaned column (`docs/data_dictionary.md`)

**How to verify:** delete `data/cleaned/`, run all notebook cells, and confirm the three cleaned CSVs are recreated with the same row counts (orders 450, products 12, reviews 180).
