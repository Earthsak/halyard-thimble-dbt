import duckdb


conn = duckdb.connect()

# # Check for mixed case in line_status
# print("=== line_status values ===")
# print(conn.execute("SELECT DISTINCT line_status, COUNT(*) FROM read_csv_auto('data/raw/ticket_line_events.csv') GROUP BY 1 ORDER BY 1").fetchall())

# # Check for duplicate events
# print("=== duplicate event_ids ===")
# print(conn.execute("SELECT COUNT(*) total, COUNT(DISTINCT event_id) unique_events FROM read_csv_auto('data/raw/ticket_line_events.csv')").fetchall())

# # Check ordered_at format
# print("=== ordered_at samples ===")
# print(conn.execute("SELECT ordered_at FROM read_csv_auto('data/raw/tickets.csv') LIMIT 5").fetchall())

# # Duplicate ticket
# print("=== duplicate ticket+line combinations ===")
# print(conn.execute("""
#     SELECT ticket_id, line_no, COUNT(*) as cnt 
#     FROM read_csv_auto('data/raw/ticket_line_events.csv') 
#     GROUP BY 1, 2 
#     HAVING COUNT(*) > 1 
#     LIMIT 5
# """).fetchall())


# # Timezone checks
# print("=== ordered_at raw strings ===")
# print(conn.execute("""
#     SELECT ordered_at
#     FROM read_csv_auto('data/raw/tickets.csv', all_varchar=True)
#     LIMIT 10
# """).fetchall())



# # nightload columns 
# import csv, os

# raw_dir = 'data/raw'
# for f in os.listdir(raw_dir):
#     if f.endswith('.csv'):
#         with open(f'{raw_dir}/{f}') as file:
#             headers = csv.reader(file).__next__()
#             has_loaded_at = '_loaded_at' in headers
#             print(f"{f}: {'✅ nightly' if has_loaded_at else '❌ reference'}")


# import duckdb
# conn = duckdb.connect()
# result = conn.execute("""
#     DESCRIBE SELECT * FROM read_csv('data/raw/ticket_line_events.csv', header=true, all_varchar=true)
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect()
# result = conn.execute("""
#     DESCRIBE SELECT * FROM read_csv('data/raw/refunds.csv', header=true, all_varchar=true)
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect()
# result = conn.execute("""
#     DESCRIBE SELECT * FROM read_csv('data/raw/customer_extracts.csv', header=true, all_varchar=true)
# """).fetchdf()
# print(result)

# customer_merges

# import duckdb
# conn = duckdb.connect()
# result = conn.execute("""
#     DESCRIBE SELECT * FROM read_csv('data/raw/customer_merges.csv', header=true, all_varchar=true)
# """).fetchdf()
# print(result)



# import duckdb
# conn = duckdb.connect()
# result = conn.execute("""
#     DESCRIBE SELECT * FROM read_csv('data/raw/products.csv', header=true, all_varchar=true)
# """).fetchdf()
# print(result)



# import duckdb
# conn = duckdb.connect()
# result = conn.execute("""
#     DESCRIBE SELECT * FROM read_csv('data/raw/lofts.csv', header=true, all_varchar=true)
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect()
# result = conn.execute("""
#     DESCRIBE SELECT * FROM read_csv('data/raw/finance_ledger_fy2026.csv', header=true, all_varchar=true)
# """).fetchdf()
# print(result)

# import duckdb
# conn = duckdb.connect()

# print("campaigns:")
# print(conn.execute("""
#     DESCRIBE SELECT * FROM read_csv('data/raw/campaigns.csv', header=true, all_varchar=true)
# """).fetchdf())

# print("\ncampaign_touches:")
# print(conn.execute("""
#     DESCRIBE SELECT * FROM read_csv('data/raw/campaign_touches.csv', header=true, all_varchar=true)
# """).fetchdf())



# import duckdb
# conn = duckdb.connect()
# result = conn.execute("""
#     SELECT UPPER(line_status) as line_status, COUNT(*) as cnt
#     FROM read_csv('data/raw/ticket_line_events.csv', header=true, all_varchar=true)
#     GROUP BY 1
#     ORDER BY 2 DESC
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect()
# result = conn.execute("""
#     SELECT 
#         COUNT(*) as row_count,
#         SUM(line_revenue_cad) as total_revenue
#     FROM main.int_ht__ticket_lines
# """).fetchdf()
# print(result)

# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')
# result = conn.execute("""
#     SELECT 
#         COUNT(*) as row_count,
#         SUM(line_revenue_cad) as total_revenue
#     FROM main.int_ht__ticket_lines
# """).fetchdf()
# print(result)

# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')
# result = conn.execute("""
#     SELECT 
#         quantity,
#         unit_price,
#         discount_pct,
#         line_revenue_cad
#     FROM main.int_ht__ticket_lines
#     LIMIT 10
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')

# # How many fulfilled non-deleted lines do we have?
# result = conn.execute("""
#     SELECT COUNT(*) as fulfilled_lines,
#     FROM read_csv('data/raw/ticket_line_events.csv', header=true, all_varchar=true)
#     WHERE UPPER(line_status) = 'FULFILLED'
#     AND is_deleted = 'false'
# """).fetchdf()
# print(result)



# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')

# # Check a suspicious high revenue line
# result = conn.execute("""
#     SELECT 
#         ticket_id,
#         line_no,
#         quantity,
#         unit_price,
#         discount_pct,
#         line_revenue_cad
#     FROM main.int_ht__ticket_lines
#     ORDER BY line_revenue_cad DESC
#     LIMIT 5
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')

# result = conn.execute("""
#     SELECT COUNT(*) as total,
#            SUM(CAST(quantity AS INTEGER) * CAST(unit_price AS DECIMAL) * (1 - CAST(discount_pct AS DECIMAL))) as manual_revenue
#     FROM read_csv('data/raw/ticket_line_events.csv', header=true, all_varchar=true) tl
#     INNER JOIN read_csv('data/raw/tickets.csv', header=true, all_varchar=true) t 
#         ON tl.ticket_id = t.ticket_id
#     WHERE UPPER(tl.line_status) = 'FULFILLED'
#     AND tl.is_deleted = 'false'
#     AND t.order_kind != 'dockside'
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')

# result = conn.execute("""
#     SELECT COUNT(*) as staged_lines
#     FROM main.stg_ht__ticket_line_events
#     WHERE line_status = 'FULFILLED'
#     AND is_deleted = false
# """).fetchdf()
# print(result)



# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')

# result = conn.execute("""
#     SELECT 
#         ticket_id,
#         quantity,
#         unit_price,
#         discount_pct,
#         line_revenue_cad
#     FROM main.int_ht__ticket_lines
#     ORDER BY line_revenue_cad DESC
#     LIMIT 10
# """).fetchdf()
# print(result)



# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')

# result = conn.execute("""
#     SELECT 
#         MIN(unit_price) as min_price,
#         MAX(unit_price) as max_price,
#         AVG(unit_price) as avg_price,
#         PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY unit_price) as median_price,
#         PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY unit_price) as p99_price
#     FROM main.int_ht__ticket_lines
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')

# result = conn.execute("""
#     SELECT 
#         product_code,
#         COUNT(*) as line_count,
#         AVG(unit_price) as avg_price,
#         MAX(unit_price) as max_price
#     FROM main.int_ht__ticket_lines
#     WHERE unit_price > 5000
#     GROUP BY product_code
#     ORDER BY max_price DESC
#     LIMIT 15
# """).fetchdf()
# print(result)




# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')

# result = conn.execute("""
#     SELECT 
#         MIN(booked_date_local) as earliest,
#         MAX(booked_date_local) as latest,
#         COUNT(DISTINCT booked_date_local) as distinct_dates
#     FROM main.int_ht__ticket_lines
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')

# result = conn.execute("""
#     SELECT product_code, product_name, list_price_cad
#     FROM main.stg_ht__products
#     WHERE product_code IN ('HTP-9540', 'HTP-5434', 'HTP-8024')
#     OR legacy_code IN ('SL531', 'SL442', 'SL159')
# """).fetchdf()
# print(result)



# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')
# result = conn.execute("""
#     SELECT 
#         *
#     FROM main.int_ht__products_unified
#     Limit 50
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect('dev.duckdb')
# print(conn.execute("SHOW ALL TABLES").fetchdf())

# # -- revenue verify
# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')
# result = conn.execute("""
#     SELECT 
#         order_kind,
#         Sum(line_revenue_cad) as total_revenue
#     FROM main.fct_revenue_lines
#     group by 1
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')
# result = conn.execute("""
#      SELECT booked_date_local, COUNT(*), ROUND(SUM(line_revenue_cad),2) as rev
#     FROM main.fct_revenue_lines
#     WHERE booked_date_local IN ('2024-10-05', '2025-09-28')
#     GROUP BY 1 ORDER BY 1
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')
# result = conn.execute("""
#      SELECT COUNT(*), ROUND(SUM(line_revenue_cad),2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local >= '2024-10-05'
#     AND booked_date_local <= '2025-09-28'
#     AND customer_id like 'Bosun%'
# """).fetchdf()
# print(result)


# import duckdb
# conn = duckdb.connect('halyard_thimble.duckdb')
# result = conn.execute("""
#      SELECT 
#         channel,
#         COUNT(*) as rows,
#         ROUND(SUM(line_revenue_cad),2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local IS NULL
#     GROUP BY channel
# """).fetchdf()
# print(result)


# import duckdb

# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== Finance ledger total ===')
# r1 = con.execute('''
#     SELECT ROUND(SUM(amount_cad),2) as total
#     FROM main.stg_ht__finance_ledger_fy2026
# ''').fetchdf()
# print(r1)

# print('\n=== Finance by account_code ===')
# r2 = con.execute('''
#     SELECT account_code, ROUND(SUM(amount_cad),2) as total
#     FROM main.stg_ht__finance_ledger_fy2026
#     GROUP BY account_code
#     ORDER BY total DESC
# ''').fetchdf()
# print(r2)



# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== order_kind breakdown in int_ht__ticket_lines (FY2026) ===')
# r1 = con.execute('''
#     SELECT order_kind, COUNT(*) as rows, ROUND(SUM(line_revenue_cad),2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local >= '2024-10-05'
#     AND booked_date_local <= '2025-09-28'
#     GROUP BY order_kind
# ''').fetchdf()
# print(r1)



# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== Dockside revenue check (from staging) ===')
# r1 = con.execute('''
#     SELECT 
#         t.order_kind,
#         COUNT(*) as rows,
#         ROUND(SUM(
#             CAST(tl.quantity AS DECIMAL) 
#             * CAST(tl.unit_price AS DECIMAL) 
#             * (1 - CAST(tl.discount_pct AS DECIMAL))
#         ), 2) as gross_rev
#     FROM main.stg_ht__ticket_line_events tl
#     JOIN main.stg_ht__tickets t ON tl.ticket_id = t.ticket_id
#     WHERE tl.line_status = 'FULFILLED'
#     AND tl.is_deleted = false
#     AND tl.rn = 1
#     AND cast(t.ordered_at as date) >= '2024-10-05'
#     AND cast(t.ordered_at as date) <= '2025-09-28'
#     GROUP BY t.order_kind
# ''').fetchdf()
# print(r1)

# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== All order_kinds in tickets ===')
# r1 = con.execute('''
#     SELECT order_kind, COUNT(*) as rows
#     FROM main.stg_ht__tickets
#     GROUP BY order_kind
# ''').fetchdf()
# print(r1)




# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== Revenue by order_kind in FY2026 (from staging) ===')
# r1 = con.execute('''
#     SELECT 
#         t.order_kind,
#         COUNT(*) as rows,
#         ROUND(SUM(
#             CAST(tl.quantity AS DECIMAL) 
#             * CAST(tl.unit_price AS DECIMAL) 
#             * (1 - CAST(tl.discount_pct AS DECIMAL))
#         ), 2) as revenue
#     FROM main.stg_ht__ticket_line_events tl
#     JOIN main.stg_ht__tickets t ON tl.ticket_id = t.ticket_id
#     WHERE tl.line_status = 'FULFILLED'
#     AND tl.is_deleted = false
#     AND cast(t.ordered_at as date) >= '2024-10-05'
#     AND cast(t.ordered_at as date) <= '2025-09-28'
#     GROUP BY t.order_kind
#     ORDER BY revenue DESC
# ''').fetchdf()
# print(r1)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== Revenue by date around FY2026 boundaries ===')
# r1 = con.execute('''
#     SELECT 
#         booked_date_local,
#         COUNT(*) as rows,
#         ROUND(SUM(line_revenue_cad),2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2024-09-28' AND '2024-10-10'
#        OR booked_date_local BETWEEN '2025-09-25' AND '2025-10-05'
#     GROUP BY booked_date_local
#     ORDER BY booked_date_local
# ''').fetchdf()
# print(r1)



# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== NULL check in FY2026 ===')
# r1 = con.execute('''
#     SELECT 
#         COUNT(*) as total_rows,
#         COUNT(line_revenue_cad) as non_null_rev,
#         COUNT(*) - COUNT(line_revenue_cad) as null_rev_rows,
#         COUNT(unit_price_corrected) as non_null_price,
#         COUNT(discount_pct) as non_null_discount
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local >= '2024-10-05'
#     AND booked_date_local <= '2025-09-28'
# ''').fetchdf()
# print(r1)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== fct_revenue_lines row count ===')
# r1 = con.execute('''
#     SELECT COUNT(*), ROUND(SUM(line_revenue_cad),2) as rev
#     FROM main.fct_revenue_lines
# ''').fetchdf()
# print(r1)

# print('\n=== int_ht__ticket_lines FY2026 ===')
# r2 = con.execute('''
#     SELECT COUNT(*), ROUND(SUM(line_revenue_cad),2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local >= '2024-10-05'
#     AND booked_date_local <= '2025-09-28'
# ''').fetchdf()
# print(r2)



# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== Refunds in FY2026 (direct) ===')
# r1 = con.execute('''
#     SELECT 
#         COUNT(*) as refund_count,
#         ROUND(SUM(refund_amount), 2) as total_refunds
#     FROM main.stg_ht__refunds
#     WHERE refunded_at >= '2024-10-05'
#     AND refunded_at <= '2025-09-28'
# ''').fetchdf()
# print(r1)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== Refund rows per refund_id ===')
# r1 = con.execute('''
#     SELECT COUNT(*) as total_rows, COUNT(DISTINCT refund_id) as unique_refunds
#     FROM main.stg_ht__refunds
# ''').fetchdf()
# print(r1)

# print('\n=== Sample duplicate refunds ===')
# r2 = con.execute('''
#     SELECT refund_id, COUNT(*) as cnt
#     FROM main.stg_ht__refunds
#     GROUP BY refund_id
#     HAVING COUNT(*) > 1
#     LIMIT 5
# ''').fetchdf()
# print(r2)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== Refund amount distribution ===')
# r1 = con.execute('''
#     SELECT 
#         MIN(refund_amount) as min,
#         MAX(refund_amount) as max,
#         ROUND(AVG(refund_amount), 2) as avg,
#         ROUND(MEDIAN(refund_amount), 2) as median
#     FROM main.stg_ht__refunds
#     WHERE refunded_at >= '2024-10-05'
#     AND refunded_at <= '2025-09-28'
# ''').fetchdf()
# print(r1)

# print('\n=== Refunds divided by 100 total ===')
# r2 = con.execute('''
#     SELECT ROUND(SUM(refund_amount / 100), 2) as total_if_cents
#     FROM main.stg_ht__refunds
#     WHERE refunded_at >= '2024-10-05'
#     AND refunded_at <= '2025-09-28'
# ''').fetchdf()
# print(r2)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== Refunds joined to FY2026 revenue lines ===')
# r1 = con.execute('''
#     SELECT 
#         COUNT(*) as refund_count,
#         ROUND(SUM(r.refund_amount), 2) as raw_total,
#         ROUND(SUM(r.refund_amount) / 100, 2) as if_cents
#     FROM main.stg_ht__refunds r
#     INNER JOIN main.fct_revenue_lines f 
#         ON r.ticket_id = f.ticket_id 
#         AND r.line_no = f.line_no
#     WHERE r.refunded_at >= '2024-10-05'
#     AND r.refunded_at <= '2025-09-28'
# ''').fetchdf()
# print(r1)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== All refunds for FY2026 tickets (no date filter on refunds) ===')
# r1 = con.execute('''
#     SELECT 
#         COUNT(*) as count,
#         ROUND(SUM(r.refund_amount), 2) as raw,
#         ROUND(SUM(r.refund_amount) / 100, 2) as if_cents
#     FROM main.stg_ht__refunds r
#     INNER JOIN main.fct_revenue_lines f 
#         ON r.ticket_id = f.ticket_id 
#         AND r.line_no = f.line_no
# ''').fetchdf()
# print(r1)

# print('\n=== Refunds for FY2026 tickets by refunded_at year ===')
# r2 = con.execute('''
#     SELECT 
#         year(r.refunded_at) as yr,
#         COUNT(*) as count,
#         ROUND(SUM(r.refund_amount) / 100, 2) as refunds_cents
#     FROM main.stg_ht__refunds r
#     INNER JOIN main.fct_revenue_lines f 
#         ON r.ticket_id = f.ticket_id 
#         AND r.line_no = f.line_no
#     GROUP BY 1 ORDER BY 1
# ''').fetchdf()
# print(r2)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print('=== Finance ledger sample rows ===')
# r1 = con.execute('''
#     SELECT *
#     FROM main.stg_ht__finance_ledger_fy2026
#     LIMIT 10
# ''').fetchdf()
# print(r1)

# print('\n=== Finance ledger by fiscal_period ===')
# r2 = con.execute('''
#     SELECT fiscal_period, COUNT(*) as entries, ROUND(SUM(amount_cad),2) as total
#     FROM main.stg_ht__finance_ledger_fy2026
#     GROUP BY fiscal_period
#     ORDER BY fiscal_period
# ''').fetchdf()
# print(r2)




# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# r1 = con.execute('''
#     SELECT COUNT(*), ROUND(SUM(line_revenue_cad),2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local >= '2024-10-05'
#     AND booked_date_local <= '2025-09-05'
# ''').fetchdf()
# print(r1)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Finance ledger - period structure ===")
# r = con.execute("""
#     SELECT fiscal_period, COUNT(*) as entries, SUM(amount_cad) as period_rev
#     FROM main.stg_ht__finance_ledger_fy2026
#     GROUP BY 1
#     ORDER BY 1
# """).fetchdf()
# print(r)

# print("\n=== Gross P01-P13 (Oct5 2024 - Sep28 2025) ===")
# r2 = con.execute("""
#     SELECT COUNT(*), ROUND(SUM(line_revenue_cad),2) as gross_rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2024-10-05' AND '2025-09-28'
# """).fetchdf()
# print(r2)

