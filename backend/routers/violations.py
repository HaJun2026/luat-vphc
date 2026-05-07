from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/violations", tags=["violations"])


@router.get("", response_model=schemas.ViolationListResponse)
def list_violations(
    q: str = Query(None),
    category: str = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(models.Violation)

    if q:
        search = f"%{q}%"
        query = query.filter(
            or_(
                models.Violation.title.ilike(search),
                models.Violation.description.ilike(search),
                models.Violation.legal_basis.ilike(search),
            )
        )

    if category:
        query = query.filter(models.Violation.category == category)

    total = query.count()
    items = query.order_by(models.Violation.id).offset((page - 1) * limit).limit(limit).all()

    return {"items": items, "total": total, "page": page, "limit": limit}


@router.get("/{violation_id}", response_model=schemas.ViolationResponse)
def get_violation(violation_id: int, db: Session = Depends(get_db)):
    violation = db.query(models.Violation).filter(models.Violation.id == violation_id).first()
    if not violation:
        raise HTTPException(status_code=404, detail="Không tìm thấy vi phạm")
    return violation
