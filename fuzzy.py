#!/usr/bin/env python3

import requests
import socket

print("\n\n\n\n"
"\t\tFFFFFFFFFFFFFFFFFFFFFF\n"                                                                             
"\t\tF::::::::::::::::::::F\n"
"\t\tF::::::::::::::::::::F\n"
"\t\tFF::::::FFFFFFFFF::::F\n"
"\t\t  F:::::F       FFFFFFuuuuuu    uuuuuu  zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzyyyyyyy           yyyyyyy\n"
"\t\t  F:::::F             u::::u    u::::u  z:::::::::::::::zz:::::::::::::::z y:::::y         y:::::y\n"
"\t\t  F::::::FFFFFFFFFF   u::::u    u::::u  z::::::::::::::z z::::::::::::::z   y:::::y       y:::::y\n"
"\t\t  F:::::::::::::::F   u::::u    u::::u  zzzzzzzz::::::z  zzzzzzzz::::::z     y:::::y     y:::::y\n"
" \t\t F:::::::::::::::F   u::::u    u::::u        z::::::z         z::::::z       y:::::y   y:::::y\n"
"\t\t F::::::FFFFFFFFFF   u::::u    u::::u       z::::::z         z::::::z         y:::::y y:::::y\n"
"\t\t  F:::::F             u::::u    u::::u      z::::::z         z::::::z           y:::::y:::::y\n"
"\t\t  F:::::F             u:::::uuuu:::::u     z::::::z         z::::::z             y:::::::::y\n"
"\t\tFF:::::::FF           u:::::::::::::::uu  z::::::zzzzzzzz  z::::::zzzzzzzz        y:::::::y\n"
"\t\tF::::::::FF            u:::::::::::::::u z::::::::::::::z z::::::::::::::z         y:::::y\n"
"\t\tF::::::::FF             uu::::::::uu:::uz:::::::::::::::zz:::::::::::::::z        y:::::y\n"
"\t\tFFFFFFFFFFF               uuuuuuuu  uuuuzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz       y:::::y\n"
"\t\t                                                                                y:::::y\n"
"\t\t                                                                               y:::::y\n"
"\t\t                                                                              y:::::y\n"
"\t\t                                                                             y:::::y\n"
"\t\t                                                                            yyyyyyy\n"
                                                                            "\n\n")
print("-------------------------------------------------------------------------------------------------------------------------------")
print(f"\t\t\t\t[+]\t Welcome to fuzzy tool\t\t\t")
print(f"\t\t\t\t[+]\t Version:\t1.0")
print(f"\t\t\t\t[+]\t This tool was created by Khalid Al-saif")
#inputs from user .. he should provide an url
# we will return that as an ip to make it easier to play with
url=input("\n\turl for example(scanme.nmap.org): ")
if "http://" not in url  and "192" not in url:
    ip = socket.gethostbyname(url)
    url = "http://" + url

elif "192" in url:
    ip = "local"
    url = url


else:
    preip=url.replace("http://","")
    ip = socket.gethostbyname(preip)
    pass




#the user most provide a text file that has a potantial names of site
wordlist=input("\twordlists (if you don't have a list to provide we got you type fuzzingpayload.txt): ")
print(f"\tstart Fuzzing on - {url} in ip - {ip} ")

#this variable stores the list file that provided by user
wordlistlines=open(wordlist,"r").readlines()



#for loop to go throw the list of potantial hidden paths
for i in range(0,len(wordlistlines)):

    #to get rid of new lines on read
    enumeration=wordlistlines[i].replace('\n',"")

    #make a GET request using the library (request) to the url
    #the word on the list that
    r=requests.get(url+"/"+enumeration)


    if r.status_code == 200:
        #print out every (found) pages on the dirictory
        print("\tfound [!] "+url+"/"+enumeration+ " - "+"The Status of this path is: "+ str(r.status_code)+" OK\n")

    elif r.status_code == 403:
        # print out every (found) pages on the dirictory
        print("\tfound [!] " + url + "/" + enumeration + " - " +"The Status of this path is: "+ str(r.status_code)+" forbidden\n")

    elif r.status_code != 404:
        # print out every (found) pages on the dirictory
        print("\tfound [!] " + url + "/" + enumeration + " - " +"The Status of this path is: "+ str(r.status_code)+"\n")
