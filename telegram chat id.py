from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging

# 设置日志
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# 定义/start命令的处理函数
async def start(update: Update, context: CallbackContext) -> None:
    # 获取 chat_id
    chat_id = update.message.chat_id
    # 输出 chat_id 到日志
    logging.debug(f"Your chat_id is: {chat_id}")
    # 回复用户
    await update.message.reply_text(f"你的 chat_id 是：{chat_id}")

# 主函数
def main():
    # 创建 Application 对象并传入 Bot Token
    application = Application.builder().token("YOUR_BOT_TOKEN").build()

    # 注册 /start 命令处理器
    application.add_handler(CommandHandler("start", start))

    # 启动 Bot
    logging.info("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
