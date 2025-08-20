from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_all": users_all},
    }
    return res


async def get_users_user_id(db: Session, user_id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.user_id == user_id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_one": users_one},
    }
    return res


async def put_users_user_id(db: Session, raw_data: schemas.PutUsersUserId):
    user_id: int = raw_data.user_id
    name: str = raw_data.name
    email: str = raw_data.email
    phone: str = raw_data.phone
    password: str = raw_data.password
    role: str = raw_data.role

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.user_id == user_id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "name": name,
            "role": role,
            "email": email,
            "phone": phone,
            "user_id": user_id,
            "password": password,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_edited_record": users_edited_record},
    }
    return res


async def delete_users_user_id(db: Session, user_id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.user_id == user_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_deleted": users_deleted},
    }
    return res


async def get_merchants(db: Session):

    query = db.query(models.Merchants)

    merchants_all = query.all()
    merchants_all = (
        [new_data.to_dict() for new_data in merchants_all]
        if merchants_all
        else merchants_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"merchants_all": merchants_all},
    }
    return res


async def get_merchants_merchant_id(db: Session, merchant_id: int):

    query = db.query(models.Merchants)
    query = query.filter(and_(models.Merchants.merchant_id == merchant_id))

    merchants_one = query.first()

    merchants_one = (
        (
            merchants_one.to_dict()
            if hasattr(merchants_one, "to_dict")
            else vars(merchants_one)
        )
        if merchants_one
        else merchants_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"merchants_one": merchants_one},
    }
    return res


async def post_merchants(db: Session, raw_data: schemas.PostMerchants):
    name: str = raw_data.name
    address: str = raw_data.address
    phone: str = raw_data.phone
    owner_id: int = raw_data.owner_id

    record_to_be_added = {
        "name": name,
        "phone": phone,
        "address": address,
        "owner_id": owner_id,
    }
    new_merchants = models.Merchants(**record_to_be_added)
    db.add(new_merchants)
    db.commit()
    db.refresh(new_merchants)
    merchants_inserted_record = new_merchants.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"merchants_inserted_record": merchants_inserted_record},
    }
    return res


async def put_merchants_merchant_id(
    db: Session, raw_data: schemas.PutMerchantsMerchantId
):
    merchant_id: int = raw_data.merchant_id
    name: str = raw_data.name
    address: str = raw_data.address
    phone: str = raw_data.phone
    owner_id: int = raw_data.owner_id

    query = db.query(models.Merchants)
    query = query.filter(and_(models.Merchants.merchant_id == merchant_id))
    merchants_edited_record = query.first()

    if merchants_edited_record:
        for key, value in {
            "name": name,
            "phone": phone,
            "address": address,
            "owner_id": owner_id,
            "merchant_id": merchant_id,
        }.items():
            setattr(merchants_edited_record, key, value)

        db.commit()
        db.refresh(merchants_edited_record)

        merchants_edited_record = (
            merchants_edited_record.to_dict()
            if hasattr(merchants_edited_record, "to_dict")
            else vars(merchants_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"merchants_edited_record": merchants_edited_record},
    }
    return res


async def delete_merchants_merchant_id(db: Session, merchant_id: int):

    query = db.query(models.Merchants)
    query = query.filter(and_(models.Merchants.merchant_id == merchant_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        merchants_deleted = record_to_delete.to_dict()
    else:
        merchants_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"merchants_deleted": merchants_deleted},
    }
    return res


async def get_orders(db: Session):

    query = db.query(models.Orders)

    orders_all = query.all()
    orders_all = (
        [new_data.to_dict() for new_data in orders_all] if orders_all else orders_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"orders_all": orders_all},
    }
    return res


async def get_products(db: Session):

    query = db.query(models.Products)

    products_all = query.all()
    products_all = (
        [new_data.to_dict() for new_data in products_all]
        if products_all
        else products_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"products_all": products_all},
    }
    return res


async def get_products_product_id(db: Session, product_id: int):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.product_id == product_id))

    products_one = query.first()

    products_one = (
        (
            products_one.to_dict()
            if hasattr(products_one, "to_dict")
            else vars(products_one)
        )
        if products_one
        else products_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"products_one": products_one},
    }
    return res


