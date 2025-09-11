// Preview da foto selecionada
document.getElementById('{{ form.foto.id_for_label }}').addEventListener('change', function(e) {
    const preview = document.getElementById('photoPreview');
    const fileInput = e.target;
    const fileName = fileInput.files[0] ? fileInput.files[0].name : "Selecione uma imagem";
    
    // Atualiza o label do arquivo
    const fileLabel = fileInput.nextElementSibling;
    fileLabel.textContent = fileName;
    
    // Mostra preview da imagem
    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            preview.innerHTML = `<img src="${e.target.result}" alt="Pré-visualização da moto">`;
        }
        
        reader.readAsDataURL(fileInput.files[0]);
    } else {
        preview.innerHTML = '<span>🏍️</span><p class="text-muted">Nenhuma imagem selecionada</p>';
    }
});

// Validação do formulário
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

// Máscara para placa (opcional)
const placaInput = document.getElementById('{{ form.placa.id_for_label }}');
if (placaInput) {
    placaInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/[^a-zA-Z0-9]/g, '').toUpperCase();
        
        if (value.length > 7) {
            value = value.slice(0, 7);
        }
        
        // Formato Mercosul: AAA0A00
        // Formato antigo: AAA0000
        if (value.length > 3) {
            value = value.slice(0, 3) + value.slice(3).replace(/[^0-9]/g, '');
        }
        
        e.target.value = value;
    });
}

// Atualizar tema para os elementos personalizados
function updateCustomTheme() {
    const isDark = document.body.classList.contains('dark-mode');
    document.documentElement.style.setProperty('--text-color', isDark ? '#e6e6e6' : '#333');
    document.documentElement.style.setProperty('--bg-color', isDark ? '#121212' : '#fff');
}

// Observar mudanças no tema
const observer = new MutationObserver(updateCustomTheme);
observer.observe(document.body, { 
    attributes: true, 
    attributeFilter: ['class'] 
});

// Inicializar tema
updateCustomTheme();