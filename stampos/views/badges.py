from stampos.views.rest_dispatch import RESTDispatch
from django.utils import simplejson
from django.http import HttpResponse

class BadgeView(RESTDispatch):
    def GET(self, request):
        badge = {"id": 235, "name": "My First Badge", "Description": "This is a badge, you should earn it"}
        return HttpResponse(simplejson.dumps(badge), mimetype="application/json")