from weather_check import get_weather
from colorama import Fore, Style
import sys, time, os
# Add your code here and remember to remove all unused comments



print(f"""                                                                          {Fore.YELLOW} +   .       .  {Style.RESET_ALL}
     *  .  *                                                                  {Fore.YELLOW}  .  +  .     .   +{Style.RESET_ALL}
   . _\/ \/_ .                                                                 {Fore.YELLOW}.........   .  {Style.RESET_ALL}
    \  \ /  /                                                       --------{Fore.YELLOW} ............. +{Style.RESET_ALL}
  -==>: X :<==-     {Fore.CYAN}_  _  ____  __     ___  __   _  _  ____ {Style.RESET_ALL}      -------------{Fore.YELLOW}.............. . . {Style.RESET_ALL}
    / _/ \_ \      {Fore.CYAN}/ )( \(  __)(  )   / __)/  \ ( \/ )(  __){Style.RESET_ALL}    -----------------.---- {Fore.YELLOW}.......{Style.RESET_ALL}
   '  /\ /\  '     {Fore.CYAN}\ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _){Style.RESET_ALL}    -----------------------{Fore.YELLOW}.......  {Style.RESET_ALL}
     *  '  *       {Fore.CYAN}(_/\_)(____)\____/ \___)\__/ \_)(_/(____){Style.RESET_ALL} ----------------------------{Fore.YELLOW}...  . . {Style.RESET_ALL}
               .      .                                    ------------------------------------  
               _\/  \/_                 {Fore.LIGHTGREEN_EX} ____  __  {Style.RESET_ALL}          ------------------------------------ 
                _\/\/_                  {Fore.LIGHTGREEN_EX}(_  _)/  \  {Style.RESET_ALL}           --------------------------------
            _\_\_\/\/_/_/_              {Fore.LIGHTGREEN_EX}  )( (  O ) {Style.RESET_ALL}       {Fore.BLUE}+       +         -       . +{Style.RESET_ALL}
             / /_/\/\_\ \               {Fore.LIGHTGREEN_EX} (__) \__/  {Style.RESET_ALL}          {Fore.BLUE}+            +       +      + {Style.RESET_ALL}
                _/\/\_                             {Fore.BLUE}     + _       ' +          .      +        -  +{Style.RESET_ALL}
                /\  /\  {Fore.LIGHTMAGENTA_EX} _  _  ____   __  ____  _  _  ____  ____     ___  _  _  ____  ___  __ _  ____  ___{Fore.BLUE}+   + {Style.RESET_ALL}         
               '      ' {Fore.LIGHTMAGENTA_EX}/ )( \(  __) / _\(_  _)/ )( \(  __)(  _ \   / __)/ )( \(  __)/ __)(  / )(  __)(  _ \    
                        \ /\ / ) _) /    \ )(  ) __ ( ) _)  )   /  ( (__ ) __ ( ) _)( (__  )  (  ) _)  )   /    
                        (_/\_)(____)\_/\_/(__) \_)(_/(____)(__\_)   \___)\_)(_/(____)\___)(__\_)(____)(__\_)   {Style.RESET_ALL}
                                                                                                                                                                                     
""")

print(f"{Fore.LIGHTBLACK_EX}===========================================================================\n{Style.RESET_ALL}" )
print(f"{Fore.LIGHTBLUE_EX}                             ~ INSTRUCTION ~ {Style.RESET_ALL}\n")
print("              📍🔎 Enter a city to get the current weather 🏙️🌧️☀️🌦️❄️")
print("              🔴 If you want to quit, enter n or N 🤩")

while True:
    print("       ✨___________________________________________________________✨\n")
    city = input("             📍🔎 Enter the city that you want to know: ")
    result = get_weather(city)
    print(f"\n{Fore.LIGHTBLACK_EX}==========================================================================={Style.RESET_ALL}")



    
    print(f"""\n                                                       .==================.
                                                          {Fore.LIGHTMAGENTA_EX}CITY : {result['name']} {Style.RESET_ALL}
                    __I__                              '=================='
                .-'"  .  "'-.
              .'  / . ' . \  '.
             /_.-..-..-..-..-._\   .-----------------------------.
                  #  _,,_         ( {Fore.CYAN}  The temperature is {result['temp']} {Style.RESET_ALL}
                  #/`    `\      (  {Fore.LIGHTRED_EX}   but I feel like {result['feel']} {Style.RESET_ALL}
                  / / 6 6\ \  __/'-------------------------------'
                  \/\  Y /\/       /\-/\                        
                  #/ `'U` \       /a a  \               _      .-------------------------------------.
                , (  \   | \     =\ Y  =/-~~~~~~-,_____/ )    ( {Fore.LIGHTYELLOW_EX}  It's {result['description']} right now.{Style.RESET_ALL} 
                |\|\_/#  \_/       '^--'          ______/  __/'--------------------------------------'
                \/'.  \  /'\         \           /
                  \    /=\  /         ||  |---'\  \ 
                  /____)/____)       (_(__|   ((__|    

            
            """)
    print(f"{Fore.LIGHTBLACK_EX}==========================================================================={Style.RESET_ALL}")
    con = input("                 🔴 Do you want to continue? (Y/N) ")
    print(f"{Fore.LIGHTBLACK_EX}==========================================================================={Style.RESET_ALL}")
    if con.lower() == 'n':

        print(f"""\n
                                         {Fore.BLUE} _.--'_......----........
                                       _,i,,-'' __,,...........___
                                    {Fore.CYAN}  ;-' _.--''    ___,,......___
                                   ,;'_,''   _.--'''    __,,......
                              {Fore.LIGHTYELLOW_EX} ,;','   _.-'   _,.--'''__,,......    {Style.RESET_ALL}  " Hope you have a great day...
                  .-.         {Fore.LIGHTYELLOW_EX}//,'   ,'   _.-'_,.--''' {Style.RESET_ALL} .-.          Don't forget to drink water...
                 ;. .;   {Fore.LIGHTRED_EX}   ///  ,-'  ,-' ,-'  {Style.RESET_ALL} .-.    ;. .;      {Style.RESET_ALL}Stay hydrated 🩵 "
             .-"-.. ..-"`.{Fore.LIGHTRED_EX} /// ,'  ,-' ,-'   {Style.RESET_ALL} ;. ..-"-.. ..-"`.
             `. _.(_)._ .'{Fore.LIGHTRED_EX} /// /  ,' ,-'  {Style.RESET_ALL} .'"-.. .`."_.(_)._ .'
              "/.' '. "  {Fore.LIGHTRED_EX} /// / ,' ,'  {Style.RESET_ALL}    `. _.(_)._"/.' '. "
              ,';' '; {Fore.LIGHTRED_EX}   |||/ - ,'    {Style.RESET_ALL}       " .` `.\,';' ';
             |   '-'    \oOoO '                ;` `;`|  '-'
             |          oOoOOo                  `-`  |
             \         (_____)                       \ 
              |         )   (                         |
              `.       (_____)                        `.
         {Fore.GREEN} MMWwwMmWwMmWwMmWwMmWwMmWwMmWwMmWwMmWwMmWwMmWwMmWwMm


""")
        break

