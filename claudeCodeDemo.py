#!/usr/bin/env python3
"""
Claude API Demo Script

This script demonstrates various features of the Anthropic Claude API
for AI-powered coding assistance.
"""

import asyncio
import os
import sys
from dotenv import load_dotenv

# Install required packages if missing
def install_requirements():
    """Install required packages if not available"""
    try:
        import anthropic
        print("✓ Anthropic SDK available")
    except ImportError:
        print("Installing Anthropic SDK...")
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'anthropic'])
        print("✓ Anthropic SDK installed")

def setup_api_key():
    """Setup API key from environment or .env file"""
    # Load from .env file
    # load_dotenv(dotenv_path='ib_invoice_ops/.env')
    load_dotenv(dotenv_path='.env')
    api_key = os.getenv('ANTHROPIC_API_KEY')
    
    if api_key:
        os.environ["ANTHROPIC_API_KEY"] = api_key
        print("✓ API key configured from .env file")
        return True
    else:
        print("❌ No API key found in .env file")
        print("Please set ANTHROPIC_API_KEY in ib_invoice_ops/.env")
        return False

async def demo_hello_world():
    """Demo 1: Simple Hello World"""
    print("\n=== Demo 1: Hello World ===")
    
    import anthropic
    
    try:
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
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    return True

async def demo_code_generation():
    """Demo 2: Code Generation"""
    print("\n=== Demo 2: Code Generation ===")
    
    import anthropic
    
    try:
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
    
    import anthropic
    
    try:
        client = anthropic.AsyncAnthropic()
        prompt = f"Review this Python code and suggest improvements:\n\n{sample_code}"
        response = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
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
    
    import anthropic
    
    try:
        client = anthropic.AsyncAnthropic()
        prompt = f"This code has a bug. Explain the issue and provide a fix:\n\n{error_code}"
        response = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        print("Debugging Help:")
        print(response.content[0].text)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

async def demo_multi_turn():
    """Demo 5: Multi-turn Conversation"""
    print("\n=== Demo 5: Multi-turn Conversation ===")
    
    import anthropic
    
    try:
        client = anthropic.AsyncAnthropic()
        
        # First turn
        response1 = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": "Help me design a simple calculator class. Start with the basic structure."
            }]
        )
        
        print("\nTurn 1:")
        turn1_content = response1.content[0].text
        print(turn1_content[:300] + "..." if len(turn1_content) > 300 else turn1_content)
        
        # Second turn
        response2 = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": "Help me design a simple calculator class. Start with the basic structure."},
                {"role": "assistant", "content": turn1_content},
                {"role": "user", "content": "Now add methods for basic arithmetic operations."}
            ]
        )
        
        print("\nTurn 2:")
        turn2_content = response2.content[0].text
        print(turn2_content[:300] + "..." if len(turn2_content) > 300 else turn2_content)
        
        print("\nCompleted 2 turns")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

async def demo_error_handling():
    """Demo 6: Error Handling Best Practices"""
    print("\n=== Demo 6: Error Handling ===")
    
    import anthropic
    
    try:
        client = anthropic.AsyncAnthropic()
        response = await client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": "Write a brief guide on Python error handling"
            }]
        )
        print("Success!")
        content = response.content[0].text
        print(content[:200] + "...")
        return True
    except Exception as e:
        print(f"✓ Error handled: {type(e).__name__}: {e}")
        return False

def check_claude_cli():
    """Check if Claude CLI is installed (optional for this demo)"""
    import subprocess
    try:
        result = subprocess.run(['claude', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Claude CLI is installed")
            return True
        else:
            print("ℹ️ Claude CLI not found (optional)")
            return True  # Not required for this demo
    except FileNotFoundError:
        print("ℹ️ Claude CLI not found (optional)")
        print("Install with: npm install -g @anthropic-ai/claude-code")
        return True  # Not required for this demo

async def run_all_demos():
    """Run all demos in sequence"""
    print("Claude API Demo Starting...")
    print("=" * 50)
    
    # Setup
    install_requirements()
    if not setup_api_key():
        return
    
    check_claude_cli()  # Optional check
    
    # Run demos with better error handling
    demos = [
        ("Hello World", demo_hello_world),
        ("Code Generation", demo_code_generation),
        ("Code Review", demo_code_review),
        ("Debugging Help", demo_debugging_help),
        ("Multi-turn", demo_multi_turn),
        ("Error Handling", demo_error_handling)
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