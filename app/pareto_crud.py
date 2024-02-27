from sqlalchemy.ext.asyncio import AsyncSession
from datastore import pareto_datastore
from schema import PostItemPareto

async def post_item_pareto(data: PostItemPareto, db_session:AsyncSession):
    async with db_session as session:
        try:  
            print(data)  
            if data.nama_item == "" :
                raise Exception("nama_item item harus di isi")
            
            if data.kategori == "" :
                raise Exception("kategori item harus di isi")
            
            if data.ttl_item == "" :
                raise Exception("Total item harus di isi")
            
            if data.stock_out == "" :
                raise Exception("Stock out harus di isi")

            resPostItemPareto, e = await pareto_datastore.pareto_item(data, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resPostItemPareto, None


        except Exception as e:
            return data, e

async def get_list_item_pareto(page: int, limit:int, nama_item:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetListItemPareto, e = await pareto_datastore.getListItemPareto(page, limit, nama_item, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetListItemPareto, None


        except Exception as e:
            return resgetListItemPareto, e

async def get_list_detail_pareto(nama_item:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetListDetailPareto, e = await pareto_datastore.getListDetailPareto(nama_item, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetListDetailPareto, None


        except Exception as e:
            return resgetListDetailPareto, e

async def update_kategori_pareto(dept_before, new_dept, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resUpdatekategoriPareto, e = await pareto_datastore.UpdatekategoriPareto(dept_before, new_dept, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resUpdatekategoriPareto, None


        except Exception as e:
            return None, e

async def delete_pareto_by_id(no_id, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resDeleteParetoById, e = await pareto_datastore.DeleteParetoById(no_id, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resDeleteParetoById, None


        except Exception as e:
            return None, e