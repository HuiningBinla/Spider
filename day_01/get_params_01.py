import urllib.request

# 有中文时需要转译的模块
import urllib.parse
import string

def get_method_params():

    url = "http://www.baidu.com/s?wd="   # 这是百度的一个通用公式，=后边接搜索内容，
    # 中文情况下要进行转译。如下：

    # 拼接字符串（汉字）
    name = "美女"
    # 字符串拼接
    final_url = url + name
    print(final_url)

    # 代码发送了请求
    # 网致里包含了中文，ASCII码是没有汉字的，
    # 有汉字时需要转译，需要两个模块：urllib.parse、string
    # 将包含汉字的网址进行转译
    encode_new_url = urllib.parse.quote(final_url,safe=string.printable)
    print(encode_new_url)
    # 使用代码发送网络请求
    response = urllib.request.urlopen(encode_new_url)
    print(response)

    # 读取数据
    data = response.read().decode()
    # 查看数据类型
    # print(type(data))
    # print(data)
    # 转换成字符串
    # str_data = data.decode("utf-8")
    # decode() 函数默认：utf-8
    # str_data = data.decode()
    # print(str_data)

    # 将数据写入文件
    with open("get_encode.html", "w", encoding="utf-8")as f:
        f.write(data)



    # UnicodeEncodeError: 'ascii' codec can't encode characters
    # in position 10-11: ordinal not in range(128)
    # 对上两行的解释：python是解释性语言，解析器只支持ASCII码0-127，即不支持中文


get_method_params()


