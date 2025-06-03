import React from 'react';
import { UIProvider } from './contexts/UIContext';
import ChatInterface from './components/ChatInterface';
import './App.css';

function App() {
  return (
    <UIProvider>
      <div className="min-h-screen bg-background">
        <ChatInterface />
      </div>
    </UIProvider>
  );
}

export default App;

