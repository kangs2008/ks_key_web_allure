import pytest
import allure
import sys
from Common.login_datas import data1
from Common.handle_logger import logger
from Pages.BaiduPage.baidu_page import BaiduPage
from TestCases.web_data_keywords import get_excel_data, data_value

@allure.feature("login 异常测试用例，feature")
@pytest.mark.usefixtures('start_session')
# @pytest.mark.usefixtures('report')
# @pytest.mark.usefixtures('refresh_page')
class TestLogin:

    # 异常测试用例
    @allure.story("111测试login 方法，baidu")
    @pytest.mark.parametrize('data', get_excel_data())
    def test_login(self, data, start_session):
        """描述！！！！"""
        logger.info(f" 执行 {self.__class__.__name__} 测试套件Suite ")
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例Case ")
        logger.info(f" 执行 {data}")

        return_value = data_value(start_session, data)


        # baidu = BaiduPage(start_session)
        # news = baidu.get_news_text()
        #
        # baidu.search(data['input'])
        # assert news == data['news']
        # logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))






    # # 异常测试用例
    # @allure.story("login 异常1，story")
    # @pytest.mark.parametrize('data', invalid_data2)
    # # @allure.dynamic.description('动态描述？')
    # def test_login_user_error(self, data, start_session):
    #     allure.dynamic.description('动态描述？')
    #     logger.info(" 执行 {0} 测试套件Suite ".format(self.__class__.__name__))
    #     logger.info(" 执行 {0} 测试用例Case ".format(sys._getframe().f_code.co_name))
    #
    #     BaiduPage(start_session).input_username(data['user'])
    #     BaiduPage(start_session).input_pwd(data['pwd'])
    #     BaiduPage(start_session).login_btn()
    #     # msg = BaiduPage(start_session).get_login_errMsg()
    #     msg = BaiduPage(start_session).get_user_errMsg()
    #     logger.info("期望值：{0}".format(data['expect']))
    #     logger.info("实际值：{0}".format(msg))
    #     try:
    #         assert msg, data['expect']
    #         logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
    #         BaiduPage(start_session).save_screenshot("{0}-正常截图".format(data['user']))
    #     except:
    #         logger.error(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
    #         BaiduPage(start_session).save_screenshot("{0}-异常截图".format(data['user']))
    #         raise

