# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    return url[0:url.index('.')]


print(domain_name("http://github.com/carbonfive/raygun"))  # "github"
print(domain_name("http://www.zombie-bites.com"))  # "zombie-bites"
print(domain_name("https://www.cnet.com"))  # "cnet"


