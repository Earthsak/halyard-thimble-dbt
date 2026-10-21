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


import duckdb
conn = duckdb.connect('halyard_thimble.duckdb')

result = conn.execute("""
    SELECT product_code, product_name, list_price_cad
    FROM main.stg_ht__products
    WHERE product_code IN ('HTP-9540', 'HTP-5434', 'HTP-8024')
    OR legacy_code IN ('SL531', 'SL442', 'SL159')
""").fetchdf()
print(result)



# import duckdb
# conn = duckdb.connect('dev.duckdb')
# print(conn.execute("SHOW ALL TABLES").fetchdf())