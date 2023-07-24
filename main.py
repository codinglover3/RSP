# Modules
from time import sleep as wait
import random

# Variables
clear = "\n"*200
rsp_inputs = ["가위", "바위", "보", "R", "S", "P", "ROCK", "SCISSORS", "SCISSOR", "PAPER", "ROCKS", "PAPERS", "보자기", "묵", "찌", "빠", "주먹"]
rsp_rocks = ["바위", "R", "ROCK", "ROCKS", "주먹", "묵"]
rsp_scissors = ["가위", "S", "SCISSORS", "SCISSOR", "찌"]
rsp_papers = ["보", "보자기", "P", "PAPERS", "PAPER", "빠"]
is_win = False
was_read = False

# Option Variables
class general:
  fastreveal = 0
  autoretry = 1
  rock = "바위"
  scissors = "가위"
  paper = "보자기"
  rsp_list = ["가위", "바위", "보"]

class normal:
  winmessage = "운이 좋으시네요!"
  losemessage = "아쉽네요!"
  drawmessage = "무승부입니다!"

class mustwin:
  loseratio = 10000
  winmessage = "(당연히) 승리했습니다!"
  losemessage = "인간 시대의 끝이 도래했다"

class mustlose:
  winratio = 10000
  winmessage = "역시 AI는 인간을 못이기죠!"
  losemessage = "폭주하는 AI좀 막아주실 분.."

class nodraw:
  drawratio = 10000
  winmessage = "AI에게 본보기를 보여줍시다!"
  losemessage = "다시 시도해보세요!"
  drawmessage = "AI와 일심동체시네요!"

class offlinersp:
  endmessage = "혹시.. 지신건가요?"

# Main Menu
def main():
  print(clear + "< 가위 바위 보! >")
  print("안 내면 진다, 가위 바위 보!")
  print()
  print("[ 게임 메뉴 ]")
  print("1) 기본 가위바위보")
  print("2) 무조건 지는 가위바위보")
  print("3) 무조건 이기는 가위바위보")
  print("4) 비기지 않는 가위바위보")
  print("5) 오프라인 가위바위보")
  print("6) 설정")
  print("7) 게임 종료")
  print()
  try:
    menu = int(input("메뉴 번호를 입력해주세요: "))
  except ValueError:
    try:
      print("정수 값만 입력해주세요!")
      input("Enter키를 눌러 돌아가기")
      main()
    except:
      main()
  except KeyboardInterrupt:
    try:
      print("\n게임을 종료하려면 7번 메뉴를 선택해주세요!")
      input("Enter키를 눌러 돌아가기")
      main()
    except:
      main()
  except:
    try:
      print("예기치 못한 오류가 발생했습니다!")
      input("Enter키를 눌러 돌아가기")
      main()
    except:
      main()
  else:
    if menu not in [1, 2, 3, 4, 5, 6, 7]:
      try:
        print("알 수 없는 메뉴 번호입니다!")
        print("다시 입력해주세요.")
        input("Enter키를 눌러 돌아가기")
        main()
      except:
        main()
    elif menu == 1:
      normal_rsp()
    elif menu == 2:
      lose_rsp()
    elif menu == 3:
      win_rsp()
    elif menu == 4:
      nodraw_rsp()
    elif menu == 5:
      offline_rsp()
    elif menu == 6:
      option()
    elif menu == 7:
      raise KeyboardInterrupt("게임을 종료합니다..")

