import pathlib
import time

from selenium import webdriver

# 基本信息
# 视频存放路径
catalog_mp4 = r"C:\Users\67099\PycharmProjects\pythonProject\publish"
# 视频描述
describe = "三国演义周瑜专栏 #国学 #电视 #智慧"
time.sleep(5)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

path = pathlib.Path(catalog_mp4)

# 视频地址获取
path_mp4 = ""
for i in path.iterdir():
    if ".mp4" in str(i):
        path_mp4 = str(i)
        break

if path_mp4 != "":
    print("检查到视频路径：" + path_mp4)
else:
    print("未检查到视频路径，程序终止！")
    exit()

# 封面地址获取
path_cover = ""
for i in path.iterdir():
    if ".png" in str(i) or ".jpg" in str(i):
        path_cover = str(i)
        break

if path_cover != "":
    print("检查到封面路径：" + path_cover)
else:
    print("未检查到封面路径，程序终止！")
    exit()


def publish_douyin():
    '''
     作用：发布抖音视频
    '''

    # 进入创作者页面，并上传视频
    driver.get("https://creator.douyin.com/creator-micro/home")
    time.sleep(2)
    driver.find_element_by_xpath('//*[text()="发布视频"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//input[@type="file"]').send_keys(path_mp4)

    # 等待视频上传完成
    while True:
        time.sleep(3)
        try:
            driver.find_element_by_xpath('//*[text()="重新上传"]')
            break
        except Exception as e:
            print("视频还在上传中···")

    print("视频已上传完成！")
    time.sleep(3)
    # 添加封面
    driver.find_element_by_xpath('//*[text()="编辑封面"]').click()

    time.sleep(5)
    driver.find_element_by_xpath('//div[text()="上传封面"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//input[@type="file"]').send_keys(path_cover)
    time.sleep(3)
    driver.find_element_by_xpath('//*[text()="裁剪封面"]/..//*[text()="确定"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="operation--2_JP2"]//*[text()="确定"]').click()
    # //div[@class="dialog-operation--35HYf"]//*[text()="确定"]
    # //*[text()="设置封面"]/..//*[contains(@class,"upload")]//*[text()="确定"]
    time.sleep(5)
    # 输入视频描述
    driver.find_element_by_xpath('//div[@aria-autocomplete="list"]//br').send_keys(
        describe + " #上热门 #dou上热门 #我要上热门")

    # 设置选项
    time.sleep(1)
    driver.find_element_by_xpath('//*[@class="radio--4Gpx6"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@class="semi-select-selection"]//span[contains(text(),"输入")]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@class="semi-select-selection"]//input').send_keys("深圳")

    time.sleep(5)
    driver.find_element_by_xpath('//*[@class="semi-popover-content"]//*[text()="深圳人才公园"]').click()

    # 同步到西瓜视频
    # driver.find_element_by_xpath('//div[@class="preview--27Xrt"]//input').click()   # 默认启用一次后，后面默认启用了。

    # driver.find_element_by_xpath( '//*[@class="card-pen--2P8rh"]' ).click( )
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[12]/div[1]/div/div[2]/div/input')
    # driver.find_element_by_xpath( '//*[@class="DraftEditor-root"]//br' ).send_keys( describe + " #上热门" )

    # driver.find_element_by_xpath( '//button[text()="确定"]' ).click( )

    # 人工进行检查并发布
    # time.sleep(3)
    # # 点击发布
    driver.find_element_by_xpath('//button[text()="发布"]').click()


# 开始执行视频发布
publish_douyin()
