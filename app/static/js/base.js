// Verifica o tema salvo no localStorage
const currentTheme = localStorage.getItem('theme') || 'light';
    
// Aplica o tema salvo
if (currentTheme === 'dark') {
  document.body.classList.add('dark-mode');
  document.getElementById('themeToggle').textContent = '☀️';
}

// Alternar tema
document.getElementById('themeToggle').addEventListener('click', function() {
  document.body.classList.toggle('dark-mode');
  
  const isDark = document.body.classList.contains('dark-mode');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
  
  this.textContent = isDark ? '☀️' : '🌙';
});

document.querySelector('#link-contato').addEventListener('click', function() {
  alert("Essa função ainda está em desenvolvimento")
})