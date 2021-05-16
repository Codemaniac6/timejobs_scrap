from bs4 import BeautifulSoup
import lxml
import requests
import time


url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
response = requests.get(url).text
def find_jobs():
    with open('index.html', 'r') as response:
        unfamiliar_skill = input(f'''Enter a skills you're not familiar with to filter it out
or press q to skip: ''')

        soup = BeautifulSoup(response, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        with open('job_posts.txt', 'w') as f:
            for job in jobs:
                position = job.find('h2').text.strip()
                company_name = job.find('h3', class_='joblist-comp-name').text.strip()
                job_description_class = job.find('ul', class_='list-job-dtl clearfix')
                job_description = job_description_class.find('li').text.replace('Job Description:', '').strip()
                skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
                job_published_date = job.find('span', class_='sim-posted').span.text.strip()
                more_info = job.header.h2.a['href']
                if unfamiliar_skill != 'q':
                    if unfamiliar_skill not in skills:
                        print(f'''
                    POSITION: {position}
                    COMPANY NAME: {company_name}
                    JOB DESCRIPTION: {job_description.replace('More Details', '')}
                    REQUIRED SKILL: {skills}
                    PUBLISHED: {job_published_date}
                    APPLY: {more_info}
                    ''')
                else:
                    print(f'''
                POSITION: {position}
                COMPANY NAME: {company_name}
                JOB DESCRIPTION: {job_description.replace('More Details', '')}
                REQUIRED SKILL: {skills}
                PUBLISHED: {job_published_date}
                APPLY: {more_info}
                    ''')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        time.sleep(time_wait * 60)