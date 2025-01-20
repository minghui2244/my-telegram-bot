import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
from flask import Flask, request
import os
import asyncio

# 你的 Telegram Bot Token
TOKEN = '7485272939:AAElnZbnpRPKbMt0RP5gPWQSPd4f9_IO630'  # 替换为你自己的 Bot Token

# 设置 Webhook URL
WEBHOOK_URL = 'https://your-heroku-app.herokuapp.com/YOUR_ENDPOINT'  # 替换为你自己的 HTTPS URL

# 配置日志
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建 Flask 应用
app = Flask(__name__)

# Webhook 接口
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = request.get_json()  # 获取 POST 请求中的 JSON 数据
    dispatcher.process_update(update)  # 处理该更新
    return '', 200

# 设置 Webhook
async def set_webhook():
    application = Application.builder().token(TOKEN).build()
    webhook_url = WEBHOOK_URL  # 设置为你的 Webhook URL

    try:
        await application.bot.set_webhook(webhook_url)
        logger.info(f'Webhook set to: {webhook_url}')
    except Exception as e:
        logger.error(f"Error while setting webhook: {e}")

# /start 命令处理函数
async def start(update: Update, context: CallbackContext):
    user_first_name = update.message.from_user.first_name
    welcome_text = f"你好，{user_first_name}！欢迎使用我的 Bot。"
    await update.message.reply_text(welcome_text)

# 处理所有文本消息
async def handle_all_messages(update: Update, context: CallbackContext):
    # 这里只是简单回显收到的消息
    await update.message.reply_text(f"你说了: {update.message.text}")

# 主函数，启动 Bot 和 Webhook 设置
async def main():
    # 设置 Webhook
    await set_webhook()

    # 创建 Application 实例
    application = Application.builder().token(TOKEN).build()

    # 注册 /start 命令处理器
    application.add_handler(CommandHandler("start", start))

    # 注册处理所有文本消息的处理器
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_all_messages))

    # 启动 Bot，开始监听更新
    await application.run_polling()

# 启动 Flask 服务和 asyncio 事件循环
if __name__ == '__main__'


















