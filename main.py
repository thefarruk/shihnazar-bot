from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

import time
import json
import requests
import os
TOKEN = os.getenv("TOKEN")


TOKEN = "7532027868:AAGfw7-QvazuId3r_9TzrJLmho5_jomyqg0"  # <-- сюда вставь токен Бота Shihnazar Alymov
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

STATE = {}  # chat_id -> {"lang": "ru"/"tr"/"tm"}


def send_message(chat_id, text, reply_markup=None):
    data = {
        "chat_id": chat_id,
        "text": text
    }
    if reply_markup is not None:
        data["reply_markup"] = json.dumps(reply_markup)

    resp = requests.post(f"{BASE_URL}/sendMessage", data=data)
    print("send_message:", resp.text)


# -------------------- ТЕКСТЫ ПО ЯЗЫКАМ --------------------

LANGS = {
    "ru": {
        "button_lang": "Русский",
        "start_text": (
            "Shihnazar Alymov — офисные услуги и перевод денег.\n\n"
            "Выберите язык:"
        ),
        "menu_title": "Выберите раздел:",
        "btn_office": "🏢 Офисные услуги",
        "btn_transfer": "💸 Перевод денег",
        "btn_contacts": "📞 Контакты",
        "btn_back_main": "⬅️ В главное меню",

        "office_text": (
            "🏢 Офисные услуги\n\n"
            "Телефон офиса:\n"
            "02125878090\n"
            "+90 555 037 39 97"
        ),

        "transfer_choose_bank": "Выберите банк для перевода:",

        "btn_bank_garanti": "Garanti Bank (TRY – USD)",
        "btn_bank_ziraat": "Ziraat Bankası (TRY – USD)",
        "btn_bank_isbank": "İşbank",
        "btn_bank_vakif": "Vakıfbank",
        "btn_bank_sber": "Sberbank (RUB)",
        "btn_bank_tether": "Tether USDT (TRC20)",

        "garanti_text": (
            "💸 Garanti Bank (TRY – USD)\n\n"
            "IBAN TRY: TR51 0006 2000 6320 0006 6694 67\n"
            "IBAN USD: TR26 0006 2000 6320 0009 0967 60"
        ),
        "ziraat_text": (
            "💸 Ziraat Bankası (TRY – USD)\n\n"
            "IBAN TRY: TR2600 0100 2131 7564 2356 5005\n"
            "IBAN USD: TR9600 0100 2131 7564 2356 5006"
        ),
        "isbank_text": (
            "💸 İşbank\n\n"
            "IBAN TRY: TR5300 0640 0000 1140 0099 3169\n"
            "IBAN USD: TR5900 0640 0000 2140 0025 7505"
        ),
        "vakif_text": (
            "💸 Vakıfbank\n\n"
            "IBAN TRY: TR63 0001 5001 5800 7317 3967 32\n"
            "IBAN USD: TR65 0001 5001 5804 8022 7796 27"
        ),
        "sber_text": (
            "💸 Sberbank (RUB)\n\n"
            "Телефон: +7 926 084 39 97\n"
            "Карта: 2202 2063 0890 4304"
        ),
        "tether_text": (
            "💸 Tether USDT (TRC20)\n\n"
            "Адрес: TRswofHEP2mukbjAFLbBXHN342BUxarLNj\n"
            "Сеть: TRON (TRC20)"
        ),

        "contacts_text": (
            "📞 Контакты\n\n"
            "Телефон: +90 555 037 39 97\n\n"
            "Нажмите на кнопку ниже, чтобы открыть WhatsApp, Telegram или Instagram."
        ),
    },

    "tr": {
        "button_lang": "Türkçe",
        "start_text": (
            "Shihnazar Alymov — ofis hizmetleri ve para transferi.\n\n"
            "Dil seçin:"
        ),
        "menu_title": "Bölüm seçin:",
        "btn_office": "🏢 Ofis hizmetleri",
        "btn_transfer": "💸 Para transferi",
        "btn_contacts": "📞 İletişim",
        "btn_back_main": "⬅️ Ana menüye dön",

        "office_text": (
            "🏢 Ofis hizmetleri\n\n"
            "Ofis telefonu:\n"
            "02125878090\n"
            "+90 555 037 39 97"
        ),

        "transfer_choose_bank": "Para transferi için banka seçin:",

        "btn_bank_garanti": "Garanti Bank (TRY – USD)",
        "btn_bank_ziraat": "Ziraat Bankası (TRY – USD)",
        "btn_bank_isbank": "İşbank",
        "btn_bank_vakif": "Vakıfbank",
        "btn_bank_sber": "Sberbank (RUB)",
        "btn_bank_tether": "Tether USDT (TRC20)",

        "garanti_text": (
            "💸 Garanti Bank (TRY – USD)\n\n"
            "IBAN TRY: TR51 0006 2000 6320 0006 6694 67\n"
            "IBAN USD: TR26 0006 2000 6320 0009 0967 60"
        ),
        "ziraat_text": (
            "💸 Ziraat Bankası (TRY – USD)\n\n"
            "IBAN TRY: TR2600 0100 2131 7564 2356 5005\n"
            "IBAN USD: TR9600 0100 2131 7564 2356 5006"
        ),
        "isbank_text": (
            "💸 İşbank\n\n"
            "IBAN TRY: TR5300 0640 0000 1140 0099 3169\n"
            "IBAN USD: TR5900 0640 0000 2140 0025 7505"
        ),
        "vakif_text": (
            "💸 Vakıfbank\n\n"
            "IBAN TRY: TR63 0001 5001 5800 7317 3967 32\n"
            "IBAN USD: TR65 0001 5001 5804 8022 7796 27"
        ),
        "sber_text": (
            "💸 Sberbank (RUB)\n\n"
            "Telefon: +7 926 084 39 97\n"
            "Kart: 2202 2063 0890 4304"
        ),
        "tether_text": (
            "💸 Tether USDT (TRC20)\n\n"
            "Adres: TRswofHEP2mukbjAFLbBXHN342BUxarLNj\n"
            "Ağ: TRON (TRC20)"
        ),

        "contacts_text": (
            "📞 İletişim\n\n"
            "Telefon: +90 555 037 39 97\n\n"
            "WhatsApp, Telegram veya Instagram için aşağıdaki düğmeleri kullanın."
        ),
    },

    "tm": {
        "button_lang": "Türkmençe",
        "start_text": (
            "Shihnazar Alymov — ofis hyzmatlary we pul geçirilişi.\n\n"
            "Dil saýlaň:"
        ),
        "menu_title": "Bölüm saýlaň:",
        "btn_office": "🏢 Ofis hyzmatlary",
        "btn_transfer": "💸 Pul geçirilişi",
        "btn_contacts": "📞 Habarlaşmak",
        "btn_back_main": "⬅️ Esasy menýu",

        "office_text": (
            "🏢 Ofis hyzmatlary\n\n"
            "Ofis telefonlary:\n"
            "02125878090\n"
            "+90 555 037 39 97"
        ),

        "transfer_choose_bank": "Pul geçirmek üçin bank saýlaň:",

        "btn_bank_garanti": "Garanti Bank (TRY – USD)",
        "btn_bank_ziraat": "Ziraat Bankası (TRY – USD)",
        "btn_bank_isbank": "İşbank",
        "btn_bank_vakif": "Vakıfbank",
        "btn_bank_sber": "Sberbank (RUB)",
        "btn_bank_tether": "Tether USDT (TRC20)",

        "garanti_text": (
            "💸 Garanti Bank (TRY – USD)\n\n"
            "IBAN TRY: TR51 0006 2000 6320 0006 6694 67\n"
            "IBAN USD: TR26 0006 2000 6320 0009 0967 60"
        ),
        "ziraat_text": (
            "💸 Ziraat Bankası (TRY – USD)\n\n"
            "IBAN TRY: TR2600 0100 2131 7564 2356 5005\n"
            "IBAN USD: TR9600 0100 2131 7564 2356 5006"
        ),
        "isbank_text": (
            "💸 İşbank\n\n"
            "IBAN TRY: TR5300 0640 0000 1140 0099 3169\n"
            "IBAN USD: TR5900 0640 0000 2140 0025 7505"
        ),
        "vakif_text": (
            "💸 Vakıfbank\n\n"
            "IBAN TRY: TR63 0001 5001 5800 7317 3967 32\n"
            "IBAN USD: TR65 0001 5001 5804 8022 7796 27"
        ),
        "sber_text": (
            "💸 Sberbank (RUB)\n\n"
            "Telefon: +7 926 084 39 97\n"
            "Kart: 2202 2063 0890 4304"
        ),
        "tether_text": (
            "💸 Tether USDT (TRC20)\n\n"
            "Adres: TRswofHEP2mukbjAFLbBXHN342BUxarLNj\n"
            "Tordan: TRON (TRC20)"
        ),

        "contacts_text": (
            "📞 Habarlaşmak üçin\n\n"
            "Telefon: +90 555 037 39 97\n\n"
            "Aşakdaky dügmelerden WhatsApp, Telegram ýa-da Instagram saýlaň."
        ),
    }
}


