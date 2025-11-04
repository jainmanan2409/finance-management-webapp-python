from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, database, oauth2

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# ✅ Create a transaction
@router.post("/", response_model=schemas.TransactionResponse)
def create_transaction(
    transaction: schemas.TransactionCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    db_transaction = models.Transaction(
        amount=transaction.amount,
        type=transaction.type,
        note=transaction.note,
        user_id=current_user.id
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


# ✅ Get all transactions
@router.get("/", response_model=list[schemas.TransactionResponse])
def get_transactions(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)                     
):
    transactions = db.query(models.Transaction).filter(models.Transaction.user_id == current_user.id).all()
    return transactions


# ✅ Get transaction by ID
@router.get("/{transaction_id}", response_model=schemas.TransactionResponse)
def get_transaction(transaction_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)
):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


# ✅ Delete a transaction
@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)
):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(transaction)
    db.commit()
    return {"message": "Transaction deleted successfully"}
