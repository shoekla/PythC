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


def compileA(code):
	res = "Executed Code: \n"
	firstGo = ""
	try:
		with stdoutIO() as s:
    		exec code
    	return s.getvalue()
	except Exception,e: 
		firstGo = "Error \n str(e)"

	res = str(res +"\n"+firstGo)
	return res

a="print 'Halo'"
d = compileA(a)
print d
