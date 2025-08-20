from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    name: Optional[str]=None
    email: str
    phone: Optional[str]=None
    password: Optional[str]=None
    role: Optional[str]=None


class ReadUsers(BaseModel):
    name: Optional[str]=None
    email: str
    phone: Optional[str]=None
    password: Optional[str]=None
    role: Optional[str]=None
    class Config:
        from_attributes = True


class Merchants(BaseModel):
    name: Optional[str]=None
    address: Optional[str]=None
    phone: Optional[str]=None
    owner_id: Optional[int]=None


class ReadMerchants(BaseModel):
    name: Optional[str]=None
    address: Optional[str]=None
    phone: Optional[str]=None
    owner_id: Optional[int]=None
    class Config:
        from_attributes = True


class Products(BaseModel):
    merchant_id: Optional[int]=None
    name: Optional[str]=None
    price: Optional[Any]=None
    available: Optional[bool]=None


class ReadProducts(BaseModel):
    merchant_id: Optional[int]=None
    name: Optional[str]=None
    price: Optional[Any]=None
    available: Optional[bool]=None
    class Config:
        from_attributes = True


class Orders(BaseModel):
    user_id: Optional[int]=None
    merchant_id: Optional[int]=None
    rider_id: Optional[int]=None
    total_amount: Optional[Any]=None
    status: Optional[str]=None
    created_at: Optional[datetime.time]=None


class ReadOrders(BaseModel):
    user_id: Optional[int]=None
    merchant_id: Optional[int]=None
    rider_id: Optional[int]=None
    total_amount: Optional[Any]=None
    status: Optional[str]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class OrderItems(BaseModel):
    order_id: Optional[int]=None
    product_id: Optional[int]=None
    quantity: Optional[int]=None


class ReadOrderItems(BaseModel):
    order_id: Optional[int]=None
    product_id: Optional[int]=None
    quantity: Optional[int]=None
    class Config:
        from_attributes = True




class PutUsersUserId(BaseModel):
    user_id: Optional[int]=None
    name: Optional[str]=None
    email: Optional[str]=None
    phone: Optional[str]=None
    password: Optional[str]=None
    role: Optional[str]=None

    class Config:
        from_attributes = True



class PostMerchants(BaseModel):
    name: Optional[str]=None
    address: Optional[str]=None
    phone: Optional[str]=None
    owner_id: Optional[int]=None

    class Config:
        from_attributes = True



class PutMerchantsMerchantId(BaseModel):
    merchant_id: Optional[int]=None
    name: Optional[str]=None
    address: Optional[str]=None
    phone: Optional[str]=None
    owner_id: Optional[int]=None

    class Config:
        from_attributes = True



class PostProducts(BaseModel):
    merchant_id: Optional[int]=None
    name: Optional[str]=None
    price: Optional[str]=None
    available: Optional[bool]=None

    class Config:
        from_attributes = True



class PutProductsProductId(BaseModel):
    product_id: Optional[int]=None
    merchant_id: Optional[int]=None
    name: Optional[str]=None
    price: Optional[str]=None
    available: Optional[bool]=None

    class Config:
        from_attributes = True



class PostOrders(BaseModel):
    user_id: Optional[int]=None
    merchant_id: Optional[int]=None
    rider_id: Optional[int]=None
    total_amount: Optional[str]=None
    status: Optional[str]=None
    created_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PutOrdersOrderId(BaseModel):
    order_id: Optional[int]=None
    user_id: Optional[int]=None
    merchant_id: Optional[int]=None
    rider_id: Optional[int]=None
    total_amount: Optional[str]=None
    status: Optional[str]=None
    created_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PostOrderItems(BaseModel):
    order_id: Optional[int]=None
    product_id: Optional[int]=None
    quantity: Optional[int]=None

    class Config:
        from_attributes = True



class PutOrderItemsOrderItemId(BaseModel):
    order_item_id: Optional[int]=None
    order_id: Optional[int]=None
    product_id: Optional[int]=None
    quantity: Optional[int]=None

    class Config:
        from_attributes = True



class PostLoginUser(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    name: Optional[str]=None
    email: Optional[str]=None
    phone: Optional[str]=None
    password: Optional[str]=None
    role: Optional[str]=None

    class Config:
        from_attributes = True

