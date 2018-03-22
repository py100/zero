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

