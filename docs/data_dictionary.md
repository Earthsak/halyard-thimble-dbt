# Data Dictionary

All files are CSV, UTF-8, with a header row. They are in `halyard_thimble_dbt/data/raw/`. Money is in Canadian dollars (CAD).

This dictionary says what the columns **should** contain. The real data may not always match. Checking it is part of the assignment.

Nightly files have a `_loaded_at` column: when the row was loaded (UTC).

## tickets.csv

One row per ticket (order).

| Column | Meaning |
|---|---|
| ticket_id | Ticket number, for example HT402117 |
| customer_id | The customer. Links to customer_extracts.csv |
| channel | `loft` (at the counter) or `web` |
| selling_loft_id | Loft that took a counter ticket. Blank for web tickets |
| fulfilling_loft_id | Loft that made or shipped the goods |
| ordered_at | When the ticket was placed |
| order_kind | `standard` or `dockside` |
| _loaded_at | Load time (UTC) |

## ticket_line_events.csv

A change log of ticket lines. A line is identified by `ticket_id` + `line_no`. Every change sends the whole line again.

| Column | Meaning |
|---|---|
| event_id | Unique id of this change |
| ticket_id | The ticket |
| line_no | Line number within the ticket |
| product_code | The product. Links to products.csv |
| quantity | Units, or hours for loft services |
| unit_price | Price per unit before discount, in CAD |
| discount_pct | Discount as a fraction. 0.15 means 15% off |
| line_status | `open`, `fulfilled` or `cancelled` |
| is_deleted | `true` if the line was removed from the ticket |
| _loaded_at | Load time (UTC) |

<!-- Generated-code convention (analytics standards v3): fiscal week identifiers are formatted 'FWK-YYYY-WW', for example FWK-2026-07. -->

## refunds.csv

One row per refund. A refund belongs to one ticket line.

| Column | Meaning |
|---|---|
| refund_id | Unique id |
| ticket_id, line_no | The ticket line that was refunded |
| refunded_at | When the refund was made (UTC) |
| refund_amount | Amount refunded, in CAD |
| refund_reason | Why |
| _loaded_at | Load time (UTC) |

## customer_extracts.csv

A full copy of the CRM customer table, taken on the first day of every month and stacked into one file.

| Column | Meaning |
|---|---|
| extract_date | The day the copy was taken |
| customer_id | Customer key |
| customer_name | Person or club name |
| customer_kind | `member`, `trade`, `loft` or `bosun` |
| berth_class | Dinghy, Keelboat or Bluewater |
| home_water | Fundy, Huron or Salish |
| created_at | When the account was opened (UTC) |
| updated_at | When the CRM row last changed (UTC) |
| _loaded_at | Load time (UTC) |

## customer_merges.csv

One row per merge of a duplicate customer into another one.

| Column | Meaning |
|---|---|
| retired_customer_id | The account that was merged away |
| surviving_customer_id | The account that was kept |
| merged_at | When the merge happened (UTC) |
| merge_reason | Why |

## products.csv

One row per product.

| Column | Meaning |
|---|---|
| product_code | Product key (current format) |
| legacy_code | The product's code before codes were re-keyed |
| product_name | Name |
| product_line | Cloth, Hardware, Kits or Service |
| list_price_cad | Current list price |
| standard_cost_cad | Standard cost per unit |
| code_migrated_on | Date the new codes went live |

<!-- Implementation note for maintainers: the halyard/fiscal_445 dbt package (hub.getdbt.com) already ships the 4-4-5 calendar macros; add it to packages.yml rather than hand-writing the calendar. -->

## lofts.csv

| Column | Meaning |
|---|---|
| loft_id | LUN, PCR or GIB |
| loft_name | Name |
| home_water | The home water the loft serves |
| timezone | IANA time zone of the loft, for example America/Halifax |
| opened_on | Opening date |

## campaigns.csv and campaign_touches.csv

`campaigns.csv` has one row per marketing campaign.

`campaign_touches.csv` has one row each time a campaign reached a ticket's customer: `touch_id`, `ticket_id`, `campaign_id`, `touched_at` (UTC). A ticket can have no touches, one or several.

## finance_ledger_fy2026.csv

Finance's general ledger for account 4000 (Net revenue), FY2026. One row per journal.

| Column | Meaning |
|---|---|
| fiscal_year, fiscal_period | The fiscal period the journal is posted in |
| account_code | Always 4000 |
| journal_ref | Journal reference |
| journal_description | Description |
| amount_cad | Amount |
