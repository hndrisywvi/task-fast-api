from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import user_crud
from utils import RespApp, get_async_session
from schema import CreateNewTransaksi


router = APIRouter()

@router.post("/new-transaksi")
async def CreateNewTransaksi(
    request: CreateNewTransaksi,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.create_new_transaksi(request, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-transaksi")
async def GetListTransaksi(
    page: int = 0,
    limit: int = 10,
    nama_item: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.get_list_transaksi(page, limit, nama_item, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-detail-transaksi")
async def GetListDetailTransaksi(
    nama_item: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.get_list_detail_transaksi(nama_item, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.put("/put-user-otorisasi")
async def UpdateUserOtorisasi(
    user_lama: str = None,
    user_baru: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.update_user_otorisasi(user_lama, user_baru, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.delete("/delete-transaksi-by-id")
async def DeleteTransaksiById(
    no_id: int = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.delete_transaksi_by_id(no_id, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)