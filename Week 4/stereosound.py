import sound

##def rem_vocals(snd):
##    snd_copy=sound.Sound.copy(snd)
##    for sample in snd_copy:
##        left= sample.get_left()
##        right= sample.get_right()
##        new_value= int((left-right)/2.0)
##        new_value_left=sample.set_left(new_value)
##        new_value_right=sample.set_right(new_value)
##    return snd_copy


def fade_in(snd, fade_length):
    snd_copy=sound.Sound.copy(snd)
    for sample in snd_copy:
        fadevalue=float((int(fade_length)))
        i=sample.get_index()
        fade_multiple = i/fadevalue
        left= sample.get_left()
        right= sample.get_right()
        #print i , left , right
        if i < fade_length:
            new_value_l= int(left * fade_multiple)
            new_value_r= int(right * fade_multiple)
            new_value_left=sample.set_left(new_value_l)
            new_value_right=sample.set_right(new_value_r)
            #print new_value_l , new_value_r
        else:
            left= sample.get_left()
            right= sample.get_right()
    return snd_copy


##def fade_out(snd, fade_length):
##    global snd_copyy
##    subtract=0 
##    snd_copyy=sound.Sound.copy(snd)
##    number_samples = len(snd_copyy)
##    for sample in snd_copyy:
##        fadevalue=float((int(fade_length)))
##        indexes_faded = number_samples - fadevalue
##        i = sample.get_index()
##        left = sample.get_left()
##        right = sample.get_right()
##
##        if i >= indexes_faded:
##            subtract+=1
##            reverse = fadevalue - subtract
##            fade_multiple = reverse/fadevalue
##            new_value_l= left * fade_multiple
##            new_value_r= right * fade_multiple
##            new_value_left=sample.set_left(int(new_value_l))
##            new_value_right=sample.set_right(int(new_value_r))
##        else:
##            left= sample.get_left()
##            right= sample.get_right()
##    return snd_copyy
##
##
##def fade(snd, fade_length):
##    snd_copy = snd_copy()
##    snd_copy = fadein(snd_copy, fade_length)
##    snd_copy = fade_out(snd_copy, fade_length)
##    return snd_copy
