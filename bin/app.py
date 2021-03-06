import web

urls = (
    '/hello', 'Index',
    '/upload', 'Upload',
    # trying out sessions
    '/state', 'State',
    '/login', 'Login',
    '/logout', 'Logout'
)

app = web.application(urls, globals())

# this tells lpthw.web to use the templates/layout.html as the base template
render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        # the GET function runs first and returns the hello_form
        return render.hello_form_laid_out()

    def POST(self):
        # instead of just a string we're now using web.input to get data
        # from the browser. This func parses the ?name=Frank part of the
        # URL you give it, and then returns an object for you to use
        # This function takes a key=value set of defaults
        # So make sure each variable has a default value
        form = web.input(name="Nobody", greet=None)

        greeting = "%s, %s" % (form.greet, form.name)
        # Shows that the name of the function you call on render is just
        # matched to a .html file in templates/
        # everything else can refer to index
        return render.index_laid_out(greeting = greeting)


# ---------------------UPLOADING FILE -----------------------------


class Upload(object):
    def GET(self):
        return render.upload_form()

    def POST(self):
        # This function takes a key=value set of defaults
        # So make sure each variable has a default value
        x = web.input(myfile = {})

        # Uploading a file
        # Where you want to store the file in
        filedir = 'C:\Users\Zarif\OneDrive\Documents\Python Projects\gothonweb'
        # To check if the file-object is created
        if 'myfile' in x:
            filepath= x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename= filepath.split('/')[-1] # splits the / and chooses the last part (the filename with extension)
            #'wb' means binary mode
            fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.

        # Go to another web page where you have the output message
        return render.upload()


#------------------ SESSIONS ------------------------------------


# Hack to make session play nice with the reloader (in debug mode)
if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'))
    web.config._session = session
else:
    session = web.config._session

class State(object):
    def GET(self):
        # 'False' is the value to be returned in case key doesn't exist
        if session.get('logged_in', False):
            return '<h1>You are logged in</h1><a href="/logout">Logout</a>'
        return '<h1>You are not logged in.</h1><a href="/login">Login now</a>'

class Login:
    def GET(self):
        session.logged_in = True
        raise web.seeother('/state')

class Logout:
    def GET(self):
        session.logged_in = False
        raise web.seeother('/state')

# What does this mean?
if __name__ == "__main__":
    app.run()
