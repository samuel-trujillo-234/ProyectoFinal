// Coding Dojo - Python Bootcamp Jan 2025
// Proyecto final
// Wavely - Scripts Java

//
// Funciones para favoritos & likes

// Función para manejar los favoritos
function handleFavorite(button) {
    const noticiaId = button.getAttribute('data-id');
    
    if (button.classList.contains('active')) {
        // Eliminar de favoritos
        fetch(`/eliminar_favorito/${noticiaId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(function(response) {
            return response.json(); // Parse the JSON response
        })
        .then(function(data) {
            if (data.success) {
                button.classList.remove('active');
                const icon = button.querySelector('i');
                if (icon) {
                    icon.style.color = ''; // Restablecer color
                }
                const counter = button.querySelector('.counter');
                if (counter) {
                    // Use the count from the server instead of manually decrementing
                    counter.textContent = data.count || 0;
                }
                // Mostrar mensaje de éxito usando toastr si existe
                if (window.toastr) {
                    toastr.success('Noticia eliminada de tus favoritos');
                }
            }
        })
        .catch(function(error) {
            console.error('Error al eliminar favorito:', error);
        });
    } else {
        // Añadir a favoritos
        fetch(`/crear_favorito/${noticiaId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(function(response) {
            return response.json(); // Parse the JSON response
        })
        .then(function(data) {
            if (data.success) {
                button.classList.add('active');
                const icon = button.querySelector('i');
                if (icon) {
                    icon.style.color = '#ffd700'; // Color dorado para favoritos
                }
                const counter = button.querySelector('.counter');
                if (counter) {
                    // Use the count from the server instead of manually incrementing
                    counter.textContent = data.count || 0;
                }
                // Mostrar mensaje de éxito usando toastr si existe
                if (window.toastr) {
                    toastr.success('Noticia añadida a tus favoritos');
                }
            }
        })
        .catch(function(error) {
            console.error('Error al añadir favorito:', error);
        });
    }
}

// Función para actualizar contadores
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