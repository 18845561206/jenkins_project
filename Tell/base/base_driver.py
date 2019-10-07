from appium import webdriver

def init_driver():
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 需要启动的程序的包名
    desired_caps['appPackage'] = 'com.android.settings'
    # 需要启动的程序的界面名
    desired_caps['appActivity'] = '.Settings'
    # 设置手机不重置
    desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)