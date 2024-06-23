import pygame
import pandas as pd
import os
import random

pygame.init()

# 화면 설정
width = 1200
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('음료수 만들기')

# 배경 음악 설정
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

# 과일 및 재료 이미지 로드
images = {
    '딸기': pygame.image.load('strawberry.png'),
    '바나나': pygame.image.load('banana.png'),
    '복숭아': pygame.image.load('peach.png'),
    '체리': pygame.image.load('cherry.png'),
    '꿀': pygame.image.load('honey.png'),
    '얼음': pygame.image.load('ice.png'),
    '우유': pygame.image.load('milk.png'),
    '초콜릿': pygame.image.load('chocolate.png')
}

# 이미지 크기 조정 및 확대 이미지 생성
scaled_images = {}
hovered_images = {}
for key in images:
    scaled_images[key] = pygame.transform.scale(images[key], (160, 190))
    hovered_images[key] = pygame.transform.scale(images[key], (200, 230))

# 글꼴 설정
font_name = './NanumBarunpenB.ttf'
font = pygame.font.Font(font_name, 60)
small_font = pygame.font.Font(font_name, 40)

# 시간 설정
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
time_limit = 30

# 점수 변수 초기화
score = 0

# 최고 기록 파일 경로
highscore_file = 'highscores.xlsx'

# 최고 기록 불러오기
def read_db(file_path):
    if os.path.exists(file_path):
        return pd.read_excel(file_path)
    else:
        return pd.DataFrame(columns=['Name', 'Score'])

# 최고 기록 저장하기
def write_db(file_path, df):
    df.to_excel(file_path, index=False)

highscores_df = read_db(highscore_file)

# 주문서 초기화
fruits_order = []
ingredients_order = []
completion_message = ''  # 주문 완료 메시지

def new_order():
    global fruits_order, ingredients_order, fruits_clicked, ingredients_clicked
    fruits = ['딸기', '바나나', '복숭아', '체리']
    ingredients = ['꿀', '얼음', '우유', '초콜릿']
    fruits_order = random.sample(fruits, 1)
    ingredients_order = random.sample(ingredients, 1)
    fruits_clicked = False
    ingredients_clicked = False

new_order()

# 시작 화면 표시 여부
show_start_screen = True

