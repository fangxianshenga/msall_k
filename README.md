
# 欢迎使用Markdown编辑器

你好！ 这是你第一次使用 **Markdown编辑器** 所展示的欢迎页。如果你想学习如何使用Markdown编辑器, 可以仔细阅读这篇文章，了解一下Markdown的基本语法知识。


------------------------------------------

主要功能

下载搜索后的视频(https://video.kuaishou.com/)

------------------------------------------

运行环境

python3

win10

------------------------------------------
第三方库
需要使用到的库已经放在requirements.txt，使用pip安装的可以使用指令
pip install -r requirements.txt
如果国内安装第三方库比较慢，可以使用以下指令进行清华源加速 pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

-------------------------------------------


使用教程


1.安装谷歌浏览器及谷歌驱动，两者版本要一致(这里给的是87.0.4280.88版本的)，谷歌不是这个版本的需要自行下载对应版本驱动(http://npm.taobao.org/mirrors/chromedriver/)
   把安装的谷歌目录添加到环境变量中(path).

2.把chromdriver分别添加到浏览器的安装目录，python安装目录Scripts文件夹中,重启电脑。

3.打开命令提示符(菜单+R,输入cmd即可打开)，在命令运行中输入以下命令：
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"

4.在新弹出谷歌浏览器框里打开网址，登入。搜索框搜索要下载的视频，再运行即可。
