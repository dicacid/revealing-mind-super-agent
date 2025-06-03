import React from 'react';
import { useUI } from '../contexts/UIContext';
import BasicModeChat from './modes/BasicModeChat';
import IntermediateModeChat from './modes/IntermediateModeChat';
import AdvancedModeChat from './modes/AdvancedModeChat';

const ChatInterface = () => {
  const { currentMode, UI_MODES } = useUI();

  // Render the appropriate interface based on current mode
  switch (currentMode) {
    case UI_MODES.BASIC:
      return <BasicModeChat />;
    case UI_MODES.INTERMEDIATE:
      return <IntermediateModeChat />;
    case UI_MODES.ADVANCED:
      return <AdvancedModeChat />;
    default:
      return <BasicModeChat />;
  }
};

export default ChatInterface;

