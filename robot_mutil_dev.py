#coding=utf-8
import threading
from time import ctime,sleep
import os 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def run(arg):
   os.system(str(arg))

threads = []
testsuite=sys.argv[1]
tags=sys.argv[2]
sele_remote_host=sys.argv[3]
taglist=tags.split(',')

if sele_remote_host=='None':
   cmd='pybot -o .\\resultDir\\output.xml -l .\\resultDir\\log.html -r .\\resultDir\\report.html --variable sele_remote_host:{1} {0}'.format(sys.argv[1],sys.argv[3])
   t= threading.Thread(target=run,args=(cmd,))
   threads.append(t)
   
else:   
   for tag in taglist:
      cmd='pybot -i {0} -o .\\resultDir\\output-{0}.xml -l .\\resultDir\\log-{0}.html -r .\\resultDir\\report-{0}.html --variable sele_remote_host:{2} {1}'.format(tag,sys.argv[1],sys.argv[3]) 
      t= threading.Thread(target=run,args=(cmd,))
      threads.append(t)

if __name__ == '__main__':
    os.system('del /f/s/q/a .\\resultDir\\*')
    for t in threads:
        t.setDaemon(True)
        t.start()
        
    for t in threads:
        t.join()

    if sele_remote_host=='None':
       pass
    else:
       os.system(u"rebot --output .\\resultDir\\output.xml  -l .\\resultDir\\log.html -r .\\resultDir\\report.html --merge .\\resultDir\\output-*.xml")
    sleep(2)
    print "Test Finish"
