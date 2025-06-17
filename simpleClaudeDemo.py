#!/usr/bin/env python3
"""
Simple Claude API Demo Script

This script demonstrates basic usage of the Anthropic SDK
for AI-powered coding assistance.
"""

import asyncio
import os
from dotenv import load_dotenv

def setup_api_key():
    """Setup API key from environment or .env file"""
    load_dotenv(dotenv_path='.env')
    api_key = os.getenv('ANTHROPIC_API_KEY')
    
    if api_key:
        os.environ["ANTHROPIC_API_KEY"] = api_key
        print("✓ API key configured from .env file")
        return True
    else:
        print("❌ No API key found in .env file")
        print("Please set ANTHROPIC_API_KEY in .env")
        return False

async def demo_hello_world():
    """Demo 1: Simple Hello World"""
    print("\n=== Demo 1: Hello World ===")
    
    try:
        import anthropic
        client = anthropic.AsyncAnthropic()
        
        response = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{
                "role": "user", 
                "content": "Say hello and briefly introduce yourself as Claude"
            }]
        )
        
        print(f"Claude: {response.content[0].text}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

async def demo_code_generation():
    """Demo 2: Code Generation"""
    print("\n=== Demo 2: Code Generation ===")
    
    try:
        import anthropic
        client = anthropic.AsyncAnthropic()
        
        response = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": "Write a Python function to reverse a string with error handling"
            }]
        )
        
        print("Generated Code:")
        print(response.content[0].text)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

async def demo_code_review():
    """Demo 3: Code Review"""
    print("\n=== Demo 3: Code Review ===")
    
    sample_code = '''
def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i] > 0:
            result.append(data[i] * 2)
    return result
'''
    
    try:
        import anthropic
        client = anthropic.AsyncAnthropic()
        
        response = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": f"Review this Python code and suggest improvements:\n\n{sample_code}"
            }]
        )
        
        print("Code Review:")
        print(response.content[0].text)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

async def demo_debugging_help():
    """Demo 4: Debugging Help"""
    print("\n=== Demo 4: Debugging Help ===")
    
    error_code = '''
def divide_numbers(a, b):
    return a / b

# This causes an error
result = divide_numbers(10, 0)
print(result)
'''
    
    try:
        import anthropic
        client = anthropic.AsyncAnthropic()
        
        response = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": f"This code has a bug. Explain the issue and provide a fix:\n\n{error_code}"
            }]
        )
        
        print("Debugging Help:")
        print(response.content[0].text)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

async def run_all_demos():
    """Run all demos in sequence"""
    print("Simple Claude API Demo Starting...")
    print("=" * 50)
    
    # Setup
    if not setup_api_key():
        return
    
    # Install anthropic if needed
    try:
        import anthropic
        print("✓ Anthropic SDK available")
    except ImportError:
        print("Installing Anthropic SDK...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'anthropic'])
        print("✓ Anthropic SDK installed")
    
    # Run demos
    demos = [
        ("Hello World", demo_hello_world),
        ("Code Generation", demo_code_generation),
        ("Code Review", demo_code_review),
        ("Debugging Help", demo_debugging_help)
    ]
    
    successful = 0
    for name, demo_func in demos:
        try:
            result = await demo_func()
            if result:
                successful += 1
        except Exception as e:
            print(f"❌ {name} demo failed: {e}")
    
    print("\n" + "=" * 50)
    print(f"Completed {successful}/{len(demos)} demos successfully!")

def main():
    """Main entry point"""
    try:
        asyncio.run(run_all_demos())
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user")
    except Exception as e:
        print(f"\nDemo failed: {e}")

if __name__ == "__main__":
    main()