import urllib.request

def fetch_hbtn_status():
    """
    Fetches status from https://alu-intranet.hbtn.io/status
    and displays response details
    """
    url = 'https://alu-intranet.hbtn.io/status'
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))

if __name__ == "__main__":
    fetch_hbtn_status()
