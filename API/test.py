import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url="https://api.github.com/search/repositories?q=language:python&sort=stars"

r=requests.get(url)
r.encoding="UTF-8"
response_dict=r.json()

# print("total: ",response_dict['total_count'])
repo_dicts=response_dict['items']
# print("Repositories returned:",len(repo_dicts))

# repo_dict=repo_dicts[0]

# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
# print("\nSelected infomation about first repository:")

# for repo_dict in repo_dicts:
    # print('Name:',repo_dict['name'])
    # print('Descripttion:'+str(repo_dict['description'])+'\r\n')
names,stars=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title='Most-Starred Python Projects on Github'
chart.x_labels=names
chart.add('',stars)
chart.render_to_file('python_repos.bak.svg')