# streamlit-keepalive

Mantiene despiertas las apps de Streamlit Community Cloud:
- https://formulariorma.streamlit.app/
- https://rma-altavista.streamlit.app/

Un GitHub Action corre cada 2 horas, abre cada app con un navegador headless
(Playwright) y, si está dormida, aprieta "Yes, get this app back up!".

Para agregar más apps, editá la lista `URLS` en `wake.py`.
