// Script para o botão de favoritos

document.getElementById('favorite-btn').addEventListener('click', function() {
    const isFavorited = this.textContent.includes('Favoritado');
    this.innerHTML = isFavorited ? '<i class="fas fa-heart"></i> Adicionar aos Favoritos' : '<i class="fas fa-check"></i> Favoritado ✓';
    
    if (!isFavorited) {
        this.style.background = 'linear-gradient(145deg, #4CAF50, #2E7D32)';
    } else {
        this.style.background = 'linear-gradient(145deg, var(--danger-color), #b71c1c)';
    }
});

// Efeito de hover nas informações detalhadas
document.querySelectorAll('.detail-item').forEach(item => {
    item.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-3px)';
        this.style.boxShadow = '0 5px 12px rgba(255, 46, 46, 0.2)';
    });
    
    item.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
        this.style.boxShadow = '0 3px 6px rgba(0,0,0,0.1)';
    });
});