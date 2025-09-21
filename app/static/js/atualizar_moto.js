// Preview da foto selecionada
function setupPhotoPreview() {
    const fotoInput = document.getElementById('id_foto');
    if (!fotoInput) return;
    
    const preview = document.getElementById('photoPreview');
    if (!preview) return;
    
    fotoInput.addEventListener('change', function(e) {
        const fileInput = e.target;
        const fileName = fileInput.files[0] ? fileInput.files[0].name : "Selecione uma imagem";
        
        // Atualiza o label do arquivo
        const fileLabel = fileInput.nextElementSibling;
        if (fileLabel) {
            fileLabel.textContent = fileName;
        }
        
        // Mostra preview da imagem
        if (fileInput.files && fileInput.files[0]) {
            const reader = new FileReader();
            
            reader.onload = function(e) {
                preview.innerHTML = `<img src="${e.target.result}" alt="Pré-visualização da moto" style="width: 100%; height: 100%; object-fit: cover;">`;
            }
            
            reader.readAsDataURL(fileInput.files[0]);
        } else {
            // Se não houver arquivo selecionado, mostra o placeholder
            preview.innerHTML = '<span>🏍️</span><p class="text-muted">Nenhuma imagem selecionada</p>';
        }
    });
}

// Validação do formulário
function setupFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
}

// Validação específica para cilindradas (mínimo 50cc)
function setupCilindradasValidation() {
    const cilindradasInput = document.getElementById('id_cilindradas');
    if (!cilindradasInput) return;
    
    cilindradasInput.addEventListener('change', function() {
        if (this.value && parseInt(this.value) < 50) {
            this.setCustomValidity('As cilindradas devem ser pelo menos 50cc');
        } else {
            this.setCustomValidity('');
        }
    });
}

// Máscara para placa (formato ABC1234 ou ABC1D23)
function setupPlacaMask() {
    const placaInput = document.getElementById('id_placa');
    if (!placaInput) return;
    
    placaInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/[^a-zA-Z0-9]/g, '').toUpperCase();
        
        if (value.length > 7) {
            value = value.substring(0, 7);
        }
        
        // Formato Mercosul (ABC1D23) ou antigo (ABC1234)
        if (value.length > 3) {
            value = value.substring(0, 3) + value.substring(3).replace(/\D/g, '');
        }
        
        e.target.value = value;
    });
}

// Atualizar tema para os elementos personalizados
function updateCustomTheme() {
    const isDark = document.body.classList.contains('dark-mode');
    document.documentElement.style.setProperty('--text-color', isDark ? '#e6e6e6' : '#333');
    document.documentElement.style.setProperty('--bg-color', isDark ? '#121212' : '#f8f9fa');
}

// Observar mudanças no tema
function setupThemeObserver() {
    const observer = new MutationObserver(updateCustomTheme);
    observer.observe(document.body, { 
        attributes: true, 
        attributeFilter: ['class'] 
    });
}

// Inicializar todas as funcionalidades quando o documento estiver pronto
document.addEventListener('DOMContentLoaded', function() {
    setupPhotoPreview();
    setupFormValidation();
    setupCilindradasValidation();
    setupPlacaMask();
    setupThemeObserver();
    updateCustomTheme();
    
    console.log('Script de atualização de moto carregado com sucesso!');
});

// Função para lidar com erros
window.addEventListener('error', function(e) {
    console.error('Erro no script:', e.error);
});