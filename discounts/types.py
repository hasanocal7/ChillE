import typing
import strawberry
from datetime import date

@strawberry.type
class DiscountCouponType:
    code: str
    discount_rate: float
    start_date: date
    end_date: date
    min_order_amount: float