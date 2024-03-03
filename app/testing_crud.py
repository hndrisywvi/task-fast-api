from sqlalchemy.ext.asyncio import AsyncSession
from datastore import user_datastore, pareto_datastore
from schema import PostItemTransaksi, PostItemPareto
from models import user_models
from sqlalchemy.future import select
from sqlalchemy.orm import Session

async def post_item_transaksi(data: PostItemTransaksi, db_session: AsyncSession):
    async with db_session as session:
        try:
            print(data)

            if not (data.nama_item and data.jenis_transaksi and data.trx_in and data.trx_out and
                    data.kategori and data.ttl_item and data.stock_out):
                raise Exception("Semua kolom harus diisi")

            result, e = await user_datastore.data_transaksi(data, session)
            result, e = await pareto_datastore.pareto_item(data, session)
            return data, None
        except Exception as e:
            return None, e

async def update_qty_item(nama_item, qty_item, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resUpdateQtyItem, e = await pareto_datastore.UpdateQtyItem(nama_item, qty_item, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resUpdateQtyItem, None

        except Exception as e:
            return None, e

# async def post_item_transaksi(data: PostItemTransaksi, db_session: AsyncSession):
#     async with db_session as session:
#         try:
#             print(data)

#             if not (data.nama_item and data.jenis_transaksi and data.trx_in and data.trx_out and
#                     data.kategori and data.ttl_item and data.stock_out):
#                 raise Exception("Semua kolom harus diisi")

#             sql = select(user_models.transaksi).where(user_models.transaksi.nama_item == data.nama_item)
#             existing_transaksi = await session.execute(sql)
#             existing_transaksi_list = await existing_transaksi.scalars().all()

#             if existing_transaksi:
#                 sql_update = update(user_models.pareto).where(user_models.pareto.nama_item == data.nama_item).values(ttl_item=user_models.pareto.ttl_item + data.ttl_item)
#                 await session.execute(sql_update)
#             else:
#                 result, e = await user_datastore.data_transaksi(data, session)
#                 result, e = await pareto_datastore.pareto_item(data, session)

#             await session.commit()

#             return data, None
#         except Exception as e:
#             return None, e