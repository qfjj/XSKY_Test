import requests
import json
import math

url = 'https://xskydata.jobs.feishu.cn/api/v1/search/job/posts'
cookie  = 'device-id=7026364675575088644; channel=saas-career; platform=pc; s_v_web_id=verify_kvks6rsa_nKbCvmNA_eUei_4jf2_9GhI_80jES2V9M4IA; tea_uid=7026364864487622180; SLARDAR_WEB_ID=676f3e60-228f-44e2-b581-e5c83cef4986; atsx-csrf-token=RG8B-cT0Ke5TpPkXx4QCngcYwPQ7nhty-2UMYJozDQo%3D'
x_csrf_token = 'RG8B-cT0Ke5TpPkXx4QCngcYwPQ7nhty-2UMYJozDQo='

def getData(page):
    headers = {
        'cookie': cookie,
        "x-csrf-token": x_csrf_token,
        'website-path': 'school'
    }

    params = {
        'job_category_id_list': [],
        'keyword': '',
        'limit': 10,
        'location_code_list': [],
        'offset': page * 10,
        'portal_entrance': 1,
        'portal_type': 6,
        'recruitment_id_list': [],
        'subject_id_list': [],
        '_signature': 'VVA9MAAgEA11UIOgPvHjNlVQPSAADTX',
    }

    request = requests.post(url, headers=headers, data=json.dumps(params))
    return request.json()


if __name__ == '__main__':
    index = getData(0)
    count = index['data']['count']
    page = math.ceil(count / 10)
    result = []

    for i in range(page):
        data = getData(i)
        data = data['data']['job_post_list']

        for j in data:
            temp = {}
            temp['职位名称'] = j['title']
            temp['职位类别'] = j['job_category']['parent']['name'] + ' - ' + j['job_category']['name']
            temp['工作城市'] = j['city_info']['name']
            temp['职位描述'] = j['description']
            temp['职位要求'] = j['requirement']
            result.append(temp)

    with open("XSKY_Test.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(result, indent=2, ensure_ascii=False))

    print('完成！')