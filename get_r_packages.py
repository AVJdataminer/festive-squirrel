#get_r_packages.py
""" This program allows the user to download the source files for r modules from the cran based on the input list.
updated on:24JAN2021
aiden.dataminer@gmail.com
"""

def get_r_packages(pack_list):
    for p in pack_list:
        #get the package full name with version
        url = 'https://cran.r-project.org/web/packages/{}'.format(p)
        ext = 'tar.gz'

        def listFD(url, ext=''):
            page = requests.get(url).text
            #print(page)
            soup = BeautifulSoup(page, 'html.parser')
            return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

        for file in listFD(url, ext):
            #print(file)
            fullname = file.rsplit('/', 1)[-1]
            print(fullname)

        file_url = "https://cran.r-project.org/src/contrib/{}".format(fullname)
        r = requests.get(file_url)
        fullname = file_url.rsplit('/', 1)[-1] 
        with open(fullname,'wb') as f: 
            f.write(r.content)