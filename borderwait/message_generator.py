def enter_exit(border, entry_min, entry_max, exit_min,exit_max):
    entry_time = convert_time(entry_min, entry_max)
    exit_time  = convert_time(exit_min, exit_max)
    return 'Kufiri #%s: pritja 'u'\xeb''sht'u'\xeb'' %s p'u'\xeb''r t'u'\xeb'' hyr'u'\xeb'' n'u'\xeb'' #Kosov'u'\xeb'' dhe %s p'u'\xeb''r t'u'\xeb'' dalur.\n #Mir'u'\xeb''sevini #Rrug'u'\xeb''T'u'\xeb''Mbar'u'\xeb''' % (border,entry_time, exit_time)

def enter(border, entry_min, entry_max):
    entry_time = convert_time(entry_min, entry_max)
    return 'Kufiri #%s: pritja 'u'\xeb''sht'u'\xeb'' %s p'u'\xeb''r t'u'\xeb'' hyr'u'\xeb'' n'u'\xeb'' #Kosov'u'\xeb''. #Mir'u'\xeb''sevini' % (border, entry_time)

def exit(border, exit_min, exit_max):
    exit_time  = convert_time(exit_min, exit_max)
    return 'Kufiri #%s: pritja 'u'\xeb''sht'u'\xeb'' %s p'u'\xeb''r t'u'\xeb'' dalur nga #Kosova. #Rrug'u'\xeb''T'u'\xeb''Mbar'u'\xeb''' % (border, exit_time)

def convert_time(min_time, max_time):
    min_hours = min_time / 60
    min_minutes = min_time % 60
    max_hours = max_time / 60
    max_minutes = max_time % 60
    text = ''
    if min_hours == 0 and max_hours == 0:
        text += '%s deri %s minuta' % (min_minutes, max_minutes)
    elif min_minutes == 0 and max_minutes == 0:
        text += '%s deri %s or'u'\xeb''' % (min_hours, max_hours)
    elif  min_minutes != 0 and min_hours ==0 and max_minutes !=0 and max_hours !=0:
        text += '%s minuta deri %s or'u'\xeb'' e %s minuta' % (min_minutes, max_hours, max_minutes)
    elif min_minutes != 0 and min_hours ==0 and max_minutes !=0 and max_hours ==0:
        text += '% minuta deri %s or'u'\xeb''' % (min_minutes, min_hours)
    elif  min_minutes == 0 and min_hours !=0 and max_minutes !=0 and max_hours !=0:
        text += '%s or'u'\xeb'' deri %s or'u'\xeb'' e %s minuta' % (min_minutes, max_hours, max_minutes)
    elif min_minutes != 0 and min_hours !=0 and max_minutes ==0 and max_hours !=0:
        text += '%s or'u'\xeb'' e %s minuta deri %s or'u'\xeb''' % (min_hours, min_minutes, max_hours)
    else:
        text += '%s or'u'\xeb'' e %s minuta deri %s or'u'\xeb'' e %s minuta' % (min_hours, min_minutes, max_hours, max_minutes)
    return text
