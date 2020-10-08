import pandas as pd

# Thông Tin Bộ Chỉ Số HoseIndex
#https://www.hsx.vn/Modules/Listed/Web/CustomIndexView/?fid=377673779e9c41d090004a3d22a1dd61

VNDIAMON = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/188802591'
VNFINLEAD = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/188802592'
VNFINSELECT = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/188802593'
# Thông Tin Bộ Chỉ Số HoseIndex
HOSE = 'https://www.hsx.vn/Modules/Listed/Web/HoseIndexView/?fid=726e15cba4b04cb09ae4aa0b04bffee0'
VN100 = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/188803177'
VN30 = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/1964531007'
VNALL = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/951937685'
VNMID = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/699240157'
VNSI = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/'
VNSML = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/434493689'
#Thông Tin Bộ Chỉ Số SectorIndex
sector_index = 'https://www.hsx.vn/Modules/Listed/Web/SectorIndexView/?fid=218ca2db035948beac048d862ac03d30'


key = 'AIzaSyCq7clqV7mxkIogvndxNsjpqwG7FZYmq9g' #from my last name

import gspread

gc = gspread.service_account()