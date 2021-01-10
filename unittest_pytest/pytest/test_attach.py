# 【05】测试报告美化与定制
import allure


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)  # 后面部分不确定是否写全?


def test_attach_photo():
    allure.attach.file("/Users/jinlianfu/Desktop/loan.png", name="这是一个图片", attachment_type=allure.attachment_type.PNG)

# def test_attach_video():
#     allure.attach.file("///","这是一个视频",attachment_type=allure.attachment_type.MP4)