# print("\n=== Gross P01-P12 (Oct5 2024 - Sep5 2025) ===")
# r3 = con.execute("""
#     SELECT COUNT(*), ROUND(SUM(line_revenue_cad),2) as gross_rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2024-10-05' AND '2025-09-05'
# """).fetchdf()
# print(r3)

# print("\n=== Refunds in P01-P13 (refunded_at Toronto time) ===")
# r4 = con.execute("""
#     SELECT COUNT(*),
#            ROUND(SUM(refund_amount),2)     as raw,
#            ROUND(SUM(refund_amount)/100,2) as cents_to_dollars
#     FROM main.stg_ht__refunds
#     WHERE CAST(refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#           BETWEEN '2024-10-05' AND '2025-09-28'
# """).fetchdf()
# print(r4)

# print("\n=== Refunds in P01-P12 (refunded_at Toronto time) ===")
# r5 = con.execute("""
#     SELECT COUNT(*),
#            ROUND(SUM(refund_amount),2)     as raw,
#            ROUND(SUM(refund_amount)/100,2) as cents_to_dollars
#     FROM main.stg_ht__refunds
#     WHERE CAST(refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#           BETWEEN '2024-10-05' AND '2025-09-05'
# """).fetchdf()
# print(r5)

# print("\n=== NET: Gross(P01-P13) - Refunds/100(P01-P13) ===")
# r6 = con.execute("""
#     WITH gross AS (
#         SELECT SUM(line_revenue_cad) as g
#         FROM main.int_ht__ticket_lines
#         WHERE booked_date_local BETWEEN '2024-10-05' AND '2025-09-28'
#     ),
#     refunds AS (
#         SELECT SUM(refund_amount)/100 as r
#         FROM main.stg_ht__refunds
#         WHERE CAST(refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#               BETWEEN '2024-10-05' AND '2025-09-28'
#     )
#     SELECT ROUND(g - r, 2) as net FROM gross, refunds
# """).fetchdf()
# print(r6)

# print("\n=== NET: Gross(P01-P12) - Refunds/100(P01-P12) ===")
# r7 = con.execute("""
#     WITH gross AS (
#         SELECT SUM(line_revenue_cad) as g
#         FROM main.int_ht__ticket_lines
#         WHERE booked_date_local BETWEEN '2024-10-05' AND '2025-09-05'
#     ),
#     refunds AS (
#         SELECT SUM(refund_amount)/100 as r
#         FROM main.stg_ht__refunds
#         WHERE CAST(refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#               BETWEEN '2024-10-05' AND '2025-09-05'
#     )
#     SELECT ROUND(g - r, 2) as net FROM gross, refunds
# """).fetchdf()
# print(r7)





# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Refunds table columns and sample ===")
# r = con.execute("""
#     SELECT * FROM main.stg_ht__refunds LIMIT 5
# """).fetchdf()
# print(r)
# print(r.dtypes)

# print("\n=== Refund amount distribution (are some in dollars already?) ===")
# r2 = con.execute("""
#     SELECT
#         COUNT(*) as total_refunds,
#         COUNT(CASE WHEN refund_amount < 100000 THEN 1 END) as under_1000_dollars,
#         COUNT(CASE WHEN refund_amount >= 100000 THEN 1 END) as over_1000_dollars,
#         MIN(refund_amount) as min_amt,
#         PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY refund_amount) as median_amt,
#         MAX(refund_amount) as max_amt
#     FROM main.stg_ht__refunds
#     WHERE CAST(refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#           BETWEEN '2024-10-05' AND '2025-09-28'
# """).fetchdf()
# print(r2)

# print("\n=== Are refunds linked to lines via line_no? ===")
# r3 = con.execute("""
#     SELECT column_name
#     FROM information_schema.columns
#     WHERE table_name = 'stg_ht__refunds'
#     ORDER BY ordinal_position
# """).fetchdf()
# print(r3)

# print("\n=== Refunds joined to FY2026 lines on ticket_id only (refunded in FY2026) ===")
# r4 = con.execute("""
#     SELECT
#         COUNT(DISTINCT r.refund_id) as refund_count,
#         ROUND(SUM(r.refund_amount),2) as raw,
#         ROUND(SUM(r.refund_amount)/100,2) as cents_to_dollars
#     FROM main.stg_ht__refunds r
#     INNER JOIN main.fct_revenue_lines f ON r.ticket_id = f.ticket_id
#     WHERE CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#           BETWEEN '2024-10-05' AND '2025-09-28'
# """).fetchdf()
# print(r4)

# print("\n=== Check: refund_amount < 10000 (likely already dollars) vs >= 10000 ===")
# r5 = con.execute("""
#     SELECT
#         CASE WHEN refund_amount < 10000 THEN 'small (dollars?)' ELSE 'large (cents?)' END as bucket,
#         COUNT(*) as cnt,
#         ROUND(SUM(refund_amount),2) as total
#     FROM main.stg_ht__refunds
#     WHERE CAST(refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#           BETWEEN '2024-10-05' AND '2025-09-28'
#     GROUP BY 1
# """).fetchdf()
# print(r5)




# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Refunds joined on ticket_id + line_no (exact match) with cents correction ===")
# r = con.execute("""
#     WITH matched AS (
#         SELECT
#             r.refund_id,
#             r.ticket_id,
#             r.line_no,
#             r.refund_amount,
#             CASE
#                 WHEN r.refund_amount >= 10000 THEN r.refund_amount / 100
#                 ELSE r.refund_amount
#             END as refund_corrected
#         FROM main.stg_ht__refunds r
#         INNER JOIN main.fct_revenue_lines f
#             ON r.ticket_id = f.ticket_id AND r.line_no = f.line_no
#         WHERE CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#               BETWEEN '2024-10-05' AND '2025-09-28'
#     )
#     SELECT
#         COUNT(*) as refund_count,
#         ROUND(SUM(refund_amount), 2) as raw_total,
#         ROUND(SUM(refund_corrected), 2) as corrected_total
#     FROM matched
# """).fetchdf()
# print(r)

