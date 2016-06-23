import sys
import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

def com(code):
	try:
		with stdoutIO() as s:
   			exec code
		sr = s.getvalue()
		return sr
	except Exception,e: 
		return "Error "+str(e)


