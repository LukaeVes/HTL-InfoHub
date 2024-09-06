const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electron', {
  toggleLanguageMenu: () => ipcRenderer.invoke('toggle-language-menu'),
  changeLanguage: (language) => ipcRenderer.invoke('change-language', language)
});