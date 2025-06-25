import os
import sys

import requests

import subprocess
import pyautogui
import time


def get_post_by_id(id):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{str(id)}", timeout=5)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return response.json()  # Return parsed JSON if successful
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # e.g. 404 Not Found
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
    return None


def save_post_to_file(post):
    post_id = post["id"]
    post_title = post["title"]
    post_body = post["body"]
    try:
        subprocess.Popen(["notepad.exe"])
    except FileNotFoundError:
        print("Notepad.exe not found")
        return False
    except PermissionError:
        print("Notepad.exe permission error")
        return False
    except Exception as e:
        print(f"Notepad.exe error {e}")
        return False
    time.sleep(2)
    try:
        pyautogui.write(f"Title: {post_title}", interval=0.05)
        pyautogui.press("enter")
        pyautogui.write(f"Body: {post_body}", interval=0.05)
        pyautogui.press("enter")
        pyautogui.hotkey('ctrl', 's')
        time.sleep(2)
        filename = f"post {post_id}.txt"
        project_path = os.path.abspath(filename)

        pyautogui.write(project_path)
        pyautogui.press("enter")

        time.sleep(2)
    except pyautogui.FailSafeException:
        print("PyAutoGUI fail-safe triggered.")
        return False
    except Exception as e:
        print(f"Error typing text: {e}")
        return False

    try:
        pyautogui.hotkey('alt', 'f4')
    except Exception as e:
        print(f"Error closing Notepad: {e}")
        return False


def load_first_posts(count):
    success, failed = 0, 0
    for x in range(1, count + 1):
        post = get_post_by_id(x)
        if post is not None:
            print(post)
            is_saved = save_post_to_file(post)
            if is_saved:
                success += 1
            else:
                failed += 1
        else:
            failed += 1
    return count, success, failed
# load_first_ten_posts()
# save_post_to_file(get_post_by_id(1))
