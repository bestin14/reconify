import subprocess
from termcolor import cprint
import requests


print('\n\n\n')

print('''██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗███████╗██╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██║██╔════╝╚██╗ ██╔╝
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║██║█████╗   ╚████╔╝ 
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██║██╔══╝    ╚██╔╝  
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██║██║        ██║   
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝        ╚═╝   
                                                               ''')



def resume():

  cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="Resuming where the script has been stopped before"']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  completed_cmds =  [line.rstrip() for line in open('resume.txt')]

  for cmd,run in url_finding_cmds.items() :

    if cmd not in completed_cmds :
      run() 




#--------------------------- url finding fucntions ----------------------------------------------


url_files = ''
js_files = ''
js_urls = ''


#---------- passive url finding--------

def wayback():

  cprint('Using passive methods for url finding \n','magenta') 
  global url_files

  ''' Finding wayback urls '''
  
  cprint('[*] Using the waybackurl tool \n','yellow')
  cmd = ['sh', '-c', f'waybackurls {dom_ch}> wayback_urls']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  url_files += 'wayback_urls '
  cprint('[*] Tool ran succesfully\n','green')

  cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="Wayback url tool ran sucessfully"']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  save_prog.write('Wayback\n')




def gau() :

  global url_files

  ''' Finding gau urls '''

  cprint('[*] Using the gau tool \n','yellow')
  cmd = ['sh', '-c', f'gau {dom_ch}> gau_urls']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  url_files += 'gau_urls '
  cprint('[*] Tool ran succesfully\n','green')

  cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="Gau tool ran succesfully"']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  save_prog.write('Gau\n')

#---------- active url finding--------

def gospider():

  cprint('Using active methods to find urls \n','magenta')

  global url_files
  save_prog.write('Gospider\n')

  ''' Finding gospider urls '''
    
  
  cprint('[*] Using the gospider tool \n','yellow')
  url_files += 'gospider_urls '
  cprint('[-->] Beware if the target is using a protection your ip may get blocked , so choose the thread wisely\n','red')
  thread = int(input('Enter the threads for crawling '))
  cmd = ['sh', '-c', f"gospider -s https://{dom_ch} -c {thread} -m 10 | grep -Eo '(http|https)://{dom_ch}[a-zA-Z0-9./?_%:-=&+-~:#@!$,;()]*' > gospider_urls"]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="Gospider tool ran succesfully"']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  cprint('[*] Tool ran succesfully\n','green')

  req = requests.head(f"https://{dom_ch}")
  status = req.status_code

    
  if status != 200:

    cprint('[*] Tool has been caught, urls upto current this has been captured . Please restart the router\n','red') 

    cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="Gospider tool got blocked, firewall is placed. Please restart the router to get access to target again and resume"']
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
    exit()




def xlinks() :

  global url_files
  cprint('[*] Running the xnlinkfinder tool \n','yellow')
  cmd = ['sh', '-c', f"python3 xnLinkFinder/xnLinkFinder.py -i {dom_ch} -sp https://{dom_ch} -o hi;cat hi | grep  -Eo '(http|https)://{dom_ch}[a-zA-Z0-9./?_%:-=&+-~:#@!$,;()]*' > xlinks"]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  cprint('[*] Tool ran succesfully\n','green')
  url_files += 'xlinks '

  cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="Xlink tool ran sucessfully"']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  save_prog.write('Xlinks\n')


def hawcrawler() :

  global url_files
  save_prog.write('Hawcrawler\n')

  try:
    cprint('[*] Running the hawcraler tool\n','yellow')
    url_files += 'hakrawler_urls '
    cmd = ['sh', '-c', f"echo https://{dom_ch} | hakrawler -u  | grep -Eo '(http|https)://{dom_ch}[a-zA-Z0-9./?_%:-=&+-~:#@!$,;()]*'> hakrawler_urls"]   #in dev
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL,timeout=180)
    cprint('[*] Tool ran succesfully\n','green')

    cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="Hakrawler tool ran succesfully"']
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  except:
    cprint('[*] Tool has been caught, urls upto current this has been captured\n ','red') 

    cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="Hakrawler tool got blocked, firewall is placed. Please restart the router to get access to target again and resume"']
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL) 
    exit()
    

#-----------------------------------arranging the found links ---------------------------------------------


def url_links() :

  save_prog.write('Url_links')

  cmd = ['sh', '-c', f"cat {url_files} | httpx -status-code -mc 200,204,302,307,401,403,405,500 | sed  's/\[[^]]*\]//g' | sort | uniq -u >final_urls" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)


def js_links() :

  save_prog.write('Js_links')
  
  cmd = ['sh', '-c', f"cat {js_files} | sort | uniq -u >js_urls" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)


