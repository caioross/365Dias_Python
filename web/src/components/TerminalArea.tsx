import { XCircle, Ban, TerminalSquare } from 'lucide-react';
import { useEffect, useRef } from 'react';

interface TerminalAreaProps {
    output: string[];
    onClear: () => void;
    isExpanded: boolean;
    toggleExpanded: () => void;
    onClose: () => void;
}

export function TerminalArea({ output, onClear, isExpanded, toggleExpanded, onClose }: TerminalAreaProps) {
    const scrollRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (scrollRef.current) {
            scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
        }
    }, [output]);

    return (
        <div className={`flex flex-col shrink-0 bg-vscode-terminal border-t border-vscode-border transition-all duration-300 ease-in-out select-text ${isExpanded ? 'h-1/2' : 'h-48'}`}>

            {/* Terminal Header */}
            <div className="flex items-center justify-between px-3 h-9 bg-vscode-bg border-b border-vscode-border select-none">

                <div className="flex gap-4 h-full pt-2">
                    <div className="uppercase text-[11px] font-semibold text-vscode-textActive border-b border-vscode-primary">Terminal</div>
                    <div className="uppercase text-[11px] font-semibold text-vscode-text opacity-50 cursor-pointer hover:opacity-100 transition-opacity">Output</div>
                </div>

                <div className="flex gap-3 text-vscode-text opacity-80">
                    <button onClick={onClear} className="hover:text-vscode-textActive transition-colors" title="Limpar Terminal">
                        <Ban size={14} />
                    </button>
                    <button onClick={toggleExpanded} className="hover:text-vscode-textActive transition-colors" title={isExpanded ? "Reduzir Terminal" : "Expandir Terminal"}>
                        <TerminalSquare size={14} />
                    </button>
                    <button onClick={onClose} className="hover:text-vscode-textActive transition-colors hover:text-red-400" title="Fechar Terminal">
                        <XCircle size={14} />
                    </button>
                </div>
            </div>

            {/* Output Console */}
            <div
                ref={scrollRef}
                className="flex-1 overflow-y-auto p-3 text-sm terminal-output"
            >
                {output.length === 0 ? (
                    <div className="opacity-40 italic">O output do seu código aparecerá aqui...</div>
                ) : (
                    output.map((line, idx) => (
                        <div key={idx} className="mb-0.5" style={{
                            // Check if it's an error stack trace simply
                            color: line.includes('Traceback (most recent call last)') || line.includes('Error:') ? '#f48771' : 'inherit'
                        }}>
                            {line}
                        </div>
                    ))
                )}
            </div>

        </div>
    );
}
