import tornado.web
import tornado.ioloop
import json

class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World this is a python command execcuted form the backend")

class ListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class QueryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer.")


class ResourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(f"Welcome {studentName} the course you are viewing is {courseId}")


class ListJSONRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully."}))

class MainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index2.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        # (r"/", BasicRequestHandler),
        (r"/animal", ListRequestHandler),
        (r"/iseven", QueryParamRequestHandler),
        (r"/students/([a-zA-Z]+)/([0-9]+)", ResourceParamRequestHandler),
        (r"/getfruits", ListJSONRequestHandler),
        (r"/", MainRequestHandler),
    ])

    port = 9000
    app.listen(port)
    print(f'Application is ready and listening on port {port}')
    tornado.ioloop.IOLoop.current().start()