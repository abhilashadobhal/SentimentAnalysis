import py7zr

with py7zr.SevenZipFile('historical_data.7z', mode='r') as z:
    z.extractall()