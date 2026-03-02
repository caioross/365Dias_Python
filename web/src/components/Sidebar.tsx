import { useState, useMemo } from 'react';
import type { PythonCode } from '../types';
import { Search, Folder, Calendar as CalendarIcon, FileCode2, ChevronRight, ChevronDown } from 'lucide-react';
import { format } from 'date-fns';

interface SidebarProps {
    codes: PythonCode[];
    onSelect: (code: PythonCode) => void;
    selectedCode: PythonCode | null;
}

export function Sidebar({ codes, onSelect, selectedCode }: SidebarProps) {
    const [activeTab, setActiveTab] = useState<'explorer' | 'search' | 'calendar'>('explorer');
    const [searchQuery, setSearchQuery] = useState('');
    const [searchFilter, setSearchFilter] = useState<'all' | 'title' | 'library'>('all');

    // Calendar state
    const [currentMonthDate, setCurrentMonthDate] = useState(new Date(2026, 0, 1));

    // Collapse state for explorer
    const [expandedMonths, setExpandedMonths] = useState<Record<string, boolean>>({
        'Janeiro': true
    });

    const toggleMonth = (month: string) => {
        setExpandedMonths(prev => ({ ...prev, [month]: !prev[month] }));
    }

    const groupedByMonth = useMemo(() => {
        const groups: Record<string, PythonCode[]> = {};
        codes.forEach(c => {
            if (!groups[c.month]) groups[c.month] = [];
            groups[c.month].push(c);
        });
        return groups;
    }, [codes]);

    const searchResults = useMemo(() => {
        if (!searchQuery.trim()) return [];
        const lower = searchQuery.toLowerCase();
        return codes.filter(c => {
            const matchTitle = c.filename.toLowerCase().includes(lower) || c.description.toLowerCase().includes(lower);
            const matchLib = c.importedLibs.some(lib => lib.toLowerCase().includes(lower));

            if (searchFilter === 'title') return matchTitle;
            if (searchFilter === 'library') return matchLib;
            return matchTitle || matchLib;
        });
    }, [codes, searchQuery, searchFilter]);

    // --- Calendar Logic ---
    const getDaysInMonth = (year: number, month: number) => new Date(year, month + 1, 0).getDate();
    const getFirstDayOfMonth = (year: number, month: number) => new Date(year, month, 1).getDay();

    const currentYear = currentMonthDate.getFullYear();
    const currentMonthIndex = currentMonthDate.getMonth();
    const daysInMonth = getDaysInMonth(currentYear, currentMonthIndex);
    const firstDay = getFirstDayOfMonth(currentYear, currentMonthIndex);

    const prevMonth = () => setCurrentMonthDate(new Date(currentYear, currentMonthIndex - 1, 1));
    const nextMonth = () => setCurrentMonthDate(new Date(currentYear, currentMonthIndex + 1, 1));

    const calendarCodeMap = useMemo(() => {
        const map: Record<string, PythonCode> = {};
        codes.forEach(c => {
            if (c.date) map[c.date.substring(0, 10)] = c; // match YYYY-MM-DD
        });
        return map;
    }, [codes]);

    return (
        <div className="w-64 h-full bg-vscode-sidebar border-r border-vscode-border flex flex-col select-none">
            {/* Activity Bar (Icons) + Title */}
            <div className="flex border-b border-vscode-border">
                <button
                    onClick={() => setActiveTab('explorer')}
                    className={`px-3 py-2 flex-1 flex justify-center border-b-2 font-semibold text-[10px] uppercase tracking-wider ${activeTab === 'explorer' ? 'border-vscode-primary text-vscode-textActive bg-vscode-sidebarHover' : 'border-transparent text-vscode-text opacity-70 hover:opacity-100'}`}
                >
                    <Folder size={16} />
                </button>
                <button
                    onClick={() => setActiveTab('search')}
                    className={`px-3 py-2 flex-1 flex justify-center border-b-2 font-semibold text-[10px] uppercase tracking-wider ${activeTab === 'search' ? 'border-vscode-primary text-vscode-textActive bg-vscode-sidebarHover' : 'border-transparent text-vscode-text opacity-70 hover:opacity-100'}`}
                >
                    <Search size={16} />
                </button>
                <button
                    onClick={() => setActiveTab('calendar')}
                    className={`px-3 py-2 flex-1 flex justify-center border-b-2 font-semibold text-[10px] uppercase tracking-wider ${activeTab === 'calendar' ? 'border-vscode-primary text-vscode-textActive bg-vscode-sidebarHover' : 'border-transparent text-vscode-text opacity-70 hover:opacity-100'}`}
                >
                    <CalendarIcon size={16} />
                </button>
            </div>

            <div className="p-2 text-xs font-bold uppercase tracking-wider opacity-80 border-b border-vscode-border text-vscode-text flex justify-between items-center">
                <span>
                    {activeTab === 'explorer' && 'Explorador: 2026'}
                    {activeTab === 'search' && 'Buscar Código'}
                    {activeTab === 'calendar' && 'Calendário'}
                </span>
                {activeTab === 'search' && (
                    <div className="flex gap-1">
                        <button title="Tudo" onClick={() => setSearchFilter('all')} className={`px-1 rounded ${searchFilter === 'all' ? 'bg-vscode-primary text-white' : 'hover:bg-vscode-sidebarHover'}`}>T</button>
                        <button title="Por Título/Descrição" onClick={() => setSearchFilter('title')} className={`px-1 rounded ${searchFilter === 'title' ? 'bg-vscode-primary text-white' : 'hover:bg-vscode-sidebarHover'}`}>N</button>
                        <button title="Por Biblioteca" onClick={() => setSearchFilter('library')} className={`px-1 rounded ${searchFilter === 'library' ? 'bg-vscode-primary text-white' : 'hover:bg-vscode-sidebarHover'}`}>B</button>
                    </div>
                )}
            </div>

            {/* Content Area */}
            <div className="flex-1 overflow-y-auto overflow-x-hidden text-sm">

                {activeTab === 'explorer' && (
                    <div className="py-2">
                        {Object.keys(groupedByMonth).sort().map(month => {
                            const isExpanded = !!expandedMonths[month];
                            return (
                                <div key={month}>
                                    <div
                                        className="flex items-center px-1 py-1 cursor-pointer hover:bg-vscode-sidebarHover text-vscode-text transition-colors"
                                        onClick={() => toggleMonth(month)}
                                    >
                                        {isExpanded ? <ChevronDown size={14} className="mr-1" /> : <ChevronRight size={14} className="mr-1" />}
                                        <Folder size={14} className="mr-2 text-vscode-folder" />
                                        <span className="font-medium text-xs truncate">{month}</span>
                                    </div>

                                    {isExpanded && (
                                        <div className="pl-6 ml-2 border-l border-vscode-border">
                                            {groupedByMonth[month].map(code => {
                                                const isSelected = selectedCode?.filename === code.filename;
                                                return (
                                                    <div
                                                        key={code.filename}
                                                        onClick={() => onSelect(code)}
                                                        className={`flex items-center px-1 py-1 cursor-pointer transition-colors ${isSelected ? 'bg-vscode-primary text-vscode-textActive' : 'hover:bg-vscode-sidebarHover text-vscode-text opacity-80 hover:opacity-100'}`}
                                                        title={code.description}
                                                    >
                                                        <FileCode2 size={13} className="mr-2 text-vscode-python min-w-[13px]" />
                                                        <span className="text-[11px] truncate">{code.filename}</span>
                                                    </div>
                                                );
                                            })}
                                        </div>
                                    )}
                                </div>
                            );
                        })}
                    </div>
                )}

                {activeTab === 'search' && (
                    <div className="p-3">
                        <input
                            type="text"
                            placeholder="Buscar bibliotecas, temas, etc..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            className="w-full bg-vscode-bg border border-vscode-border text-vscode-textActive p-1.5 text-xs rounded-sm focus:outline-none focus:border-vscode-primary"
                        />

                        <div className="mt-4 break-words">
                            {searchQuery && searchResults.length === 0 && (
                                <div className="text-xs opacity-60 italic p-2 text-vscode-text">Nenhum resultado encontrado.</div>
                            )}
                            {searchResults.map(code => (
                                <div
                                    key={code.filename}
                                    onClick={() => onSelect(code)}
                                    className={`p-2 mb-2 cursor-pointer border border-transparent rounded-sm transition-colors ${selectedCode?.filename === code.filename ? 'bg-vscode-sidebarHover border-vscode-border' : 'hover:bg-vscode-sidebarHover'}`}
                                >
                                    <div className="flex items-center gap-1.5 font-bold text-vscode-primary text-xs truncate">
                                        <FileCode2 size={13} />
                                        {code.filename}
                                    </div>
                                    <div className="text-[10px] text-vscode-text mt-1 opacity-80 line-clamp-2">
                                        {code.description}
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                )}

                {activeTab === 'calendar' && (
                    <div className="p-3 text-vscode-text select-none">
                        <div className="flex items-center justify-between mb-4">
                            <button onClick={prevMonth} className="p-1 hover:bg-vscode-sidebarHover rounded" title="Mês Anterior">&lt;</button>
                            <span className="font-bold text-sm">{format(currentMonthDate, 'MMMM yyyy')}</span>
                            <button onClick={nextMonth} className="p-1 hover:bg-vscode-sidebarHover rounded" title="Próximo Mês">&gt;</button>
                        </div>

                        <div className="grid grid-cols-7 gap-1 text-center font-bold text-[10px] mb-2 opacity-50">
                            <div>Dom</div><div>Seg</div><div>Ter</div><div>Qua</div><div>Qui</div><div>Sex</div><div>Sáb</div>
                        </div>

                        <div className="grid grid-cols-7 gap-1 text-center text-xs">
                            {Array.from({ length: firstDay }).map((_, i) => <div key={`empty-${i}`} className="p-1"></div>)}
                            {Array.from({ length: daysInMonth }).map((_, i) => {
                                const day = i + 1;
                                const dateStr = `${currentYear}-${String(currentMonthIndex + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
                                const codeForDay = calendarCodeMap[dateStr];
                                const isSelected = selectedCode?.date?.includes(dateStr);

                                return (
                                    <div
                                        key={day}
                                        className={`p-1 flex items-center justify-center h-8 rounded-sm ${codeForDay ? 'cursor-pointer hover:border-vscode-primary border border-transparent bg-vscode-sidebarHover font-bold text-vscode-primary' : 'opacity-20'} ${isSelected ? 'bg-vscode-primary text-white border-white font-bold' : ''}`}
                                        title={codeForDay ? codeForDay.description : "Nenhum código neste dia"}
                                        onClick={() => codeForDay && onSelect(codeForDay)}
                                    >
                                        {day}
                                    </div>
                                );
                            })}
                        </div>
                        <div className="mt-4 text-[10px] opacity-60 text-center italic">
                            Dias coloridos contêm scripts em Python. Clique neles para carregar.
                        </div>
                    </div>
                )}

            </div>
        </div>
    );
}
