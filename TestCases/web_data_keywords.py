import pytest
import allure
import os, sys, re, json
from Common.handle_logger import logger
from Common.handle_excel import excel_to_case, load_excel, excel_to_save, Handle_excel
from Common.handle_config import ReadWriteConfFile
from Common.setting import REPORT_DIR, BASE_DIR
from Common.basepage import BasePage
from Pages.BaiduPage.baidu_page import BaiduPage
from functools import wraps


def get_excel_data():
    execfile = ReadWriteConfFile().get_option('exec', 'exec_file_path')
    execst = ReadWriteConfFile().get_option('exec', 'st')
    execsheet = ReadWriteConfFile().get_option('exec', 'exec_sheet_name')
    webdata = excel_to_case(execfile, execst, execsheet)
    return webdata


def data_value(start_session, data):

    allure.dynamic.description(f'FILE SHEET： {list(data.values())[0]}  \n\nFILE NAME： {list(data.values())[1]}  \n\nFILE PATH： {list(data.values())[2]}')
    # logger.info(f'API_interface_test')
    logger.info(f'FILE SHEET： {list(data.values())[0]}  FILE NAME： {list(data.values())[1]}  FILE PATH： {list(data.values())[2]}')
    logger.info(list(data.values())[2])
    _data = list(data.values())[3]
    logger.info(_data)
    # data_list = []
    # for kv in _data:
    #     kv[param] = kv.pop('return_values')
    #     data_list.append(kv)
    # logger.info(data_list)
    logger.info('aaaaaaaaaaaaaaa')

    _dict = {}
    for va in list(data.values())[3]:

        allurestep(va) # tilte only
        __t_data(va)
        re_value = va['return_values']
        re_p= va['parameter']


        func = getattr(BaiduPage(start_session), va['method'])
        logger.info('0000000000000000000000000000000000000000000000000000000')
        ps = [_dict.get(p, p) for p in (va['parameter']).split(',')]
        if ps[0] == '':
            ps.clear()
            ps.append('1')
        else:
            ps.append('1')
        logger.info(f'--ps----{ps}')
        if va['method'].startswith('assert'):
            func(ps[0], va['expect'])
        else:
            return_value = func(*ps)
            if return_value:
                _dict[re_value] = return_value
        logger.info(f'------return_value---------------{return_value}')

        logger.info(f'55555555555555555555{_dict}')

def actions(func):
    @wraps(func)
    def wrapper(*args, **ksargs):
        result = func(*args, **ksargs)
        print('12121212')
        return wrapper
@actions
def get_dict(**ex_args):
    pass







def __new_data(param, _data):
    pattern = r'[$][{](.*?)[}]'
    param = param.replace('\'', '"').replace('\n', '').replace('\r', '').replace('\t', '')
    for key in _data:
        logger.info(f"----------数据--------------------[{key}]>>{_data[key]}--")
        res = re.findall(pattern, param)
        if res:
            for r in res:
                if r == key:
                    param = param.replace('${' + key + '}', str(_data[key]))
                    logger.info(f"----------数据预处理after:--self.relations[{key}]>>{_data[key]}--")
    return param

def __new_dict(param, return_value, _dict):
    param = param.replace('\'', '"').replace('\n', '').replace('\r', '').replace('\t', '')
    if param is None or param == '':
        return _dict
    else:
        if (param).startswith('${') and (param).endswith('}'):
            pass
        else:
            _dict[param] = return_value
            logger.info('66666666666666666')
        return _dict

def __get_relations(param, _data):
    pattern = r'[$][{](.*?)[}]'
    if param is None or param == '':
        return None
    else:
        for key in _data:
            logger.info(f"----------数据--------------------[{key}]>>{_data[key]}--")
            res = re.findall(pattern, param)
            if res:
                for r in res:
                    if r == key:
                        param = param.replace('${' + key + '}', str(_data[key]))
                        logger.info(f"----------数据预处理after:--self.relations[{key}]>>{_data[key]}--")
        return param
def __get_data(param, _data):
    if (param is None) or param == '':
        return None
    else:
        param = param.replace('\'', '"').replace('\n', '').replace('\r', '').replace('\t', '')
        paramn = __get_relations(param, _data)
        # paramn = json.loads(paramn)
        logger.info(f"----------数据预处理before:--json.loads(paramn)>>{type(param)}>>{param}--")
        logger.info(f"----------数据预处理after :--json.loads(paramn)>>{type(paramn)}>>{paramn}--")
        return  paramn

        # try:
        #     func = getattr(BaiduPage(start_session), va['method'])
        #     logger.info(func)
        #     logger.info('0000000000000000000000000000000000000000000000000000000')
        #     return_value = func('1')
        #     __get_data(return_value, va)
        #     logger.info(return_value)
        #     return return_value
        # except:
        #     logger.info('444444444')
        # logger.info('55555555555555555555')
        # row_pos = va['exec']
        # res = func(va, sheet, row_pos, col_pos_c, col_pos_v)

        # logger.info(f'Function return value：{str(res)}')

