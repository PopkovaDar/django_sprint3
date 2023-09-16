from django.shortcuts import render


def about(reqeust):
    about_name = 'pages/about.html'
    return render(reqeust, about_name)


def rules(reqeust):
    rules_name = 'pages/rules.html'
    return render(reqeust, rules_name)
