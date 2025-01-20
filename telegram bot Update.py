import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# 替换为你的 Bot API Token
TOKEN = '7485272939:AAElnZbnpRPKbMt0RP5gPWQSPd4f9_IO630'

# 设置日志配置
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# 定义/start命令的处理函数
def start(update: Update, context: CallbackContext) -> None:
    logging.debug(f"Received message: {update.message.text}")
    update.message.reply_text('你好！我是jienimiao。')

# 定义消息处理函数（回显消息）
def echo(update: Update, context: CallbackContext) -> None:
    logging.debug(f"Received message: {update.message.text}")
    update.message.reply_text(update.message.text)

def main():
    # 创建 Updater 对象并传入 Bot Token
    updater = Updater(TOKEN)

    # 获取调度器
    dispatcher = updater.dispatcher

    # 注册命令处理器
    dispatcher.add_handler(CommandHandler("start", start))

    # 注册消息处理器（回显消息）
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 启动 Bot
    logging.info("Bot is starting...")
    updater.start_polling()

    # 保持程序运行
    updater.idle()

if __name__ == '__main__':
    main()

