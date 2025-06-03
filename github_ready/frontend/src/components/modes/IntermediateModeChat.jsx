import React from 'react';
import { Button } from '@/components/ui/button';
import { useUI } from '../../contexts/UIContext';

const IntermediateModeChat = () => {
  const { switchMode, UI_MODES } = useUI();

  return (
    <div className="flex items-center justify-center h-screen bg-background">
      <div className="text-center space-y-4">
        <h2 className="text-2xl font-bold">Intermediate Mode</h2>
        <p className="text-muted-foreground">Coming soon in the next phase!</p>
        <Button onClick={() => switchMode(UI_MODES.BASIC)}>
          Back to Basic Mode
        </Button>
      </div>
    </div>
  );
};

export default IntermediateModeChat;

