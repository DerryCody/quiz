import pgzrun

WIDTH=1000
HEIGHT=900
TITLE="Quiz Game"

time=5
skipsleft=3
marque_box=Rect(10,0,1000,100)
question_box=Rect(10,120,750,150)
answer_box1=Rect(10,300,365,150)
answer_box2=Rect(10,475,365,150)
answer_box3=Rect(395,300,365,150)
answer_box4=Rect(395,475,365,150)
timer=Rect(780,120,230,150)
skip=Rect(780,300,230,325)
welcome="Welcome to the quiz game"
q=""
time_left=10
score=0
questions=[]
tot=0
current=0
gameov=False
boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
question=[]
def draw():
  screen.clear()
  screen.draw.filled_rect(marque_box,"green")
  screen.draw.filled_rect(question_box,"red")
  screen.draw.filled_rect(answer_box1,"black")
  screen.draw.filled_rect(answer_box2,"black")
  screen.draw.filled_rect(answer_box3,"black")
  screen.draw.filled_rect(answer_box4,"black")
  screen.draw.filled_rect(timer,"pink")
  screen.draw.filled_rect(skip,"pink")

  screen.draw.textbox(welcome,marque_box,color="White")
  screen.draw.textbox(question[0],question_box,color="White")
  screen.draw.textbox(question[1],answer_box1,color="White")
  screen.draw.textbox(question[2],answer_box2,color="White")
  screen.draw.textbox(question[3],answer_box3,color="White")
  screen.draw.textbox(question[4],answer_box4,color="White")
  screen.draw.textbox(str(time_left),timer,color="White")
  screen.draw.textbox("SKIP",skip,color="White")
  
def questionnaire():
  global questions
  global tot
  file=open("questions.txt","r")
  questions=file.readlines()
  file.close()
  tot=len(questions)

def skipq():
  global gameov,skipsleft
  if current<11and gameov==False and skipsleft>0:
    nq()
    skipsleft=skipsleft-1
  else:
    go()

def timedown():
  global time_left
  if time_left==0:
    go()
  else:
    time_left=time_left-1
    
def nq():
  global current,question,time_left
  question=questions[current].split(',')
  current=current+1
  time_left=10
  print(question)
questionnaire()
nq()

def right():
  global score,tot
  score=score+1
  if current<tot:
    nq()
  else:
    go()
  

def go():
  global question,time_left,score,gameov
  msg="Well played, you got a score of "+str(score)
  question=[msg,"-","-","-","-",5]
  time_left=0
  gameov=True
  
def on_mouse_down(pos):
  index=1
  for box in boxes:
    if box.collidepoint(pos):
      if index==int(question[5]):
        right()
      else:
        go()      
    index=index+1
  if skip.collidepoint(pos):
    skipq()
clock.schedule_interval(timedown,1)
pgzrun.go()