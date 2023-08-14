import time

import requests

rq = requests.session()

token = ''

rq.headers = {
    'Access-Token': token,
    'Origin': 'https://yxzx.bj-jiling.com',
    'Referer': 'https://yxzx.bj-jiling.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}


# 获取资源信息
def get_res_info(student_id, resource_id):
    res = rq.post('https://yxzx.bj-jiling.com/user/course/getCourseResourceData',
                  {
                      'student_id': student_id,
                      'resource_id': resource_id
                  }).json()
    return res


# 上传学习时间
def update_time(resource_id, course_id, student_id, record_study_period=10):
    data = {"resource_id": resource_id, "course_id": course_id, "student_id": student_id,
            "record_study_period": record_study_period}
    res = rq.post('https://yxzx.bj-jiling.com/user/course/insertCourseStudyRecordData',
                  data).json()
    return res


# 更新课程记录
def update_record(resource_id, course_id, student_id, record_resource_duration, resource_duration):
    data = {
        'resource_id': resource_id,
        'course_id': course_id,
        'student_id': student_id,
        'record_resource_duration': record_resource_duration,
        'resource_duration': resource_duration
    }
    res = rq.post('https://yxzx.bj-jiling.com/user/course/updateCourseRecordData',
                  data).json()
    return res


if __name__ == '__main__':
    student_id = ''
    course_id = ''

    course_info = {}
    with open('course.json', 'r+', encoding='utf8') as f:
        t = f.read()
        import json
        course_info = json.loads(t)['data']
        import pprint
        # pprint.pprint(course_info)

    print(f'技领平台学习中'
          f'课程名{course_info["course"]["course_name"]}')

    # 所有资源信息
    res_list_info = course_info["course"]["course_section"]
    for res in res_list_info:
        c_res = res['course_resource'][0]
        print(len(c_res))
        print(
            f"section_code：{res['section_code']}\n"
            f"section_name: {res['section_name']}\n"
            f"具体资源信息"
            f"resource_id: {c_res['resource_id']}\n"
            f"resource_duration: {c_res['resource_duration']}\n"
            f"resource_status: {c_res['resource_status']}\n"
        )

        #
        # print(get_res_info(student_id, resource_id))

        # 上传学习进度
        r = update_record(c_res['resource_id'], course_id=course_id, student_id=student_id,
                          record_resource_duration=c_res['resource_duration'],
                          resource_duration=c_res['resource_duration'])
        print('上传学习进度', r)
        # 上传学习时间
        r = update_time(c_res['resource_id'], course_id=course_id, student_id=student_id, record_study_period=10)
        print('上传学习时间', r)

        time.sleep(2)

        # for t in range((c_res['resource_duration'] // 10) + 1):

