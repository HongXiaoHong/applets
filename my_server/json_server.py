from http.server import HTTPServer, BaseHTTPRequestHandler

host = ('localhost', 8888)

class Resquest(BaseHTTPRequestHandler):
    timeout = 5
    server_version = "Apache"  # 设置服务器返回的的响应头

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")  # 设置服务器响应头
        self.end_headers()
        buf = '''{
                    "wapPopAdvert": {
                        "open": true
                    }
                }'''
        self.wfile.write(buf.encode())  # 里面需要传入二进制数据，用encode()函数转换为二进制数据   #设置响应body，即前端页面要展示的数据


if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
