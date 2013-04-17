from django.template import RequestContext
from home.models import SimpleModel
from django.shortcuts import render_to_response
import MySQLdb

def index(request):
    if request.method == 'POST':
        # save new post
        message = request.POST['message']

        post = SimpleModel(message=message) 
        post.save()
    # Get all posts from DB
    posts = SimpleModel.objects 
    db = MySQLdb.connect(user='root', db='junior_db', passwd='root', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT message FROM home_simplemodel ')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('sample_home.html', {'Posts': names},
                              context_instance=RequestContext(request))
