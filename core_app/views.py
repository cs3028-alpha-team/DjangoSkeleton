from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .clean_data import process_data
from .matching import *
from .algorithm import run_gale_shapley
import subprocess
import csv
import os

# View for hello.html
def homepage(request):
    return render(request, 'homepage.html')

# View for IForm.html
def internship(request):
    return render(request, 'internship.html')

# View for SForm.html
def student(request):
    return render(request, 'student.html')

def admin_page(request):
    return render(request, 'sysadmin.html')



#Function to get user input and populate the candidates csv in the data folder
def submit_student(request):
    if request.method == 'POST':
        fullname = request.POST.get('Fullname', '')
        course = request.POST.get('Course', '')
        score = request.POST.get('Score', '')
        experience = request.POST.get('Experience', '')
        study_mode = request.POST.get('StudyMode', '')
        study_pattern = request.POST.get('StudyPattern', '')

        csv_content = f"{fullname},{course},{score},{experience},{study_mode},{study_pattern}\n"

        file_path = 'data/candidates.csv'

        with open(file_path, 'a') as file:
            if os.path.getsize(file_path) == 0:
                file.write("Fullname,Course,Score,Experience,StudyMode,StudyPattern\n")
            file.write(csv_content)

       
        return HttpResponse('Form submitted')
    else:
        return render(request, 'your_template.html')

#Function to get user input and populate the jobs csv in the data folder
def submit_internship(request):
    if request.method == 'POST':
        title = request.POST.get('Title', '')
        company = request.POST.get('Company', '')
        field = request.POST.get('Field', '')
        min_score = request.POST.get('MinScore', '')
        positions = request.POST.get('Positions', '')

        csv_content = f"{title},{company},{field},{min_score},{positions}\n"

        file_path = 'data/jobs.csv'

        with open(file_path, 'a') as file:
            if os.path.getsize(file_path) == 0:
                file.write("Title,Company,Field,MinScore,Experience,Positions\n")
            file.write(csv_content)

        return HttpResponse('Form submitted')
    else:
        # TODO : change this to a 404 template!
        return render(request, 'your_template.html')
        
def clean_data(request):

    # NOTE : Mattia - modified the condition of if request.method == post ... so process data works universally for now

    # Call the data processing function
    jobs, candidates = process_data()

    # Save the processed dataframes to CSV files
    jobs.to_csv('data/processed_jobs.csv', index=False)
    candidates.to_csv('data/processed_candidates.csv', index=False)

    return HttpResponse('Data processed successfully')


def matching_view(request):
    if request.method == 'POST':
        # Call the compute_compatibility_matrix function
        compatibility_matrix = compute_compatibility_matrix(candidates, jobs)
        
        # Save compatibility_matrix to a CSV file
        csv_file_path = 'data/compatibility_matrix.csv'
        file_exists = os.path.exists(csv_file_path)
        with open(csv_file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            if not file_exists:
                writer.writerow(['Candidate IDs'] + [str(job_id) for job_id in compatibility_matrix.columns])
            
            for index, row in compatibility_matrix.iterrows():
                writer.writerow([index] + row.tolist())
        
        return HttpResponse('Matching process completed. Compatibility matrix saved to CSV file.')
    else:
        return HttpResponse('Error: POST request expected.')




def run_matching_algorithm(request):
    candidates = pd.read_csv('data/processed_candidates.csv')
    jobs = pd.read_csv('data/processed_jobs.csv')
    number_of_candidates = len(candidates)
    number_of_jobs = len(jobs)

    # Activate algorithm
    print("Calling Gale-Shapley algorithm...")
    offers = run_gale_shapley(candidates, jobs, number_of_candidates, number_of_jobs)

    # Save file path
    #output_file = 'data/matching_results.csv'
    
    print(" ================ offers ========================")
    format_pairings(offers, candidates, jobs)

    # Save file 
    output_file = 'data/offers.csv'
    save_results_to_csv(offers, output_file)
    
    print("Results saved to CSV file.")
    
    return HttpResponse('Matching algorithm executed successfully. Results saved to CSV file.')
