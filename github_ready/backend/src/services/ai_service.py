import os
import openai
from typing import List, Dict, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIService:
    """
    AI Service that supports multiple providers (OpenAI, Claude, etc.)
    """
    
    def __init__(self):
        self.openai_client = None
        self.setup_openai()
    
    def setup_openai(self):
        """Initialize OpenAI client if API key is available"""
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key:
            self.openai_client = openai.OpenAI(api_key=api_key)
            logger.info("OpenAI client initialized successfully")
        else:
            logger.warning("OPENAI_API_KEY not found in environment variables")
    
    async def generate_response(self, 
                              message: str, 
                              conversation_history: List[Dict] = None,
                              provider: str = "openai",
                              model: str = "gpt-3.5-turbo") -> str:
        """
        Generate AI response using specified provider
        
        Args:
            message: User's message
            conversation_history: Previous messages in conversation
            provider: AI provider to use ("openai", "claude", "fallback")
            model: Specific model to use
            
        Returns:
            AI-generated response string
        """
        
        # Try OpenAI first if available
        if provider == "openai" and self.openai_client:
            try:
                return await self._generate_openai_response(message, conversation_history, model)
            except Exception as e:
                logger.error(f"OpenAI API error: {e}")
                # Fall back to basic responses
                return self._generate_fallback_response(message)
        
        # If OpenAI not available or requested, use fallback
        return self._generate_fallback_response(message)
    
    async def _generate_openai_response(self, 
                                      message: str, 
                                      conversation_history: List[Dict] = None,
                                      model: str = "gpt-3.5-turbo") -> str:
        """Generate response using OpenAI API"""
        
        # Build conversation context
        messages = [
            {
                "role": "system", 
                "content": """You are a helpful AI assistant for Revealing Mind AI. You are part of a super agent system that helps users with various tasks.

Key traits:
- Be helpful, friendly, and professional
- Provide clear, concise responses
- If users ask about capabilities, mention you're part of a larger AI agent system
- Be encouraging and supportive
- Keep responses conversational but informative

Current mode: Basic Mode (simple interface for all users)"""
            }
        ]
        
        # Add conversation history if available
        if conversation_history:
            for msg in conversation_history[-10:]:  # Last 10 messages for context
                if msg['type'] == 'user':
                    messages.append({"role": "user", "content": msg['content']})
                elif msg['type'] == 'ai':
                    messages.append({"role": "assistant", "content": msg['content']})
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        # Call OpenAI API
        response = self.openai_client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=500,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        return response.choices[0].message.content.strip()
    
    def _generate_fallback_response(self, message: str) -> str:
        """Enhanced fallback responses when AI APIs aren't available"""
        
        message_lower = message.lower()
        
        # Intelligent keyword-based responses
        if any(word in message_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return "Hello! I'm your AI assistant from Revealing Mind AI. I'm here to help you with questions, tasks, and conversations. What would you like to work on today?"
        
        elif any(word in message_lower for word in ['help', 'what can you do', 'capabilities']):
            return "I'm part of the Revealing Mind AI super agent system! I can help you with:\n\n• Answering questions and providing information\n• Having conversations and brainstorming\n• Helping with writing and analysis\n• General problem-solving\n\nRight now you're using Basic Mode - our simple, clean interface. There are also Intermediate and Advanced modes coming soon with more specialized tools!\n\nWhat would you like to explore?"
        
        elif any(word in message_lower for word in ['thank', 'thanks', 'appreciate']):
            return "You're very welcome! I'm happy I could help. Feel free to ask me anything else - I'm here whenever you need assistance. Is there anything else you'd like to work on?"
        
        elif any(word in message_lower for word in ['bye', 'goodbye', 'see you', 'farewell']):
            return "Goodbye! It was great chatting with you. Come back anytime you need help or just want to have a conversation. Have a wonderful day! 👋"
        
        elif '?' in message:
            return f"That's a great question! You asked about: '{message}'\n\nI'd love to help you explore this topic. Could you tell me a bit more about what specific aspect you're most interested in? The more context you provide, the better I can assist you."
        
        elif len(message) > 100:
            return f"I can see you've shared quite a bit of detail with me - that's helpful! You mentioned several important points.\n\nTo give you the most useful response, could you help me understand what your main goal or question is? Are you looking for:\n• Analysis or feedback\n• Suggestions or recommendations\n• Help with a specific problem\n• Just a thoughtful discussion\n\nLet me know and I'll focus my response accordingly!"
        
        elif any(word in message_lower for word in ['openai', 'api', 'key', 'setup', 'configure']):
            return "I notice you're asking about API setup! To enable advanced AI capabilities, you'll need to:\n\n1. Get an OpenAI API key from platform.openai.com\n2. Add it as an environment variable: OPENAI_API_KEY\n3. Restart the system\n\nOnce configured, I'll be powered by GPT models for much more intelligent conversations! Would you like help with the setup process?"
        
        else:
            return f"I understand you're telling me about: '{message}'\n\nI'm currently running in basic mode, but I'm here to help! Could you let me know:\n• What you'd like me to help you with\n• Any specific questions you have\n• What kind of response would be most useful\n\nI'm designed to be helpful, so just let me know how I can assist you best!"

# Global AI service instance
ai_service = AIService()

