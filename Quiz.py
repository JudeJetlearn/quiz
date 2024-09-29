import pgzrun

TITLE = "QUIZ MASTER"
WIDTH = 870
HEIGHT = 650 

narquee_box = Rect(0,0 10,75)
question_box = Rect(0,0 25,100)
timer_box = Rect(0,0 50,50)
answer_box1 = Rect(0,0 60,50)
answer_box2 = Rect(0,0 60,50)
answer_box3 = Rect(0,0 60,50)
answer_box4 = Rect(0,0 60,50)
skip_box = Rect(0,0 60,100)

score = 0
time_left = 10
questions_file_name = "question.txt"
narquee_measage = ""
is_game_over = False

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
question = []
question_count = 0
question_index = 0

narquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global narquee_box
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(narquee_box,"black")
    screen.draw.filled_rect(question_box,"silver")
    screen.draw.filled_rect(timer_box,"blue")
    screen.draw.filled_rect(skip_box,"green")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"gold")

    narquee_measage="Welcome To Quiz Master!"
    narquee_measage=narquee_measage+"Q:" {question_index} of {question_count}

    screen.draw.textbox(narquee_measage,narquee_box,color="white")
    screen.draw.textbox(
        str(time_left)timer_box,
        color="white",shadow=(0.5,0.5),
        scolor="dim grey"
    )

    screen.draw.textbox(
        "skip", skip_box,
        color="black",angle=-90
    )

    screen.draw.textbox(
        question[0].strip(), question_box,
        color="white",shadow=(0.5,0.5),
        scolor="dim grey"
    )

    index = 1 
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(), answer_box, color="black")
        index = index + 1

def update():
    move_narquee_box()


    def move_narquee_box():
        narquee_box.x = narquee_box.x-2
        if narquee_box.right < 0 :
            narquee_box.x = WIDTH     
        

    

  
