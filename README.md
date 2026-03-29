# AI Translation Agent

智能翻译服务 - 保留语气和文化特色的高质量翻译

## 特色功能

✅ 自动识别源语言
✅ 保留原文语气和风格
✅ 支持20+语言
✅ 文化特色保留
✅ 专业术语优化

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env` 并填写你的API密钥：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的Claude API Key。

### 3. 启动服务

```bash
python main.py
```

服务将在 http://localhost:8000 启动

## API使用

### 翻译接口

**POST** `/translate`

请求示例：
```json
{
  "text": "Hello, how are you?",
  "target_language": "Chinese",
  "source_language": "auto",
  "preserve_tone": true
}
```

响应示例：
```json
{
  "translated_text": "你好，你好吗？",
  "source_language": "auto",
  "target_language": "Chinese",
  "character_count": 18,
  "cost": 0.0018
}
```

## 定价

- $0.01 / 100字符

## 技术栈

- FastAPI
- Claude 3.5 Sonnet
- Python 3.8+
