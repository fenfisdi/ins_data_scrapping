import pandas as pd
import numpy as np

from covidcolombia import Report

def get_each_df(region, init_day, final_day, path):
    '''
    '''

    # Report creation
    report = Report(path, date=final_day, region=region, age_range=(0,'MAX_AGE'))

    # df filling
    dates = pd.date_range(init_day, final_day)
    deaths = []; recovered = []; infected = []; active_cases = []

    for days1 in dates:
        one, two, three = report.get_SIR_populations(day=days1, mode='cummulative')
        deaths.append(one); recovered.append(two); infected.append(three)
        active_cases.append(three-two-one)

    all_data = np.transpose(np.array([active_cases, infected, recovered, deaths]))
    df = pd.DataFrame(all_data, columns=['active_cases', 'I', 'R', 'D'] )
    df['date'] = dates

    return df
