import urllib.request
import json
import gzip
import pickle

print('-----------天气查询-----------')

def get_weather_data() :
    pickle_file = open('C:\\Users\\Stalker\\Desktop\\python\\python02文件操作\\city_data.pkl','rb')
    city = pickle.load(pickle_file)

    city_name = input('请输入城市:')
    if city_name in city.keys():#在字典city中查找是否有city_name这个键
        name1 = city[city_name]

        '''
        url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
        url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
        #网址1只需要输入城市名，网址2需要输入城市代码 网址1直接调用函数获取城市编码
        '''
         #这里name1是使用pickle取出了存放在文件city_data.pkl中的城市编码,所以可以直接调用name1
        url1 = 'http://wthrcdn.etouch.cn/weather_mini?citykey='+name1
        #读取网页数据 
        weather_data = urllib.request.urlopen(url1).read()
        #解压网页数据
        weather_data = gzip.decompress(weather_data).decode('utf-8')#读入打开的url
        #将json数据转换为dict数据
        weather_dict = json.loads(weather_data)

        return weather_dict
    else:
        #创建一个字典,将键设为desc,对应的值为invilad-citykey,和api接口对应
        error_dict = dict(desc ="invilad-citykey")
        
        return error_dict


def show_weather(weather_data):
    weather_dict = weather_data 
    #将json数据转换为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        print('你输入的城市名有误，或者天气中心未收录你所在城市')
    elif weather_dict.get('desc') =='OK':
        forecast = weather_dict.get('data').get('forecast')
        print('城市：',weather_dict.get('data').get('city'))
        print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
        print('感冒：',weather_dict.get('data').get('ganmao'))
        print('风向：',forecast[0].get('fengxiang'))
        print('风级：',forecast[0].get('fengli'))
        print('高温：',forecast[0].get('high'))
        print('低温：',forecast[0].get('low'))
        print('天气：',forecast[0].get('type'))
        print('日期：',forecast[0].get('date'))
        print('*******************************')
        four_day_forecast =input('是否要显示未来四天天气，是/否：')
        if four_day_forecast =='是' or 'Y' or 'y':
            for i in range(1,5):
                print('日期：',forecast[i].get('date'))
                print('风向：',forecast[i].get('fengxiang'))
                print('风级：',forecast[i].get('fengli'))
                print('高温：',forecast[i].get('high'))
                print('低温：',forecast[i].get('low'))
                print('天气：',forecast[i].get('type'))
                print('--------------------------')
        else:
            pass
    print('***********************************')

show_weather(get_weather_data())




'''
#下面是不使用pickle查询天气代码
import urllib.request
import gzip
import json
print('------天气查询------')
def get_weather_data() :
    city_name = input('请输入要查询的城市名称：')
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
    url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
    #网址1只需要输入城市名，网址2需要输入城市代码
    #print(url1)
    weather_data = urllib.request.urlopen(url1).read()
    #读取网页数据
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    #解压网页数据
    weather_dict = json.loads(weather_data)
    #将json数据转换为dict数据
    return weather_dict

def show_weather(weather_data):
    weather_dict = weather_data 
    #将json数据转换为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        print('你输入的城市名有误，或者天气中心未收录你所在城市')
    elif weather_dict.get('desc') =='OK':
        forecast = weather_dict.get('data').get('forecast')
        print('城市：',weather_dict.get('data').get('city'))
        print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
        print('感冒：',weather_dict.get('data').get('ganmao'))
        print('风向：',forecast[0].get('fengxiang'))
        print('风级：',forecast[0].get('fengli'))
        print('高温：',forecast[0].get('high'))
        print('低温：',forecast[0].get('low'))
        print('天气：',forecast[0].get('type'))
        print('日期：',forecast[0].get('date'))
        print('*******************************')
        four_day_forecast =input('是否要显示未来四天天气，是/否：')
        if four_day_forecast == '是' or 'Y' or 'y':
            for i in range(1,5):
                print('日期：',forecast[i].get('date'))
                print('风向：',forecast[i].get('fengxiang'))
                print('风级：',forecast[i].get('fengli'))
                print('高温：',forecast[i].get('high'))
                print('低温：',forecast[i].get('low'))
                print('天气：',forecast[i].get('type'))
                print('--------------------------')
    print('***********************************')

show_weather(get_weather_data())


'''
