<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-checkbpm

_✨ 基于Librosa的音频文件BPM计算器 ✨_

[![LICENSE](https://img.shields.io/github/license/Ant1816/nonebot-plugin-checkbpm.svg)](https://github.com/Ant1816/nonebot-plugin-checkbpm/blob/master/LICENSE)
[![PYPI](https://img.shields.io/pypi/v/nonebot-plugin-checkbpm.svg)](https://pypi.python.org/pypi/nonebot-plugin-checkbpm)
[![Python3.9+](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org)
[![nonebot2](https://img.shields.io/badge/NoneBot2-2.3.1+-red)](https://github.com/nonebot/nonebot2)
[![onebotv11](https://img.shields.io/badge/OneBot-v11-yellow)](https://github.com/botuniverse/onebot-11)

</div>

## 📖 介绍

通过上传到群文件方式计算音频文件的bpm值（beat per minute）

<div align="center">

## 有问题或想法欢迎提issue以及pr！！！

</div>

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-checkbpm

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-checkbpm
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-checkbpm
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-checkbpm
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-checkbpm
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_checkbpm"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 |   默认值   |                            说明                             |
|:---:|:--:|:-------:|:---------------------------------------------------------:|
|  无  |  无  |  无  |  无  |

## 🎉 使用
### 指令表
|                        指令                        | 权限 | 需要@ | 范围 |        说明        |
|:------------------------------------------------:|:----:|:----:|:----:|:----------------:|
|                     bpm help                     | 群员 | 否 | 群聊 |      获取指令帮助      |
| bpmcheck/bpm计算/checkbpm/bpm检查 <文件名.mp3/flac/wav> | 群员 | 否 | 群聊 |      计算指定音频文件BPM值      |
