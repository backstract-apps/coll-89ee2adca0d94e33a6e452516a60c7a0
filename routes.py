from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/user_id')
async def get_users_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_user_id(db, user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/user_id/')
async def put_users_user_id(raw_data: schemas.PutUsersUserId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_user_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/user_id')
async def delete_users_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_user_id(db, user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/merchants/')
async def get_merchants(db: Session = Depends(get_db)):
    try:
        return await service.get_merchants(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/merchants/merchant_id')
async def get_merchants_merchant_id(merchant_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_merchants_merchant_id(db, merchant_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/merchants/')
async def post_merchants(raw_data: schemas.PostMerchants, db: Session = Depends(get_db)):
    try:
        return await service.post_merchants(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/merchants/merchant_id/')
async def put_merchants_merchant_id(raw_data: schemas.PutMerchantsMerchantId, db: Session = Depends(get_db)):
    try:
        return await service.put_merchants_merchant_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/merchants/merchant_id')
async def delete_merchants_merchant_id(merchant_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_merchants_merchant_id(db, merchant_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/orders/')
async def get_orders(db: Session = Depends(get_db)):
    try:
        return await service.get_orders(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/products/')
async def get_products(db: Session = Depends(get_db)):
    try:
        return await service.get_products(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/products/product_id')
async def get_products_product_id(product_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_products_product_id(db, product_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/products/')
async def post_products(raw_data: schemas.PostProducts, db: Session = Depends(get_db)):
    try:
        return await service.post_products(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/products/product_id/')
async def put_products_product_id(raw_data: schemas.PutProductsProductId, db: Session = Depends(get_db)):
    try:
        return await service.put_products_product_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/products/product_id')
async def delete_products_product_id(product_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_products_product_id(db, product_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/orders/order_id')
async def get_orders_order_id(order_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_orders_order_id(db, order_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/orders/')
async def post_orders(raw_data: schemas.PostOrders, db: Session = Depends(get_db)):
    try:
        return await service.post_orders(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/orders/order_id/')
async def put_orders_order_id(raw_data: schemas.PutOrdersOrderId, db: Session = Depends(get_db)):
    try:
        return await service.put_orders_order_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/orders/order_id')
async def delete_orders_order_id(order_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_orders_order_id(db, order_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/order_items/')
async def get_order_items(db: Session = Depends(get_db)):
    try:
        return await service.get_order_items(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/order_items/order_item_id')
async def get_order_items_order_item_id(order_item_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_order_items_order_item_id(db, order_item_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/order_items/')
async def post_order_items(raw_data: schemas.PostOrderItems, db: Session = Depends(get_db)):
    try:
        return await service.post_order_items(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/order_items/order_item_id/')
async def put_order_items_order_item_id(raw_data: schemas.PutOrderItemsOrderItemId, db: Session = Depends(get_db)):
    try:
        return await service.put_order_items_order_item_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/order_items/order_item_id')
async def delete_order_items_order_item_id(order_item_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_order_items_order_item_id(db, order_item_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login/user')
async def post_login_user(raw_data: schemas.PostLoginUser, db: Session = Depends(get_db)):
    try:
        return await service.post_login_user(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

