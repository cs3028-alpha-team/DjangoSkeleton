import sys
import random
import pandas as pd
from time import time
from .matching import compute_compatibility, compute_compatibility_matrix

# given a list of jobs, return the index of a job with offers to still give out, or -1 if none are found
def find_job(company_ids):
    for i in range(len(company_ids)):
        if company_ids[i] >= 0: return i
    return -1  

def suitable_candidates(company_index, compatibility_matrix):
    # retrieve the column with key of company_index from the compatibility matrix
    # print("Company index:", company_index)
    # print("Compatibility matrix shape:", compatibility_matrix.shape)
    suit_cands = [(i, compatibility_matrix[company_index][i]) for i in range(len(compatibility_matrix[company_index]))]
    # print("Suitable candidates:", suit_cands)
    
    # sort the candidates by their compatibility score descending, so company makes offer to most relevant candidates first
    suit_cands.sort(key = lambda x: x[1])
    
    return suit_cands


#@benchmark
# run the gale-shapley algorithm on the input candidates and jobs sets
def gale_shapley(company_ids, offers, compatibility_matrix, available_positions, max_iterations=10000):
    
    # keep track of number of companies fulfilled at each iteration
    fulfillments = []
    iterations = 0
    
    # trigger time-out when algorithm reaches a stagnant point
    while iterations < max_iterations:
        
        # find a company with job offers to give out
        company_id = find_job(company_ids)
        

        # stop condition when all companies have given out jobs
        if company_id == -1: break
            
        # job J with positions still to fill-out
        j = company_ids[company_id]
        
        # find most compatible candidate who company j has not offered a job to yet
        comps = suitable_candidates(j, compatibility_matrix)
        
        # check whether all students reject this company
        all_reject = True
        
        for candidate in comps:
            candidate_id = candidate[0]
            
            # make an offer to this candidate
            if j not in offers[candidate_id][1]:
                
                # check if candidate has no offer yet
                if offers[candidate_id][0] == None:
                    
                    # make the offer 
                    offers[candidate_id][0] = j
                    
                    # change reject status
                    all_reject = False
                    
                    # reduce number of jobs available for job j
                    available_positions[j] -= 1
                    
                    # check number of positions 
                    if available_positions[j] == 0:
                        
                        # all positions have been filled
                        company_ids[j] = -1
                        break
                        
                    # make sure this company cannot make another offer to the same candidate
                    offers[candidate_id][1].append(company_id)
                    break
                    
                else:
                    # make offer, then candidate chooses the company they compare best with
                    k = offers[candidate_id][0] # id of company candidate has an offer from
                    prev_offer_score = compatibility_matrix.loc[candidate_id, k]
                    curr_offer_score = compatibility_matrix.loc[candidate_id, j]
                    
                    if curr_offer_score > prev_offer_score:
                        
                        # candidate accepts new offer 
                        offers[candidate_id][0] = j
                        
                        # change reject status
                        all_reject = False
                        
                        # old offer now becomes free
                        available_positions[k] += 1
                        
                        # current job position is not available to other candidates, so decrement
                        available_positions[j] -= 1
                        
                        # check if old job has new positions free
                        if available_positions[k] == 1: company_ids[k] = k    
                            
                        # check if new job has been completely filled out
                        if available_positions[j] == 0: company_ids[j] = -1  
                            
                    else:
                        # candidate rejects new offer - add this company to the banned list for this candidate
                        offers[candidate_id][1].append(company_id)
                    break
                    
        # if company rejected by all students, then remove it from being considered next
        if all_reject: company_ids[j] = -1
            
        # save number of fulfilled companies after current iteration
        fulfillments.append(company_ids.count(-1))
        iterations += 1
        
    if iterations >= max_iterations: print("Termination due to time-out")
        
    return [offers, fulfillments]

# run the Gale-Shapley algorithm for a range of candidates and jobs
def run_gale_shapley(candidates, jobs, number_of_candidates, number_of_jobs):
    
    print(f"\nRunning Gale-Shapley for {number_of_candidates} candidates and {number_of_jobs} jobs...")

    # reduce size of candidates and jobs dataframes 
    candidates_dataframe = candidates.loc[:number_of_candidates]
    jobs_dataframe = jobs.loc[:number_of_jobs]
    
    # compute the compatibility matrix
    compatibility_matrix = compute_compatibility_matrix(candidates_dataframe, jobs_dataframe)

    # keeps track of companies with job offers to still give out 
    company_ids = compatibility_matrix.columns.tolist()

    # keeps track of the offers made so far, candidate_id : (current_offer_company_id, [refusing_company_id1, ...])
    offers = { candidate_id : [None, []] for candidate_id in range(number_of_candidates + 1) }

    # keeps track of the number of positions left per job
    available_positions = [ jobs_dataframe.loc[job_id, "Positions"] for job_id in range(len(jobs_dataframe)) ]
    
    # compute the total number of positions across number_of_jobs jobs
    total_jobs = sum(available_positions)
    
    # run the Gale-Shapley algorithm between the jobs and candidates dataset
    offers, fulfillments = gale_shapley(company_ids, offers, compatibility_matrix, available_positions)

    return offers