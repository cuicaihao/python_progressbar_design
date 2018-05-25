# There are many ways to use Python ProgressBar, you can see a few basic examples here but there are more in the next example.py file.

#%% 1 wrapping and iterable
import time
import progressbar

progressbar.streams.flush()

for i in progressbar.progressbar(range(100)):
	time.sleep(0.02)

#%% Progressbar with loggingg

#import progressbar 
#progressbar.streams.flush()
#for i in progressbar.progressbar(range(100)):
#	time.sleep(0.02)