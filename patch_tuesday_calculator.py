import calendar
from datetime import datetime, date, timedelta

def get_patch_tuesday(arg1, arg2):
    cal = calendar.monthcalendar(arg1, arg2)
    first_week = cal[0]
    second_week = cal[1]
    third_week = cal[2]
    #Checks to see which week of the month the 2nd Tuesday falls on
    if first_week[calendar.TUESDAY] != 0:
        patch_tuesday = second_week[calendar.TUESDAY]
    else:
        patch_tuesday = third_week[calendar.TUESDAY]

    release_date = date(arg1,arg2,patch_tuesday)
    return release_date

def get_qa_deployment(arg1):
    #This deployment takes place 1 day after Patch Tuesday
    qa_deployment = (arg1 + timedelta(days = 1))
    qa_result = qa_deployment.strftime("%A, %B %d %Y")
    return qa_result

def get_dev_deployment(arg1):
    #This deployment takes place 3 days after Patch Tuesday
    dev_deployment = (arg1 + timedelta(days = 3))
    dev_result = dev_deployment.strftime("%A, %B %d %Y")
    return dev_result

def get_prod_deployment(arg1):
    #This deployment takes place 11 days after Patch Tuesday
    prod_deployment = (arg1 + timedelta(days = 11))
    prod_result = prod_deployment.strftime("%A, %B %d %Y")
    return prod_result

def main():
    #Calculates Patch Tuesday & deployment dates using today's date by default
    today = date.today()
    this_month = today.month
    this_year = today.year
    days_this_month = calendar.monthrange(this_year,this_month)[1]
    first_day = date(this_year, this_month, 1)
    next_month = (first_day + timedelta(days=days_this_month)).month

    target = get_patch_tuesday(this_year, this_month)
    #If current month's Patch Tuesday has already past
    if target < today:
        #If it's December and today's date is after December's Patch Tuesday,
        #the target year is changed to the new year
        if this_month == 12:
            target_year = today.replace(year=this_year + 1).year
        else:
            target_year = this_year
        result = get_patch_tuesday(target_year,next_month)
        format_result = result.strftime("%A, %B %d %Y")
        days_until = (result - today).days
        print("Next Patch Tuesday is:",format_result,"-",days_until,"days away")
    #If current month's Patch Tuesday is upcoming
    elif target > today:
        result = get_patch_tuesday(this_year,this_month)
        format_result = result.strftime("%A, %B %d %Y")
        days_until = (result - today).days
        print("Next Patch Tuesday is:",format_result,"-",days_until,"days away")
    elif target == today:
        result = date.today()
        format_result = result.strftime("%A, %B %d %Y")
        print("Patch Tuesday is today:", format_result)

    qa_deploy_date = get_qa_deployment(result)
    dev_deploy_date = get_dev_deployment(result)
    prod_peploy_date = get_prod_deployment(result)

    print("QA deployment date is:", qa_deploy_date)
    print("Dev deployment date is:", dev_deploy_date)
    print("Prod deployment date is:", prod_peploy_date)

if __name__ == "__main__":
    main()
