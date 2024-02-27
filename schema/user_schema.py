from pydantic import BaseModel

class CreateNewTransaksi(BaseModel):
    nama_item : str = "susu"
    jenis_transaksi : str = "pembelian"
    trx_in : str = "k"
    trx_out : str = "d"
    user_otorisasi : str = "hendris"

class PostItemPareto(BaseModel):
    nama_item : str = "surya 12"
    kategori : str = "tobacco"
    ttl_item : int = 199
    stock_out : int = 20

class PostItemTransaksi(BaseModel):
    nama_item : str = "mallboro"
    jenis_transaksi : str = "pembelian"
    trx_in : str = "k"
    trx_out : str = "d"
    user_otorisasi : str = "hendris"
    kategori : str = "tobacco"
    ttl_item : int = 340
    stock_out : int = 70
