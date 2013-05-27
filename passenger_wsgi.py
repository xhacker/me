import sys, os
INTERP = os.path.join(os.environ['HOME'], 'www', 'bin', 'python')
if sys.executable != INTERP:
	os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

sys.path.append('.')
from hello import app as application
