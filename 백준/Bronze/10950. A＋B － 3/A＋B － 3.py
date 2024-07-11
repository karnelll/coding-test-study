T = int(input())
results = []  # 리스트 이름 수정

for _ in range(T):  
    A, B = map(int, input().split())
    results.append(A + B)  # 합계를 리스트에 추가
    
for sum in results:  # range 함수를 사용하지 않고 직접 리스트 순회
    print(sum)