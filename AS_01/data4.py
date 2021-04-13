# import required modules
import random

# define global variables
jobs_list = ['medical', 'military', 'diplomatic', 'essential', 'teacher',
             'engineer', 'musician', 'chef', 'janitor', 'astronaut',
             'data scientist', 'salesperson', 'artist', 'builder', 'farmer']
data_no = 100


def data_p4(local_jobs_list, local_data_no):
    """
    This function will generate data for p4
    :param local_jobs_list: list of all the job titles
    :param local_data_no: total number of data entries in the dict
    :return: a dataset in dictionary format
    """
    # create an empty dict to begin with
    local_data_dict = {}

    # generate a data_no of entries in the dict
    for i in range(local_data_no):
        local_person_id = random.randint(10000, 99999)
        local_job = random.choice(local_jobs_list)
        local_age = random.randint(0, 120)
        local_area = random.choice([True, False])

        # add the generated data to a list
        local_data_dict[local_person_id] = [local_job, local_age, local_area]

    return local_data_dict


# test function
# data_dict = data_p4(jobs_list, data_no)
# print(data_dict)
