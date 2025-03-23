import requests
from bs4 import BeautifulSoup
import sqlite3
import csv



def scrape_jobs():
    url = 'https://realpython.github.io/fake-jobs'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for job_element in soup.find_all('div', class_='card-content'):
        title = job_element.find('h2', class_='title').text.strip()
        company = job_element.find('h3', class_='company').text.strip()
        location = job_element.find('p', class_='location').text.strip()
        description = job_element.find('div', class_='description').text.strip()
        application_link = job_element.find('a', class_='card-footer-item')['href']

        jobs.append((title, company, location, description, application_link))

    return jobs



def store_jobs(jobs):
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(title, company, location)
        )
    ''')

    for job in jobs:
        cursor.execute('''
            INSERT OR IGNORE INTO jobs (title, company, location, description, application_link)
            VALUES (?, ?, ?, ?, ?)
        ''', job)

        cursor.execute('''
            UPDATE jobs
            SET description = ?, application_link = ?
            WHERE title = ? AND company = ? AND location = ?
        ''', (job[3], job[4], job[0], job[1], job[2]))

    conn.commit()
    conn.close()
