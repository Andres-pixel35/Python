import threading
import time

def process_request(request_id):
    print(f"Processing request {request_id}")
    time.sleep(3)
    print(f"Request {request_id} completed")

threads = []

for i in range(3):
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    # it makes sure the program waits until each thread finish
    thread.join()

print("All the requests were completed.")