async def post_products(db: Session, raw_data: schemas.PostProducts):
    merchant_id: int = raw_data.merchant_id
    name: str = raw_data.name
    price: str = raw_data.price
    available: bool = raw_data.available

    record_to_be_added = {
        "name": name,
        "price": price,
        "available": available,
        "merchant_id": merchant_id,
    }
    new_products = models.Products(**record_to_be_added)
    db.add(new_products)
    db.commit()
    db.refresh(new_products)
    products_inserted_record = new_products.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"products_inserted_record": products_inserted_record},
    }
    return res


async def put_products_product_id(db: Session, raw_data: schemas.PutProductsProductId):
    product_id: int = raw_data.product_id
    merchant_id: int = raw_data.merchant_id
    name: str = raw_data.name
    price: str = raw_data.price
    available: bool = raw_data.available

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.product_id == product_id))
    products_edited_record = query.first()

    if products_edited_record:
        for key, value in {
            "name": name,
            "price": price,
            "available": available,
            "product_id": product_id,
            "merchant_id": merchant_id,
        }.items():
            setattr(products_edited_record, key, value)

        db.commit()
        db.refresh(products_edited_record)

        products_edited_record = (
            products_edited_record.to_dict()
            if hasattr(products_edited_record, "to_dict")
            else vars(products_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"products_edited_record": products_edited_record},
    }
    return res


async def delete_products_product_id(db: Session, product_id: int):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.product_id == product_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        products_deleted = record_to_delete.to_dict()
    else:
        products_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"products_deleted": products_deleted},
    }
    return res


async def get_orders_order_id(db: Session, order_id: int):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.order_id == order_id))

    orders_one = query.first()

    orders_one = (
        (orders_one.to_dict() if hasattr(orders_one, "to_dict") else vars(orders_one))
        if orders_one
        else orders_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"orders_one": orders_one},
    }
    return res


async def post_orders(db: Session, raw_data: schemas.PostOrders):
    user_id: int = raw_data.user_id
    merchant_id: int = raw_data.merchant_id
    rider_id: int = raw_data.rider_id
    total_amount: str = raw_data.total_amount
    status: str = raw_data.status
    created_at: datetime.datetime = raw_data.created_at

    record_to_be_added = {
        "status": status,
        "user_id": user_id,
        "rider_id": rider_id,
        "created_at": created_at,
        "merchant_id": merchant_id,
        "total_amount": total_amount,
    }
    new_orders = models.Orders(**record_to_be_added)
    db.add(new_orders)
    db.commit()
    db.refresh(new_orders)
    orders_inserted_record = new_orders.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"orders_inserted_record": orders_inserted_record},
    }
    return res


async def put_orders_order_id(db: Session, raw_data: schemas.PutOrdersOrderId):
    order_id: int = raw_data.order_id
    user_id: int = raw_data.user_id
    merchant_id: int = raw_data.merchant_id
    rider_id: int = raw_data.rider_id
    total_amount: str = raw_data.total_amount
    status: str = raw_data.status
    created_at: datetime.datetime = raw_data.created_at

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.order_id == order_id))
    orders_edited_record = query.first()

    if orders_edited_record:
        for key, value in {
            "status": status,
            "user_id": user_id,
            "order_id": order_id,
            "rider_id": rider_id,
            "created_at": created_at,
            "merchant_id": merchant_id,
            "total_amount": total_amount,
        }.items():
            setattr(orders_edited_record, key, value)

        db.commit()
        db.refresh(orders_edited_record)

        orders_edited_record = (
            orders_edited_record.to_dict()
            if hasattr(orders_edited_record, "to_dict")
            else vars(orders_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"orders_edited_record": orders_edited_record},
    }
    return res


async def delete_orders_order_id(db: Session, order_id: int):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.order_id == order_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        orders_deleted = record_to_delete.to_dict()
    else:
        orders_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"orders_deleted": orders_deleted},
    }
    return res


async def get_order_items(db: Session):

    query = db.query(models.OrderItems)

    order_items_all = query.all()
    order_items_all = (
        [new_data.to_dict() for new_data in order_items_all]
        if order_items_all
        else order_items_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"order_items_all": order_items_all},
    }
    return res


async def get_order_items_order_item_id(db: Session, order_item_id: int):

    query = db.query(models.OrderItems)
    query = query.filter(and_(models.OrderItems.order_item_id == order_item_id))

    order_items_one = query.first()

    order_items_one = (
        (
            order_items_one.to_dict()
            if hasattr(order_items_one, "to_dict")
            else vars(order_items_one)
        )
        if order_items_one
        else order_items_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"order_items_one": order_items_one},
    }
    return res


