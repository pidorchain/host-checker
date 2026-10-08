import os
import time
import requests

URL = "https://adminpanelcasuev-github-io.onrender.com/admin"
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


def check():
    try:
        start = time.time()
        # Render на бесплатном тарифе "просыпается" долго, поэтому таймаут 60 сек
        r = requests.get(URL, timeout=60)
        ms = int((time.time() - start) * 1000)
        if r.status_code < 500:
            return f"✅ Сайт активен\nКод: {r.status_code}, ответ за {ms} мс"
        return f"🔴 Сайт лёг\nКод ответа: {r.status_code}"
    except Exception as e:
        return f"🔴 Сайт лёг\nОшибка: {type(e).__name__}"


def send(text):
    for chat_id in CHAT_ID.split(","):
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id.strip(), "text": f"{text}\n{URL}"},
            timeout=30,
        )


if __name__ == "__main__":
    send(check())
