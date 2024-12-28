import librosa
import nonebot
import numpy as np

from nonebot import on_command
from nonebot.params import ArgPlainText
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata, inherit_supported_adapters
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Event, MessageEvent, PrivateMessageEvent, MessageSegment


__plugin_meta__ = PluginMetadata(
    name="音频文件BPM计算器",
    description="通过上传到群文件方式计算音频文件的bpm值（beat per minute）",
    usage="发送 bpm help 查看帮助",
    config=None,
    type="application",
    supported_adapters={"~onebot.v11"},
    homepage="https://github.com/Ant1816/nonebot-plugin-checkbpm",
    extra={
            "author": "Ant1",
            "version": "1.0.1",
            "priority": 10,
    },
)

help_ = nonebot.on_command("bpm help", priority=10, block=True)

bpmcheck = nonebot.on_command("bpmcheck", aliases={"bpm计算", "checkbpm", "bpm检查"}, priority=10, block=True)


async def process_audio(local_path):
    y, sr = librosa.load(local_path)
    await bpmcheck.send("已载入文件，分析文件中...")
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=512, aggregate=np.median)
    tempo_, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
    return tempo_


@help_.handle()
async def handle_help_message(bot: Bot, event: GroupMessageEvent):
    message = (
        "音频文件BPM计算器帮助\n"
        "请先发送文件后使用命令\n"
        "bpmcheck/bpm计算 <文件名.mp3/flac/wav>  计算指定音频文件BPM值"
    )
    await help_.send(message)


@bpmcheck.handle()
async def handle_bpmcheck_message(bot: Bot, event: MessageEvent, arg: Message = CommandArg()):
    if isinstance(event, GroupMessageEvent):
        group_id = str(event.group_id)
        root = await bot.get_group_root_files(group_id=int(group_id))
        file_name = arg.extract_plain_text().strip()

        if not file_name:
            await bpmcheck.finish("语法错误，请指定文件名（如：bpmcheck example.mp3）")

        await bpmcheck.send("寻找发送文件中...")
        files = root.get('files')

        for file in files:
            if file.get('file_name') == file_name:
                url_dict = await bot.get_group_file_url(group_id=int(group_id), file_id=str(file.get('file_id')), busid=int(file.get('busid')))
                url = str(url_dict.get('url')).replace('%20', '+')[8:]  # 切片去除file://
                await bpmcheck.send("已找到文件，载入文件中...")
                tempo = await process_audio(url)
                await bpmcheck.finish(f"{file_name}的bpm值为：{int(tempo[0])}({tempo[0]})")

        await bpmcheck.finish(f"未找到文件{file_name},请确认您已发送文件后再使用此指令")
    else:
        await bpmcheck.finish("暂时仅支持群聊中的文件操作。")
