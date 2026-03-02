export interface PythonCode {
    filename: string;
    date: string | null; // YYYY-MM-DD
    day: string;
    month: string;
    year: string;
    description: string;
    codeUrl: string;
    readmeContent: string;
    importedLibs: string[];
}

export type Theme = 'dark' | 'light';
