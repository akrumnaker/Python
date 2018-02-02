# This script will periodically open a browser telling
# telling the user to take a break and playing one of
# their favorite songs on youtube

import random
import time
import webbrowser

# list of songs to choose from
songs = ['https://www.youtube.com/watch?v=pBkHHoOIIn8',
         'https://www.youtube.com/watch?v=rVeMiVU77wo',
         'https://www.youtube.com/watch?v=bpOSxM0rNPM',
         'https://www.youtube.com/watch?v=aNYjOVo5IEw',
         'https://www.youtube.com/watch?v=TRqiFPpw2fY',
         'https://www.youtube.com/watch?v=SBjQ9tuuTJQ']

# number of repetitions during the day
repeat = 3

# amount of time to wait between playing songs (in seconds)
wait_time = 7200

# number of current iterations
num_times = 0

while num_times < repeat:
    # wait the specified amount of time
    time.sleep(wait_time)
    # increment number of times the loop has run
    num_times += 1
    # get a random index from the songs array
    index = random.randrange(0, len(songs))
    # open a new window with the url found at index in songs
    webbrowser.open(songs[index], 1)