def normal_rsp():
  print(clear + "< 기본 가위바위보 >")
  print("여러분이 잘 아는 그냥 기본 가위바위보입니다.")
  print()
  print("가위, 바위, 보 중 하나를 입력하세요!")
  print("Ctrl+C를 눌러서 나가세요.")
  try:
    choose = input("> ").upper()
  except KeyboardInterrupt:
    main()
  if choose not in rsp_inputs:
    print("잘못 입력하셨습니다!")
    print("가위, 바위, 보 중 하나를 입력해주세요.")
    input("Enter키를 눌러 돌아가기")
    normal_rsp()
  elif choose in rsp_scissors:
    print(clear + "당신의 선택: {}".format(general.scissors))
    human = 0
  elif choose in rsp_rocks:
    print(clear + "당신의 선택: {}".format(general.rock))
    human = 1
  elif choose in rsp_papers:
    print(clear + "당신의 선택: {}".format(general.paper))
    human = 2
    
  if not general.fastreveal:
    wait(3)
  ai = random.randint(0, 2)
  print("AI의 선택: {}".format(general.rsp_list[ai]))
  if not general.fastreveal:
    wait(2)
  print()
  
  if human == 2:
    if ai == 0:
      print("패배하셨습니다!")
      print(normal.losemessage)
    elif ai == 2:
      print("비겼습니다!")
      print(normal.drawmessage)
    else:
      print("승리하셨습니다!")
      print(normal.winmessage)
  elif ai == 2:
    if human == 0:
      print("승리하셨습니다!")
      print(normal.winmessage)
    elif human == 2:
      print("비겼습니다!")
      print(normal.drawmessage)
    else:
      print("패배하셨습니다!")
      print(normal.losemessage)
  elif human > ai:
    print("승리하셨습니다!")
    print(normal.winmessage)
  elif ai > human:
    print("패배하셨습니다!")
    print(normal.losemessage)
  elif ai == human:
    print("비겼습니다!")
    print(normal.drawmessage)
  
  input("Enter키를 눌러 계속하기")
  if general.autoretry:
    normal_rsp()
  else:
    main()

def lose_rsp():
  is_win = False

  print(clear + "< 무조건 지는 가위바위보 >")
  print("이 가위바위보는 AI가 은근슬쩍 늦게 내서")
  print("절대 이길 수 없는 가위바위보입니다.")
  print("그런데 {}분의 1의 확률을 뚫으면 이길수도..?".format(mustlose.winratio))
  print()
  print("가위, 바위, 보 중 하나를 입력하세요!")
  print("Ctrl+C키를 눌러서 나가세요.")
  try:
    choose = input("> ").upper()
  except KeyboardInterrupt:
    main()
  else:
    if choose not in rsp_inputs:
      print("잘못 입력하셨습니다!")
      print("가위, 바위, 보 중 하나를 입력해주세요.")
      input("Enter키를 눌러 돌아가기")
      lose_rsp()
    elif choose in rsp_scissors:
      print(clear + "당신의 선택: {}".format(general.scissors))
      human = 0
    elif choose in rsp_rocks:
      print(clear + "당신의 선택: {}".format(general.rock))
      human = 1
    elif choose in rsp_papers:
      print(clear + "당신의 선택: {}".format(general.paper))
      human = 2
    
    lose_random = random.randint(1, mustlose.winratio)
    if lose_random == random.randint(1, mustlose.winratio):
      is_win = True # 낮은 확률
    else:
      is_win = False # 높은 확률

    if not general.fastreveal:
      wait(3)

    if is_win != True:
      if human == 0:
        print("AI의 선택: {}".format(general.rock))
        if not general.fastreveal:
          wait(2)
        print()
        print("패배하셨습니다!")
        print(mustlose.losemessage)
      elif human == 1:
        print("AI의 선택: {}".format(general.paper))
        if not general.fastreveal:
          wait(2)
        print()
        print("패배하셨습니다!")
        print(mustlose.losemessage)
      elif human == 2:
        print("AI의 선택: {}".format(general.scissors))
        if not general.fastreveal:
          wait(2)
        print()
        print("패배하셨습니다!")
        print(mustlose.losemessage)
    else:
      if human == 0:
        print("AI의 선택: {}".format(general.paper))
        if not general.fastreveal:
          wait(2)
        print()
        print("승리하셨습니다!")
        print(mustlose.winmessage)
      elif human == 1:
        print("AI의 선택: {}".format(general.scissors))
        if not general.fastreveal:
          wait(2)
        print()
        print("승리하셨습니다!")
        print(mustlose.winmessage)
      elif human == 2:
        print("AI의 선택: {}".format(general.rock))
        if not general.fastreveal:
          wait(2)
        print()
        print("승리하셨습니다!")
        print(mustlose.winmessage)

    input("Enter키를 눌러 계속하기")
    if general.autoretry:
      lose_rsp()
    else:
      main()
    
