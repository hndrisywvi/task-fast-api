from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import pareto_crud
from utils import RespApp, get_async_session
from schema import PostItemPareto


router = APIRouter()

@router.post("/new-item-pareto")
async def PostItemPareto(
    request: PostItemPareto,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await pareto_crud.post_item_pareto(request, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-item-pareto")
async def GetListItemPareto(
    page: int = 0,
    limit: int = 10,
    kategori: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await pareto_crud.get_list_item_pareto(page, limit, kategori, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-detail-pareto")
async def GetListDetailPareto(
    nama_item: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await pareto_crud.get_list_detail_pareto(nama_item, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.put("/put-kategori-pareto-item")
async def UpdatekategoriPareto(
    dept_before: str = None,
    new_dept: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await pareto_crud.update_kategori_pareto(dept_before, new_dept, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.delete("/delete-pareto-by-id")
async def DeleteParetoById(
    no_id: int = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await pareto_crud.delete_pareto_by_id(no_id, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)