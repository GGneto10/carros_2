// Função para filtrar as motos
function filterMotos() {
  const marcaFilter = document.getElementById('marca-filter').value;
  const cilindradasFilter = document.getElementById('cilindradas-filter').value;
  const priceFilter = document.getElementById('price-filter').value;
  const motoCards = document.querySelectorAll('.moto-card');
  
  motoCards.forEach(card => {
    let show = true;
    const marca = card.getAttribute('data-marca');
    const cilindradas = parseInt(card.getAttribute('data-cilindradas'));
    const price = parseFloat(card.getAttribute('data-price'));
    
    // Filtro por marca
    if (marcaFilter && marca !== marcaFilter) {
      show = false;
    }
    
    // Filtro por cilindradas
    if (cilindradasFilter && cilindradas) {
      if (cilindradasFilter === '0-125' && cilindradas > 125) show = false;
      if (cilindradasFilter === '126-300' && (cilindradas <= 125 || cilindradas > 300)) show = false;
      if (cilindradasFilter === '301-600' && (cilindradas <= 300 || cilindradas > 600)) show = false;
      if (cilindradasFilter === '601+' && cilindradas <= 600) show = false;
    }
    
    // Filtro por preço
    if (priceFilter && price) {
      if (priceFilter === '0-10000' && price > 10000) show = false;
      if (priceFilter === '10000-20000' && (price <= 10000 || price > 20000)) show = false;
      if (priceFilter === '20000-30000' && (price <= 20000 || price > 30000)) show = false;
      if (priceFilter === '30000+' && price <= 30000) show = false;
    }
    
    // Mostra ou esconde o card conforme os filtros
    card.style.display = show ? 'block' : 'none';
  });
  
  // Verifica se há motos visíveis
  const visibleCards = document.querySelectorAll('.moto-card[style="display: block"]');
  const emptyState = document.querySelector('.empty-state');
  
  if (visibleCards.length === 0) {
    if (!emptyState) {
      const motosContainer = document.getElementById('motos-container');
      const emptyDiv = document.createElement('div');
      emptyDiv.className = 'empty-state';
      emptyDiv.innerHTML = '<p>Nenhuma moto encontrada com os filtros aplicados.</p>';
      motosContainer.appendChild(emptyDiv);
    }
  } else if (emptyState) {
    emptyState.remove();
  }
}

// Adiciona eventos aos filtros
document.addEventListener('DOMContentLoaded', function() {
  const marcaFilter = document.getElementById('marca-filter');
  const cilindradasFilter = document.getElementById('cilindradas-filter');
  const priceFilter = document.getElementById('price-filter');
  
  if (marcaFilter) marcaFilter.addEventListener('change', filterMotos);
  if (cilindradasFilter) cilindradasFilter.addEventListener('change', filterMotos);
  if (priceFilter) priceFilter.addEventListener('change', filterMotos);
  
  // Botão de favorito
  document.querySelectorAll('.btn-secondary').forEach(button => {
    button.addEventListener('click', function() {
      this.textContent = this.textContent === 'Favorito' ? 'Favoritado ✓' : 'Favorito';
    });
  });
  
  // Busca automática ao digitar
  const searchInput = document.querySelector('input[name="search"]');
  let searchTimeout;
  
  if (searchInput) {
    searchInput.addEventListener('input', function() {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        this.form.submit();
      }, 500);
    });
  }
  
  // Formatação de preços e quilometragem
  function formatPrice(price) {
    return 'R$ ' + parseFloat(price).toLocaleString('pt-BR', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    });
  }
  
  function formatKm(km) {
    return parseFloat(km).toLocaleString('pt-BR') + ' km';
  }
  
  // Aplicar formatação aos elementos
  document.querySelectorAll('.moto-price').forEach(function(element) {
    if (!element.hasAttribute('data-formatted')) {
      const price = element.textContent.replace('R$', '').trim();
      element.textContent = formatPrice(price);
      element.setAttribute('data-formatted', 'true');
    }
  });
  
  document.querySelectorAll('.moto-detail').forEach(function(element) {
    const text = element.textContent;
    if (text.includes('KM:') && !element.hasAttribute('data-formatted')) {
      const kmValue = element.querySelector('span:last-child').textContent;
      element.querySelector('span:last-child').textContent = formatKm(kmValue);
      element.setAttribute('data-formatted', 'true');
    }
  });
});