def start_screen():
    global show_start_screen
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start = False
                show_start_screen = False

        screen.fill((255, 255, 255))
        title_text = font.render('< 음료수 만들기 >', True, (0, 0, 0))
        screen.blit(title_text, (width // 2 - 200, height // 2 - 100))
        start_text = small_font.render('시작하려면 마우스로 클릭하세요.', True, (0, 0, 0))
        screen.blit(start_text, (width // 2 - 220, height // 2 + 30))
        pygame.display.flip()
        clock.tick(30)

running = True
game_over = False
input_active = False
user_text = ''

while running:
    if show_start_screen:
        start_screen()
        start_ticks = pygame.time.get_ticks()  # 게임 시작 시 시간 초기화

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # 클릭 감지
            mouse_x, mouse_y = event.pos
            keys = list(scaled_images.keys())
            for i in range(len(keys)):
                key = keys[i]
                image = scaled_images[key]
                col = i % 4  # 열 계산
                row = i // 4  # 행 계산
                x = 100 + col * 200
                y = 250 + row * 250
                rect = image.get_rect(topleft=(x, y))
                if rect.collidepoint(mouse_x, mouse_y):
                    if key in ingredients_order:
                        ingredients_clicked = True
                    if key in fruits_order:
                        fruits_clicked = True

                    if ingredients_clicked and fruits_clicked:
                        score += 100  # 두 가지 조건 모두 충족 시 점수 증가
                        # 주문 완료 메시지 설정
                        fruit = fruits_order[0]
                        ingredient = ingredients_order[0]
                        if ingredient == '꿀':
                            completion_message = f'{fruit} 주스 완성!'
                        elif ingredient == '얼음':
                            completion_message = f'{fruit} 스무디 완성!'
                        elif ingredient == '우유':
                            completion_message = f'{fruit} 라떼 완성!'
                        elif ingredient == '초콜릿':
                            completion_message = f'{fruit} 초코 완성!'
                        new_order()  # 새로운 주문 생성
        elif event.type == pygame.KEYDOWN and game_over:
            if input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    # 점수 저장
                    if score > 0:
                        new_score_df = pd.DataFrame([[user_text, score]], columns=['Name', 'Score'])
                        highscores_df = pd.concat([highscores_df, new_score_df], ignore_index=True)
                        highscores_df = highscores_df.sort_values(by='Score', ascending=False)
                        write_db(highscore_file, highscores_df)
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

    if not game_over:
        # 화면을 흰색으로 채우기
        screen.fill((255, 255, 255))

        # 세로선 그리기
        pygame.draw.line(screen, (0, 0, 0), (width // 2 + 300, 0), (width // 2 + 300, height), 5)

        # 마우스 위치 가져오기
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # 과일 및 재료 이미지 그리기
        keys = list(scaled_images.keys())
        for i in range(len(keys)):
            key = keys[i]
            image = scaled_images[key]
            col = i % 4  # 열 계산
            row = i // 4  # 행 계산
            x = 100 + col * 200
            y = 250 + row * 250
            rect = image.get_rect(topleft=(x, y))

            # 마우스가 이미지 위에 있으면 확대된 이미지 그리기
            if rect.collidepoint(mouse_x, mouse_y):
                screen.blit(hovered_images[key], (x - 15, y - 15))
            else:
                screen.blit(image, (x, y))

        # 텍스트 렌더링
        order_text = font.render('<주문서>', True, (0, 0, 0))
        screen.blit(order_text, (width - 250, 250))

        # 설명문
        explain_text = small_font.render('* 주문서에 해당하는 그림을 마우스로 클릭하세요. *', True, (0, 0, 0))
        screen.blit(explain_text, (width // 20, 150))

        # 주문서 아이템 렌더링
        order_items = fruits_order + ingredients_order
        i = 0  # 인덱스 초기화
        for item in order_items:
            item_text = font.render(item, True, (0, 0, 0))
            screen.blit(item_text, (width - 250, 350 + i * 100))
            i += 1  # 인덱스 증가

        # 경과 시간 계산
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        countdown = time_limit - seconds

        # 타이머 텍스트 렌더링
        timer_text = font.render(f'시간: {int(countdown)}s', True, (0, 0, 0))
        screen.blit(timer_text, (width - 250, 50))

        # 점수 텍스트 렌더링
        score_text = font.render(f'점수: {score}', True, (0, 0, 0))
        screen.blit(score_text, (50, 50))

        # 주문 완료 메시지 렌더링
        if completion_message:
            completion_text = small_font.render(completion_message, True, (0, 0, 0))
            screen.blit(completion_text, (width - 270, height - 100))

        # 시간이 0이 되면 게임 오버
        if countdown <= 0:
            game_over = True
            input_active = True

        # 화면 업데이트
        pygame.display.flip()

        # 초당 프레임 설정
        clock.tick(30)

    else:
        # 게임 오버 화면
        screen.fill((255, 255, 255))

        game_over_text = font.render('<게임 오버>', True, (0, 0, 0))
        screen.blit(game_over_text, (width // 2 - 150, height // 2 - 300))

        if input_active:
            prompt_text = small_font.render('이름을 영어로 입력해주세요.', True, (0, 0, 0))
            screen.blit(prompt_text, (width // 2 - 200, height // 2 - 100))
            # 텍스트 입력 상자 그리기
            input_box = pygame.Rect(width // 2 - 150, height // 2 - 50, 300, 130)
            pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
            input_text = font.render(user_text, True, (0, 0, 0))
            screen.blit(input_text, (input_box.x + 10, input_box.y + 10))

        else:
            # 최고 기록 표시
            highscore_text = font.render('최고 기록', True, (0, 0, 0))
            screen.blit(highscore_text, (width // 2 - 125, height // 2 - 200))

            # 상위 5위 점수 표시
            top_5_scores = highscores_df.head(5)
            i = 0  # 인덱스 초기화
            for idx, row in top_5_scores.iterrows():
                score_text = font.render(f'{i + 1}. {row["Name"]}: {row["Score"]}', True, (0, 0, 0))
                screen.blit(score_text, (width // 2 - 160, height // 2 - 100 + i * 80))
                i += 1  # 인덱스 증가

        pygame.display.flip()

# 종료
pygame.quit()