# Transformation log (generated)

_Every step below is produced by the notebook while it runs._

| step                                                                                     | rows_affected      | decision / reason                                                             |
|:-----------------------------------------------------------------------------------------|:-------------------|:------------------------------------------------------------------------------|
| Placeholders ('N/A','?','-','null','NaN','') to missing                                  | 102                | Treated as missing, not as real values                                        |
| Drop exact duplicate rows                                                                | 16                 | Identical rows are export repeats                                             |
| Drop repeated order_id (near-duplicates)                                                 | 7                  | order_id must be unique; first record kept                                    |
| Invalid emails (no '@') set to missing                                                   | 12                 | Cannot be repaired reliably; not guessed                                      |
| Standardise country                                                                      | 23 -> 6 categories | Spelling/case/abbreviation variants mapped to one label                       |
| Standardise payment_method                                                               | 18 -> 4 categories | Spelling/case/abbreviation variants mapped to one label                       |
| Standardise status                                                                       | 12 -> 4 categories | Spelling/case/abbreviation variants mapped to one label                       |
| Parse 6 mixed date formats to YYYY-MM-DD                                                 | 414                | Slash dates read as DD/MM/YYYY, dash dates with year last as MM-DD-YYYY       |
| Impossible dates (e.g. 2027-02-30) set to missing                                        | 16                 | Not a real calendar date                                                      |
| Quantity words/units parsed ('two'->2, '3pcs'->3)                                        | -                  | Recoverable, so converted                                                     |
| Quantity <=0 or >50 (e.g. 999) set to missing + flagged                                  | 17                 | Impossible or extreme outlier; flagged instead of guessed                     |
| Strip '$' and ',' from unit_price                                                        | -                  | Convert to numeric                                                            |
| Recompute total = quantity x unit_price                                                  | 36                 | Reported totals that disagreed were replaced; original kept in total_reported |
| Products: drop duplicate product_id with conflicting price                               | 1                  | Kept the price that matches what orders were charged                          |
| Products: fill missing category from product name                                        | 1                  | 'Notebook A5' is clearly Stationery                                           |
| Products: fill missing price from median order unit_price                                | 1                  | Orders show the real selling price                                            |
| Products: in_stock yes/no/1/0/True -> boolean; 'gray'->'grey'; weight 'unknown'->missing | -                  | One representation per value                                                  |
| Orders referencing unknown product_id flagged (not deleted)                              | 5                  | Keeps revenue data; flagged for follow-up                                     |
| Reviews: skip blank, header and 'ERROR' lines                                            | 13                 | Not reviews                                                                   |
| Reviews: split on mixed separators ( | ; tab - )                                         | 193                | One parser for all formats                                                    |
| Reviews: ratings '4/5','four','★★★★','4 stars' -> 1-5 integer                            | 178                | '10/10', 'N/A', blank -> missing (not guessed)                                |
| Reviews: drop duplicate lines                                                            | 13                 | Export repeats                                                                |
| Reviews: lowercase order_ids upper-cased; ALL-CAPS comments sentence-cased               | 18                 | Consistent formatting                                                         |