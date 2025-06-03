import React from 'react';
import { useUI } from '../contexts/UIContext';
import { Button } from '@/components/ui/button';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import { ChevronDown, MessageCircle, Wrench, Zap } from 'lucide-react';

const ModeSwitcher = () => {
  const { currentMode, switchMode, getModeInfo, UI_MODES } = useUI();
  const currentModeInfo = getModeInfo(currentMode);

  const modeIcons = {
    [UI_MODES.BASIC]: MessageCircle,
    [UI_MODES.INTERMEDIATE]: Wrench,
    [UI_MODES.ADVANCED]: Zap
  };

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" className="flex items-center gap-2">
          {React.createElement(modeIcons[currentMode], { size: 16 })}
          <span className="hidden sm:inline">{currentModeInfo.name}</span>
          <ChevronDown size={14} />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-64">
        {Object.values(UI_MODES).map((mode) => {
          const modeInfo = getModeInfo(mode);
          const IconComponent = modeIcons[mode];
          const isActive = mode === currentMode;
          
          return (
            <DropdownMenuItem
              key={mode}
              onClick={() => switchMode(mode)}
              className={`flex items-start gap-3 p-3 cursor-pointer ${
                isActive ? 'bg-accent' : ''
              }`}
            >
              <IconComponent size={16} className="mt-0.5 flex-shrink-0" />
              <div className="flex-1">
                <div className="font-medium">{modeInfo.name}</div>
                <div className="text-sm text-muted-foreground">
                  {modeInfo.description}
                </div>
              </div>
              {isActive && (
                <div className="w-2 h-2 bg-primary rounded-full flex-shrink-0 mt-1.5" />
              )}
            </DropdownMenuItem>
          );
        })}
      </DropdownMenuContent>
    </DropdownMenu>
  );
};

export default ModeSwitcher;

