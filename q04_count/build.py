# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    deliveries_1 = data['innings'][0]['1st innings']['deliveries']
    for x in deliveries_1:
        for i in x:
            if x[i]['batsman'] == 'RT Ponting':
                count = count+1
        
    
    

    return count

deliveries_count() 


