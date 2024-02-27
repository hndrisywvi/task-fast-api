from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import testing_crud
from utils import RespApp, get_async_session
from schema import PostItemTransaksi, PostItemPareto


router = APIRouter()

@router.post("/post-item-transaksi")
async def PostItemTransaksi(
    request: PostItemTransaksi,
    db: AsyncSession = Depends(get_async_session)
):
    out_resp, e = await testing_crud.post_item_transaksi(request, db)
    if e is not None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.put("/put-qty-item")
async def UpdateQtyItem(
    nama_item: str = None,
    qty_item: int = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await testing_crud.update_qty_item(nama_item, qty_item, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)