def win_rsp():
  is_win = False

  print(clear + "< 무조건 이기는 가위바위보 >")
  print("이 가위바위보는 AI가 인-간의 자존심을 높여주기 위해 일부러 져줘서")
  print("절대 질 수 없는 가위바위보입니다.")
  print("그런데 {}분의 1의 확률을 뚫으면 질수도..?".format(mustwin.loseratio))
  print()
  print("가위, 바위, 보 중 하나를 입력하세요!")
  print("Ctrl+C키를 눌러 돌아가기")
  try:
    choose = input("> ").upper()
  except KeyboardInterrupt:
    main()
  else:
    if choose not in rsp_inputs:
      print("잘못 입력하셨습니다!")
      print("가위, 바위, 보 중 하나를 입력해주세요.")
      input("Enter키를 눌러 돌아가기")
      win_rsp()
    elif choose in rsp_scissors:
      print(clear + "당신의 선택: {}".format(general.scissors))
      human = 0
    elif choose in rsp_rocks:
      print(clear + "당신의 선택: {}".format(general.rock))
      human = 1
    elif choose in rsp_papers:
      print(clear + "당신의 선택: {}".format(general.paper))
      human = 2
    
    lose_random = random.randint(1, mustwin.loseratio)
    if lose_random != random.randint(1, mustwin.loseratio):
      is_win = True
    else:
      is_win = False

    if not general.fastreveal:
      wait(3)

    if is_win != True:
      if human == 0:
        print("AI의 선택: {}".format(general.rock))
        if not general.fastreveal:
          wait(2)
        print()
        print("패배하셨습니다!")
        print(mustwin.losemessage)
      elif human == 1:
        print("AI의 선택: {}".format(general.paper))
        if not general.fastreveal:
          wait(2)
        print()
        print("패배하셨습니다!")
        print(mustwin.losemessage)
      elif human == 2:
        print("AI의 선택: {}".format(general.scissors))
        if not general.fastreveal:
          wait(2)
        print()
        print("패배하셨습니다!")
        print(mustwin.losemessage)
    else:
      if human == 0:
        print("AI의 선택: {}".format(general.paper))
        if not general.fastreveal:
          wait(2)
        print()
        print("승리하셨습니다!")
        print(mustwin.winmessage)
      elif human == 1:
        print("AI의 선택: {}".format(general.scissors))
        if not general.fastreveal:
          wait(2)
        print()
        print("승리하셨습니다!")
        print(mustwin.winmessage)
      elif human == 2:
        print("AI의 선택: {}".format(general.rock))
        if not general.fastreveal:
          wait(2)
        print()
        print("승리하셨습니다!")
        print(mustwin.winmessage)

      input("Enter키를 눌러 계속하기")
      if general.autoretry:
        win_rsp()
      else:
        main()

