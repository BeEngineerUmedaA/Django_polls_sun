from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    question_list = [
        "ゲームは好きですか？",
        "勉強は好きですか？",
        "あなたは私ですか？",
    ]
    context = {
        "question_list": question_list,
        "is_polled": True,
        "polled_msg": "投票ありがとうございました❤️",
        "not_polled_msg": "さっさと投票してよー泣",
    }
    return render(request, "main/index.html", context)