import time
import unittest

from test_unittest import TPShopLogin
from tools.HTMLTestRunner import HTMLTestRunner


# 测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TPShopLogin))

# 报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件
with open(report, "wb") as f:
    # 创建运行器
    runner = HTMLTestRunner(f, title="tp_shop测试报告")
    # 执行套件
    runner.run(suite)
