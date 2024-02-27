from models import user_models
from sqlalchemy import select, or_, and_, update, delete

async def pareto_item(data, session):
    try:
        params_insert = user_models.pareto(
            nama_item=data.nama_item,
            kategori=data.kategori,
            ttl_item=data.ttl_item,
            stock_out=data.stock_out
        )

        session.add(params_insert)
        await session.commit()
        return data, None
    except Exception as e:
        return None, e

async def getListItemPareto(page, limit, kategori, session):
    try:
        terms = []
        if nama_item not in (None, ""):
            terms.append(
                or_(
                    (user_models.pareto.nama_item.ilike(f"%{nama_item.lower()}%"))
                )
            )

        offset = (page*limit)
        query = select(user_models.pareto).filter(and_(*(terms))).offset(offset).limit(limit)
        proxy_rows = await session.execute(query)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return data, e

async def getListDetailPareto(nama_item, session):
    try:
        query = select(user_models.pareto).where(user_models.pareto.nama_item==nama_item)
        proxy_rows = await session.execute(query)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return data, e

async def UpdatekategoriPareto(dept_before, new_dept, session):
    try:
        query = update(user_models.pareto).where(user_models.pareto.kategori==dept_before).values(kategori=new_dept)
        await session.execute(query)
        await session.commit()
        
        return dept_before, None
    except Exception as e:
        return None, e

async def DeleteParetoById(no_id, session):
    try:
        query = delete(user_models.pareto).where(user_models.pareto.id == no_id)
        await session.execute(query)
        await session.commit()
        
        return no_id, None
    except Exception as e:
        return None, e

async def UpdateQtyItem(nama_item, qty_item, session):
    try:
        query = update(user_models.pareto).where(user_models.pareto.nama_item==nama_item).values(ttl_item=qty_item)
        await session.execute(query)
        await session.commit()
        
        return nama_item, None
    except Exception as e:
        return None, e