#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
# Author: liuchuan
# Contact: liuchuan910927@gmail.com
# File: QQMusicMV.py
# Datetime: 2019/12/9 22:54
# Software: PyCharm

import requests
import os

from multiprocessing import Pool
from selenium import webdriver                          # 引入 selenium 的浏览器驱动接口
from selenium.webdriver.chrome.options import Options   # 引入 chrome 选项


# 请求头
HEADERS = {
    'referer': 'https://y.qq.com/portal/mv_lib.html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}


def selenium_chrome(html):
    '''
    使用 Selenium启动Chrome浏览器测试
    :param html: 浏览器需要打开的网址
    :return: WebDriver对象
    '''
    '''
     Chrome-headless 模式: Google 针对 Chrome 浏览器 59版 新增加的一种模式，可以让你不打开UI界面的情况下使用 Chrome 浏览器，所以运行效果与 Chrome 保持完美一致。
     webdriver安装路径: macOS：复制webdriver到/usr/local/bin目录下之后,就不需要指定path
    '''
    # 配置Chrome浏览器 (Headless无界面启动模式)
    option = Options()
    option.headless = True                      # 设置是否启动无界面化
    browser = webdriver.Chrome(options=option)  # 打开chrome浏览器 声明 chrome 浏览器
    browser.get(html)                           # 访问网页
    browser.implicitly_wait(5)                  # 等待5秒, 1秒加载完毕, 5秒是最长时间
    # print(browser.page_source)                # 将源码打印到终端
    return browser



def make_dir(folder_name):
    """
    新建文件夹并切换到该目录下
    :param folder_name: 文件夹名称
    :return:
    """
    # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    # path = os.path.join(Dir_PATH, folder_name)

    # 根据文件名，检查路径是否存在？
    # 如果目录已经存在，就不用再次爬取，避免重复，提高效率。存在返回 Flase，否则反之
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)  # 如果不存在路径，根据 folder_name 创建文件夹
        # os.chdir(folder_name)       # 改变当前工作目录
        return True
    print("文件夹已经存在！")
    return False


def download_music(music_url, dst_path):
    '''
    下载音乐到本地
    :param music_url: 音乐链接地址
    :param dst_path: 保存路径
    :return:
    '''
    try:
        req = requests.get(url=music_url, headers=HEADERS)
        with open(dst_path, "wb+") as f:    # 将下载的图片保存到对应的路径
            f.write(req.content)
            print(f"[INFO]: 已保存视频文件: {dst_path}")
            f.close()
    except requests.exceptions.RequestException as e:
        raise e


def get_mv_max_page_numbers():
    '''
    获取网页中 MV 的最大页码
    :return: MV最大页码
    '''
    baseURL = 'https://y.qq.com/portal/mv_lib.html'

    browser = selenium_chrome(baseURL)

    # 最大页码
    MaxPageNumber = browser.find_element_by_xpath('//div[@class="mod_page_nav js_pager"]/a[4]').get_attribute('data-index')
    # print(f'最大页码: {MaxPageNumber}')

    return MaxPageNumber


def parse_all_pages_to_get_url():
    '''
    解析所有页面得到网址
    '''
    # 最大页面
    max_page = get_mv_max_page_numbers()

    # 构造分页数字列表
    page_indexs = range(0, int(max_page), 1)

    for idx in page_indexs:     # 通过循环获取所有页面 URL

        # 每一页URL
        url = f'https://y.qq.com/portal/mv_lib.html#page={idx}&&order=1&&version=7&area=15&t6=1'

        get_all_urls_of_mv(url)


def get_all_urls_of_mv(html):
    '''
    根据所有页面网址, 获取所有 MV 的 data_vid
    '''

    # WebDriver浏览器对象
    browser = selenium_chrome(html)

    # 构造分页数字列表
    page_indexs = range(1, 21, 1)

    for idx in page_indexs:
        # MV 的id
        data_vid = browser.find_element_by_xpath(f'//*[@id="mv_list"]/li[{idx}]').get_attribute('data-vid')
        print()
        print(f'data-vid: {data_vid}')

        get_mv_info(data_vid)


def get_mv_info(vedio_vid):
    '''
    根据视频的vid, 获取视频信息(链接\名称\艺人..等等)
    :param vedio_vid: 视频 id
    '''

    # https://y.qq.com/n/yqq/mv/v/o0032i34nid.html

    # MV 播放真正链接
    realURL = f'https://y.qq.com/n/yqq/mv/v/{vedio_vid}.html'

    # WebDriver浏览器对象
    browser = selenium_chrome(realURL)

    # MV 名称
    mv_name = browser.find_element_by_xpath('//div/h1/span[1]').get_attribute('title')
    # MV 艺人
    mv_singer = browser.find_element_by_xpath('//*[@id="mv_control"]/h1/a').text
    # MV 播放链接
    mv_link = browser.find_element_by_tag_name('video').get_attribute('src')

    print('================  MV真实下载链接  ================')
    print(f'MV名称 = {mv_name}')
    print(f'艺人   = {mv_singer}')
    print(f'下载链接 = {mv_link}')

    # ====================== 根据获取到视频链接,下载到本地 ==================

    # 文件路径名
    fileName = f'/Users/liuchuan/Desktop/QQ音乐/{mv_name}'

    # 目录名
    dirname = f'{fileName}/{mv_name}.mp4'

    make_dir(fileName)

    download_music(mv_link, dirname)

    browser.close()  # 关闭浏览器


if __name__ == '__main__':
    '''
    主函数.程序的入口
    '''

    # 创建多个进程
    # 进程池, 表示可以同时执行的进程数量
    # Pool默认大小是 CPU 的核心数
    pool = Pool(2)

    for i in range(5):
        # 创建进程, 放入进程池 统一管理
        pool.apply_async(parse_all_pages_to_get_url(), args=(i, ))
    print('父进程结束!!!')

    pool.close()
    pool.join()     # 在调用join之前,必须close.在调用 close 之后,就不能再添加新的进程.