def allurestep(va):
    if va['title'] != '':
        with allure.step(f"Test title：{va['title']}"):
            logger.info(f"Test title：{va['title']}")
def __t_data(va):
    title = ''
    page = ''
    method = ''
    parameter = ''
    return_values = ''
    expect = ''
    capture = ''

    if va['title'] != '':
        title = va['title']
    if va['page'] != '':
        page = va['page']
    if va['method'] != '':
        method = va['method']
    if va['parameter'] != '':
        parameter = va['parameter']
    if va['return_values'] != '':
        return_values = va['return_values']
    if va['expect'] != '':
        expect = va['expect']
    if va['capture'] != '':
        capture = va['capture']
    logger.info(f"Test datas:【title:[{title}], page:[{page}], method:[{method}], parameter:[{parameter}], return_values:[{return_values}], expect:[{expect}], capture:[{capture}]】")


#
# @pytest.mark.usefixtures('start_class')
# class TestWEB():
#
#     @pytest.mark.parametrize('data', webdata)
#     def test_all_web(self, start_class, data):
#
#         allure.dynamic.feature(f'API_interface_test')
#         allure.dynamic.story(f'{list(data.values())[1]}<>{list(data.values())[0]}')
#         allure.dynamic.description(f'FILE SHEET： {list(data.values())[0]}  \n\nFILE NAME： {list(data.values())[1]}  \n\nFILE PATH： {list(data.values())[2]}')
#         logger.info(f'API_interface_test')
#         logger.info(f'FILE SHEET： {list(data.values())[0]}  FILE NAME： {list(data.values())[1]}  FILE PATH： {list(data.values())[2]}')
#         logger.info(list(data.values())[2])
#         wb, sheet, write_path = self.load_excel_setup(list(data.values())[0], list(data.values())[1], list(data.values())[2])
#
#         exec_c, col_pos_c = Handle_excel(list(data.values())[2]).getColumnValuesByTitle(sheet, 'return_code')
#         exec_v, col_pos_v = Handle_excel(list(data.values())[2]).getColumnValuesByTitle(sheet, 'return_values')
#
#         logger.info(f"Execute test suite: {self.__class__.__name__}")
#         logger.info(f"Execute test case: {list(data.values())[0]}")
#
#         for va in list(data.values())[3]:
#
#             self.allurestep(va) # tilte only
#             self.__t_data(va)
#
#             func = getattr(BasePage(), va['method'])
#             row_pos = va['exec']
#             res = func(va, sheet, row_pos, col_pos_c, col_pos_v)
#
#             logger.info(f'Function return value：{str(res)}')
#
#         self.save_excel_teardown(wb, write_path)
#
#         logger.info(f"Write Excel：{'save_excel_teardown'}")
#
#     def allurestep(self, va):
#         if va['title'] != '':
#             with allure.step(f"Test title：{va['title']}"):
#                 logger.info(f"Test title：{va['title']}")
#
#     def __t_data(self, va):
#         title = ''
#         method = ''
#         input = ''
#         request_data = ''
#         status = ''
#
#         if va['title'] != '':
#             title = va['title']
#         if va['method'] != '':
#             method = va['method']
#         if va['input'] != '':
#             input = va['input']
#         if va['request_data'] != '':
#             request_data = va['request_data']
#         logger.info(f"Test datas:【title:[{title}], method:[{method}], input:[{input}], request_data:[{request_data}]】")
#
#     # def load_excel_setup(self, sheet_name, file_name, file_path):
#     #     if num == '':
#     #         numstr = ''
#     #     else:
#     #         numstr = f'(' + num + ')'
#     #     p = self._re_file_path(file_path)
#     #     write_file_name = os.path.splitext(file_name)[0] + '_report' + numstr + os.path.splitext(file_name)[1]
#     #     new_path = file_path.replace(file_path, tmp_excel_path)
#     #
#     #     if p:
#     #         new_path = new_path + p
#     #
#     #     write_file_path = os.path.join(new_path, write_file_name)
#     #     logger.info(f'aaaaaaaa{write_file_path}')
#     #     wb, sheet = load_excel(write_file_path, sheet_name)
#     #     return wb, sheet, write_file_path
#     def _re_file_path(self, file_path):
#         datas_path = os.path.join(BASE_DIR, "Datas")
#         logger.info(file_path)
#         logger.info(datas_path)
#         logger.info('datas_path')
#         if sys.platform == 'win32':
#             new_report_path = file_path.replace(datas_path.replace('\\', '/'), '')
#             # p, f = os.path.split(new_report_path.replace('/', '\\'))
#             p, f = os.path.split(new_report_path)
#         else:
#             new_report_path = file_path.replace(datas_path, '')
#             p, f = os.path.split(new_report_path)
#         return p
#
#     def save_excel_teardown(self, wb, file_path):
#         excel_to_save(wb, file_path)
#
#     def __to_list(self, file_str, name):
#         fileList = str(file_str).split(',')
#         for one in fileList:
#             pre = os.path.splitext(one)[0]
#             if pre in name:
#                 return name
