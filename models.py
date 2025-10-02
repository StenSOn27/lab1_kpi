from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional


@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    phone: str
    address: str
    created_at: datetime
    orders: List["Order"] = field(default_factory=list)


@dataclass
class Category:
    category_id: int
    name: str
    products: List["Product"] = field(default_factory=list)


@dataclass
class Product:
    product_id: int
    name: str
    description: str
    price: Decimal
    stock: int
    category: Optional[Category]
    order_items: List["OrderItem"] = field(default_factory=list)


@dataclass
class Order:
    order_id: int
    customer: Optional[Customer]
    order_date: datetime = field(default_factory=datetime.now)
    total: Decimal = Decimal(0)
    items: List["OrderItem"] = field(default_factory=list)


@dataclass
class OrderItem:
    order_item_id: int
    order: Optional[Order]
    product: Optional[Product]
    quantity: int = 1
    price: Decimal = Decimal(0)