def get_lang_keyboard():
    return {
        "keyboard": [
            [{"text": LANGS["ru"]["button_lang"]}],
            [{"text": LANGS["tr"]["button_lang"]}],
            [{"text": LANGS["tm"]["button_lang"]}],
        ],
        "resize_keyboard": True,
        "one_time_keyboard": True
    }


def get_main_menu_keyboard(lang_code):
    l = LANGS[lang_code]
    return {
        "keyboard": [
            [{"text": l["btn_office"]}],
            [{"text": l["btn_transfer"]}],
            [{"text": l["btn_contacts"]}],
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }


def get_bank_menu_keyboard(lang_code):
    l = LANGS[lang_code]
    return {
        "keyboard": [
            [{"text": l["btn_bank_garanti"]}],
            [{"text": l["btn_bank_ziraat"]}],
            [{"text": l["btn_bank_isbank"]}],
            [{"text": l["btn_bank_vakif"]}],
            [{"text": l["btn_bank_sber"]}],
            [{"text": l["btn_bank_tether"]}],
            [{"text": l["btn_back_main"]}],
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }


def get_contacts_inline_keyboard(lang_code):
    # Тексты на кнопках можно чуть отличать по языку, но ссылки одинаковые
    if lang_code == "ru":
        btn_whatsapp = "💬 WhatsApp"
        btn_telegram = "📨 Telegram"
        btn_instagram = "📷 Instagram"
    elif lang_code == "tr":
        btn_whatsapp = "💬 WhatsApp"
        btn_telegram = "📨 Telegram"
        btn_instagram = "📷 Instagram"
    else:
        btn_whatsapp = "💬 WhatsApp"
        btn_telegram = "📨 Telegram"
        btn_instagram = "📷 Instagram"

    return {
        "inline_keyboard": [
            [
                {"text": btn_whatsapp, "url": "https://api.whatsapp.com/send/?phone=905550373997&text&type=phone_number&app_absent=0&wame_ctl=1"}
            ],
            [
                {"text": btn_telegram, "url": "https://t.me/shihnazaralymov"}
            ],
            [
                {"text": btn_instagram, "url": "https://www.instagram.com/shihnazaralymov/"}
            ]
        ]
    }

def detect_lang_from_button(text):
    for code, data in LANGS.items():
        if text == data["button_lang"]:
            return code
    return None


def handle_update(update):
    message = update.get("message")
    if not message:
        return

    chat_id = message["chat"]["id"]
    text = (message.get("text") or "").strip()

    # /start — всегда выбор языка
    if text == "/start":
        STATE[chat_id] = {"lang": None}
        send_message(
            chat_id,
            "Shihnazar Alymov\n\nВыберите язык / Dil seçin / Dil saýlaň:",
            reply_markup=get_lang_keyboard()
        )
        return

    # если язык ещё не выбран — ждём выбор языка
    if chat_id in STATE and STATE[chat_id].get("lang") is None:
        lang_code = detect_lang_from_button(text)
        if not lang_code:
            send_message(chat_id, "Пожалуйста, выберите язык кнопкой.", reply_markup=get_lang_keyboard())
            return
        STATE[chat_id]["lang"] = lang_code
        lang = LANGS[lang_code]
        send_message(chat_id, lang["start_text"], reply_markup=get_main_menu_keyboard(lang_code))
        return

    # если вообще нет состояния — отправим на /start
    if chat_id not in STATE or not STATE[chat_id].get("lang"):
        send_message(chat_id, "Напишите /start, чтобы выбрать язык.")
        return

    lang_code = STATE[chat_id]["lang"]
    lang = LANGS[lang_code]

    # --- ОБРАБОТКА ГЛАВНОГО МЕНЮ ---

    # Офисные услуги
    if text == lang["btn_office"]:
        send_message(chat_id, lang["office_text"], reply_markup=get_main_menu_keyboard(lang_code))
        return

    # Перевод денег — показать меню банков
    if text == lang["btn_transfer"]:
        send_message(
            chat_id,
            lang["transfer_choose_bank"],
            reply_markup=get_bank_menu_keyboard(lang_code)
        )
        return

    # Контакты — текст + inline-кнопки
    if text == lang["btn_contacts"]:
        send_message(
            chat_id,
            lang["contacts_text"],
            reply_markup=get_contacts_inline_keyboard(lang_code)
        )
        return

    # --- ОБРАБОТКА МЕНЮ БАНКОВ ---

    if text == lang["btn_bank_garanti"]:
        send_message(chat_id, lang["garanti_text"], reply_markup=get_bank_menu_keyboard(lang_code))
        return

    if text == lang["btn_bank_ziraat"]:
        send_message(chat_id, lang["ziraat_text"], reply_markup=get_bank_menu_keyboard(lang_code))
        return

    if text == lang["btn_bank_isbank"]:
        send_message(chat_id, lang["isbank_text"], reply_markup=get_bank_menu_keyboard(lang_code))
        return

    if text == lang["btn_bank_vakif"]:
        send_message(chat_id, lang["vakif_text"], reply_markup=get_bank_menu_keyboard(lang_code))
        return

    if text == lang["btn_bank_sber"]:
        send_message(chat_id, lang["sber_text"], reply_markup=get_bank_menu_keyboard(lang_code))
        return

    if text == lang["btn_bank_tether"]:
        send_message(chat_id, lang["tether_text"], reply_markup=get_bank_menu_keyboard(lang_code))
        return

    if text == lang["btn_back_main"]:
        send_message(chat_id, lang["menu_title"], reply_markup=get_main_menu_keyboard(lang_code))
        return

    # Любой другой текст — просто показываем главное меню
    send_message(chat_id, lang["menu_title"], reply_markup=get_main_menu_keyboard(lang_code))


def main():
    offset = None
    while True:
        params = {"timeout": 50}
        if offset is not None:
            params["offset"] = offset

        resp = requests.get(f"{BASE_URL}/getUpdates", params=params)
        data = resp.json()

        for update in data.get("result", []):
            offset = update["update_id"] + 1
            handle_update(update)

        time.sleep(1)


if __name__ == "__main__":
    main()

def run_flask():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    # здесь запускается твой бот
    main()