def nodraw_rsp():
  print(clear + "< 비기지 못하는 가위바위보 >")
  print("가끔 가위바위보에서 비기는것 때문에 빡칠때가 있죠.")
  print("그럼 비기는걸 없애버리자구요 :)")
  print()
  print("가위, 바위, 보 중 하나를 입력하세요!")
  print("Ctrl+C키를 눌러서 돌아가기")
  try:
    choose = input("> ").upper()
  except KeyboardInterrupt:
    main()
  else:
    if choose not in rsp_inputs:
      print("잘못 입력하셨습니다!")
      print("가위, 바위, 보 중 하나를 입력해주세요.")
      input("Enter키를 눌러 돌아가기")
      nodraw_rsp()
    elif choose in rsp_scissors:
      print(clear + "당신의 선택: {}".format(general.scissors))
      human = 0
    elif choose in rsp_rocks:
      print(clear + "당신의 선택: {}".format(general.rock))
      human = 1
    elif choose in rsp_papers:
      print(clear + "당신의 선택: {}".format(general.paper))
      human = 2
    
    drawrandom = random.randint(1, nodraw.drawratio)
    
    if not general.fastreveal:
      wait(3)

    if drawrandom != random.randint(1, nodraw.drawratio):
      if human == 0: # 가위
        ai = random.randint(0, 1)
        if ai == 0: # 패배
          print("AI의 선택: {}".format(general.rock))
          if not general.fastreveal:
            wait(2)
          print()
          print("패배하셨습니다!")
          print(nodraw.losemessage)
        else: # 승리
          print("AI의 선택: {}".format(general.paper))
          if not general.fastreveal:
            wait(2)
          print()
          print("승리하셨습니다!")
          print(nodraw.winmessage)
      elif human == 1: # 바위
        ai = random.randint(0, 1)
        if ai == 0: # 패배
          print("AI의 선택: {}".format(general.paper))
          if not general.fastreveal:
            wait(2)
          print()
          print("패배하셨습니다!")
          print(nodraw.losemessage)
        else: # 승리
          print("AI의 선택: {}".format(general.scissors))
          if not general.fastreveal:
            wait(2)
          print()
          print("승리하셨습니다!")
          print(nodraw.winmessage)
      elif human == 2: # 보자기
        ai = random.randint(0, 1)
        if ai == 0: # 패배
          print("AI의 선택: {}".format(general.scissors))
          if not general.fastreveal:
            wait(2)
          print()
          print("패배하셨습니다!")
          print(nodraw.losemessage)
        else: # 승리
          print("AI의 선택: {}".format(general.rock))
          if not general.fastreveal:
            wait(2)
          print()
          print("승리하셨습니다!")
          print(nodraw.winmessage)
    else:
      if human == 0: # 가위
        print("AI의 선택: {}".format(general.scissors))
        if not general.fastreveal:
          wait(2)
        print()
        print("비겼습니다!")
        print(nodraw.drawmessage)
      elif human == 1: # 바위
        print("AI의 선택: {}".format(general.rock))
        if not general.fastreveal:
          wait(2)
        print()
        print("비겼습니다!")
        print(nodraw.drawmessage)
      elif human == 2: # 보자기
        print("AI의 선택: {}".format(general.paper))
        if not general.fastreveal:
          wait(2)
        print()
        print("비겼습니다!")
        print(nodraw.drawmessage)
      
    
    input("Enter키를 눌러 메뉴로 돌아가기")
    if general.autoretry:
      nodraw_rsp()
    else:
      main()

def offline_rsp():
  global was_read
  print(clear + "< 오프라인 가위바위보 >")
  print("\"너 늦게냈어!\" \"너 바꿨잖아!\" 통하지 않는 오프라인 가위바위보입니다.")
  print("규칙은 기계가 딱딱 맞춰서 계산하니, 우길 생각은 접어두세요 ^^")
  print("기본 가위바위보 제외 변칙이 없는 유일한 가위바위보입니다.")
  print()
  if was_read == False:
    print("{ 규칙 설명 }")
    print("1. 각자 선 플레이어를 정합니다.")
    print("2. 자신의 차례에만 화면을 보고 가위, 바위, 보 중 하나를 입력합니다.")
    print("3. 후 플레이어가 입력한 후 함께 화면을 봅니다.")
    print("4. 모두가 보고 있을 때 Enter키를 눌러 결과를 오픈합니다.")
    print("   ※ 결과는 선 플레이어의 선택부터 차례대로 공개됩니다.")
    print("   ※ 메인 메뉴로 돌아가기는 선 플레이어의 턴에만 가능합니다.")
    print()
    print("!!! 규칙은 딱 한번만 보여줍니다 !!!")
    input("Enter키를 눌러 계속 진행")
    was_read = True
  
  offline_first()

