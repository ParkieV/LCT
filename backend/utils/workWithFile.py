import aiofiles
import pandas as pd
import xlrd
from xlutils.copy import copy

from ..sql_app import schemas


async def get_flats_from_excel_file(file):
    new_file = await file.read()
    flats = pd.read_excel(new_file)
    return flats.values.tolist()


async def save_file(file, out_file_path):
    async with aiofiles.open(out_file_path, 'wb') as out_file:
        while content := await file.read(1024):  # async read chunk
            await out_file.write(content)


async def update_file(flat_request: schemas.FlatRequest):
    old_workbook = xlrd.open_workbook('files/' + flat_request.filename)
    workbook = copy(old_workbook)
    worksheet = workbook.get_sheet(0)
    worksheet.write(0, 0, 'Цена')
    for curr_flat in range(1, len(flat_request.flats_prices) + 1):
        worksheet.write(curr_flat, 11, flat_request.flats_prices[curr_flat - 1])
    workbook.save('files/' + flat_request.filename)



