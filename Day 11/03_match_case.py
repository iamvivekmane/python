# it works same as switch case statement 
def http_status(status):
    match status:
        case 200:
            return 'OK'
        case 404:
            return 'Page not found'
        case 500:
            return 'Internal server error'
        case _:
            return 'Unknown status'
print(http_status(400))
 