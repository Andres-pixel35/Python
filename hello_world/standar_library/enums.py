from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3

def check_status(status: OrderStatus):
    if status == OrderStatus.PENDING:
        return "Order is still pending"
    elif status == OrderStatus.SHIPPED:
        return "The order has been shipped"
    elif status == OrderStatus.DELIVERED:
        return "The order has been delivered"
    
print(check_status(OrderStatus.DELIVERED))