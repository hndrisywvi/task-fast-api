from sqlalchemy.ext.asyncio import AsyncSession
from datastore import user_datastore, pareto_datastore
from schema import PostItemTransaksi, PostItemPareto

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
