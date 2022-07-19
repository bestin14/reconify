import subprocess
from termcolor import colored, cprint


print('\n\n\n')

print('''██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗███████╗██╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██║██╔════╝╚██╗ ██╔╝
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║██║█████╗   ╚████╔╝ 
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██║██╔══╝    ╚██╔╝  
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██║██║        ██║   
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝        ╚═╝   
                                                               ''')


#--------------------------- url finding fucntions ----------------------------------------------


url_files = ''
js_files = ''
js_urls = ''


#---------- passive url finding--------

def wayback():

  global url_files

  ''' Finding wayback urls '''
  
  cprint('[*] Using the waybackurl tool \n','yellow')
  cmd = ['sh', '-c', f'waybackurls {dom_ch}> wayback_urls']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  url_files += 'wayback_urls '
  cprint('[*] Tool ran succesfully\n','green')




def gau() :

  global url_files

  ''' Finding gau urls '''

  cprint('[*] Using the gau tool \n','yellow')
  cmd = ['sh', '-c', f'gau {dom_ch}> gau_urls']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  url_files += 'gau_urls '
  cprint('[*] Tool ran succesfully\n','green')

#---------- active url finding--------

def gospider():

  global url_files

  ''' Finding gospider urls '''

  try :
    cprint('[*] Using the gospider tool \n','yellow')
    url_files += 'gospider_urls '
    cprint('[-->] Beware if the target is using a protection your ip may get blocked , so choose the thread wisely','red')
    thread = int(input('Enter the threads for crawling '))
    cmd = ['sh', '-c', f"gospider -s https://{dom_ch} -c {thread} -m 10 | grep -Eo '(http|https)://{dom_ch}[a-zA-Z0-9./?_%:-]*' > gospider_urls"]
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
    cprint('[*] Tool ran succesfully\n','green')

  except:
    cprint('[*] Tool has been stuck, urls upto current this has been captured \n','red') 




def xlinks() :

  global url_files
  cprint('[*] Running the xnlinkfinder tool \n','yellow')
  cmd = ['sh', '-c', f'python3 xnLinkFinder/xnLinkFinder.py -i {dom_ch} -sp https://{dom_ch} -o hi;cat hi | grep {dom_ch} > xlinks']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  cprint('[*] Tool ran succesfully\n','green')
  url_files += 'xlinks '



# def crawlergo():

#   global url_files

#   # chromium should be installed before running

#   cmd = ['sh', '-c', f"bin/crawlergo -c /tmp/chromium/chrome f{dom_ch} | grep http > crawlurls" ]
#   subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
#   url_files += 'gospider_urls '  




def hawcrawler() :

  global url_files

  try:
    cprint('[*] Running the hawcraler tool\n','yellow')
    url_files += 'hakrawler_urls '
    cmd = ['sh', '-c', f'echo https://{dom_ch} | hakrawler -u > hakrawler_urls']   #in dev
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL,timeout=180)
    cprint('[*] Tool ran succesfully\n','green')

  except:
    cprint('[*] Tool has been stuck, urls upto current this has been captured\n ','red')  
    

#-----------------------------------arranging the found links ---------------------------------------------


def url_links() :

  cmd = ['sh', '-c', f"cat {url_files} | httpx -status-code -mc 200,204,302,307,401,403,405,500 | sed  's/\[[^]]*\]//g' | sort | uniq -u >final_urls" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)


def js_links() :
  
  cmd = ['sh', '-c', f"cat {js_files} | sort | uniq -u >js_urls" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)


def final_urls():

  cmd = ['sh', '-c', f"cat {js_urls} | httpx -status-code -mc 200,204,302,307,401,403,405,500 | sed  's/\[[^]]*\]//g' | sort | uniq -u >>final_urls" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)


#-----------------------------------finding javascript files ---------------------------------------------



