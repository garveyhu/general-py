import tkinter as tk
import random
import threading
import time
import pygame
from pathlib import Path


def play_background_music():
    """播放背景音乐"""
    try:
        pygame.mixer.init()

        # 获取当前脚本所在目录
        current_dir = Path(__file__).parent
        music_file = current_dir / "Princess (0.8x) - J-I-E.mp3"

        if music_file.exists():
            pygame.mixer.music.load(str(music_file))
            pygame.mixer.music.play(-1)  # -1表示循环播放
            print(f"正在播放音乐: {music_file.name}")
        else:
            print(f"音乐文件未找到，请确保 '{music_file.name}' 文件在项目根目录下")
            print(f"查找路径: {music_file}")
    except Exception as e:
        print(f"播放音乐时出错: {e}")


def show_warm_tip():
    # 创建窗口
    window = tk.Tk()

    # 获取屏幕宽高
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 随机窗口位置（确保窗口完全显示在屏幕内）
    window_width = 250
    window_height = 60
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)

    # 设置窗口标题和大小位置
    window.title("温馨提示")
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 提示文字列表（已添加新内容）
    tips = [
        "多喝水哦~",
        "保持微笑呀",
        "每天都要元气满满",
        "记得吃水果",
        "保持好心情",
        "好好爱自己",
        "我想你了",
        "梦想成真",
        "期待下一次见面",
        "顺顺利利",
        "早点休息",
        "愿所有烦恼都消失",
        "别熬夜",
        "今天过得开心嘛",
        "天冷了，多穿衣服",
    ]
    tip = random.choice(tips)

    # 多样的背景颜色
    bg_colors = [
        "lightpink",
        "skyblue",
        "lightgreen",
        "lavender",
        "lightyellow",
        "plum",
        "coral",
        "bisque",
        "aquamarine",
        "mistyrose",
        "honeydew",
        "lavenderblush",
        "oldlace",
    ]
    bg = random.choice(bg_colors)

    # 创建标签并显示文字
    tk.Label(window, text=tip, bg=bg, font=("微软雅黑", 16), width=30, height=3).pack()

    # 窗口置顶显示
    window.attributes("-topmost", True)

    # 10秒后自动关闭窗口
    window.after(20000, window.destroy)

    window.mainloop()


# 启动背景音乐
music_thread = threading.Thread(target=play_background_music)
music_thread.start()

# 创建线程列表
threads = []

# 窗口数量（根据屏幕大小可调整）
for i in range(300):
    t = threading.Thread(target=show_warm_tip)
    threads.append(t)
    time.sleep(0.005)  # 快速弹出窗口
    threads[i].start()

# 10秒后停止程序并停止音乐
time.sleep(20)

# 停止音乐
try:
    pygame.mixer.music.stop()
    pygame.mixer.quit()
except:
    pass
