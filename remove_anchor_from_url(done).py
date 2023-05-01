'''Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"'''


def remove_url_anchor(url):
    if "#" not in url:
        return url
    no_url = ''
    for i in url:
        no_url += i
        if i == '#':
            new_no_url = no_url.replace('#', '')
            break
    return new_no_url

print(remove_url_anchor("www.codewars.com#about"))

#Done!!!