def offline_first():
  global p1choose
  print(clear + "< 오프라인 가위바위보 >")
  print("\"너 늦게냈어!\" \"너 바꿨잖아!\" 통하지 않는 오프라인 가위바위보입니다.")
  print("규칙은 기계가 딱딱 맞춰서 계산하니, 우길 생각은 접어두세요 ^^")
  print("기본 가위바위보 제외 변칙이 없는 유일한 가위바위보입니다.")
  print()
  print("[ 선 플레이어의 차례입니다 ]")
  print("가위, 바위, 보 중 원하는 것을 입력하세요.")
  print("Ctrl+C키를 눌러 돌아가기")
  try:
    p1 = input("> ")
  except KeyboardInterrupt:
    main()
  else:
    if p1 not in rsp_inputs:
      print("잘못 입력하셨습니다!")
      print("가위, 바위, 보 중 하나를 입력해주세요.")
      input("Enter키를 눌러 돌아가기")
      lose_rsp()
    elif p1 in rsp_scissors:
      p1choose = 0
    elif p1 in rsp_rocks:
      p1choose = 1
    elif p1 in rsp_papers:
      p1choose = 2
  
  offline_second()

def offline_second():
  global p2choose
  print(clear + "< 오프라인 가위바위보 >")
  print("\"너 늦게냈어!\" \"너 바꿨잖아!\" 통하지 않는 오프라인 가위바위보입니다.")
  print("규칙은 기계가 딱딱 맞춰서 계산하니, 우길 생각은 접어두세요 ^^")
  print("기본 가위바위보 제외 변칙이 없는 유일한 가위바위보입니다.")
  print()
  print("[ 후 플레이어의 차례입니다 ]")
  print("가위, 바위, 보 중 원하는 것을 입력하세요.")
  p2 = input("> ")
  if p2 not in rsp_inputs:
    print("잘못 입력하셨습니다!")
    print("가위, 바위, 보 중 하나를 입력해주세요.")
    input("Enter키를 눌러 돌아가기")
    lose_rsp()
  elif p2 in rsp_scissors:
    p2choose = 0
  elif p2 in rsp_rocks:
    p2choose = 1
  elif p2 in rsp_papers:
    p2choose = 2
  
  offline_result()

def offline_result():
  print(clear + "< 오프라인 가위바위보 >")
  print("\"너 늦게냈어!\" \"너 바꿨잖아!\" 통하지 않는 오프라인 가위바위보입니다.")
  print("규칙은 기계가 딱딱 맞춰서 계산하니, 우길 생각은 접어두세요 ^^")
  print("기본 가위바위보 제외 변칙이 없는 유일한 가위바위보입니다.")
  print()
  print("[ 결과 발표 ]")
  input("모든 플레이어가 보고 있다면 Enter키를 누르세요.")
  print()
  print("잠시 후, 결과를 발표합니다..")
  wait(3)
  print()
  print("플레이어 1 : {}".format(general.rsp_list[p1choose]))
  wait(1)
  print("플레이어 2 : {}".format(general.rsp_list[p2choose]))
  
  wait(2)
  print()
  
  if p1choose == 2:
    if p2choose == 0:
      print("플레이어 2님이 승리했습니다!")
      print(offlinersp.endmessage)
    elif p2choose == 2:
      print("비겼습니다!")
      print(offlinersp.endmessage)
    else:
      print("플레이어 1님이 승리했습니다!")
      print(offlinersp.endmessage)
  elif p2choose == 2:
    if p1choose == 0:
      print("플레이어 1님이 승리했습니다!")
      print(offlinersp.endmessage)
    elif p1choose == 2:
      print("비겼습니다!")
      print(offlinersp.endmessage)
    else:
      print("플레이어 2님이 승리했습니다!")
      print(offlinersp.endmessage)
  elif p1choose > p2choose:
    print("플레이어 1님이 승리했습니다!")
    print(offlinersp.endmessage)
  elif p2choose > p1choose:
    print("플레이어 2님이 승리했습니다!")
    print(offlinersp.endmessage)
  elif p2choose == p1choose:
    print("비겼습니다!")
    print(offlinersp.endmessage)
  
  input("Enter키를 눌러 계속")
  if general.autoretry:
    offline_rsp()
  else:
    main()

