// Coding Dojo - Python Bootcamp Jan 2025
// Final project
// Wavely - Scripts Java


//
// Funciones utilizadas para creación & edición de notícias


// Manejar la selección de etiquetas
document.querySelectorAll('.tag-btn').forEach(button => {
    button.addEventListener('click', function() {
        this.classList.toggle('active');
        this.classList.toggle('fw-bold');
        
        // Actualizar el campo de etiquetas
        const selectedTags = Array.from(document.querySelectorAll('.tag-btn.active'))
            .map(btn => btn.dataset.tag);
        document.getElementById('tags').value = selectedTags.join(', ');
    });
});

 // Vista previa de imagen/video
document.getElementById('archivo_multimedia').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        document.getElementById('foto_video').value = ''; // Limpiar URL si hay archivo
    }
});

 document.getElementById('foto_video').addEventListener('input', function(e) {
    if (e.target.value) {
        document.getElementById('archivo_multimedia').value = ''; // Limpiar archivo si hay URL
    }
});

