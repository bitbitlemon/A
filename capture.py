#使用mss库可以进行截屏操作
import mss
import time
# 创建 mss 的实例
with mss.mss() as sct:
    # 循环捕捉屏幕
    while True:
        # 获取屏幕截图
        screenshot = sct.shot(output="screenshot.png") #默认图片保存在当前目录
        # 暂停一段时间，可以根据需要调整间隔时间
        time.sleep(1)


