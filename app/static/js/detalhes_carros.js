// Adicionar event listeners aos botões
document.querySelectorAll('.btn-primary').forEach(button => {
    button.addEventListener('click', function() {
        if (this.textContent.includes('Contato')) {
            alert('Funcionalidade de contato em desenvolvimento');
        } else if (this.textContent.includes('Test Drive')) {
            alert('Funcionalidade de test drive em desenvolvimento');
        }
    });
});

document.getElementById('favorite-btn').addEventListener('click', function() {
    const isFavorited = this.textContent.includes('Favoritado');
    this.innerHTML = isFavorited ? '<i class="fas fa-heart"></i> Adicionar aos Favoritos' : '<i class="fas fa-check"></i> Favoritado ✓';
    
    if (!isFavorited) {
        this.style.background = 'linear-gradient(145deg, #4CAF50, #2E7D32)';
    } else {
        this.style.background = 'linear-gradient(145deg, var(--danger-color), #b71c1c)';
    }
});