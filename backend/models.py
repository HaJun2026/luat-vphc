from sqlalchemy import Column, Integer, String, Text, BigInteger, DateTime
from sqlalchemy.sql import func
from database import Base


class Violation(Base):
    __tablename__ = "violations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False, index=True)
    description = Column(Text)
    category = Column(String(100), nullable=False, index=True)
    min_fine = Column(BigInteger, default=0)
    max_fine = Column(BigInteger, default=0)
    legal_basis = Column(String(500))
    additional_penalty = Column(Text)
    remedial_measure = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