async def post_order_items(db: Session, raw_data: schemas.PostOrderItems):
    order_id: int = raw_data.order_id
    product_id: int = raw_data.product_id
    quantity: int = raw_data.quantity

    record_to_be_added = {
        "order_id": order_id,
        "quantity": quantity,
        "product_id": product_id,
    }
    new_order_items = models.OrderItems(**record_to_be_added)
    db.add(new_order_items)
    db.commit()
    db.refresh(new_order_items)
    order_items_inserted_record = new_order_items.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"order_items_inserted_record": order_items_inserted_record},
    }
    return res


async def put_order_items_order_item_id(
    db: Session, raw_data: schemas.PutOrderItemsOrderItemId
):
    order_item_id: int = raw_data.order_item_id
    order_id: int = raw_data.order_id
    product_id: int = raw_data.product_id
    quantity: int = raw_data.quantity

    query = db.query(models.OrderItems)
    query = query.filter(and_(models.OrderItems.order_item_id == order_item_id))
    order_items_edited_record = query.first()

    if order_items_edited_record:
        for key, value in {
            "order_id": order_id,
            "quantity": quantity,
            "product_id": product_id,
            "order_item_id": order_item_id,
        }.items():
            setattr(order_items_edited_record, key, value)

        db.commit()
        db.refresh(order_items_edited_record)

        order_items_edited_record = (
            order_items_edited_record.to_dict()
            if hasattr(order_items_edited_record, "to_dict")
            else vars(order_items_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"order_items_edited_record": order_items_edited_record},
    }
    return res


async def delete_order_items_order_item_id(db: Session, order_item_id: int):

    query = db.query(models.OrderItems)
    query = query.filter(and_(models.OrderItems.order_item_id == order_item_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        order_items_deleted = record_to_delete.to_dict()
    else:
        order_items_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"order_items_deleted": order_items_deleted},
    }
    return res


async def post_login_user(db: Session, raw_data: schemas.PostLoginUser):
    email: str = raw_data.email
    password: str = raw_data.password

    query = db.query(models.Users)
    query = query.filter(
        and_(models.Users.email == email, models.Users.password == password)
    )

    login_record = query.first()

    login_record = (
        (
            login_record.to_dict()
            if hasattr(login_record, "to_dict")
            else vars(login_record)
        )
        if login_record
        else login_record
    )

    try:
        is_exist_login = bool(login_record)
        is_true = True
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    is_As: bool = is_true

    if is_As == is_exist_login:

        bs_jwt_payload = {
            "exp": int(
                (
                    datetime.datetime.utcnow() + datetime.timedelta(seconds=100000)
                ).timestamp()
            ),
            "data": login_record,
        }

        jwt_secret_keys_login = jwt.encode(
            bs_jwt_payload,
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            algorithm="HS256",
        )

    else:

        raise HTTPException(status_code=401, detail="user not exist")

    res = {
        "status": 200,
        "message": "The request has been successfully processed",
        "data": {"jwt_1": jwt_secret_keys_login, "login": login_record},
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    name: str = raw_data.name
    email: str = raw_data.email
    phone: str = raw_data.phone
    password: str = raw_data.password
    role: str = raw_data.role

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.email == email))

    email_details = query.first()

    email_details = (
        (
            email_details.to_dict()
            if hasattr(email_details, "to_dict")
            else vars(email_details)
        )
        if email_details
        else email_details
    )

    if email == email_details["email"]:

        raise HTTPException(status_code=401, detail="email is already exist")

    record_to_be_added = {
        "name": name,
        "role": role,
        "email": email,
        "phone": phone,
        "password": password,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    bs_jwt_payload = {
        "exp": int(
            (
                datetime.datetime.utcnow() + datetime.timedelta(seconds=100000)
            ).timestamp()
        ),
        "data": users_inserted_record,
    }

    jwt_secret_keys = jwt.encode(
        bs_jwt_payload,
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
        algorithm="HS256",
    )

    res = {
        "status": 200,
        "message": "users created successful",
        "data": {
            "jwt_secret_keys": jwt_secret_keys,
            "users_inserted_record": users_inserted_record,
        },
    }
    return res
