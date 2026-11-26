# streamlit-keepalive

Mantiene despiertas las apps de Streamlit Community Cloud:
- https://formulariorma.streamlit.app/
- https://rma-altavista.streamlit.app/

Un GitHub Action corre cada 2 horas, abre cada app con un navegador headless
(Playwright) y, si está dormida, aprieta "Yes, get this app back up!".

Para agregar más apps, editá la lista `URLS` en `wake.py`.

## Índice de búsqueda de la tienda

`search-index.yml` llama cada 12 horas a la URL de cron que reconstruye el
índice de búsqueda de www.altavistasa.com.ar. La URL lleva el token, así que
está guardada como secret `PRESTASHOP_SEARCH_CRON_URL` (Settings → Secrets and
variables → Actions), no en el código.
