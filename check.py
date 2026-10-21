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

import duckdb
conn = duckdb.connect()

print("campaigns:")
print(conn.execute("""
    DESCRIBE SELECT * FROM read_csv('data/raw/campaigns.csv', header=true, all_varchar=true)
""").fetchdf())

print("\ncampaign_touches:")
print(conn.execute("""
    DESCRIBE SELECT * FROM read_csv('data/raw/campaign_touches.csv', header=true, all_varchar=true)
""").fetchdf())