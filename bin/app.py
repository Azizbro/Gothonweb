import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

# this tells lpthw.web to use the templates/layout.html as the base template
render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        # the GET function runs first and returns the hello_form
        return render.hello_form()

    def POST(self):
        # instead of just a string we're now using web.input to get data
        # from the browser. This func parses the ?name=Frank part of the
        # URL you give it, and then returns an object for you to use
        form = web.input(name="Nobody", greet=None)

        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
            # Shows that the name of the function you call on render is just
            # matched to a .html file in templates/
            # everything else can refer to index
            return render.index(greeting = greeting)
        else:
            return "ERROR: greet is required"

if __name__ == "__main__":
    app.run()
