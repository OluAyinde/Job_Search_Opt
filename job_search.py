import requests
import json
import pandas as pd
from time import sleep

API_KEY = 'API_KEY'  #Replace with your key
BASE_URL = 'https://serpapi.com/search'

def fetch_jobs(query, location, max_results=2000):
    job_listings = []
    params = {
        'engine': 'google_jobs',
        'q': query,
        'location': location,
        'api_key': API_KEY,
        'hl': 'en'
    }
    
    while len(job_listings) < max_results:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            jobs = data.get('jobs_results', [])
            
            for job in jobs:
                title = job.get('title', '').lower()
                description = job.get('description', '').lower()
                company = job.get('company_name', '')
                location = job.get('location', '')
                
                #Filter for job role
                if 'product manager' in title or 'senior' in title or ('sponsorship' in description or 'visa' in description):
                    #Get the best available link
                    apply_options = job.get('apply_options', [])
                    if apply_options:  #Use the first apply_options link
                        link = apply_options[0].get('link', '')
                    else:  #Fallback to share_link
                        link = job.get('share_link', '')
                    
                    job_listings.append({
                        'Title': job.get('title'),
                        'Company': company,
                        'Location': location,
                        'Description': job.get('description'),
                        'Link': link
                    })
            
            print("Collected {} jobs so far...".format(len(job_listings)))
            
            serpapi_pagination = data.get('serpapi_pagination', {})
            next_page_token = serpapi_pagination.get('next_page_token')
            if not next_page_token:
                break
            
            params['next_page_token'] = next_page_token
            sleep(1)
        else:
            print("Error: {} - {}".format(response.status_code, response.text))
            break
    
    return job_listings[:max_results]

def save_to_csv(jobs, filename='product_manager_jobs.csv'):
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print("Saved {} jobs to {}".format(len(jobs), filename))

if __name__ == "__main__":
    query = 'product manager'
    location = 'Beijing'
    
    jobs = fetch_jobs(query, location, max_results=2000)
    
    if jobs:
        save_to_csv(jobs)
    else:
        print("No jobs found.")