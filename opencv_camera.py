"""
OpenCV Camera Test
Please install OpenCV
```
pip install opencv-python
pip install opencv-contrib-python
```
"""

import cv2
from picamera2 import Picamera2
from libcamera import controls
import os
import asyncio

import seeed_python_reterminal.core as rt
import seeed_python_reterminal.button as rt_btn

import TkEasyGUI as sg

rt_btn.key_code = [0x290, 0x291, 0x292, 0x293]
btn_device = rt.get_button_device()


# ボタンの状態を取得する関数
async def btn_coroutine(device):
    async for event in device.async_read_loop():
        buttonEvent = rt_btn.ButtonEvent(event)
        if buttonEvent.name != None:
            print(f"name={str(buttonEvent.name)} value={buttonEvent.value}")

# メイン関数
async def hw_loop():
    # 非同期タスクをスケジュール
    asyncio.ensure_future(btn_coroutine(btn_device))
    # イベントループを無限に実行
    while True:
        await asyncio.sleep(1)

# Load the pre-trained Haar Cascade classifier for face detection                     
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

WIDTH = 1200
HEIGHT = 600

# camera
picam2 = Picamera2()
#HDRをオンにする
os.system("v4l2-ctl --set-ctrl wide_dynamic_range=1 -d /dev/v4l-subdev1")
print("Setting HDR to ON")

picam2.preview_configuration.main.size = (2304,1296)
#picam2.preview_configuration.main.size = (WIDTH,HEIGHT)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

#カメラを連続オートフォーカスモードにする
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast})

# layout
layout = [
    [
        sg.Button("Save", key="-save-"),
        sg.Text("／Date："),
        sg.InputText("2024/09/01", size=(10, 1), key="-date-"),
        sg.Text("／Position："),
        sg.InputText("hara", size=(10, 1), key="-pos-"),
        sg.Text("／品種："),
        sg.Combo(["コシヒカリ", "ひゃくまん穀", "ゆめみづほ","能登ひかり"], default_value="コシヒカリ", size=(15, 1), key="-kind-", enable_events=True),
        sg.Text("／pos_cnt："),
        sg.InputText("01", size=(5, 1), key="-pos_cnt-"),
        sg.Text("／pic_cnt："),
        sg.InputText("001", size=(5, 1), key="-pic_cnt-"),
        sg.VSeparator(),
        sg.Button("Exit", key="-exit-"),
    ],
    [sg.Image(key="-image-", size=(WIDTH, HEIGHT))],
]

async def gui_loop():

    try:
        # event loop
        print("Window start")
        window = sg.Window("Genmai Capture", layout)
        while True:
            event, values = window.read(timeout=100)
            print('#', event, values)
            if event in (sg.WIN_CLOSED, "-exit-"):
                break

            frame_raw = picam2.capture_array()
            frame_rev = cv2.flip(frame_raw, -1)  # Flip the frame horizontally
            frame_disp = frame_rev.copy()  # Create a copy of the flipped frame

            # Convert the image to grayscale for face detection
            frame_gray = cv2.cvtColor(frame_disp, cv2.COLOR_BGR2GRAY)

            # Perform face detection
            faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame_disp, (x, y), (x+w, y+h), (255, 0, 0), 2)

            frame = cv2.resize(frame_disp, (WIDTH, HEIGHT), fx=0, fy=0)
            img = cv2.imencode(".png", frame)[1].tobytes()

            window["-image-"].update(img)

            if event == "-save-":
                str_file = ""
                str_date = values["-date-"].replace("/", "")
                str_pos = values["-pos-"]
                str_kind = values["-kind-"]
                str_pos_cnt = values["-pos_cnt-"]
                str_pic_cnt = values["-pic_cnt-"]
                str_file = str_date + "_" + str_pos + "_" + str_kind + "_" + str_pos_cnt + "_" + str_pic_cnt + ".jpg"
                cv2.imwrite(os.path.join(r'./_capture', str_file), frame_rev)
                # cv2.imwrite(os.path.join(r'./_capture', str_file), picam2.capture_array())
                sg.popup(str_file)

                num_pic_cnt = int(str_pic_cnt)
                num_pic_cnt += 1
                str_pic_cnt = str(num_pic_cnt).zfill(3)
                window["-pic_cnt-"].update(text=str_pic_cnt)

    finally:
        # Release resources
        window.close()
        picam2.stop()
        picam2.close()

# メインのイベントループを作成し、コルーチンを実行
async def main():
    await asyncio.gather(hw_loop(), gui_loop())

asyncio.run(gui_loop())
# asyncio.run(main())

