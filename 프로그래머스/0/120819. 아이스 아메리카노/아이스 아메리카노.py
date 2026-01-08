def solution(money):
    cups = money // 5500
    remain = money % 5500
    return [cups, remain]