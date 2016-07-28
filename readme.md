# ocrtool
使用百度ORC做的照片转文字

![](http://oav6fgfj1.bkt.clouddn.com/baidu_ocr6ad619e3.png)

# 缘起
我有读书摘记的习惯，平时逛书店，遇到有意思的段落会用手机拍下

另外阅读扫描版的书籍时，做读书摘记也十分艰难（我近期在读《数据可视化的基本原理与方法》，也是扫描版的）

日积月累这类`照片摘记`让人望而生畏，要手动敲成文字，工作量着实不小，弃之又可惜，所以写了这个图片转文字的工具


# 使用  
*  pip install ocrtool 
*  创建`~/.ocrtool.yml`，登录你的百度开发者账号，获得你的apikey，写入`~/.ocrtool.yml`，形如：`apikey: xxx`
* ocrtool /tmp/text.jpg


# todo
作为云服务，或是bot

# 说明
百度的ocr似乎已经在百度apistore中下架了，不过使用还正常
