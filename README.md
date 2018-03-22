# zero
Data mining for MOOC behavior


### Part of data filter
filter 能够通过配置文件筛选出所需要的列并保存在新的文件中。配置文件的样例参照config文件夹中的例子。我自己的目录结构如下，也可以根据自己需要修改。写好配置文件之后直接运行utility.py就ok。
```
|~code/
| |~config/
| | |-folder_to_process.txt
| | |-moc_course_conf.txt
| | |-tables.txt
| | `-wda_mooc_conf.txt
| |+cpp/
| `~py/
|   |+data-processing/
|   |+tests/
|   `~utility/
|     |-__init__.py
|     `-utility.py
|~data/
| |+2016-11-01/
| `-表定义.xlsx
```
### 配置文件的撰写方法
```
tables.txt
选择要操作的表和该表的列数，用tab分隔。#代表忽略，方便调试用
------------------
#wda_mooc	41
moc_course	27
------------------
```
```
folder_to_process.txt
选择要操作的子文件夹目录
------
20001
------
```
```
[table_name].txt
对于每一个tables.txt中指定的table，需要有一个对应的文件指定需要读的内容和对应的列号
-----------
logtime	0
uid	16
sid	17
ip	21
region	22
url	39
refer	40
-----------
```
