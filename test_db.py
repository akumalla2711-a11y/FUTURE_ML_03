import os
import sys

# Test the correct aws-1 pooler URL
url = "postgresql://postgres.vyyzjekdzmqpjmymxdwd:1YimhMDgp7aQUA9O@aws-1-us-west-2.pooler.supabase.com:6543/postgres"

print("Testing Supabase Database Connection to the correct aws-1 Pooler...")
print("--------------------------------------------------")

try:
    import psycopg2
    conn = psycopg2.connect(url, connect_timeout=5)
    print("SUCCESS: Connected to Supabase via aws-1 Shared Pooler!")
    conn.close()
except Exception as e:
    print(f"FAILED: {str(e).strip()}")

print("\n--------------------------------------------------")
print("Test completed.")
