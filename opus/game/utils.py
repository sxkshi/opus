from django.utils import timezone
import datetime
from pytz import timezone as tz
from user.models import UserProfile

REDIRECT='redirect'

STAY='stay'


DAYS={
    'day1':{
        'start_question':1,
        'end_question':22,
        'branches':[101,102,103,104,105,106,107,108,109],
        'date':datetime.datetime(2022,10,11,00,00,00,00,tzinfo=tz('Asia/Kolkata')),
    },
   'day2':{
        'start_question':23,
        'end_question':45,
        'branches':[110,111,112],
        'date':datetime.datetime(2022,10,11,tzinfo=tz('Asia/Kolkata')),
    },
    'day3':{
        'start_question':46,
        'end_question':69,
        'branches':[113,114,115],
        'date':datetime.datetime(2022,10,12,tzinfo=tz('Asia/Kolkata')),
    },
    'day4':{
        'start_question':70,
        'end_question':100,
        'branches':[129,130,131,132,143,144,133,134,145,146,147,148,135,136],
        'date':datetime.datetime(2022,10,12,tzinfo=tz('Asia/Kolkata')),
    },
}


BRANCHES=list(range(101,115))



def check_day_end(question_number) ->dict:
    now=timezone.localtime()
    print(now)

    # print("now: ",now.date())

    # print("day1: ",DAYS['day1']['date'].date())
    
    if now.date() < DAYS['day1']['date'].date(): #Redirect to welcome page
        return {'status':REDIRECT,'day':0}

    for day in range(1,3):
        if (now.date() < DAYS['day'+str(day+1)]['date'].date()) and (question_number>DAYS['day'+str(day)]['end_question']) and (question_number not in BRANCHES): 
            return {'status':REDIRECT,'day':day}  #Redirect to particular day end
    
    if now.date() > DAYS['day3']['date'].date():
        return {'status':REDIRECT,'day':3}

    return {'status':STAY,'day':-1} #Continue





def get_rank(user:UserProfile) ->int:

    pk=user.pk
    rank =1

    people=UserProfile.objects.filter(points__gte=user.points).exclude(user__is_active=False).order_by('-points','last_answered')

    rank =1

    for person in people:
        if person.pk==pk:
            break
        rank+=1

    return rank
