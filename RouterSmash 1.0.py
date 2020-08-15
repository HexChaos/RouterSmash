###########################################################################################
#                                 RouterSmash                                             #
# Designed to find what IP address a router is using for identification and exploitation. #
# For use to test your own networks only yada yada don't break the law and all that.      #
#                               Made by HexChaos                                          #
#   hexchaos.xyz    github.com/hexchaos    twitter.com/hexchaossec    TryHackMe.com       #
###########################################################################################
def splash_screen(seconds):
  print("\n")
  print("   _____             _            _____                     _     ")
  print("  |  __ \           | |          / ____|                   | |    ")
  print("  | |__) |___  _   _| |_ ___ _ _| (___  _ __ ___   __ _ ___| |__  ")
  print("  |  _  // _ \| | | | __/ _ \ '__\___ \| '_ ` _ \ / _` / __| '_ \ ")
  print("  | | \ \ (_) | |_| | ||  __/ |  ____) | | | | | | (_| \__ \ | | |")
  print("  |_|  \_\___/ \__,_|\__\___|_| |_____/|_| |_| |_|\__,_|___/_| |_|")
  print("   _   _              ____ _                                      ")
  print("  | | | | _____  __  / ___| |__   __ _  ___  ___  __  ___   _ ____")
  print("  | |_| |/ _ \ \/ / / |   | '_ \ / _` |/ _ \/ __| \ \/ / | | |_  /")
  print("  |  _  |  __/>  <  | |___| | | | (_| | (_) \__ \_ >  <| |_| |/ / ")
  print("  |_| |_|\___/_/\_\  \____|_| |_|\__,_|\___/|___(_)_/\_\\__, /___|")
  print("                                                        |___/     ")
  print("               Open Source LAN Router Scanning                    ")
  print("Do not use in Military or Secret Service Organzations, or for illegal purposes")
splash_screen(3)
def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0

# test call
print ("192.168.0.1 is")
print(ping("192.168.0.1"))
#
print ("192.168.1.1 is")
print(ping("192.168.1.1"))
# 192.168.1.254
print ("192.168.1.254 is")
print(ping("192.168.1.254"))
# 192.168.2.1
print ("192.168.2.1 is")
print(ping("192.168.2.1"))
# 192.168.254.254
print ("192.168.254.254 is")
print(ping("192.168.254.254"))
# 192.168.1.1
print ("192.168.1.1 is")
print(ping("192.168.1.1"))
# 192.168.1.1
print ("192.168.1.1 is")
print(ping("192.168.1.1"))
# 10.0.0.138
print ("10.0.0.138 is")
print(ping("10.0.0.138"))
# 10.0.0.1
print ("10.0.0.1 is")
print(ping("10.0.0.1"))
# 10.1.1.1
print ("10.1.1.1 is")
print(ping("10.1.1.1"))
# 10.0.0.2
print ("10.0.0.2 is")
print(ping("10.0.0.2"))
# 192.168.0.30
print ("192.168.0.30 is")
print(ping("192.168.0.30"))
# 192.168.0.101
print ("192.168.0.101 is")
print(ping("192.168.0.101"))
# 192.168.0.50
print ("192.168.0.50 is")
print(ping("192.168.0.50"))
# 192.168.0.101
print ("192.168.0.101 is")
print(ping("192.168.0.101"))
# 192.168.1.254
print ("192.168.1.254 is")
print(ping("192.168.1.254"))
# 10.90.90.90
print ("10.90.90.90 is")
print(ping("10.90.90.90"))

#GOOGLE SPECIFIC
# 192.168.86.1
print ("192.168.86.1 is")
print(ping("192.168.86.1"))

#NETGEAR SPECIFIC
# 192.168.0.227
print ("192.168.0.227 is")
print(ping("192.168.0.227"))
#
print(" ")
#
print ("If it says true that IP address is reachable. There is still a possibility for false positives or routers that use more than one address for admin panels.")
print ("Alternatively this could detect Intranet Services.")
print ("If none appear, end user could have changed it or the router is a non-common device.")
print("")

