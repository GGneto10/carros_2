document.querySelectorAll('.btn-secondary').forEach(button => {
  button.addEventListener('click', function() {
    this.textContent = this.textContent === 'Favorito' ? 'Favoritado ✓' : 'Favorito';
  });
});

// Busca automática ao digitar
const searchInput = document.querySelector('input[name="search"]');
let searchTimeout;

searchInput.addEventListener('input', function() {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    this.form.submit();
  }, 500);
});

// Esta parte seria normalmente no custom_filters.py, mas adaptada para JS
document.addEventListener('DOMContentLoaded', function() {
  // Função para formatar preço (equivalente ao filter 'currency')
  function formatPrice(price) {
      return 'R$ ' + parseFloat(price).toLocaleString('pt-BR', {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2
      });
  }
  
  // Função para formatar quilometragem (equivalente ao filter 'km_format')
  function formatKm(km) {
      return parseFloat(km).toLocaleString('pt-BR') + ' km';
  }
  
  // Aplicar formatação aos elementos
  document.querySelectorAll('.car-price').forEach(function(element) {
      if (!element.hasAttribute('data-formatted')) {
          const price = element.textContent.replace('R$', '').trim();
          element.textContent = formatPrice(price);
          element.setAttribute('data-formatted', 'true');
      }
  });
  
  document.querySelectorAll('.car-details').forEach(function(element) {
      const text = element.textContent;
      if (text.includes('KM:') && !element.hasAttribute('data-formatted')) {
          const parts = text.split('|');
          if (parts.length > 1 && parts[1].includes('KM:')) {
              const kmPart = parts[1].split(':');
              if (kmPart.length > 1) {
                  const kmValue = kmPart[1].trim();
                  parts[1] = ' KM: ' + formatKm(kmValue);
                  element.textContent = parts.join(' | ');
                  element.setAttribute('data-formatted', 'true');
              }
          }
      }
  });
});