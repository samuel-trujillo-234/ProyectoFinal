// Coding Dojo - Python Bootcamp Jan 2025
// Proyecto final
// Wavely - Scripts Java

//
// Funciones para favoritos & likes

// Función para manejar los favoritos
function handleFavorite(button) {
    const noticiaId = button.getAttribute('data-id');
    
    if (button.classList.contains('active')) {
        // Eliminar de favoritos (solo visual)
        button.classList.remove('active');
        const icon = button.querySelector('i');
        if (icon) {
            icon.style.color = ''; // Restablecer color
        }
        const counter = button.querySelector('.counter');
        if (counter) {
            let count = parseInt(counter.textContent);
            counter.textContent = Math.max(0, count - 1);
        }
        // Mostrar mensaje de éxito usando toastr si existe
        if (window.toastr) {
            toastr.success('Noticia eliminada de tus favoritos');
        }
    } else {
        // Añadir a favoritos (solo visual)
        button.classList.add('active');
        const icon = button.querySelector('i');
        if (icon) {
            icon.style.color = '#ffd700'; // Color dorado para favoritos
        }
        const counter = button.querySelector('.counter');
        if (counter) {
            let count = parseInt(counter.textContent);
            counter.textContent = count + 1;
        }
        // Mostrar mensaje de éxito usando toastr si existe
        if (window.toastr) {
            toastr.success('Noticia añadida a tus favoritos');
        }
    }
}

// Función para manejar los likes
function handleLike(button) {
    if (button.classList.contains('active')) {
        // Quitar like (solo visual)
        button.classList.remove('active');
        const icon = button.querySelector('i');
        if (icon) {
            icon.style.color = '';
        }
        const counter = button.querySelector('.counter');
        if (counter) {
            let count = parseInt(counter.textContent);
            counter.textContent = Math.max(0, count - 1);
        }
    } else {
        // Dar like (solo visual)
        button.classList.add('active');
        const icon = button.querySelector('i');
        if (icon) {
            icon.style.color = '#ff4d4d';
        }
        const counter = button.querySelector('.counter');
        if (counter) {
            let count = parseInt(counter.textContent);
            counter.textContent = count + 1;
        }
        
        // Si hay un botón de dislike activo, desactivarlo
        const dislikeButton = button.parentElement.querySelector('.dislike.active');
        if (dislikeButton) {
            dislikeButton.classList.remove('active');
            const dislikeIcon = dislikeButton.querySelector('i');
            if (dislikeIcon) {
                dislikeIcon.style.color = '';
            }
            const dislikeCounter = dislikeButton.querySelector('.counter');
            if (dislikeCounter) {
                let count = parseInt(dislikeCounter.textContent);
                dislikeCounter.textContent = Math.max(0, count - 1);
            }
        }
    }
}

// Función para manejar los dislikes
function handleDislike(button) {
    if (button.classList.contains('active')) {
        // Quitar dislike (solo visual)
        button.classList.remove('active');
        const icon = button.querySelector('i');
        if (icon) {
            icon.style.color = '';
        }
        const counter = button.querySelector('.counter');
        if (counter) {
            let count = parseInt(counter.textContent);
            counter.textContent = Math.max(0, count - 1);
        }
    } else {
        // Dar dislike (solo visual)
        button.classList.add('active');
        const icon = button.querySelector('i');
        if (icon) {
            icon.style.color = '#4d79ff';
        }
        const counter = button.querySelector('.counter');
        if (counter) {
            let count = parseInt(counter.textContent);
            counter.textContent = count + 1;
        }
        
        // Si hay un botón de like activo, desactivarlo
        const likeButton = button.parentElement.querySelector('.like.active');
        if (likeButton) {
            likeButton.classList.remove('active');
            const likeIcon = likeButton.querySelector('i');
            if (likeIcon) {
                likeIcon.style.color = '';
            }
            const likeCounter = likeButton.querySelector('.counter');
            if (likeCounter) {
                let count = parseInt(likeCounter.textContent);
                likeCounter.textContent = Math.max(0, count - 1);
            }
        }
    }
}

// Función general para actualizar contadores 
// (compatible con el código existente en las plantillas HTML)
function updateCounter(button, action) {
    if (action === 'like') {
        handleLike(button);
    } else if (action === 'dislike') {
        handleDislike(button);
    } else if (action === 'favorite') {
        handleFavorite(button);
    }
}