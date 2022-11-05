import paho.mqtt.client as mqtt
import picamera
import io
import time

flag = False

# command 토픽으로 구독신청


def on_connect(client, userdata, flag, rc):
    client.subscribe("command", qos=0)

# command 토픽으로 받은 명령어 인식 start, stop


def on_message(client, userdata, msg):
    global flag
    global stream
    command = msg.payload.decode("utf-8")  # b'start' b'stop'으로 입력되는것 방지
    print(command + " 명령어 입력됨 ")
    if command == "start":
        print("moving jpeg print start!")
        flag = True  # start 입력시 무한반복 시작 => 이미지 출력
    elif command == "stop":
        print("moving jpeg print stop!")
        flag = False  # stop => 무한반복 종료


ip = input("브로커의 IP 주소>>")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip, 1883)

# 예제 6-5 응용
while True:
    with picamera.PiCamera(resolution=(640, 480), framerate=90) as camera:  # 최대 프레임 90
        stream = io.BytesIO()
        # 스탑 명령 입력전까지 계속 화면 출력
        # client.loop() #start 명령 인식
        print("command waiting")
        while flag == False:  # flag가 fasle라면 start 입력대기
            client.loop()
        for _ in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
            client.loop()  # stop명령인식
            if flag == False:  # stop 명령 입력시, 반복종료 start 입력전까지  무한대기
                break
            stream.seek(0)
            time.sleep(0.04)  # 출력속도와 영상의 실시간 싱크를 맞추기 위함
            # sleep사용하지 않을시, 출력속도에 밀려 실시간이 되지않음
            client.publish("mjpeg", stream.read(), qos=0)
            stream.seek(0)
            stream.truncate(0)
