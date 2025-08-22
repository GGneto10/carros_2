// Adicionar event listeners aos botões
document.querySelectorAll('.btn-primary').forEach(button => {
    button.addEventListener('click', function() {
      // Esta função não é mais necessária aqui pois o redirecionamento
      // agora é feito diretamente no onclick do botão
    });
  });

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