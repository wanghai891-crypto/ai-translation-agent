"""
测试翻译Agent
"""
import requests

BASE_URL = "http://localhost:8000"

def test_translation():
    """测试翻译功能"""
    print("🧪 测试翻译Agent...")
    
    # 测试1：英译中
    print("\n测试1: 英译中")
    response = requests.post(f"{BASE_URL}/translate", json={
        "text": "Hello! How are you doing today?",
        "target_language": "Chinese",
        "preserve_tone": True
    })
    print(f"原文: Hello! How are you doing today?")
    print(f"译文: {response.json()['translated_text']}")
    print(f"费用: ${response.json()['cost']}")
    
    # 测试2：中译英
    print("\n测试2: 中译英")
    response = requests.post(f"{BASE_URL}/translate", json={
        "text": "你好！今天天气真不错。",
        "target_language": "English",
        "preserve_tone": True
    })
    print(f"原文: 你好！今天天气真不错。")
    print(f"译文: {response.json()['translated_text']}")
    print(f"费用: ${response.json()['cost']}")
    
    print("\n✅ 测试完成！")

if __name__ == "__main__":
    test_translation()
