import React, { createContext, useContext, useState, useEffect } from 'react';

// UI Mode types
export const UI_MODES = {
  BASIC: 'basic',
  INTERMEDIATE: 'intermediate', 
  ADVANCED: 'advanced'
};

// Feature flags for each mode
const FEATURE_FLAGS = {
  [UI_MODES.BASIC]: {
    showSidebar: false,
    showToolsPanel: false,
    showAgentSelector: false,
    showAdvancedSettings: false,
    showMemoryView: false,
    showWorkflowBuilder: false,
    showDebugPanel: false,
    maxChatHistory: 50
  },
  [UI_MODES.INTERMEDIATE]: {
    showSidebar: true,
    showToolsPanel: true,
    showAgentSelector: true,
    showAdvancedSettings: false,
    showMemoryView: false,
    showWorkflowBuilder: false,
    showDebugPanel: false,
    maxChatHistory: 100
  },
  [UI_MODES.ADVANCED]: {
    showSidebar: true,
    showToolsPanel: true,
    showAgentSelector: true,
    showAdvancedSettings: true,
    showMemoryView: true,
    showWorkflowBuilder: true,
    showDebugPanel: true,
    maxChatHistory: 500
  }
};

// Create context
const UIContext = createContext();

// Custom hook to use the context
export const useUI = () => {
  const context = useContext(UIContext);
  if (!context) {
    throw new Error('useUI must be used within a UIProvider');
  }
  return context;
};

// Provider component
export const UIProvider = ({ children }) => {
  const [currentMode, setCurrentMode] = useState(() => {
    // Load from localStorage or default to basic
    const saved = localStorage.getItem('ui_mode');
    return saved && Object.values(UI_MODES).includes(saved) ? saved : UI_MODES.BASIC;
  });

  // Get current feature flags
  const featureFlags = FEATURE_FLAGS[currentMode];

  // Update localStorage when mode changes
  useEffect(() => {
    localStorage.setItem('ui_mode', currentMode);
  }, [currentMode]);

  // Switch UI mode
  const switchMode = (newMode) => {
    if (Object.values(UI_MODES).includes(newMode)) {
      setCurrentMode(newMode);
    }
  };

  // Get mode display info
  const getModeInfo = (mode) => {
    const modeInfo = {
      [UI_MODES.BASIC]: {
        name: 'Simple Chat',
        description: 'Clean, simple interface for quick conversations',
        icon: '💬'
      },
      [UI_MODES.INTERMEDIATE]: {
        name: 'Business Tools',
        description: 'Enhanced features for small businesses',
        icon: '🔧'
      },
      [UI_MODES.ADVANCED]: {
        name: 'Power User',
        description: 'Full feature set for developers and experts',
        icon: '⚡'
      }
    };
    return modeInfo[mode] || modeInfo[UI_MODES.BASIC];
  };

  const value = {
    currentMode,
    featureFlags,
    switchMode,
    getModeInfo,
    UI_MODES
  };

  return (
    <UIContext.Provider value={value}>
      {children}
    </UIContext.Provider>
  );
};

export default UIProvider;

