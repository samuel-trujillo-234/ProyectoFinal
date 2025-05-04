// Coding Dojo - Python Bootcamp Jan 2025
// Final project
// Wavely - Scripts Java

//
// Funciones para favoritos & likes

// Función para manejar los favoritos
function handleFavorite(button) {
    if (button.classList.contains('active')) {
        button.classList.remove('active');
        // Aquí puedes agregar la lógica para eliminar de favoritos
    } else {
        button.classList.add('active');
        // Aquí puedes agregar la lógica para agregar a favoritos
    }
}

//

// Función para atualizar contadores
function updateCounter(button, action) {
    const counter = button.querySelector('.counter');
    let count = parseInt(counter.textContent);
    counter.textContent = count + 1;
    button.classList.add('active');
    
    // Cambiar el color del ícono si es el botón de favoritos
    if (action === 'favorite') {
        const icon = button.querySelector('i');
        icon.style.color = '#ffd700';
    }
}