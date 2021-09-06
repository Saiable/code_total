from utils import *

class Tpl():
    def __init__(self,table_name):
        self.table_name = table_name
        self.store = Postgresql(table_name=self.table_name)
        self.get_proxy = get_proxy
        self.TOTAL_FIELD = TOTAL_FIELD
