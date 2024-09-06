const { app, BrowserWindow } = require('electron');
const path = require('path');

// Enable auto-reload for Electron during development
require('electron-reload')(path.join(__dirname, '/'));

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      preload: path.join(__dirname, 'preload.js') // Falls du preload.js hast
    },
    fullscreen: true // Fullscreen setzen
  });

  win.loadFile('index.html');
}

app.whenReady().then(() => {
  createWindow();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});