from robot.api.deco import keyword
import openpyxl
from robot.api import logger
from libraries.LibraryBase import LibraryBase
from libraries.utils import (
    debug,
    run_kw,
    get_variable,
)

class ExcelLibrary(LibraryBase):

    def __init__(self):
        super().__init__()
        self.env = get_variable("${ENV}")


    @keyword
    def debug_library(self):
        logger.info(f"{self.__class__}")
        debug()


    @keyword
    def fetch_urls_from_excel(self, file_path):
        """FETCH URL FROM EXCEL SHEET -  producer stage"""
        workbook = openpyxl.load_workbook(file_path)
        worksheet = workbook['Taul1']
        domains = []
        for row in worksheet.iter_rows(min_row=2, values_only=True):
            domain = row[0]
            dict_domain = {"domain":domain}
            domains.append(dict_domain)

        return domains