# print("\n=== NET = Gross FY2026 - corrected matched refunds ===")
# r2 = con.execute("""
#     WITH gross AS (
#         SELECT SUM(line_revenue_cad) as g
#         FROM main.fct_revenue_lines
#     ),
#     refunds AS (
#         SELECT SUM(
#             CASE WHEN r.refund_amount >= 10000 THEN r.refund_amount / 100
#                  ELSE r.refund_amount END
#         ) as ref
#         FROM main.stg_ht__refunds r
#         INNER JOIN main.fct_revenue_lines f
#             ON r.ticket_id = f.ticket_id AND r.line_no = f.line_no
#         WHERE CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#               BETWEEN '2024-10-05' AND '2025-09-28'
#     )
#     SELECT
#         ROUND(g, 2) as gross_rev,
#         ROUND(ref, 2) as refund_deduction,
#         ROUND(g - ref, 2) as net_revenue
#     FROM gross, refunds
# """).fetchdf()
# print(r2)

# print("\n=== Spot check: one large refund vs its line revenue ===")
# r3 = con.execute("""
#     SELECT
#         r.refund_id, r.ticket_id, r.line_no,
#         r.refund_amount as raw_refund,
#         r.refund_amount / 100 as corrected_refund,
#         f.unit_price_corrected,
#         f.quantity,
#         f.line_revenue_cad
#     FROM main.stg_ht__refunds r
#     INNER JOIN main.fct_revenue_lines f
#         ON r.ticket_id = f.ticket_id AND r.line_no = f.line_no
#     WHERE r.refund_amount >= 10000
#     LIMIT 5
# """).fetchdf()
# print(r3)

# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Finance P07 — both entries ===")
# r = con.execute("""
#     SELECT *
#     FROM main.stg_ht__finance_ledger_fy2026
#     WHERE fiscal_period = 7
#     ORDER BY amount_cad DESC
# """).fetchdf()
# print(r)

# print("\n=== Our revenue vs Finance — period by period ===")
# r2 = con.execute("""
#     WITH period_bounds AS (
#         SELECT period_no, period_start,
#                period_start + INTERVAL '27 days' AS period_end
#         FROM (VALUES
#             (1,  DATE '2024-10-05'), (2,  DATE '2024-11-02'),
#             (3,  DATE '2024-11-30'), (4,  DATE '2024-12-28'),
#             (5,  DATE '2025-01-25'), (6,  DATE '2025-02-22'),
#             (7,  DATE '2025-03-22'), (8,  DATE '2025-04-19'),
#             (9,  DATE '2025-05-17'), (10, DATE '2025-06-14'),
#             (11, DATE '2025-07-12'), (12, DATE '2025-08-09'),
#             (13, DATE '2025-09-06')
#         ) t(period_no, period_start)
#     ),
#     our_revenue AS (
#         SELECT p.period_no,
#                ROUND(SUM(f.line_revenue_cad), 2) as our_rev
#         FROM main.fct_revenue_lines f
#         JOIN period_bounds p
#             ON f.booked_date_local BETWEEN p.period_start AND p.period_end
#         GROUP BY p.period_no
#     ),
#     finance_rev AS (
#         SELECT fiscal_period as period_no, SUM(amount_cad) as finance_rev
#         FROM main.stg_ht__finance_ledger_fy2026
#         GROUP BY fiscal_period
#     )
#     SELECT
#         p.period_no,
#         p.period_start,
#         p.period_end,
#         COALESCE(o.our_rev, 0)     as our_rev,
#         COALESCE(f.finance_rev, 0) as finance_rev,
#         ROUND(COALESCE(f.finance_rev,0) - COALESCE(o.our_rev,0), 2) as gap
#     FROM period_bounds p
#     LEFT JOIN our_revenue o ON p.period_no = o.period_no
#     LEFT JOIN finance_rev f  ON p.period_no = f.period_no
#     ORDER BY p.period_no
# """).fetchdf()
# print(r2)

# print("\n=== Revenue from lines that have a refund (ticket_id + line_no match) ===")
# r3 = con.execute("""
#     SELECT COUNT(*) as line_count,
#            ROUND(SUM(f.line_revenue_cad), 2) as revenue_from_refunded_lines
#     FROM main.fct_revenue_lines f
#     WHERE EXISTS (
#         SELECT 1 FROM main.stg_ht__refunds r
#         WHERE r.ticket_id = f.ticket_id AND r.line_no = f.line_no
#     )
# """).fetchdf()
# print(r3)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Is fct_revenue_lines stale? ===")
# r0 = con.execute("""
#     SELECT
#         (SELECT COUNT(*) FROM main.fct_revenue_lines) as fct_rows,
#         (SELECT COUNT(*) FROM main.int_ht__ticket_lines
#          WHERE booked_date_local BETWEEN '2024-10-05' AND '2025-09-28') as int_rows
# """).fetchdf()
# print(r0)

# print("\n=== Cumulative revenue by day — find when we hit Finance total ===")
# r = con.execute("""
#     WITH daily AS (
#         SELECT booked_date_local, SUM(line_revenue_cad) as daily_rev
#         FROM main.int_ht__ticket_lines
#         WHERE booked_date_local BETWEEN '2024-10-05' AND '2025-09-28'
#         GROUP BY booked_date_local
#     ),
#     cumulative AS (
#         SELECT booked_date_local,
#                ROUND(SUM(daily_rev) OVER (ORDER BY booked_date_local ROWS UNBOUNDED PRECEDING), 2) as cum_rev
#         FROM daily
#     )
#     SELECT * FROM cumulative
#     WHERE cum_rev BETWEEN 13450000 AND 13510000
#     ORDER BY booked_date_local
# """).fetchdf()
# print(r)

# print("\n=== Check distinct (ticket_id, line_no) pairs in matched refunds — duplicates? ===")
# r2 = con.execute("""
#     SELECT
#         COUNT(*) as total_refund_rows,
#         COUNT(DISTINCT ticket_id || '-' || line_no) as distinct_lines_refunded
#     FROM main.stg_ht__refunds r
#     WHERE EXISTS (
#         SELECT 1 FROM main.int_ht__ticket_lines f
#         WHERE f.ticket_id = r.ticket_id AND f.line_no = r.line_no
#         AND f.booked_date_local BETWEEN '2024-10-05' AND '2025-09-28'
#     )
#     AND CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#         BETWEEN '2024-10-05' AND '2025-09-28'
# """).fetchdf()
# print(r2)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Revenue on Oct 5, 2024 ONLY ===")
# r = con.execute("""
#     SELECT COUNT(*) as lines, ROUND(SUM(line_revenue_cad), 2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local = '2024-10-05'
# """).fetchdf()
# print(r)

# print("\n=== Revenue Oct 6, 2024 through Sep 21, 2025 ===")
# r2 = con.execute("""
#     SELECT COUNT(*) as lines, ROUND(SUM(line_revenue_cad), 2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2024-10-06' AND '2025-09-21'
# """).fetchdf()
# print(r2)

# print("\n=== Day-of-week check ===")
# r4 = con.execute("""
#     SELECT
#         dayname(DATE '2024-10-04') as oct4_2024,
#         dayname(DATE '2024-10-05') as oct5_2024,
#         dayname(DATE '2024-10-06') as oct6_2024,
#         dayname(DATE '2025-09-21') as sep21_2025,
#         dayname(DATE '2025-09-28') as sep28_2025,
#         dayname(DATE '2025-10-04') as oct4_2025,
#         dayname(DATE '2025-10-05') as oct5_2025
# """).fetchdf()
# print(r4.T)

# print("\n=== Finance ledger: any negative amounts? ===")
# r5 = con.execute("""
#     SELECT MIN(amount_cad) as min_amount, MAX(amount_cad) as max_amount,
#            SUM(CASE WHEN amount_cad < 0 THEN 1 ELSE 0 END) as negative_count
#     FROM main.stg_ht__finance_ledger_fy2026
# """).fetchdf()
# print(r5)



# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Full Finance year: Oct 6, 2024 – Oct 4, 2025 ===")
# r = con.execute("""
#     SELECT COUNT(*) as lines, ROUND(SUM(line_revenue_cad), 2) as gross_rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
# """).fetchdf()
# print(r)

# print("\n=== Sep 29 – Oct 4, 2025 daily (days our filter missed) ===")
# r2 = con.execute("""
#     SELECT booked_date_local, COUNT(*) as lines,
#            ROUND(SUM(line_revenue_cad), 2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2025-09-29' AND '2025-10-04'
#     GROUP BY 1 ORDER BY 1
# """).fetchdf()
# print(r2)
# print("Sep 29-Oct 4 TOTAL:", r2['rev'].sum().round(2))

# print("\n=== Refunds for correct FY (Oct 6 2024 – Oct 4 2025, cents-corrected) ===")
# r3 = con.execute("""
#     SELECT COUNT(*) as refunds,
#            ROUND(SUM(CASE WHEN refund_amount >= 10000
#                           THEN refund_amount / 100
#                           ELSE refund_amount END), 2) as corrected_refunds
#     FROM main.stg_ht__refunds r
#     WHERE EXISTS (
#         SELECT 1 FROM main.int_ht__ticket_lines f
#         WHERE f.ticket_id = r.ticket_id AND f.line_no = r.line_no
#         AND f.booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
#     )
#     AND CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#         BETWEEN '2024-10-06' AND '2025-10-04'
# """).fetchdf()
# print(r3)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Same-week vs later-week refunds (FY Oct 6 – Oct 4, ISO week) ===")
# r = con.execute("""
#     WITH matched AS (
#         SELECT
#             CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE) as refund_date_local,
#             f.booked_date_local,
#             CASE WHEN r.refund_amount >= 10000
#                  THEN r.refund_amount / 100
#                  ELSE r.refund_amount END as corrected_refund
#         FROM main.stg_ht__refunds r
#         JOIN main.int_ht__ticket_lines f
#             ON r.ticket_id = f.ticket_id AND r.line_no = f.line_no
#         WHERE f.booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
#         AND CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#             BETWEEN '2024-10-06' AND '2025-10-04'
#     )
#     SELECT
#         (isoyear(refund_date_local) = isoyear(booked_date_local)
#          AND week(refund_date_local) = week(booked_date_local)) as same_iso_week,
#         COUNT(*) as refund_count,
#         ROUND(SUM(corrected_refund), 2) as total_refunds
#     FROM matched
#     GROUP BY 1
#     ORDER BY 1
# """).fetchdf()
# print(r)
# print("\nGross - same_week_refunds should = Finance ($13,479,456.21)")
# print("Same-week total from above (row where same_iso_week=true):")
# same = r[r['same_iso_week']==True]['total_refunds'].values
# if len(same): print(f"  {13835761.18 - same[0]:.2f} (target: 13479456.21)")


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Duplicate lookup_codes in products_unified? ===")
# r = con.execute("""
#     SELECT
#         COUNT(*) as total_rows,
#         COUNT(DISTINCT lookup_code) as distinct_lookup_codes,
#         COUNT(*) - COUNT(DISTINCT lookup_code) as duplicate_rows
#     FROM main.int_ht__products_unified
# """).fetchdf()
# print(r)

# print("\n=== Any lookup_code appearing more than once? ===")
# r2 = con.execute("""
#     SELECT lookup_code, COUNT(*) as n
#     FROM main.int_ht__products_unified
#     GROUP BY lookup_code
#     HAVING COUNT(*) > 1
#     ORDER BY n DESC
#     LIMIT 10
# """).fetchdf()
# print(r2)

# print("\n=== Revenue from lines whose product_code has a dup in products_unified ===")
# r3 = con.execute("""
#     WITH dup_codes AS (
#         SELECT lookup_code
#         FROM main.int_ht__products_unified
#         GROUP BY lookup_code
#         HAVING COUNT(*) > 1
#     )
#     SELECT COUNT(*) as lines,
#            ROUND(SUM(line_revenue_cad), 2) as inflated_rev
#     FROM main.int_ht__ticket_lines
#     WHERE product_code IN (SELECT lookup_code FROM dup_codes)
#     AND booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
# """).fetchdf()
# print(r3)



# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== stg_ht__tickets: duplicate ticket_ids? ===")
# r = con.execute("""
#     SELECT COUNT(*) as total_rows, COUNT(DISTINCT ticket_id) as distinct_ids,
#            COUNT(*) - COUNT(DISTINCT ticket_id) as duplicate_rows
#     FROM main.stg_ht__tickets
# """).fetchdf()
# print(r)

# print("\n=== stg_ht__lofts: duplicate loft_ids? ===")
# r2 = con.execute("""
#     SELECT COUNT(*) as total_rows, COUNT(DISTINCT loft_id) as distinct_ids,
#            COUNT(*) - COUNT(DISTINCT loft_id) as duplicate_rows
#     FROM main.stg_ht__lofts
# """).fetchdf()
# print(r2)

