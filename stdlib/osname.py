import sys
f=open("./buffer.af","w")
platform=sys.platform
f.write('v nameos = "'+platform+'"')