#reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 0x00000001 /f

colors = {\
    'OKBLUE' : '\033[94m',
     'OKGREEN' : '\033[92m',
    'WARNING' : '\033[93m',
    'RED' : '\033[1;31;40m',
}

def colorText(text):
    for color in colors:
        text = text.replace("[[" + color + "]]", colors[color])
    return text

hola = '''


[[OKGREEN]] 
_  _ ____  _  _ ____ 
/ )( (  _ \/ )( (  _ \
\ /\ /)   /\ /\ /)   /
[[RED]]_/\_|__\_)(_/\_|__\_)


'''

banner='''
[[RED]]     )                                                               
  ( /(             )                                                 
  )\()) (   (   ( /(                          )  (       )    (      
((_)\  )(  )\  )\()) (   (    (   (       ( /(  )(     (     )\ )   
_)((_)(()\((_)((_)\  )\  )\   )\  )\      )(_))(()\    )\  '(()/(   
[[OKGREEN]]| |/ /  [[RED]]((_)[[OKGREEN]](_)[[RED]]| |(_)((_)((_) ((_)((_)    ((_)_  ((_) _((_))  )(_))  
[[OKGREEN]]| ' <  | '_|| || / // _ \(_-</ _ \(_-<    / _` || '_|| '  \()| || |  
[[OKGREEN]]|_|\_\ |_|  |_||_\_\\\___//__/\___//__/    \__,_||_|  |_|_|_|  \_, |  
                                                              |__/  
                                                              '''
                                                              
xd = '''


                                                               
[[WARNING]]    )            )                                             
[[WARNING]] ( /( (   (   ( /(                       )  (       )    (     
[[WARNING]] )\()))(  )\  )\()) (   (    (   (    ( /(  )(     (     )\ )  
[[WARNING]]((_)\(()\((_)((_)\  )\  )\   )\  )\   )(_))(()\    )\  '(()/(  
[[OKGREEN]]| |[[WARNING]](_)((_)(_)[[OKGREEN]]| |[[WARNING]](_)((_)((_) ((_)((_) ((_)_  ((_) _((_))  )(_)) 
[[OKGREEN]]| / /| '_|| || / // _ \(_-</ _ \(_-< / _` || '_|| '  \[[WARNING]]()[[OKGREEN]]| || | 
[[OKGREEN]]|_\_\|_|  |_||_\_\\___//__/\___/ /__/ \__,_||_|  |_|_|_|  \_, | 
                                                         |__/  

[[OKBLUE]]
'''
             
print(colorText(banner))
print(colorText(xd))
print(colorText(hola))