import pandas as pd
from .candidate_analysis import candidate_histogram_code
from django.shortcuts import render
import os
import tempfile


def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def candidate_histogram(request):
    # Data is taken form processed_candidates.py in the data folder
    # Set file path to get the information for the histogram
    file_path = 'data/processed_candidates.csv'
    
    #read the file
    candidates = pd.read_csv(file_path)
    
    # Define the path for the temporary chart image
    temp_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'histogram_chart.png')
    
    # Check if the histogram exists and overwrite it it it does to show newer data
    if os.path.exists(temp_file):
        os.remove(temp_file)
    # call the function in the candidate_analysis.py file using the data from processed_candidates.py
    chart = candidate_histogram_code(candidates)
    chart.figure.savefig(temp_file)
    
    # Render the template with the path to the chart image
    return render(request, 'dashboard.html', {'chart_path': temp_file})
