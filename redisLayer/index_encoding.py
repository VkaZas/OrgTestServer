province_name_list = ['香港', '澳门', '江西', '广东', '山东', '浙江', '广西', '云南', '福建', '江苏', '海南', '贵州',
                      '湖南', '北京', '陕西', '天津', '安徽', '上海', '河北', '四川', '湖北', '西藏', '重庆', '新疆',
                      '宁夏', '河南', '甘肃', '吉林', '黑龙江', '内蒙古', '辽宁', '山西', '青海']


def gender_encoding(gender):
    output = '01'
    if gender == '1':
        output = '01'
    elif gender == '2':
        output = '02'
    return output


def timeslot_encoding(timeslot):
    output = '01'
    if int(timeslot) <= 10 and int(timeslot) >= 6:
        output = '01'
    elif int(timeslot) > 10 and int(timeslot) <= 14:
        output = '02'
    elif int(timeslot) > 14 and int(timeslot) <= 20:
        output = '03'
    elif int(timeslot) > 20 or int(timeslot) < 6:
        output = '04'
    return output


def province_encoding(province):
    output = province_name_list.index(province) + 1
    output = str(output)
    output = '0' + output
    output = output[-2:]
    return output


def index_encoding(gender, timeslot, province):
    gender_idx = gender_encoding(gender)
    timeslot_idx = timeslot_encoding(timeslot)
    province_idx = province_encoding(province)
    index_output = timeslot_idx + gender_idx + province_idx
    return index_output
