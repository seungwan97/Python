#목적지까지의 거리를 input으로 입력받는다.
#목적지까지의 거리를 택시로 갈 돈이 있으면 택시 탑승/아니면 버스 선택
#택시 평균시속:60km/h 1초에 16.67m
#버스 평균시속:20km/h 1초에 5.56m
#도보 평균시속:4km/h 1초에 1.11m
#거리/속력=시간
#각 운송수단 혹은 도보로 이동하는 경우 소요된 시간 계산하여 출력
#기본 요금 3300원 2km동안 3300원 고정
#추가 133m마다 100원 추가
#버스요금 1500원 거리무관

money=int(input("금액:"))
print(money)

dis=int(input("거리:"))
print(dis)

lp=91600//60

if money>=1500:
    if money>=3300:
        if ((money>3300) and (money>(3300+((dis-2000)/133*100)))):
            print("돈이 3300원 이상있고 거리에 따른 추가비용을 합산한 금액보다도 돈이 많아서")
            print("택시")
            print("소요시간(분)")
            print(dis/(60/60*1000))
            if (dis / (60/60*1000)) >= (dis / (20/60*1000)):
                print("시간우선:bus")
            else:
                print("시간우선:taxi")
            if (3300+((dis-2000)/133*100)) <= 1500:
                print("금액우선:taxi")
            else:
                print("금액우선:bus")
            if (3300+((dis-2000)/133*100)) - (dis / (60/60*1000) * lp) <= 1500:
                print("편리함추가:taxi")
            else:
                print("편리함추가:bus")
        else:
            print("돈이 3300원 이상 있지만 거리에 따른 추가비용을 합산한 금액보다는 돈이 적어서")
            print("버스")
            print("소요시간(분)")
            print(dis/(20/60*1000))

        if money==3300:
            if dis<=2000:
                print("돈이 3300원 있고 거리는 2km보다 같거나 짧아서")
                print("택시")
                print("소요시간(분)")
                print(dis/(60/60*1000))

            else:
                print("돈이 3300원 있지만 거리가 2km보다 길어서")
                print("버스")
                print("소요시간(분)")
                print(dis/(20/60*1000))
    else:
        print("돈이 1500원 이상이지만 3300원보다는 적어서")
        print("버스")
        print("소요시간(분)")
        print(dis/(20/60*1000))
else:
    print("돈이 1500원보다 적어서")
    print("걷기")
    print("소요시간(분)")
    print(dis/(4/60*1000))