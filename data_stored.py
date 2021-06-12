import pandas as pd
import os
import random

def data_store_to_csv(fullname,relocate,salary_satisfied,knowledge,experience):
    if os.path.isfile('fresher.xlsx'):
        df=pd.read_excel('fresher.xlsx')
        #df1=pd.DataFrame([[fullname,relocate,salary_satisfied,knowledge,experience]],columns=['fullname','relocate','salary_satisfied','knowledge','experience'])
        df1=pd.Series([int(random.randint(12500,99999)),fullname,relocate,salary_satisfied,knowledge,experience,None])
        df1.index=['application id','fullname','relocate','salary_satisfied','knowledge','experience','status']
        if df1.relocate=='no':
            df1.fillna(value={'status':'cancel'},inplace=True)
        elif df1.salary_satisfied=='no':
            df1.fillna(value={'status':'cancel'},inplace=True)
        elif df1.experience=='no':
            df1.fillna(value={'status':'cancel'},inplace=True)
        elif df1.knowledge=='no':
            df1.fillna(value={'status':'cancel'},inplace=True)
        else:
            df1.fillna(value={'status':'accepted'},inplace=True)
        df1=df1.to_frame()
        df1=df1.T
        df=df.append(df1,ignore_index=True)
        df.to_excel('fresher.xlsx',index=False)
        
# def print_status():
#     df=pd.read_excel('user_data.xlsx')
#     if df.iat[-1, -1]=='accepted':
#         return int(df.iat[-1, 0])#print('Your application is accepted with application id',int(df.iat[-1, 0]))
#     else:
#         return 'Your application status is rejected'
    
def print_status():
    data=pd.read_excel('fresher.xlsx')
    if data.iat[-1, -1]=='accepted':
        #a=int(data.iat[-1, 0]
        return 'Congradulations !! Your application is accepted with application id {}. Our HR team will contact with you.'.format(int(data.iat[-1, 0]))
        #print('your id',int(data.iat[-1, 0]))
    else:
        return 'Your application status is rejected'
    
def data_store_to_csv_fresher(fullname,relocate,salary_satisfied,knowledge,domain):
    if os.path.isfile('fresher.xlsx'):
        df=pd.read_excel('fresher.xlsx')
        #df1=pd.DataFrame([[fullname,relocate,salary_satisfied,knowledge,experience]],columns=['fullname','relocate','salary_satisfied','knowledge','experience'])
        df1=pd.Series([int(random.randint(12500,99999)),fullname,domain,relocate,salary_satisfied,knowledge,None])
        df1.index=['application id','fullname','domain','relocate','salary_satisfied','knowledge','status']
        if df1.relocate=='no':
            df1.fillna(value={'status':'cancel'},inplace=True)
        elif df1.salary_satisfied=='no':
            df1.fillna(value={'status':'cancel'},inplace=True)
        elif df1.knowledge=='no':
            df1.fillna(value={'status':'cancel'},inplace=True)
        else:
            df1.fillna(value={'status':'accepted'},inplace=True)
        df1=df1.to_frame()
        df1=df1.T
        df=df.append(df1,ignore_index=True)
        df.to_excel('fresher.xlsx',index=False)
        
def data_store_to_csv_experience(fullname,domain,relocate,salary_satisfied,knowledge,year_satisfied):
    if os.path.isfile('experience.xlsx'):
        df=pd.read_excel('experience.xlsx')
        #df1=pd.DataFrame([[fullname,relocate,salary_satisfied,knowledge,experience]],columns=['fullname','relocate','salary_satisfied','knowledge','experience'])
        df1=pd.Series([int(random.randint(12500,99999)),fullname,domain,relocate,salary_satisfied,knowledge,year_satisfied,None])
        df1.index=['application id','fullname','domain','relocate','salary_satisfied','knowledge','year_satisfied','status']
        if df1.relocate=='no':
            df1.fillna(value={'status':'cancel'},inplace=True)
        elif df1.salary_satisfied=='no':
            df1.fillna(value={'status':'cancel'},inplace=True)
        elif df1.knowledge=='no':
            df1.fillna(value={'status':'cancel'},inplace=True)
        else:
            df1.fillna(value={'status':'accepted'},inplace=True)
        df1=df1.to_frame()
        df1=df1.T
        df=df.append(df1,ignore_index=True)
        df.to_excel('experience.xlsx',index=False)
        
def print_status_experience():
    data=pd.read_excel('experience.xlsx')
    if data.iat[-1, -1]=='accepted':
        #a=int(data.iat[-1, 0]
        return 'Congradulations !! Your application is accepted with application id {}. Our HR team will contact with you.'.format(int(data.iat[-1, 0]))
        #print('your id',int(data.iat[-1, 0]))
    else:
        return 'Your application status is rejected'
    