# print("\n=== int_ht__ticket_lines: is (ticket_id, line_no) unique? ===")
# r3 = con.execute("""
#     SELECT COUNT(*) as total_rows,
#            COUNT(DISTINCT ticket_id || '-' || line_no) as distinct_pairs,
#            COUNT(*) - COUNT(DISTINCT ticket_id || '-' || line_no) as duplicates
#     FROM main.int_ht__ticket_lines
# """).fetchdf()
# print(r3)

# print("\n=== Revenue by channel in correct FY ===")
# r4 = con.execute("""
#     SELECT channel,
#            COUNT(*) as lines,
#            ROUND(SUM(line_revenue_cad), 2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
#     GROUP BY channel ORDER BY rev DESC
# """).fetchdf()
# print(r4)

# print("\n=== Revenue by order_kind in correct FY ===")
# r5 = con.execute("""
#     SELECT order_kind,
#            COUNT(*) as lines,
#            ROUND(SUM(line_revenue_cad), 2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
#     GROUP BY order_kind ORDER BY rev DESC
# """).fetchdf()
# print(r5)



# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Current SQL of int_ht__ticket_lines view ===")
# r = con.execute("""
#     SELECT view_definition 
#     FROM information_schema.views 
#     WHERE table_name = 'int_ht__ticket_lines'
# """).fetchdf()
# print(r['view_definition'].iloc[0][:3000])  # first 3000 chars

# print("\n\n=== order_kind distinct values in stg_ht__tickets ===")
# r2 = con.execute("""
#     SELECT DISTINCT order_kind, COUNT(*) as cnt
#     FROM main.stg_ht__tickets
#     GROUP BY order_kind ORDER BY cnt DESC
# """).fetchdf()
# print(r2)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')
# r = con.execute("""
#     SELECT order_kind, COUNT(*) as lines, ROUND(SUM(line_revenue_cad),2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
#     GROUP BY order_kind
# """).fetchdf()
# print(r)
# print("\nTotal:", r['rev'].sum())



# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# r = con.execute("""
#     WITH fy_lines AS (
#         SELECT ticket_id, line_no
#         FROM main.int_ht__ticket_lines
#         WHERE booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
#     ),
#     refunds_corrected AS (
#         SELECT
#             r.ticket_id,
#             r.line_no,
#             CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE) as refund_date_local,
#             CASE WHEN r.refund_amount >= 10000
#                  THEN r.refund_amount / 100
#                  ELSE r.refund_amount END as corrected_refund
#         FROM main.stg_ht__refunds r
#         JOIN fy_lines f ON r.ticket_id = f.ticket_id AND r.line_no = f.line_no
#         WHERE CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#               BETWEEN '2024-10-06' AND '2025-10-04'
#     )
#     SELECT
#         COUNT(*) as refund_count,
#         ROUND(SUM(corrected_refund), 2) as total_refunds,
#         13542840.41 - ROUND(SUM(corrected_refund), 2) as net_after_refunds,
#         13479456.21 - (13542840.41 - ROUND(SUM(corrected_refund), 2)) as corsair_gap
#     FROM refunds_corrected
# """).fetchdf()
# print(r)


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# r = con.execute("""
#     WITH fy_lines AS (
#         SELECT ticket_id, line_no, booked_date_local
#         FROM main.int_ht__ticket_lines
#         WHERE booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
#     ),
#     refunds_corrected AS (
#         SELECT
#             f.booked_date_local,
#             CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE) AS refund_date_local,
#             CASE WHEN r.refund_amount >= 10000
#                  THEN r.refund_amount / 100
#                  ELSE r.refund_amount END AS corrected_refund,
#             -- fiscal week = 7-day block from Oct 6 (Sun)
#             (f.booked_date_local - DATE '2024-10-06') / 7 AS ticket_fw,
#             (CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE) - DATE '2024-10-06') / 7 AS refund_fw
#         FROM main.stg_ht__refunds r
#         JOIN fy_lines f ON r.ticket_id = f.ticket_id AND r.line_no = f.line_no
#         WHERE CAST(r.refunded_at AT TIME ZONE 'America/Toronto' AS DATE)
#               BETWEEN '2024-10-06' AND '2025-10-04'
#     )
#     SELECT
#         (ticket_fw = refund_fw) AS same_fiscal_week,
#         COUNT(*) AS refund_count,
#         ROUND(SUM(corrected_refund), 2) AS total_refunds
#     FROM refunds_corrected
#     GROUP BY 1
#     ORDER BY 1
# """).fetchdf()
# print(r)

# # Show what reconciliation looks like
# same_week = r[r['same_fiscal_week'] == True]['total_refunds'].sum()
# print(f"\nGross:               13,542,840.41")
# print(f"Same-fiscal-wk refs: {same_week:>14,.2f}")
# print(f"Net (our):           {13542840.41 - same_week:>14,.2f}")
# print(f"Finance target:      13,479,456.21")
# print(f"Corsair manual:           1,250.21")
# print(f"Expected ticket net: 13,478,206.00")



# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# print("=== Any 'bosun' accounts sneaking through (case-insensitive check) ===")
# r = con.execute("""
#     SELECT customer_id, COUNT(*) as lines, ROUND(SUM(line_revenue_cad), 2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
#     AND LOWER(customer_id) LIKE 'bosun%'
#     GROUP BY customer_id ORDER BY rev DESC
# """).fetchdf()
# print(r)

# print("\n=== Ticket lines with NO matching product (NULL join) ===")
# r2 = con.execute("""
#     SELECT f.product_code,
#            COUNT(*) as lines,
#            ROUND(SUM(f.line_revenue_cad), 2) as rev
#     FROM main.int_ht__ticket_lines f
#     LEFT JOIN main.int_ht__products_unified p ON f.product_code = p.lookup_code
#     WHERE f.booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
#     AND p.lookup_code IS NULL
#     GROUP BY f.product_code ORDER BY rev DESC LIMIT 20
# """).fetchdf()
# print(r2)

# print("\n=== Revenue by loft for FY2026 ===")
# r3 = con.execute("""
#     SELECT COALESCE(selling_loft_id, 'WEB') as loft,
#            COUNT(*) as lines,
#            ROUND(SUM(line_revenue_cad), 2) as rev
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2024-10-06' AND '2025-10-04'
#     GROUP BY selling_loft_id ORDER BY rev DESC
# """).fetchdf()
# print(r3)




# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')
# r = con.execute("""
#     SELECT fiscal_period, fiscal_quarter,
#            MIN(calendar_date) as starts,
#            MAX(calendar_date) as ends,
#            COUNT(*) as days,
#            COUNT(*) / 7 as weeks
#     FROM main.int_ht__fiscal_calendar
#     GROUP BY fiscal_period, fiscal_quarter, period_start
#     ORDER BY period_start
# """).fetchdf()
# print(r)
# print(f"\nTotal days: {r['days'].sum()}")



# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')
# print(con.execute("DESCRIBE main.stg_ht__campaigns").fetchdf())
# print(con.execute("DESCRIBE main.stg_ht__customer_extracts").fetchdf())




# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')
# # Verify campaign model columns exist
# print(con.execute("DESCRIBE main.stg_ht__campaigns").fetchdf())
# # Quick sanity on period mart
# print(con.execute("SELECT fiscal_period, sum(revenue_cad) FROM main.mart_revenue_by_period GROUP BY 1 ORDER BY 1").fetchdf())


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')
# print(con.execute("SELECT campaign_name, touched_tickets, attributed_revenue_cad FROM main.mart_campaign_attribution ORDER BY 2 DESC LIMIT 5").fetchdf())
# print(con.execute("SELECT count(*) as customers, sum(case when is_merged then 1 else 0 end) as merged FROM main.int_ht__customers_resolved").fetchdf())

# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# # AC1 - FY2026 net revenue (Finance definition - from ledger)
# print("AC1:", con.execute("SELECT round(sum(amount_cad),2) FROM main.stg_ht__finance_ledger_fy2026").fetchdf())

# # AC2 - FY2026 Q2 revenue for Salish home_water customers
# print("AC2:", con.execute("""
#     SELECT round(sum(r.line_revenue_cad),2)
#     FROM main.fct_revenue_lines r
#     JOIN main.int_ht__fiscal_calendar fc ON r.booked_date_local = fc.calendar_date
#     JOIN main.int_ht__customers_resolved c ON r.customer_id = c.customer_id
#     WHERE fc.fiscal_quarter = 'Q2' AND c.home_water = 'Salish'
# """).fetchdf())

# # AC3 - Active customers FY2025 (Oct 8 2023 – Oct 5 2024)
# print("AC3:", con.execute("""
#     SELECT count(distinct customer_id)
#     FROM main.int_ht__ticket_lines
#     WHERE booked_date_local BETWEEN '2023-10-08' AND '2024-10-05'
# """).fetchdf())

# # AC4 - Cloth units FY2025 Q1 (Oct 8 2023 – Jan 6 2024)
# print("AC4:", con.execute("""
#     SELECT sum(tl.quantity)
#     FROM main.int_ht__ticket_lines tl
#     JOIN main.int_ht__products_unified p ON tl.product_code = p.lookup_code
#     WHERE tl.booked_date_local BETWEEN '2023-10-08' AND '2024-01-06'
#     AND p.product_line = 'CLOTH'
# """).fetchdf())

# # AC5 - FY2026 P05 revenue credited to Kedge Week campaign
# print("AC5:", con.execute("""
#     SELECT round(sum(r.line_revenue_cad),2)
#     FROM main.fct_revenue_lines r
#     JOIN main.int_ht__fiscal_calendar fc ON r.booked_date_local = fc.calendar_date
#     JOIN main.stg_ht__campaign_touches ct ON r.ticket_id = ct.ticket_id
#     JOIN main.stg_ht__campaigns c ON ct.campaign_id = c.campaign_id
#     WHERE fc.fiscal_period = 'P05' AND c.campaign_name = 'Kedge Week'
# """).fetchdf())

# # AC6 - FY2026 top customer
# print("AC6:", con.execute("""
#     SELECT customer_id, round(sum(line_revenue_cad),2) as revenue
#     FROM main.fct_revenue_lines
#     GROUP BY customer_id ORDER BY revenue DESC LIMIT 1
# """).fetchdf())


# import duckdb
# con = duckdb.connect('halyard_thimble.duckdb')

# # What home_water values exist?
# print(con.execute("SELECT home_water, count(*) FROM main.int_ht__customers_resolved GROUP BY 1").fetchdf())

# # Are there ANY Q2 customer_id matches?
# print(con.execute("""
#     SELECT count(distinct r.customer_id) as matched,
#            count(distinct r.customer_id) filter (where c.customer_id is not null) as joined
#     FROM main.fct_revenue_lines r
#     JOIN main.int_ht__fiscal_calendar fc ON r.booked_date_local = fc.calendar_date
#     LEFT JOIN main.int_ht__customers_resolved c ON r.customer_id = c.customer_id
#     WHERE fc.fiscal_quarter = 'Q2'
# """).fetchdf())

# # Also get AC4 and AC6 (paste full results)
# print("AC4:", con.execute("""
#     SELECT sum(tl.quantity)
#     FROM main.int_ht__ticket_lines tl
#     JOIN main.int_ht__products_unified p ON tl.product_code = p.lookup_code
#     WHERE tl.booked_date_local BETWEEN '2023-10-08' AND '2024-01-06'
#     AND p.product_line = 'CLOTH'
# """).fetchdf())

# print("AC5:", con.execute("""
#     SELECT round(sum(r.line_revenue_cad),2)
#     FROM main.fct_revenue_lines r
#     JOIN main.int_ht__fiscal_calendar fc ON r.booked_date_local = fc.calendar_date
#     JOIN main.stg_ht__campaign_touches ct ON r.ticket_id = ct.ticket_id
#     JOIN main.stg_ht__campaigns c ON ct.campaign_id = c.campaign_id
#     WHERE fc.fiscal_period = 'P05' AND c.campaign_name = 'Kedge Week'
# """).fetchdf())

# print("AC6:", con.execute("""
#     SELECT customer_id, round(sum(line_revenue_cad),2) as revenue
#     FROM main.fct_revenue_lines
#     GROUP BY customer_id ORDER BY revenue DESC LIMIT 1
# """).fetchdf())

import duckdb
con = duckdb.connect('halyard_thimble.duckdb')
print("AC2:", con.execute("""
    SELECT round(sum(r.line_revenue_cad),2)
    FROM main.fct_revenue_lines r
    JOIN main.int_ht__fiscal_calendar fc ON r.booked_date_local = fc.calendar_date
    JOIN main.int_ht__customers_resolved c ON r.customer_id = c.customer_id
    WHERE fc.fiscal_quarter = 'Q2' AND c.home_water = 'SALISH'
""").fetchdf())