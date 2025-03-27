import urllib.request
import ur11ib

def main():
    """ Fetch and display status """
    with ur11ib.request.urlopen('http://0.0.0.0:5050/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))

if __name__ == "__main__":
    main()