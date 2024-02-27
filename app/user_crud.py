from sqlalchemy.ext.asyncio import AsyncSession
from datastore import user_datastore
from schema import CreateNewTransaksi

async def create_new_transaksi(data: CreateNewTransaksi, db_session:AsyncSession):
    async with db_session as session:
        try:  
            print(data)  
            if data.nama_item == "" :
                raise Exception("Nama Transaksi harus di isi")
            
            if data.jenis_transaksi == "" :
                raise Exception("Jenis Transaksi harus di isi")
            
            if data.trx_in == "" :
                raise Exception("In harus di isi")
            
            if data.trx_out == "" :
                raise Exception("Out harus di isi")
        
            if data.user_otorisasi == "" :
                raise Exception("User harus di isi")

            resCreateNewTransaksi, e = await user_datastore.data_transaksi(data, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resCreateNewTransaksi, None


        except Exception as e:
            return data, e

async def get_list_transaksi(page: int, limit:int, nama_item:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetListTransaksi, e = await user_datastore.getListTransaksi(page, limit, nama_item, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetListTransaksi, None


        except Exception as e:
            return resgetListTransaksi, e

async def get_list_detail_transaksi(nama_item:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetListDetailTransaksi, e = await user_datastore.getListDetailTransaksi(nama_item, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetListDetailTransaksi, None


        except Exception as e:
            return resgetListDetailTransaksi, e

async def update_user_otorisasi(user_lama, user_baru, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resUpdateUserOtorisasi, e = await user_datastore.UpdateUserOtorisasi(user_lama, user_baru, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resUpdateUserOtorisasi, None


        except Exception as e:
            return None, e

async def delete_transaksi_by_id(no_id, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resDeleteTransaksiById, e = await user_datastore.DeleteTransaksiById(no_id, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resDeleteTransaksiById, None


        except Exception as e:
            return None, e