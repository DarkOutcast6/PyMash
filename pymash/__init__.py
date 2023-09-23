from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/':
      self.handle_index()
    else:
      self.send_response(404)
      self.end_headers()

  def handle_index(self):
    self.send_response(200)
    self.end_headers()

def run_server(port='0.0.0.0'):
  httpd = HTTPServer((port, 8000), SimpleHTTPRequestHandler)
  httpd.serve_forever()
  
class html:
  def __init__(self):
    '''
    A object to create and manage the HTML of the website.
    '''
    self.code = []

  def add_line(self,tag="",content="") -> None:
    '''
    Create a new line with a optional set tag type attribute (such as h1, or div), a optional argument for setting the content of the selected tag and a optional line number attribute to set what line the code should overwrite. If none is given for any arguments, defaults will be asssumed.
    '''
    if tag is None:
      self.code.append(f"{content}")
    else:
      self.code.append(f"<{tag}>{content}</{tag}>")
    return None

  def complile(self) -> None:
    '''
    Compile any defined code that has been stored in this "html" object into a legit HTML file so that user can later run and access from other "html" objects.
    '''
    try:
      file = open("index.html","r+")
    except FileNotFoundError:
      file = open("index.html","w")

    file.writelines(self.code)
    file.close()
    return None

  def run(self,port) -> None:
    run_server(port)
    return None