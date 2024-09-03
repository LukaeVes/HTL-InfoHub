const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    backgroundColor: '#ffffff', // Weißer Hintergrund
    webPreferences: {
      nodeIntegration: true,
    }
  });

  // Lade die HTML-Datei
  win.loadFile('index.html');
}

app.whenReady().then(() => {
  createWindonw();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});