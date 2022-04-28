def sortByArrival(at, n):
     
    # Selection Sort applied 
    for i in range(0, n - 1):
        for j in range(i + 1, n):
             
            # Check for lesser arrival time 
            if at[i] > at[j]:
                 
                # Swap earlier process to front
                at[i], at[j] = at[j], at[i]
 
# 코드 시작
if __name__ == '__main__':
     
    max_time = 0  # Burst Time 합계
    avgWT = 0   # Waiting Time 평균
    avgTT = 0   # Turnaround Time 평균
    n = 5       # 프로세스 개수 설정
     
    completed =         [0] * n     # 완료 개수
    WT =      [0] * n     # WT
    TT =   [0] * n     # TT
    NTT =     [0] * n     # NTT
    
    arrival_time =  [0, 1, 3, 5, 6]    # Arrival Times 설정   
    burst_time =    [3, 7, 2, 5, 3]    # Burst Times 설정
    process =       []              # 프로세스
     
    # 프로세스 이름 지정 (A, B, C, D)
    for i in range(0, n):           # 프로세스 개수만큼 생성
        process.append(chr(65 + i)) # 프로세스 이름 삽입 (A, B, C, D)
        max_time += burst_time[i]     # BT 합계
        
    sortByArrival(arrival_time, n)  # Arriaval Time 대로 정렬한다.
    print("Name            ", "AT             ",
          "BT             ", "WT             ",
          "T              ", "TT              ")
    t = arrival_time[0]     # 첫 프로세스 도착 시간
     
    while(t < max_time):
         
        # 응답률의 하한 설정 (Response Ratio = (WT + BT) / BT))
        hrr = -9999
        temp, loc = 0, 0
         
        for i in range(0, n):
             
            # 프로세스가 도착했을 때를 확인한다.
            # 완료를 판별 0: 처리 이전, 1: 처리 완료
            if arrival_time[i] <= t and completed[i] != 1:
                 
                # Response Ratio 계산 (Response Ratio = (WT + BT) / BT))
                temp = ((burst_time[i] +
                        (t - arrival_time[i])) /
                         burst_time[i])
                          
                # 가장 높은 Response Ratio 확인
                if hrr < temp:
                     
                    # Response Ratio 저장 
                    hrr = temp
                     
                    # 프로세스 인덱스 위치
                    loc = i
                    
        # Updating time value 
        t += burst_time[loc]
        
        # Waiting Time 계산
        WT[loc] = (t - arrival_time[loc] -
                                 burst_time[loc])
         
        # Turn-Around Time 계산
        TT[loc] = t - arrival_time[loc]
         
        # 평균을 위한 Turn-Around Time 합 계산
        avgTT += TT[loc]
         
        # Normalized TT 계산
        NTT = float(TT[loc] /
                              burst_time[loc])
         
        # 완료된 프로세스를 처리한다.
        completed[loc] = 1
         
        # 평균을 위한 Waiting Time 합 계산
        avgWT += WT[loc]
         
        print(process[loc], "\t\t", arrival_time[loc],
              "\t\t", burst_time[loc], "\t\t",
              WT[loc], "\t\t",
              TT[loc], "\t\t",
              "{0:.6f}".format(NTT))
 
    print("Average Waiting Time: {0:.6f}".format(avgWT / n))
    print("Average Turn-Around Time:  {0:.6f}".format(avgTT / n))