// Coding Dojo - Python Bootcamp Jan 2025
// Final project
// Wavely - Scripts Java


//
// Pre-seleccionar las etiquetas existentes cuando se carga la página de edición de notícias

document.addEventListener('DOMContentLoaded', function () {
    // Obtener las etiquetas actuales del input
    const currentTags = document.getElementById('tags').value;
    if (currentTags) {
        // Convertir la cadena de etiquetas en un array
        const tagsArray = currentTags.split(',').map(tag => tag.trim());
        // Marcar como seleccionados los botones correspondientes
        document.querySelectorAll('.tag-btn').forEach(button => {
        if (tagsArray.includes(button.dataset.tag)) {
            button.classList.add('active', 'fw-bold');
        }
        });
    }
    });