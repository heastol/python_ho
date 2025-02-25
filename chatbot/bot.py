from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import talk_ldh as tk
import gemini, os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("안녕하세요! 저는 JARVIS입니다. 무엇을 도와드릴까요?")

async def send_photo(update, context):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6JqKS121a3YEx2g3JQmwJYU8ZrKwBAEtYSw&s"
    await update.message.reply_photo(photo = photo_url, caption = "사진 이미지 불러왔습니다.")
    
async def monitor_chat(update, context):
    user_text = update.message.text # 감지된 메세지들
    chat_id = update.message.chat_id # 메세지가 온 채팅방

    if "GPT" in user_text:
        res = gemini.aiai(user_text.replace("gpt", ""))
        await context.bot.send.message(chat_id = chat_id, text = res,) #  parse_mode = "MarkdownV2"
    elif "영화정보" in user_text: pass
        # await 영화정보크롤링()함수를 실행
    elif "사진줘" in user_text:
        await send_photo(update, context)
    else:
        for key, res in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await context.bot.send_message(chat_id = chat_id, text = res)
                break # 한 개의 키워드에만 반응

def main():
    app = Application.builder().token(TOKEN).build()
    # 명령어 핸들러 추가
    app.add_handler(CommandHandler("start", start))
    # 응답 핸들러 추가
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat))

    print("텔레그램 봇이 실행중입니다. 모니터링 중...")
    app.run_polling()

if __name__ == "__main__":
    main()