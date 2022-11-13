# from collections import defaultdict
from pathlib import Path

ROOT_DIR = Path.cwd()
ASSET_SOURCE = Path(ROOT_DIR, "asset")

# print(ASSET_SOURCE)
# TODO: add sector directory

SOURCE_SECTOR = [
    {"id": 0, "sector": "NATIONAL_LIBRARY"},
    {"id": 1, "sector": "TEACHER_E_FACULTY"},
    {"id": 2, "sector": "MINISTRA_OF_LABOR"},
    {"id": 3, "sector": "SMALL_AND_MEDIUM_ENTERPRISE_ADMINISTRATION"},
]


## all sector file, (id, file_name)
FILE_NATIONAL_LIBRARY = [
    (0, f"{ASSET_SOURCE}國家圖書館_遠距學園1100902_課程清單.xlsx"),
]

FILE_TEACHER_E_FACULTY = [
    (1, f"f{ASSET_SOURCE}教師 e 學院_年度課程清單.xlsx"),
]

FILE_MINISTRA_OF_LABOR = [
    (2, f"{ASSET_SOURCE}勞動部_勞動力發展數位服務平台課程清單_1100903.csv.xlsx"),
]

FILE_SMALL_AND_MEDIUM_ENTERPRISE_ADMINISTRATION = [
    (3, f"{ASSET_SOURCE}經濟部中小企業處_中小企業網路大學校課程總表0901.xlsx"),
]

## (id, file_container)
SECTOR_FILECONTAINER = [
    (0, FILE_NATIONAL_LIBRARY),
    (1, FILE_TEACHER_E_FACULTY),
    (2, FILE_MINISTRA_OF_LABOR),
    (3, FILE_SMALL_AND_MEDIUM_ENTERPRISE_ADMINISTRATION),
]


# COURSE_ASSET = {
#     "NATIONAL_LIBRARY": None,
#     "TEACHER_E_FACULTY": None,
#     "MINISTRA_OF_LABOR": None,
#     "SMALL_AND_MEDIUM_ENTERPRISE_ADMINISTRATION": None,
# }

# def get_sector_file(sector: int | str):
#     if type(sector) == int:

#     elif type(sector) == str:
