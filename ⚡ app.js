function scrollToId(id) {
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function copyBlock(btn) {
  const pre = btn.closest('.card').querySelector('pre');
  if (!pre) return;
  const text = pre.innerText;
  navigator.clipboard.writeText(text).then(() => {
    const prev = btn.textContent;
    btn.textContent = 'Copié !';
    setTimeout(() => (btn.textContent = prev), 1200);
  });
}

// Démo: appel vers backend pywebview si disponible
async function tryPywebview() {
  if (window.pywebview?.api?.get_products) {
    try {
      const res = await window.pywebview.api.get_products();
      console.log('Produits (pywebview):', res);
    } catch (e) {
      console.warn('pywebview API non disponible:', e);
    }
  }
}

document.addEventListener('DOMContentLoaded', tryPywebview);
