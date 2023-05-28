# Job Sequencing Problem 

def job_sequencing(jobs):
    # Sort the jobs based on their profits in descending order
    jobs.sort(key=lambda x: x['profit'], reverse=True)

    max_deadline = max(jobs, key=lambda x: x['deadline'])['deadline']
    schedule = [-1] * max_deadline  # Create a schedule with all slots initially empty

    # Iterate through each job and schedule it based on its deadline
    for job in jobs:
        deadline = job['deadline']
        while deadline > 0:
            if schedule[deadline-1] == -1:  # If the slot is empty
                schedule[deadline-1] = job
                break
            else:
                deadline -= 1

    # Filter out empty slots from the schedule
    schedule = [job for job in schedule if job != -1]

    # Extract the job IDs from the schedule in the order they were scheduled
    sequence = [job['id'] for job in schedule]

    return schedule, sequence

# Input number of jobs
n = int(input("Enter the number of jobs: "))

# Input job details
jobs = []
for i in range(n):
    id = input("Enter job ID for job {}: ".format(i+1))
    deadline = int(input("Enter deadline for job {}: ".format(i+1)))
    profit = int(input("Enter profit for job {}: ".format(i+1)))
    job = {'id': id, 'deadline': deadline, 'profit': profit}
    jobs.append(job)

schedule, sequence = job_sequencing(jobs)

# Print the scheduled jobs
print("Scheduled Jobs:")
for job in schedule:
    print("Job ID: {}, Deadline: {}, Profit: {}".format(
        job['id'], job['deadline'], job['profit']))

# Print the scheduled job sequence
print("Scheduled Job Sequence: {}".format(sequence))
