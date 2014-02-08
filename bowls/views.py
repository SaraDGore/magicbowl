from django.shortcuts import render_to_response


def main(request):
    # View code here...
    return render_to_response('base.html', {"foo": "bar"})