def final_urls():

  save_prog.write('Final_urls')
  
  cmd = ['sh', '-c', f"cat {js_urls} | httpx -status-code -mc 200,204,302,307,401,403,405,500 | sed  's/\[[^]]*\]//g' | sort | uniq -u >>final_urls" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  cmd = ['sh', '-c', f"cat final_urls | urldedupe/urldedupe -u final_urls > uniq_urls" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  cmd = ['sh', '-c', f"echo status 200 live urls are shown below > output_urls; echo '' >> output_urls; cat uniq_urls | httpx -status-code -mc 200,204| sed 's/\[[^]]*\]//g' | sort | uniq -u >>output_urls; echo '' >> output_urls" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  cmd = ['sh', '-c', f"echo status 403 and other live urls are shown below >> output_urls; echo '' >> output_urls; cat uniq_urls | httpx -status-code -mc 302,307,401,403,405,500| sed 's/\[[^]]*\]//g' | sort | uniq -u >>output_urls" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  cprint('Urls from the domain has been collected and saved to output_urls file \n Removing unwanted files \n','cyan')
  cprint('Make sure to collect urls from burp spidering also!!','cyan')

  cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="THE SCRIPT IS COMPLETED"']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  #rm_files()


#-----------------------------------finding javascript files ---------------------------------------------



def fromlinks():

  cprint('Running tools for finding js files\n ','magenta')

  global js_files

  cprint('Collecting js files from final_urls\n','yellow')
  try:

    save_prog.write('Fromlinks\n')
    cmd = ['sh', '-c', "cat final_urls | grep '\.js$' > from_links" ]
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
    cmd = ['sh', '-c', f"cat final_urls from_links | sort | uniq -u >final_urls" ]
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
    js_files +='from_links '
    cprint('Proccess completed succesfully','green')
    
    cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="Js links collected from collected urls"']
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  except:
    cprint('No js urls were found in the links bro\n','blue')  

    cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="No js links found from collected urls"']
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)



def subjs():

  global js_files

  cprint('[*]Using the subjs tool\n','yellow')
  cmd = ['sh', '-c', "cat final_urls | subjs > sub_js" ]
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  js_files +='sub_js '
  cprint('[*] Tool ran succesfully\n','green')

  cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="SubJs tool ran succesfully"']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  save_prog.write('Subjs\n')




#-----------------------------------url finding from javascript files---------------------------------------------


# def linkfinder() :

#   cprint('[*] Running the linkfinder tool\n','green''')
#   cmd = ['sh', '-c','linkfinder.py -i js_urls -o linkfinder.html']    
#   subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
#   cprint('[*] Tool ran succesfully','green')


def jsfinder():

  cprint('Running tools for finding urls from js files\n','magenta')

  global js_urls
  
  cprint('[*] Running the jsfinder tool\n','yellow')
  cmd = ['sh', '-c', f'python3 JSFinder/JSFinder.py -f final_urls -ou jsfinder_urls ']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  cprint('[*] Tool ran succesfully\n','green')
  js_urls+='jsfinder_urls '

  cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="JSFinder tool ran succesfully"']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  save_prog.write('Jsfinder\n')


def xnlinfinder() :

  global js_urls

  cprint('[*] Running the xnlinkfinder tool\n','yellow')
  cmd = ['sh', '-c', f'python3 xnLinkFinder/xnLinkFinder.py -i js_urls -sp https://{dom_ch} -o xlinkfinder_urls']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
  cprint('[*] Tool ran succesfully\n','green')
  js_urls+='xlinkfinder_urls '

  cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="Xnlinkfinder tool ran succesfully"']
  subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  save_prog.write('Xnlinkfinder\n')

#-------------------------------------------------main part of the script----------------------------------------------------------------


def choose() :

  global choice

  choice = int(input(('''choose any of the following options 

          [1] Scan urls on the domain
          [2] Find vulnerable endpoints
          [3] Run vulnerabilty tools
          [3] Resume the script\n==>
          ''')))

  if choice == 1:

    cmd = ['sh', '-c', f'curl -s -X POST https://api.telegram.org/bot{token}/sendMessage -d chat_id=948413312 -d text="The script has started running"']
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

    for cmd in url_finding_cmds:
      url_finding_cmds[cmd]()


  elif choice == 3:
    
    resume() 
     

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



def rm_files():

    ## Removing unwanted files 
  try:

    cmd = ['sh', '-c', 'rm xlinkfinder_urls jsfinder_urls sub_js js_urls xlinks gospider_urls gau_urls wayback_urls hi from_links hakrawler_urls uniq_urls final_urls resume.txt parameters.txt']
    subprocess.run(cmd,check=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)

  except:
    pass


def main():

  ''' chooose for subdoamin list or enumeration '''

  global token

  token = input('Please enter your telegram bot token for notifying you on what is happening\n==>')

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
  
  url_finding_cmds = {'Wayback':wayback, 'Gau':gau, 'Gospider':gospider , 'Xlinks':xlinks, 'Hawcrawler':hawcrawler, 'Url_links':url_links, 
  'Fromlinks':fromlinks, 'Subjs':subjs, 'Js_links':js_links, 'Jsfinder':jsfinder, 'Xnlinfinder':xnlinfinder,'Final_urls':final_urls,'Rm_files':rm_files }

  save_prog = open('resume.txt','a+')

  main()

  
  
  
  




