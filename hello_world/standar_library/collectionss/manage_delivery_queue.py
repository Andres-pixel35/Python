from collections import deque

def manage_delivery_queue() -> deque:
    delivery_queue = deque(["order_1", "order_2", "order_3"])
    delivery_queue.append("order_4") #add to the final of the queue
    delivery_queue.appendleft("order_0") #add at the beginning of the queue
    delivery_queue.pop() #deletes the final value
    delivery_queue.popleft() #deletes the first value

    return delivery_queue

queue = manage_delivery_queue()
print(queue)