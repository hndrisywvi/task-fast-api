from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from utils import Base


class transaksi(Base):
    __tablename__ = 'transaksi'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_item = Column(String(50), unique=True)
    jenis_transaksi = Column(String(100))
    trx_in = Column(String(1))
    trx_out = Column(String(1))
    status = Column(String(10))
    user_otorisasi = Column(String(100))
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())

class pareto(Base):
    __tablename__ = 'pareto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_item = Column(String(50), ForeignKey('transaksi.nama_item'))
    kategori = Column(String(50))
    ttl_item = Column(Integer)
    stock_out = Column(Integer)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())

# class transaksi(Base):
#     __tablename__ = 'transaksi'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     nama_transaksi = Column(String(50))
#     jenis_transaksi = Column(String(100))
#     trx_in = Column(String(1))
#     trx_out = Column(String(1))
#     status = Column(String(10))
#     user_otorisasi = Column(String(100))
#     create_at = Column(DateTime, default=func.now())
#     update_at = Column(DateTime, default=func.now(), onupdate=func.now())

# class pareto(Base):
#     __tablename__ = 'pareto'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     kategori = Column(String(50))
#     departemen = Column(String(50))
#     ttl_item = Column(Integer)
#     stock_out = Column(Integer)
#     create_at = Column(DateTime, default=func.now())
#     update_at = Column(DateTime, default=func.now(), onupdate=func.now())
