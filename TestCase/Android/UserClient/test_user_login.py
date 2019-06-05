from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Operate.PageOperate import PageOperate
from Base.BaseReplace import ReplaceYaml

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# tc_temp = PATH("../yamls/temp.yaml")
# el_android = PATH("../yamls/el_android.yaml")
# el_iOS = PATH("../yamls/el_iOS.yaml")

tc_temp = PATH("../yamls/temp.yaml")
el_android =PATH("../yamls/el_android.yaml")
el_iOS = PATH("../yamls/el_iOS.yaml")


class UserLogin( ParametrizedTestCase ):

    # def repalce(self, tc, tc_temp):
    #     if self.platformName == 'android':
    #         ReplaceYaml( tc, tc_temp, el_android )
    #     elif self.platformName == 'iOS':
    #         ReplaceYaml( tc, tc_temp, el_iOS )

    def test_login(self):
        tc = "../yamls/Android/UserClient/test_login_user.yaml"
        #self.repalce( tc, tc_temp )
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        userLoginPage = PageOperate( app )
        userLoginPage.operate()
        userLoginPage.checkPoint()

    @classmethod
    def setUpClass(cls):
        super( UserLogin, cls ).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super( UserLogin, cls ).tearDownClass()