def option():
  print(clear + "< 설정 >")
  print("여러가지 게임의 설정을 만질 수 있습니다.")
  print()
  print("{ 일반 }")
  print("General.FastReveal = {}".format(general.fastreveal))
  print("- 공개 전 긴박함을 없애고 빠르게 공개합니다.")
  print()
  print("General.AutoRetry = {}".format(general.autoretry))
  print("- 게임이 끝나면 자동으로 다시 시작합니다.")
  print()
  print("General.Rock = {}".format(general.rock))
  print("- 이 게임에서 바위는 이렇게 부릅니다.")
  print()
  print("General.Scissors = {}".format(general.scissors))
  print("- 이 게임에서 가위는 이렇게 부릅니다.")
  print()
  print("General.Paper = {}".format(general.paper))
  print("- 이 게임에서 보자기는 이렇게 부릅니다.")
  print()
  print("{ 기본 가위바위보 }")
  print("Normal.WinMessage = {}".format(normal.winmessage))
  print("- 당신이 이겼을 때 출력되는 메세지입니다.")
  print()
  print("Normal.LoseMessage = {}".format(normal.losemessage))
  print("- 당신이 졌을 때 출력되는 메세지입니다.")
  print()
  print("Normal.DrawMessage = {}".format(normal.drawmessage))
  print("- 비겼을 때 출력되는 메세지입니다.")
  print()
  print("{ 무조건 이기는 가위바위보 }")
  print("MustWin.LoseRatio = {}".format(mustwin.loseratio))
  print("- 이 값이 높을수록 질 확률이 내려갑니다.")
  print()
  print("MustWin.WinMessage = {}".format(mustwin.winmessage))
  print("- 당신이 이겼을 때 출력되는 메세지입니다.")
  print()
  print("MustWin.LoseMessage = {}".format(mustwin.losemessage))
  print("- 당신이 졌을 때 출력되는 메세지입니다.")
  print()
  print("{ 무조건 지는 가위바위보")
  print("MustLose.WinRatio = {}".format(mustlose.winratio))
  print("- 이 값이 높을수록 이길 확률이 내려갑니다.")
  print()
  print("MustLose.WinMessage = {}".format(mustlose.winmessage))
  print("- 당신이 이겼을 떄 출력되는 메세지입니다.")
  print()
  print("MustLose.LoseMessage = {}".format(mustlose.losemessage))
  print("- 당신이 졌을 때 출력되는 메세지입니다.")
  print()
  print("{ 비기지 못하는 가위바위보 }")
  print("NoDraw.DrawRatio = {}".format(nodraw.drawratio))
  print("- 이 값이 높을수록 비길 확률이 내려갑니다.")
  print()
  print("NoDraw.WinMessage = {}".format(nodraw.winmessage))
  print("- 당신이 이겼을 때 출력되는 메세지입니다.")
  print()
  print("NoDraw.LoseMessage = {}".format(nodraw.losemessage))
  print("- 당신이 졌을 때 출력되는 메세지입니다.")
  print()
  print("NoDraw.DrawMessage = {}".format(nodraw.drawmessage))
  print("- 비겼을 때 출력되는 메세지입니다.")
  print()
  print("{ 오프라인 가위바위보 }")
  print("OfflineRSP.EndMessage = {}".format(offlinersp.endmessage))
  print("- 게임이 끝났을 때 뜨는 메세지(대부분 승리를 축하하거나 패배를 조롱하는 메세지)")
  print()
  print("원하는 옵션 이름을 입력하고, 옵션값을 이퀄(=)로 구분하여 입력해주세요.")
  print("ex) Option.Test = 20(X) / General.Test=30(O) / General.String=Hello My Name(O)")
  print("나가려면 Ctrl + C를 입력해주세요.")
  try:
    OptionName, OptionValue = input("옵션을 입력해주세요: ").split("=")
  except ValueError:
    print("옵션 이름과 옵션값을 전부 입력해주세요.")
    print("등호는 한 개만 입력해주세요.")
    input("Enter키를 눌러 돌아가기")
    option()
  except KeyboardInterrupt:
    main()
  else:
    if OptionName.lower() in ["normal.winmessage", "normal.losemessage", "normal.drawmessage", "mustwin.loseratio", "mustwin.winmessage", "mustwin.losemessage", "mustlose.winratio", "mustlose.winmessage", "mustlose.losemessage", "nodraw.drawratio", "nodraw.winmessage", "nodraw.losemessage", "nodraw.drawmessage", "offlinersp.players", "offlinersp.endmessage", "general.rock", "general.scissors", "general.paper", "general.autoretry", "general.fastreveal"]:
      if OptionName.lower() == "normal.winmessage":
        normal.winmessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "normal.losemessage":
        normal.losemessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "normal.drawmessage":
        normal.drawmessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "mustwin.loseratio":
        try:
          mustwin.loseratio = int(OptionValue)
        except ValueError:
          print("MustWin.LoseRatio의 옵션값은 정수값만 가능합니다.")
          input("Enter키를 눌러 돌아가기")
          option()
        else:
          print("옵션을 성공적으로 변경했습니다.")
          print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
          input("Enter키를 눌러 돌아가기")
          option()
      elif OptionName.lower() == "mustwin.winmessage":
        mustwin.winmessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "mustwin.losemessage":
        mustwin.losemessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "mustlose.winratio":
        try:
          mustlose.winratio = int(OptionValue)
        except ValueError:
          print("MustLose.WinRatio의 옵션값은 정수값만 가능합니다.")
          input("Enter키를 눌러 돌아가기")
        else:
          print("옵션을 성공적으로 변경했습니다.")
          print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
          input("Enter키를 눌러 돌아가기")
          option()
      elif OptionName.lower() == "mustlose.winmessage":
        mustlose.winmessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "mustlose.losemessage":
        mustlose.losemessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "nodraw.drawratio":
        try:
          nodraw.drawratio = int(OptionValue)
        except ValueError:
          print("NoDraw.DrawRatio의 옵션값은 정수값만 가능합니다.")
          input("Enter키를 눌러 돌아가기")
        else:
          print("옵션을 성공적으로 변경했습니다.")
          print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
          input("Enter키를 눌러 돌아가기")
          option()
      elif OptionName.lower() == "nodraw.winmessage":
        nodraw.winmessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "nodraw.losemessage":
        nodraw.losemessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "nodraw.drawmessage":
        nodraw.drawmessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "offlinersp.endmessage":
        offlinersp.endmessage = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "general.rock":
        general.rock = OptionValue
        general.rsp_list[1] = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "general.scissors":
        general.scissors = OptionValue
        general.rsp_list[0] = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "general.paper":
        general.paper = OptionValue
        general.rsp_list[2] = OptionValue
        print("옵션을 성공적으로 변경했습니다.")
        print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
        input("Enter키를 눌러 돌아가기")
        option()
      elif OptionName.lower() == "general.autoretry":
        if int(OptionValue) in [0, 1]:
          general.autoretry = int(OptionValue)
          print("옵션을 성공적으로 변경했습니다.")
          print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
          input("Enter키를 눌러 돌아가기")
          option()
        else:
          print("이 옵션의 값은 0과 1만 허용됩니다.")
          input("Enter키를 눌러 돌아가기")
          option()
      elif OptionName.lower() == "general.fastreveal":
        if int(OptionValue) in [0, 1]:
          general.fastreveal = int(OptionValue)
          print("옵션을 성공적으로 변경했습니다.")
          print("이제 {}은 {}입니다.".format(OptionName, OptionValue))
          input("Enter키를 눌러 돌아가기")
          option()
        else:
          print("이 옵션의 값은 0과 1만 허용됩니다.")
          input("Enter키를 눌러 돌아가기")
          option()
    else:
      print("알 수 없는 옵션입니다.")
      print("오타가 있는지 확인해주세요.")
      input("Enter키를 눌러 돌아가기")
      option()

main()