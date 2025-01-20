import os
from telegram.ext import Application, CommandHandler, CallbackContext, Update

# 从环境变量中获取 Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# 创建 /start 命令的处理器
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('你好！我是你的 Telegram bot！')

# 主函数
async def main():
    # 创建 Application 实例
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # 添加 /start 命令的处理器
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # 启动 Bot
    await application.run_polling()

# 启动主函数
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
