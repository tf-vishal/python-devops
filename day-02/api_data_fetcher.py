import requests
import json

API_KEY = "9984b1a9a0msh3fd9a917a7bcd02p19e47djsn5f06c687ac6e" #will change after few days, limited and totallyy not free
BASE_URL = "https://jsearch.p.rapidapi.com/search"


# Headers
headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "jsearch.p.rapidapi.com"
}


def api_data_fetcher(query,country,num_pages,date_posted):

    params = {
        "query" : query,
        "country": country,
        "num_pages": num_pages,
        "date_posted": date_posted   
    }


    response = requests.get(url=BASE_URL, headers=headers, params=params)
    # ERRORS HANDLING

    ## API ERROR
    if response.status_code != 200:
        print("API ERROR !!", response.text)

    ##JSON ERROR
    try:
        api_res = response.json()
    except ValueError:
        print("Invalid JSON response")
        return

    job_data = api_res.get("data",[]) # To get the job data list
    number_of_jobs = len(job_data) # Length for looping and getting all jobs list

    processed_job = [] #For saving the output as list for json

    for jobs in job_data:
        print() # For better understanding visually
        print("Job Title/Role", jobs.get("job_title")) # Prints Job Title
        print("Company Name :", jobs.get("employer_name")) # COmpanyt Name
        print("Location: ", jobs.get("job_location"))
        print("Publisher: " ,jobs.get("job_publisher", "N/A")) #Linkedin etc
        print("Type of Job: ", jobs.get("job_employment_type", "N/A")) #Internship or full time
        print("Link To Apply: ", jobs.get("job_apply_link", "N/A")) #LInk to apply


        processed_job.append({
            "job_title": jobs.get("job_title"),
            "company": jobs.get("employer_name"),
            "location": jobs.get("job_location"),
            "publisher": jobs.get("job_publisher"),
            "employment_type": jobs.get("job_employment_type"),
            "apply_link": jobs.get("job_apply_link")
        })

    print("Total jobs:", number_of_jobs)

    return(processed_job)

def file_save(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"\nData saved to {filename}")

query = input("Type the Job/Query you want to search, [EG: DevOps Engineer In India] - ")
country = input("Type the Country code [EG: us, in, etc - ]").lower()
num_pages = input("Number of pages, 1 page = 10 job value. [1-50, Default = 1]")
date_posted = input("Freshness of job(all, today, 3days, week, month) - ")

if not num_pages:
    num_pages = 1

jobs = api_data_fetcher(query=query,country=country,date_posted=date_posted,num_pages=num_pages)
if jobs:
    file_save("api_output.json", jobs)