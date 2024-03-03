from models import user_models
from sqlalchemy import select, or_, and_, update, delete, func, Integer, extract, cast

async def data_transaksi(data, session):
    try:
        params_insert = user_models.transaksi(
            nama_item=data.nama_item,
            jenis_transaksi=data.jenis_transaksi,
            trx_in=data.trx_in,
            trx_out=data.trx_out,
            status="success",
            user_otorisasi=data.user_otorisasi
        )

        session.add(params_insert)
        await session.commit()
        return data, None
    except Exception as e:
        return None, e

async def getListTransaksi(page, limit, nama_item, session):
    try:
        terms = []
        if nama_item not in (None, ""):
            terms.append(
                or_(
                    (user_models.transaksi.nama_item.ilike(f"%{nama_item.lower()}%"))
                )
            )

        offset = (page*limit)
        sql = select(user_models.transaksi).filter(and_(*(terms))).offset(offset).limit(limit)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return data, e

async def getListDetailTransaksi(nama_item, session):
    try:
        query = select(user_models.transaksi).where(user_models.transaksi.nama_item==nama_item)
        proxy_rows = await session.execute(query)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return data, e

async def UpdateUserOtorisasi(user_lama, user_baru, session):
    try:
        query = update(user_models.transaksi).where(user_models.transaksi.user_otorisasi==user_lama).values(user_otorisasi=user_baru)
        await session.execute(query)
        await session.commit()
        
        return user_lama, None
    except Exception as e:
        return None, e

async def DeleteTransaksiById(no_id, session):
    try:
        query = delete(user_models.transaksi).where(user_models.transaksi.id == no_id)
        await session.execute(query)
        await session.commit()
        
        return no_id, None
    except Exception as e:
        return None, e

async def getListTglTransaksi(page, limit, nama_item, dari_tgl, sampai_tgl, session):
    try:
        terms = []
        if nama_item not in (None, ""):
            terms.append(
                or_(
                    (user_models.transaksi.nama_item.ilike(f"%{nama_item.lower()}%")),
                    (user_models.transaksi.user_otorisasi.ilike(f"%{nama_item.lower()}%"))
                )
            )
        if dari_tgl not in (None, ""):
            terms.append(
                or_(
                    (extract('day', user_models.transaksi.create_at).cast(Integer) >= dari_tgl)
                )
            )
        if sampai_tgl not in (None, ""):
            terms.append(
                or_(
                    (extract('day', user_models.transaksi.create_at).cast(Integer) <= sampai_tgl)
                )
            )
        offset = (page * limit)
        sql = select(user_models.transaksi).filter(and_(*(terms))).offset(offset).limit(limit)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().all()

        return data, None
    except Exception as e:
        return None, e