def fromlinks():

  global js_files

  cprint('Collecting js files from final_urls\n','yellow')
  try:
    cmd = ['sh', '-c', "cat final_urls | grep '\.js$' > from_links" ]
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
    cmd = ['sh', '-c', f"cat final_urls from_links | sort | uniq -u >final_urls" ]
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
    js_files +='from_links '
    cprint('Proccess completed succesfully','green')

  except:
    cprint('No js files were found in the links bro\n','blue')  



def subjs():

  global js_files

  cprint('[*]Using the subjs tool\n','yellow')
  cmd = ['sh', '-c', "cat final_urls | subjs > sub_js" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  js_files +='sub_js '
  cprint('[*] Tool ran succesfully\n','green')




#-----------------------------------url finding from javascript files---------------------------------------------



# def linkfinder() :

#   cprint('[*] Running the linkfinder tool\n','green''')
#   cmd = ['sh', '-c','linkfinder.py -i js_urls -o linkfinder.html']    
#   subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
#   cprint('[*] Tool ran succesfully','green')



# def secretfinder() :
   
#   cprint('[*] Running the secrectfinder tool\n','green''')
#   cmd = ['sh', '-c','SecretFinder.py -i js_urls -o secrectfinder.html'] 
#   subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL) 
#   cprint('[*] Tool ran succesfully','green') 


def jsfinder():

  global js_urls

  cprint('[*] Running the jsfinder tool\n','yellow')
  cmd = ['sh', '-c', f'python3 JSFinder/JSFinder.py -f final_urls -ou jsfinder_urls ']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  cprint('[*] Tool ran succesfully\n','green')
  js_urls+='jsfinder_urls '


def xnlinfinder() :

  global js_urls

  cprint('[*] Running the xnlinkfinder tool\n','yellow')
  cmd = ['sh', '-c', f'python3 xnLinkFinder/xnLinkFinder.py -i js_urls -sp https://{dom_ch} -o xlinkfinder_urls']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  cprint('[*] Tool ran succesfully\n','green')
  js_urls+='xlinkfinder_urls '


#-------------------------------------------------main part of the script----------------------------------------------------------------


def choose() :

  choice = int(input(('''choose any of the following options 

          [1] Scan urls on the domain
          [2] Find vulnerable endpoints
          [3] Run vulnerabilty tools\n==>
          ''')))

  if choice == 1:

    cprint('Using passive methods for url finding \n','magenta')
    wayback()
    gau()
    
    cprint('Using active methods to find urls \n','magenta')
    gospider()
    xlinks()
    hawcrawler()
    url_links()
    

    cprint('Running tools for finding js files\n ','magenta')
    fromlinks()
    subjs()
    js_links()

    cprint('Running tools for finding urls from js files\n','magenta')
    jsfinder()
    xnlinfinder()
    final_urls()

    cprint('Urls from the domain has been collected and saved to final_urls file \n Removing unwanted files \n','cyan')
    cprint('Make sure to collect urls from burp spidering also!!')
    cmd = ['sh', '-c', 'rm xlinkfinder_urls jsfinder_urls sub_js js_urls xlinks gospider_urls gau_urls wayback_urls hi from_links hakrawler_urls']
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)    


  elif choice == 2:
    pass
     

  else :

    print('Wrong choice exiting the program')        


def checkf() :
  
  ''' Reciveing the subdoamin and choosing the doamin to enum '''
  
  f_name = input("Enter the file name ")
  
  try:
    f_holder = open(f"{f_name}","r")
    subdom = f_holder.readlines()
    n=1
    global dom_ch

    for i in subdom:
      print(f"[{n}] ",i.rstrip('\n'))
      n+=1
    
    ch = int(input(("please select a domain to scan: ")))
    print('\n')
    dom_ch = subdom[ch-1].rstrip('\n')


    choose()

  except Exception as e:
    raise e



def main():

  ''' chooose for subdoamin list or enumeration '''

  print("Enter your choice\n")
  print('''[1] Subdomain Enumeration
[2] Enter  Subdomain file name''')
  
  choice = int(input("\n=> "))
  if choice == 1:
    pass
    #subenum()                 # For future dev 
  elif choice == 2:
    checkf()
  


if __name__ == '__main__' :

 main()

  
  
  
  




