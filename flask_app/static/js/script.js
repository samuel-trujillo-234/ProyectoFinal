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

// Inicializar los botones de favoritos
document.addEventListener('DOMContentLoaded', function() {
    const favoriteButtons = document.querySelectorAll('.action-btn.favorite');
    favoriteButtons.forEach(button => {
        button.addEventListener('click', () => handleFavorite(button));
    });
});