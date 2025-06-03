from flask import Blueprint, request, jsonify
import time
import uuid
import asyncio
from datetime import datetime
from src.services.ai_service import ai_service

chat_bp = Blueprint('chat', __name__)

# Simple in-memory storage for demo (will be replaced with proper database later)
conversations = {}

@chat_bp.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages from the frontend."""
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        user_message = data['message'].strip()
        conversation_id = data.get('conversation_id', str(uuid.uuid4()))
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Initialize conversation if it doesn't exist
        if conversation_id not in conversations:
            conversations[conversation_id] = []
        
        # Add user message to conversation
        user_msg = {
            'id': str(uuid.uuid4()),
            'type': 'user',
            'content': user_message,
            'timestamp': datetime.now().isoformat()
        }
        conversations[conversation_id].append(user_msg)
        
        # Generate AI response using the AI service
        ai_response = asyncio.run(generate_ai_response(user_message, conversations[conversation_id]))
        
        # Add AI response to conversation
        ai_msg = {
            'id': str(uuid.uuid4()),
            'type': 'ai',
            'content': ai_response,
            'timestamp': datetime.now().isoformat()
        }
        conversations[conversation_id].append(ai_msg)
        
        return jsonify({
            'success': True,
            'conversation_id': conversation_id,
            'response': ai_msg,
            'user_message': user_msg
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chat_bp.route('/conversation/<conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    """Get conversation history."""
    try:
        if conversation_id not in conversations:
            return jsonify({'error': 'Conversation not found'}), 404
        
        return jsonify({
            'success': True,
            'conversation_id': conversation_id,
            'messages': conversations[conversation_id]
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

async def generate_ai_response(user_message, conversation_history):
    """Generate AI response using the AI service."""
    try:
        response = await ai_service.generate_response(
            message=user_message,
            conversation_history=conversation_history,
            provider="openai",  # Will fallback automatically if not available
            model="gpt-3.5-turbo"
        )
        return response
    except Exception as e:
        # Fallback to basic response if AI service fails
        return f"I apologize, but I'm having trouble processing your request right now. You said: '{user_message}' - could you try rephrasing that or ask me something else?"

@chat_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

