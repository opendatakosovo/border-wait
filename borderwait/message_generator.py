def enter_exit(border, entry_min, entry_max, exit_min,exit_max):
    entry_time = convert_time(entry_min, entry_max)
    exit_time  = convert_time(exit_min, exit_max)
    text = 'pritja 'u'\xeb''sht'u'\xeb'' '
    print
    if entry_time == '' and exit_time == '':
        return 'Kufiri #%s: nuk ka pritje p'u'\xeb''r t'u'\xeb'' hyr'u'\xeb'' dhe p'u'\xeb''r t'u'\xeb'' dalur n'u'\xeb'' #Kosov'u'\xeb''.\n #Mir'u'\xeb''sevini #Rrug'u'\xeb''T'u'\xeb''Mbar'u'\xeb''' % (border)
    if entry_time != '':
        text += entry_time
    else:
        text = 'nuk ka pritje'
    return 'Kufiri #%s: %s p'u'\xeb''r t'u'\xeb'' hyr'u'\xeb'' n'u'\xeb'' #Kosov'u'\xeb'' dhe %s p'u'\xeb''r t'u'\xeb'' dalur.\n #Mir'u'\xeb''sevini #Rrug'u'\xeb''T'u'\xeb''Mbar'u'\xeb''' % (border,text, exit_time)

def enter(border, entry_min, entry_max):
    entry_time = convert_time(entry_min, entry_max)
    text = 'pritja 'u'\xeb''sht'u'\xeb'' '
    if entry_time != '':
        text += entry_time
    else:
        text = 'nuk ka pritje'
    return 'Kufiri #%s: %s p'u'\xeb''r t'u'\xeb'' hyr'u'\xeb'' n'u'\xeb'' #Kosov'u'\xeb''. #Mir'u'\xeb''sevini' % (border, text)

def exit(border, exit_min, exit_max):
    exit_time  = convert_time(exit_min, exit_max)
    text = 'pritja 'u'\xeb''sht'u'\xeb'' '
    if exit_time != '':
        text += exit_time
    else:
        text = 'nuk ka pritje'
    return 'Kufiri #%s: %s p'u'\xeb''r t'u'\xeb'' dalur nga #Kosova. #Rrug'u'\xeb''T'u'\xeb''Mbar'u'\xeb''' % (border, text)

def convert_time(min_time, max_time):
    min_hours = min_time / 60
    min_minutes = min_time % 60
    max_hours = max_time / 60
    max_minutes = max_time % 60
    text = ''
    if min_minutes==max_minutes==min_hours==max_hours==0:
        text = ''
    elif min_hours == 0 and max_hours == 0:
        if min_minutes!=0 and max_minutes==0:
            text += '%s minuta'%(min_minutes)
        elif min_minutes != 0 and max_minutes != 0:
            if min_minutes != max_minutes:
                text += '%s deri %s minuta'%(min_minutes,max_minutes)
            else:
                text += '%s minuta'%min_minutes
        elif min_minutes == 0 and max_minutes != 0:
            text += '%s minuta'%(max_minutes)
        else:
            text += '%s minuta'%min_minutes
    elif min_hours == 0 and max_hours != 0:
        if min_minutes!=0 and max_minutes==0:
            text += '%s minuta deri %s or'u'\xeb'''%(min_minutes,max_hours)
        elif min_minutes != 0 and max_minutes != 0:
            text += '%s minuta deri %s or'u'\xeb'' e %s minuta'%(min_minutes,max_hours,max_minutes)
        elif min_minutes == 0 and max_minutes != 0:
            text += '%s or'u'\xeb'' e %s minuta'%(max_hours,max_minutes)
        else:
            text += '%s or'u'\xeb''' %max_hours
    elif min_hours != 0 and max_hours != 0:
        if min_hours == max_hours:
            if min_minutes!=0 and max_minutes==0:
                text += '%s or'u'\xeb'' e %s minuta deri %s or'u'\xeb'''%(min_hours,min_minutes,max_hours)
            elif min_minutes != 0 and max_minutes != 0:
                if min_minutes == max_minutes:
                    text += '%s or'u'\xeb'' e %s minuta'%(min_hours,min_minutes)
                else:
                    text += '%s or'u'\xeb'' e %s minuta deri %s or'u'\xeb'' e %s minuta'%(min_hours,min_minutes,max_hours,max_minutes)
            elif min_minutes == 0 and max_minutes != 0:
                text += '%s or'u'\xeb'' deri %s or'u'\xeb'' e %s minuta'%(min_hours,max_hours,max_minutes)
            else:
                text += '%s or'u'\xeb''' %min_hours
        else:
            if min_minutes!=0 and max_minutes==0:
                text += '%s or'u'\xeb'' e %s minuta deri %s or'u'\xeb'''%(min_hours,min_minutes,max_hours)
            elif min_minutes != 0 and max_minutes != 0:
                text += '%s or'u'\xeb'' e %s minuta deri %s or'u'\xeb'' e %s minuta'%(min_hours,min_minutes,max_hours,max_minutes)
            elif min_minutes == 0 and max_minutes != 0:
                text += '%s or'u'\xeb'' deri %s or'u'\xeb'' e %s minuta'%(min_hours,max_hours,max_minutes)
            else:
                text += '%s deri %s or'u'\xeb''' %(min_hours,max_hours)
    else:
        text = ''
    return text
