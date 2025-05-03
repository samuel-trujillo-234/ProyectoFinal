// Coding Dojo - Python Bootcamp Jan 2025
// Final project
// Wavely - Scripts Java


document.addEventListener('DOMContentLoaded', function() {

    // Código para búsqueda por etiquetas
    const searchInput = document.getElementById('searchInput');
    const tagButtons = document.querySelectorAll('.tag-btn');

    tagButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remover negrita de todos los botones
            tagButtons.forEach(btn => btn.classList.remove('fw-bold'));
            
            // Agregar negrita al botón clickeado
            this.classList.add('fw-bold');
            
            // Colocar el texto del botón en la barra de búsqueda
            const tagText = this.textContent.trim();
            if (tagText === 'Todo') {
                searchInput.value = ''; // Limpiar la búsqueda si se selecciona "Todo"
            } else {
                searchInput.value = tagText;
            }

            // Dar foco a la barra de búsqueda
            searchInput.focus();
        });
    });


    // Código para la eliminación de noticias
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    const deleteForm = document.getElementById('deleteNoticiaForm');
    const deleteNoticiaId = document.getElementById('deleteNoticiaId');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const noticiaId = this.getAttribute('data-id');
            deleteNoticiaId.value = noticiaId;
            deleteForm.action = `/eliminar_noticia/${noticiaId}`;
            deleteModal.show();
        });
    });
});



