document.addEventListener('DOMContentLoaded', () => {
    const languageIcon = document.querySelector('.language-icon');
    const languageMenu = document.getElementById('languageMenu');
    const loadingOverlay = document.getElementById('loadingOverlay');
  
    let isMenuOpen = false;
  
    // Toggle language menu visibility on icon click
    languageIcon.addEventListener('click', () => {
        isMenuOpen = !isMenuOpen;
        if (isMenuOpen) {
            languageMenu.classList.add('show');
        } else {
            languageMenu.classList.remove('show');
        }
    });
  
    // Handle language change
    document.querySelectorAll('.language-menu li').forEach(item => {
        item.addEventListener('click', async () => {
            const languageCode = item.getAttribute('data-language');
            languageMenu.classList.remove('show'); // Hide menu
            loadingOverlay.style.display = 'flex'; // Show the overlay
            try {
                await changeLanguage(languageCode);
            } catch (error) {
                console.error('Fehler bei der Sprachänderung:', error);
            }
            loadingOverlay.style.display = 'none'; // Hide the overlay
        });
    });
});

async function changeLanguage(languageCode) {
    console.log('Ändere Sprache zu:', languageCode);

    const elementsToTranslate = document.querySelectorAll('[data-translate-key]');
    const translations = {};

    // Collect all text elements to translate
    for (const element of elementsToTranslate) {
        const key = element.getAttribute('data-translate-key');
        translations[key] = key; // Initial text is the key
    }

    try {
        console.log('Sende Anfrage an /translate');
        const response = await fetch('http://localhost:5000/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                texts: Object.keys(translations),
                target_language: languageCode
            })
        });

        console.log('Antwort von Server:', await response.json());

        if (!response.ok) {
            throw new Error('Netzwerkantwort war nicht ok.');
        }

        const data = await response.json();
        if (data.translations) {
            const translatedTexts = data.translations;
            // Update text content with translations
            for (const [index, translated] of translatedTexts.entries()) {
                const element = document.querySelector(`[data-translate-key="${Object.keys(translations)[index]}"]`);
                if (element) {
                    element.textContent = translated;
                }
            }
        }
    } catch (error) {
        console.error('Fehler bei der Übersetzung:', error);
    }
}