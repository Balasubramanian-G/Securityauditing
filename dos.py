import requests
import threading
import time

target_url = "http://localhost:5000" 
num_threads = 100
delay_between_requests = 0.1  
running = True

def send_requests():
    while running:
        try:
            response = requests.get(target_url)
            print(f"[{threading.current_thread().name}] Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[{threading.current_thread().name}] Error: {e}")
        time.sleep(delay_between_requests)
threads = []
print(f"Sending requests to {target_url} using {num_threads} threads. Press Ctrl+C to stop...\n")

try:
    for i in range(num_threads):
        t = threading.Thread(target=send_requests, name=f"Thread-{i+1}")
        t.start()
        threads.append(t)
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\n Stopping all threads")
    running = False
    for t in threads:
        t.join()

    print("All threads stopped program ended.")
