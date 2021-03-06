import unittest, time, sys
import HTMLTestRunner_PY3.HTMLTestRunner_PY3 as HTMLTestRunner

'''
Create on 2018-3-4
author:linjian
summary:用例执行入口，统一管理
'''

test_dir = './testcase'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='Qsh_*.py')
TestRunResultErrors = []

if __name__ == '__main__':
    RunTime = str(time.strftime('%Y-%m-%d_%H%M%S'))
    #创建测试报告，执行测试
    with open('./report/Test_report_' + RunTime + '.html', 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            verbosity=2,
            stream=fp,
            title='测试报告',
            # description='autotest'
        )
        TestRunResult = runner.run(discover)
    TestRunResultErrors.append(TestRunResult.failures)
    TestRunResultErrors.append(TestRunResult.errors)

    if TestRunResult.failures != [] or TestRunResult.errors != []:
        print(TestRunResultErrors.__str__())
        sys.exit(1)
    else:
        print("【%s】| 测试成功" % (str(time.strftime('%Y-%m-%d_%H:%M:%S'))))
