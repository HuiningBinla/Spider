import urllib.request

def load_code():
    url = "http://www.baidu.com/"
    # get请求
    # http请求
    #response：http响应的对象
    response = urllib.request.urlopen(url)
    print(response)
    # 读取数据,返回byte类型
    data = response.read()
    print(data)
    # 将文件获取的内容转换成字符串
    str_data = data.decode("utf-8")
    print(str_data)
    # 将数据写入文件
    with open("baidu.html", "w", encoding="utf-8") as f:
        f.write(str_data)

    # 将字符串类型转换为bytes
    str_name = "baidu"
    bytes_name = str_name.encode("utf-8")

    # python爬取的类型：str，bytes
    # 如果爬取回来的是bytes类型：但写入的时需要字符串：decode("utf-8")
    # 如果爬取回来的是字符串类型：但写入时需要bytes：encoding("utf-8")

load_code()

