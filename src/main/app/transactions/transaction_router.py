from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from..auth.auth_middleware import auth_middleware
from..database.database import get_db
from.transaction_service import create_transaction, get_transactions, update_transaction, delete_transaction
from..schemas.transaction_schema import TransactionCreate, TransactionUpdate

router = APIRouter()

@router.post("/transactions/")
async def create_transaction_endpoint(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db=db, transaction=transaction)

@router.get("/transactions/")
async def read_transactions(user_id: int, db: Session = Depends(get_db)):
    transactions = get_transactions(db=db, user_id=user_id)
    if transactions is None:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return transactions

@router.put("/transactions/{transaction_id}")
async def update_transaction_endpoint(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    updated_transaction = update_transaction(db=db, transaction_id=transaction_id, transaction=transaction)
    if updated_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated_transaction

@router.delete("/transactions/{transaction_id}")
async def delete_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    deleted_transaction = delete_transaction(db=db, transaction_id=transaction_id)
    if deleted_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return deleted_transaction