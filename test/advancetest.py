import requests
import random
import time
import threading
from urllib.parse import urljoin

class AdvancedLoadTester:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        ]
        
        self.endpoints = ['/', '/about', '/contact', '/projects']
        
    def simulate_user_session(self, session_id):
        """Simulate a more realistic user session"""
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
        }
        
        try:
            # Simulate browsing pattern
            for endpoint in random.sample(self.endpoints, random.randint(2, 4)):
                url = urljoin(self.base_url, endpoint)
                
                # Add random think time
                time.sleep(random.uniform(1, 3))
                
                response = self.session.get(url, headers=headers, timeout=15)
                print(f"Session {session_id}: {response.status_code} - {url}")
                
        except Exception as e:
            print(f"Session {session_id} error: {e}")
    
    def run_concurrent_sessions(self, num_sessions=5):
        """Run multiple concurrent user sessions"""
        threads = []
        
        for i in range(num_sessions):
            thread = threading.Thread(target=self.simulate_user_session, args=(i,))
            threads.append(thread)
            thread.start()
            # Stagger session starts
            time.sleep(random.uniform(0.5, 2))
        
        for thread in threads:
            thread.join()

# Usage
if __name__ == "__main__":
    # ONLY USE ON YOUR OWN DEVELOPMENT SERVER
    tester = AdvancedLoadTester('http://172.31.204.104:3000')  # Your dev server
    tester.run_concurrent_sessions(num_sessions=10)