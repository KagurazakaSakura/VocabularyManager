update feb 15, 2019.
韦伯词典的免费 API 把 XML 的输出改了格式，paser 已经不能用了。所以要把那部分改成 Json 的paser 才行。

# Vocabulary Manager

# 使用说明：

从最左侧的窗口输入内容
点击提取单词
在中间的一栏，将已经认识的单词点击一下，变灰
点击开始处理
在打开的浏览器中（如果没打开，设置下默认的浏览器）
从菜单栏里面点击，打印->打印到文件，

-> 如果想要查询所有单词，删掉目录下的 word_base.sdb


# 已知的问题：
1. 输入单词的标点符号只支持 逗号（,）句点(.）叹号(!)问号(?)，任何其它符号都会导致崩溃
2. 现在实际只是筛选出不在固定范围内的单词（word_base.sdb文件里面的 3000 个单词）
3. 生成字典的过程中，窗口会进入假死状态，实际上并没有问题，命令行窗口会显示输出
4. 词典解释从 webster learner dict 获取，大部分单词的解释会有十几个，导致一个单词一页 
-> 某些情况下，输入某些字符，会有玄学性质的崩溃。。。。😩
->win10 的命令行有玄学性质，如果停了在命令行窗口点击一下回车

# Todo:

1. 从 pdf (+ epub +html)格式直接获取数据
2. 生成像扇贝那样的记单词卡片，或者转换成用于 anki app 的格式
3. 换一个字典数据来源，
4. 在文本上直接标记单词，而不是生成在另一个框里面
5. 修改生成的网页样式，现在只为打印做了简单的样式设计
