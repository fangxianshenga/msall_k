## 简介
----
通过这段时间测试(2021/3/10-2021-3-13).是可以正常上传[小k动画制作平台](https://xk.yunboai.com/user/videohandle/)。


## 主要功能
--------------------
-  视频自动上传。
- 上传成功的会自动生成一个txt文件记录(名称自定义)，然后可以根据txt文件进行下载。
- 上传失败的会自动生成一个shibai.txt文件记录，等文件上传完后会根据此文件记录的名称再次上传一次。

## 运行环境
--------------------
- windows
- python3

## 第三方库
--------------------
- 需要使用到的库已经放在requirements.txt，使用pip安装的可以使用指令
pip install -r requirements.txt
- 如果国内安装第三方库比较慢，可以使用以下指令进行清华源加速 pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

## 使用教程
--------------------

1. 安装谷歌浏览器及谷歌驱动，两者版本要一致(这里给的是87.0.4280.88版本的)，谷歌不是这个版本的需要自行下载对应版本[驱动](http://npm.taobao.org/mirrors/chromedriver/) 把安装的谷歌目录添加到环境变量中(path)。
2. 把chromdriver分别添加到浏览器的安装目录，python安装目录Scripts文件夹中,重启电脑。
3. 打开命令提示符(菜单+R,输入cmd即可打开)，在命令运行中输入以下命令会弹出谷歌浏览器界面：
```python
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
```
4. 在新弹出谷歌浏览器框里打开网址，登入。搜索框搜索要下载的视频，再运行即可
5. 打开[小k网页](https://xk.yunboai.com/user/videohandle/)，扫描登入。手动上传一次。
6. 在 上传小Kplus.py 中搜索path 修改本地视频路径。
7. 运行 上传小Kplus.py
