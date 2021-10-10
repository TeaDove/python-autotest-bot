import gspread
from ..core.settings import Settings

gc = gspread.service_account('creds/credentials.json')

sh = gc.open(Settings().sheet_title).sheet1