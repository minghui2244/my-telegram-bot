from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# 你的 Telegram Bot Token
TELEGRAM_BOT_TOKEN = '7485272939:AAElnZbnpRPKbMt0RP5gPWQSPd4f9_IO630'

# 创建 /start 命令的处理器
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('你好！我是你的 Telegram bot！')

# 主函数
async def main():
    # 使用你的 Token 创建应用
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # 添加 /start 命令处理器
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # 启动 Bot
    await application.run_polling()

# 启动主函数
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

