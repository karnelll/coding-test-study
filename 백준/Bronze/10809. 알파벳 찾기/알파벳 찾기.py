# 알파벳 리스트 생성
alphabet_list = list('abcdefghijklmnopqrstuvwxyz')

# 사용자로부터 입력받은 문자열을 리스트로 변환
s = input().strip()

# 결과 리스트 생성
results = []

# 모든 알파벳에 대해 확인하고 인덱스를 출력
for char in alphabet_list:
    if char in s:
        results.append(s.index(char)) 
    else:
        results.append(-1)

print(' '.join(map(str, results)))
