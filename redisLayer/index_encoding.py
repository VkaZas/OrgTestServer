# province_name_list = ['香港', '澳门', '江西', '广东', '山东', '浙江', '广西', '云南', '福建', '江苏', '海南', '贵州',
#                       '湖南', '北京', '陕西', '天津', '安徽', '上海', '河北', '四川', '湖北', '西藏', '重庆', '新疆',
#                       '宁夏', '河南', '甘肃', '吉林', '黑龙江', '内蒙古', '辽宁', '山西', '青海']

t1_city_list = ['北京', '上海', '广州', '深圳', '成都', '杭州', '武汉', '南京', '重庆', '天津',
                '苏州', '西安', '长沙', '沈阳', '青岛', '郑州', '大连', '东莞', '宁波']

t2_city_list = ['厦门',
                '福州',
                '无锡',
                '合肥',
                '昆明',
                '哈尔滨',
                '济南',
                '佛山',
                '长春',
                '温州',
                '石家庄',
                '南宁',
                '常州',
                '泉州',
                '南昌',
                '贵阳',
                '太原',
                '金华',
                '珠海',
                '惠州',
                '徐州',
                '烟台',
                '嘉兴',
                '南通',
                '乌鲁木齐',
                '绍兴',
                '中山',
                '台州',
                '兰州',
                '海口',
                ]

project_id_dict = {
    '27010101': 'jdb',
    '32010380': 'jlb1',
    '32010381': 'jlb2',
    '32010382': 'jlb3',
    '32010271': 'jlb4',
    '32010209': 'yh',
}

jlb123_list = ['32010380', '32010381', '32010382']
jlb123_agent_code = '3201038x'

filename_projectid_dict = {
    'data_jdb.json': '27010101',
    'data_jlb123.json': jlb123_agent_code,
    'data_jlb4.json': '32010271',
    'data_yh.json': '32010209',
}

# def gender_encoding(gender):
#     output = '01'
#     if gender == '1':
#         output = '01'
#     elif gender == '2':
#         output = '02'
#     return output
#
#
# def timeslot_encoding(timeslot):
#     output = '01'
#     if int(timeslot) <= 10 and int(timeslot) >= 6:
#         output = '01'
#     elif int(timeslot) > 10 and int(timeslot) <= 14:
#         output = '02'
#     elif int(timeslot) > 14 and int(timeslot) <= 20:
#         output = '03'
#     elif int(timeslot) > 20 or int(timeslot) < 6:
#         output = '04'
#     return output


# def province_encoding(province):
#     output = province_name_list.index(province) + 1
#     output = str(output)
#     output = '0' + output
#     output = output[-2:]
#     return output


def index_encoding(projectid, city, gender):
    index = -1
    if city in t1_city_list:
        index = 0
    elif city in t2_city_list:
        index = 2
    else:
        index = 4

    # gender = 1 MALE, gender = 2 FEMALE
    index += int(gender) - 1
    # Merge jlb1, jlb2, jlb3
    if projectid in jlb123_list:
        projectid = jlb123_agent_code

    index = str(projectid) + '_' + str(index)
    return index
