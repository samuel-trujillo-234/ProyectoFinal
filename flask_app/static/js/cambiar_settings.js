// Coding Dojo - Python Bootcamp Jan 2025
// Final project
// Wavely - Scripts Java


//
// Funciones utilizadas para cambiar los settings


document.addEventListener('DOMContentLoaded', function() {
    // Aplicar tema guardado al cargar la página
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.classList.toggle('dark-theme', savedTheme === 'dark');
    document.querySelector(`#${savedTheme}Theme`).checked = true;

    // Escuchar cambios en los radio buttons de tema
    document.querySelectorAll('input[name="theme"]').forEach(radio => {
        radio.addEventListener('change', function() {
        const theme = this.id === 'darkTheme' ? 'dark' : 'light';
        document.body.classList.toggle('dark-theme', theme === 'dark');
        localStorage.setItem('theme', theme);
        toastr.success(`Tema ${theme === 'dark' ? 'oscuro' : 'claro'} aplicado`);
        });
    });
    });