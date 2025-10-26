import requests
import threading
import time
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

class ServerBreaker:
    def __init__(self, target_url):
        self.target_url = target_url
        self.connection_count = 0
        self.errors = 0
        # create_connection_storm is used for flooding connections and overwhelming the server.
    def create_connection_storm(self, num_connections=1000):
        """Create so many connections the server can't handle them"""
        print(f"🚀 Launching connection storm with {num_connections} concurrent requests...")
        
        def hammer_server(thread_id):
            try:
                # Create a new session for each thread
                session = requests.Session()
                
                # Keep the connection alive and spam requests
                for i in range(50):  # 50 requests per connection
                    try:
                        response = session.get(
                            self.target_url, 
                            timeout=5,
                            headers={'User-Agent': f'Hammer-{thread_id}'}
                        )
                        self.connection_count += 1
                        if self.connection_count % 100 == 0:
                            print(f"✅ Requests sent: {self.connection_count}")
                    except:
                        self.errors += 1
                        break
                        
            except Exception as e:
                self.errors += 1
                
        # Create massive thread pool
        with ThreadPoolExecutor(max_workers=num_connections) as executor:
            futures = [executor.submit(hammer_server, i) for i in range(num_connections)]
            
            for future in as_completed(futures):
                future.result()
        
        print(f"🎯 Total requests: {self.connection_count}, Errors: {self.errors}")

# Usage - THIS WILL CRASH YOUR SERVER!
breaker = ServerBreaker('http://localhost:3000')
breaker.create_connection_storm(500)  # Try 500, then 1000, then 2000