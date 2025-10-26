import requests
import threading
import random
import time
from concurrent.futures import ThreadPoolExecutor
import argparse

class LoadTester:
    def __init__(self, target_url, num_threads=10, requests_per_thread=100):
        self.target_url = target_url
        self.num_threads = num_threads
        self.requests_per_thread = requests_per_thread
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15'
        ]
        
    def random_request(self):
        """Send a random request with varied parameters"""
        try:
            headers = {
                'User-Agent': random.choice(self.user_agents),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
            }
            
            # Vary request methods
            methods = ['GET', 'POST']
            method = random.choice(methods)
            
            if method == 'GET':
                response = requests.get(self.target_url, headers=headers, timeout=10)
            else:
                response = requests.post(self.target_url, headers=headers, timeout=10, data={'test': 'data'})
            
            print(f"Status: {response.status_code}, Method: {method}")
            
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
    
    def run_test(self):
        """Run the load test"""
        print(f"Starting load test on {self.target_url}")
        print(f"Threads: {self.num_threads}, Requests per thread: {self.requests_per_thread}")
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            for _ in range(self.num_threads):
                for _ in range(self.requests_per_thread):
                    executor.submit(self.random_request)
                    # Small random delay between requests
                    time.sleep(random.uniform(0.1, 0.5))
        
        end_time = time.time()
        print(f"Test completed in {end_time - start_time:.2f} seconds")

def main():
    parser = argparse.ArgumentParser(description='Load Testing Tool')
    parser.add_argument('url', help='Target URL to test')
    parser.add_argument('--threads', type=int, default=10, help='Number of concurrent threads')
    parser.add_argument('--requests', type=int, default=100, help='Requests per thread')
    
    args = parser.parse_args()
    
    # Validate URL format
    if not args.url.startswith(('http://', 'https://')):
        args.url = 'http://' + args.url
    
    tester = LoadTester(args.url, args.threads, args.requests)
    tester.run_test()

if __name__ == "__main__":
    main()