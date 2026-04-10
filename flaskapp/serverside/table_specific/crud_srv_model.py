from flaskapp.serverside.serverside_table import ServerSideTable
from flaskapp.serverside import table_schemas

# DATA_SAMPLE = [
#     {'A': 'Hello!', 'B': 'How is it going?', 'C': 3, 'D': 4},
#     {'A': 'These are sample texts', 'B': 0, 'C': 5, 'D': 6},
#     {'A': 'Mmmm', 'B': 'I do not know what to say', 'C': 7, 'D': 16},
#     {'A': 'Is it enough?', 'B': 'Okay', 'C': 8, 'D': 9},
#     {'A': 'Just one more', 'B': '...', 'C': 10, 'D': 11},
#     {'A': 'Thanks!', 'B': 'Goodbye.', 'C': 12, 'D': 13},
#     {'A': 'Yorme', 'B': 'Goodbye.', 'C': 12, 'D': 13},
#     {'A': 'Thanks_1', 'B': 'Goodbye._1', 'C': 12, 'D': 13},
#     {'A': 'Thanks_2', 'B': 'Goodbye._2', 'C': 12, 'D': 13},
#     {'A': 'Thanks_3', 'B': 'Goodbye._3', 'C': 12, 'D': 13},
#     {'A': 'Thanks_4', 'B': 'Goodbye._4', 'C': 12, 'D': 13},
#     {'A': 'Thanks_5', 'B': 'Goodbye._5', 'C': 12, 'D': 13},
#     {'A': 'Thanks_6', 'B': 'Goodbye._6', 'C': 12, 'D': 13},
# ]



class TableBuilder(object):
    # def collect_data_clientside(self):
    #     return {'data': DATA_SAMPLE}

    def collect_data_serverside(self, request, DATA_SAMPLE):
        columns = table_schemas.SERVERSIDE_TABLE_COLUMNS
        return ServerSideTable(request, DATA_SAMPLE, columns).output_result()

    # SMS Convos model
    def sms_details_serverside(self, request, DATA_SAMPLE_2):
        columns = table_schemas.SMS_DETAILS_SERVERSIDE_TBL_COLUMNS
        return ServerSideTable(request, DATA_SAMPLE_2, columns).output_result()

    # CRUD (BASIC)
    def crud_dt_serverside(self, request, tmp):
        columns = table_schemas.CRUD_SRV_TABLE_COLUMNS
        return ServerSideTable(request, tmp, columns).output_result()


